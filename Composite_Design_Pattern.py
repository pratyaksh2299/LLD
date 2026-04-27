from abc import ABC, abstractmethod
from typing import List


class FileSystemItem(ABC):

    @abstractmethod
    def ls(self, indent=0):
        pass

    @abstractmethod
    def openAll(self, indent=0):
        pass

    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def getName(self):
        pass


class File(FileSystemItem):

    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    def ls(self, indent=0):
        print(" " * indent + f"- {self._name}")

    def openAll(self, indent=0):
        print(" " * indent + f"{self._name}")

    def getSize(self):
        return self._size

    def getName(self):
        return self._name


class Folder(FileSystemItem):

    def __init__(self, name: str):
        self._name = name
        self._items: List[FileSystemItem] = []

    def addItem(self, item: FileSystemItem):
        self._items.append(item)

    def ls(self, indent=0):
        print(" " * indent + f"- {self._name}/")
        for item in self._items:
            item.ls(indent + 2)   

    def openAll(self,indent=0):
        # print(" " * indent + f"Opening folder: {self._name}")
        for item in self._items:
            item.openAll(indent + 2)     

    def getSize(self):
        total = 0
        for item in self._items:
            total += item.getSize() 
        return total

    def getName(self):
        return self._name


# Client code
if __name__ == "__main__":

    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)

    folder1 = Folder("folder1")
    folder2 = Folder("folder2")

    folder1.addItem(file1)
    folder2.addItem(file2)

    root = Folder("root")
    root.addItem(folder1)
    root.addItem(folder2)

    print("Listing all items:")
    root.ls()
    image1 = File("image1.png", 500)
    root.addItem(image1)
    root.openAll()
    print("\nListing all items after adding image1.png:")
    folder2.openAll()

    print("\nTotal size:", root.getSize())