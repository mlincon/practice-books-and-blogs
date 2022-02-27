"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.17.7
"""

from kedro.pipeline import Pipeline, pipeline
from .nodes import preprocess_companies_node, preprocess_shuttles_node


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        preprocess_companies_node,
        preprocess_shuttles_node
    ])