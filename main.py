import os

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_TEXT_EMBEDDINGS_MODEL"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
azure_search = AzureSearch(
    embedding_function=embeddings.embed_query,
    azure_search_endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    azure_search_key=os.getenv("AZURE_SEARCH_API_KEY"),
    index_name=index_name,
    semantic_configuration_name=f"{index_name}-semantic-configuration"
)

query = "LMV2023"
language = "de"
category = "arbeitsrecht-gesamtarbeitsvertraege-bauhauptgewerbe"
filters = f"(language eq '{language}' or languages/any(l: l eq '{language}')) and categories/any(c: c eq '{category}')"
score_threshold = 2.0

docs = azure_search.semantic_hybrid_search_with_score(query=query, k=2, filters=filters,
                                                      score_type="reranker_score",
                                                      score_threshold=score_threshold)

