from abc import abstractmethod , ABC

# FlyWeight class

class Tree:

    @abstractmethod
    def draw(self,x:int,y:int):
        pass

# concrete FlyWeight (shared) | intrinsic

class TreeType(Tree):
    def __init__(self,name:str,color:str,texture:str):
        self.name =name
        self.color= color
        self.texture= texture

    def draw(self,x, y):
       print(
           f'name of tree is {self.name} \n color of tree is {self.color} \n texture of tree is {self.texture} \n at positions {x} and {y}'
       )
    

# flyweight factory to create obj

class TreeFactory:
    _tree_type = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name,color,texture)
        if key not in cls._tree_type:
            cls._tree_type[key] = TreeType(name,color,texture)
        return cls._tree_type[key]

    
# context flyweight | extrinsic (unique)
class ContextTree:
    def __init__(self, x, y, tree_type):
        # Extrinsic state
        self.x = x
        self.y = y

        # Shared flyweight
        self.tree_type = tree_type
    
    def draw(self):
        self.tree_type.draw(self.x,self.y)

# client
class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(
        self,
        x,
        y,
        name,
        color,
        texture
    ):
        tree_type = TreeFactory.get_tree_type(
            name,color,texture
        )
        tree = ContextTree(x,y,tree_type)
        self.trees.append(tree)
    
    def draw(self):
        for tree in self.trees:
            tree.draw()
    
if __name__ == '__main__':
    forest = Forest()
    forest.plant_tree(
    10,
    20,
    "Oak",
    "Green",
    "oak.png"
    )

    forest.plant_tree(
        50,
        80,
        "Oak",
        "Green",
        "oak.png"
    )

    forest.plant_tree(
        100,
        150,
        "Pine",
        "Dark Green",
        "pine.png"
    )

    forest.plant_tree(
        200,
        300,
        "Oak",
        "Green",
        "oak.png"
    )

    forest.draw()

    print(
        "\nNumber of flyweights:",
        len(TreeFactory._tree_type)
    )



        