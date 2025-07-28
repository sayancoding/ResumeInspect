import re

class DocumentCleaner:
    def __init__(self) -> None:
        pass

    def text_cleanup(self,text:str) -> str:
        text = re.sub(r"\t+", "\t", text)
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r'\s+', " ", text).strip()
        return text