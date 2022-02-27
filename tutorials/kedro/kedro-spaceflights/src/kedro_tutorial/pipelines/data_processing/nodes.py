from kedro.pipeline import node
from .preprocess import preprocess_companies, preprocess_shuttles


preprocess_companies_node: node = node(
    func=preprocess_companies,
    inputs="companies",
    outputs="preprocessed_companies",
    name="preprocess_companies",           
)
preprocess_shuttles_node: node = node(
    func=preprocess_shuttles,
    inputs="shuttles",
    outputs="preprocessed_shuttles",
    name="preprocess_shuttles_node",
)