from chromadb import Documents, EmbeddingFunction, Embeddings
import chromadb
import chromadb.utils.embedding_functions as embedding_functions


client = chromadb.PersistentClient(path="./localdata")
google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key="YOUR_API_KEY")
collection = client.get_or_create_collection(name="stories", embedding_function=google_ef)

def add_document_embeddings(document:str):
	# TODO: get api key from google and load from env
	
	collection.add_document(document)


def query_document_embeddings(document:str, n:int=10):
	return collection.query(
    query_texts=[document],
    n_results=n,
    where={"metadata_field": "is_equal_to_this"},

)