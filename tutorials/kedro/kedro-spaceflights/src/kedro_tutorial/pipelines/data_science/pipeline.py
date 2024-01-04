"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.17.7
"""

from kedro.pipeline import Pipeline, pipeline

from .nodes import evaluate_model_node, split_data_node, train_model_node


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([split_data_node, train_model_node, evaluate_model_node])
