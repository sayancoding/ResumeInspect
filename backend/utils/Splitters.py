from langchain.text_splitter import RecursiveCharacterTextSplitter

class Splitters:
    def get_text_splitter(self):
        return RecursiveCharacterTextSplitter(
            chunk_size=3000,
            chunk_overlap=200)