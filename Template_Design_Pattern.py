from abc import ABC, abstractmethod

# The Template Design Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a method, called a template method, and allows subclasses to override specific steps of the algorithm without changing its structure. This pattern promotes code reuse and helps to enforce a consistent algorithm structure across different implementations.
class ModelTrainer(ABC):

    def train(self):
        self.load_data()
        self.preprocess_data()
        self.build_model()
        self.train_model()
        self.evaluate_model()

    @abstractmethod
    def load_data(self):
        print(f'common data loading steps')

    @abstractmethod
    def preprocess_data(self):
        pass

    @abstractmethod
    def build_model(self):
        pass

    @abstractmethod
    def train_model(self):
        pass

    @abstractmethod
    def evaluate_model(self):
        print(f'common model evaluation steps')


# CNNTrainer is a concrete implementation of the ModelTrainer template. It provides specific implementations for the abstract methods defined in the ModelTrainer class, allowing it to train a CNN model while still following the overall structure defined by the template method in the ModelTrainer class.
class CNNTrainer(ModelTrainer):
    
    def load_data(self):
        print(f'loading data for CNN')

    def preprocess_data(self):
        print(f'preprocessing data for CNN')

    def build_model(self):
        print(f'building CNN model')

    def train_model(self):
        print(f'training CNN model')

    def evaluate_model(self):
        print(f'evaluating CNN model')

# RNNTrainer is a concrete implementation of the ModelTrainer template. It provides specific implementations for the abstract methods defined in the ModelTrainer class, allowing it to train an RNN model while still following the overall structure defined by the template method in the ModelTrainer class.
class RNNTrainer(ModelTrainer):

    def load_data(self):
        print(f'loading data for RNN')

    def preprocess_data(self):
        print(f'preprocessing data for RNN')

    def build_model(self):
        print(f'building RNN model')

    def train_model(self):
        print(f'training RNN model')

    def evaluate_model(self):
        print(f'evaluating RNN model')

# The Template Design Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a method, called a template method, and allows subclasses to override specific steps of the algorithm without changing its structure. This pattern promotes code reuse and helps to enforce a consistent algorithm structure across different implementations.
class Client:
    def __init__(self,trainer: ModelTrainer):
        self.trainer = trainer
        self.trainer.train()

if __name__ == "__main__":
    cnn_trainer :ModelTrainer = CNNTrainer()
    rnn_trainer :ModelTrainer = RNNTrainer()
    client1 = Client(cnn_trainer)
    client2 = Client(rnn_trainer)

        