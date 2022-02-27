from kedro.pipeline import node
from .preprocess import preprocess_companies, preprocess_shuttles, create_model_input_table


preprocess_companies_node: node = node(
    name="preprocess_companies",           
    func=preprocess_companies,
    inputs="companies",
    outputs="preprocessed_companies",
)

preprocess_shuttles_node: node = node(
    name="preprocess_shuttles_node",
    func=preprocess_shuttles,
    inputs="shuttles",
    outputs="preprocessed_shuttles",
)

create_model_input_table_node: node = node(
    name="create_model_input_table_node",
    func=create_model_input_table,
    inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
    outputs="model_input_table",
)