"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from kedro_tutorial.pipelines import data_processing as dp
from kedro_tutorial.pipelines import data_science as ds


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipeline.

    Returns:
    A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    default_pipelines = data_processing_pipeline + data_science_pipeline

    return {
        "__default__": default_pipelines,
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline
    }
