from abc import ABC, abstractmethod


# -------------------- Document Elements --------------------

class DocumentElement(ABC):

    @abstractmethod
    def rendor(self) -> str:
        pass


class TextElement(DocumentElement):

    def __init__(self, text: str):
        self.__text = text

    def rendor(self) -> str:
        return self.__text


class FileElement(DocumentElement):

    def __init__(self, file: str):
        self.__file = file

    def rendor(self) -> str:
        return self.__file


# -------------------- Persistence Layer --------------------

class Persistence(ABC):

    @abstractmethod
    def save(self, data: str) -> None:
        pass


class FileStorage(Persistence):

    def save(self, data: str) -> None:
        print(f"FileStorage saved -- {data}")


class DbStorage(Persistence):

    def save(self, data: str) -> None:
        print(f"DbStorage saved -- {data}")


# -------------------- Document --------------------

class Document:
    def __init__(self):
        self.elements: list[DocumentElement] = []

    def addElement(self, element: DocumentElement) -> None:
        self.elements.append(element)

    def getElements(self) -> list[DocumentElement]:
        return self.elements


# -------------------- Renderer --------------------

class DocumentRender:

    def __init__(self, doc: Document):
        self.document = doc

    def render_element(self) -> None:
        for ele in self.document.getElements():
            print(ele.rendor())


# -------------------- Editor --------------------

class DocumentEditor:

    def __init__(self, doc: Document, persistence: Persistence):
        self.doc = doc
        self.persistence = persistence

    def addText(self, text: str) -> None:
        element : DocumentElement = TextElement(text)
        self.doc.addElement(element)
        self.persistence.save(element.rendor())

    def addImage(self, img: str) -> None:
        element : DocumentElement = FileElement(img)
        self.doc.addElement(element)
        self.persistence.save(element.rendor())


# -------------------- Main --------------------

def main():
    document = Document()

    # choose storage
    storage = FileStorage()   # change to DbStorage() if needed

    editor = DocumentEditor(document, storage)

    editor.addText("Hello World")
    editor.addText("This is a document editor example")
    editor.addImage("image.png")

    print("\n--- Document Render ---")
    renderer = DocumentRender(document)
    renderer.render_element()


if __name__ == "__main__":
    main()
