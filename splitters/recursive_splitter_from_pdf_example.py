from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

path_load = PyPDFLoader(r"/home/valls/studies/langchain/splitters/data.pdf")

pdf = path_load.load()

# print(pdf[0].page_content)

original_text = Document(page_content=pdf[0].page_content)

# print(original_text.page_content)

docs = [original_text]

# print(docs)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=40,
    chunk_overlap=10,
    length_function=len,
    separators=[""],
)

spliched_docs = text_splitter.split_documents(docs)

i = 0
for doc in spliched_docs:
    print("--" * 20)
    print(f"chunk: {i}")
    print("--" * 20)
    print(doc.page_content)
    print("--" * 20)
    i += 1
