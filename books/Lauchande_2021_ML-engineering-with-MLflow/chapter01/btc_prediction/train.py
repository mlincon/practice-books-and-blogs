import datetime
import warnings

import mlflow.sklearn
import numpy as np
import pandas as pd
import pandas_datareader.data as web
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split


def get_training_data(
    stock: str, source: str, start: datetime, end: datetime
) -> pd.DataFrame:
    """
    Get data for the provided stock from the given time period
    """
    return web.DataReader(stock, source, start, end)


def rolling_window(a: np.array, window: int) -> np.array:
    """
    Takes np.array 'a' and size 'window' as parameters
    Outputs an np.array with all the ordered sequences of values of 'a'
    of size 'window'
    e.g. Input: ( np.array([1, 2, 3, 4, 5, 6]), 4 )
        Output: array([[1, 2, 3, 4],
                       [2, 3, 4, 5],
                       [3, 4, 5, 6]])
    """
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)


def prepare_training_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Return a prepared numpy dataframe. Compute the difference between the closing
    and opening price (Delta). If the difference is positive, return 1 else 0
    """

    def _digitize(n):
        if n > 0:
            return 1
        return 0

    data["Delta"] = data["Close"] - data["Open"]
    data["to_predict"] = data["Delta"].apply(lambda d: _digitize(d))
    return data


if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    with mlflow.start_run():
        training_data = get_training_data(
            stock="BTC-USD",
            source="yahoo",
            start=datetime.datetime(2019, 7, 1),
            end=datetime.datetime(2019, 9, 30),
        )

        prepared_training_data_df = prepare_training_data(training_data)

        btc_mat = prepared_training_data_df.to_numpy()

        WINDOW_SIZE = 16

        X = rolling_window(btc_mat[:, 7], WINDOW_SIZE)[:-1, :]
        Y = prepared_training_data_df["to_predict"].to_numpy()[WINDOW_SIZE:]

        X_train, X_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.25, random_state=4284, stratify=Y
        )

        clf = RandomForestClassifier(
            bootstrap=True,
            criterion="gini",
            min_samples_split=2,
            min_weight_fraction_leaf=0.0,
            n_estimators=50,
            random_state=4284,
            verbose=0,
        )

        clf.fit(X_train, y_train)
        predicted = clf.predict(X_test)

        # explicitly task MLflow to log the random forest model and chosen metrics
        # a folder named "model_random_forest" is created inside the "artifacts"
        mlflow.sklearn.log_model(clf, "model_random_forest")

        print(classification_report(y_test, predicted))

        mlflow.log_metric(
            "precision_label_0", precision_score(y_test, predicted, pos_label=0)
        )
        mlflow.log_metric(
            "recall_label_0", recall_score(y_test, predicted, pos_label=0)
        )
        mlflow.log_metric("f1score_label_0", f1_score(y_test, predicted, pos_label=0))
        mlflow.log_metric(
            "precision_label_1", precision_score(y_test, predicted, pos_label=1)
        )
        mlflow.log_metric(
            "recall_label_1", recall_score(y_test, predicted, pos_label=1)
        )
        mlflow.log_metric("f1score_label_1", f1_score(y_test, predicted, pos_label=1))
