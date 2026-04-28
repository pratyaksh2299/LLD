from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading image from disk: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real: RealImage = None

    def display(self):
        if self._real is None:
            self._real = RealImage(self.filename)
        self._real.display()

if __name__ == '__main__':
    image: Image = ProxyImage("test_image.jpg")
    image.display()