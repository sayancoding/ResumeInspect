from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_text_splitter():
    return RecursiveCharacterTextSplitter(chunk_size=3000,chunk_overlap=200)