from kedro.pipeline import node

from .training_steps import (
    evaluate_linear_regression_model,
    split_data,
    train_linear_regression,
)

split_data_node: node = node(
    name="split_data_node",
    func=split_data,
    inputs=["model_input_table", "params:model_options"],
    outputs=["X_train", "X_test", "y_train", "y_test"],
)

train_model_node: node = node(
    name="train_model_node",
    func=train_linear_regression,
    inputs=["X_train", "y_train"],
    outputs="regressor",
)

evaluate_model_node: node = node(
    func=evaluate_linear_regression_model,
    inputs=["regressor", "X_test", "y_test"],
    outputs=None,
    name="evaluate_model_node",
)
