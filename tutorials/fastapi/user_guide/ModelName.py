from enum import Enum

class ModelName(str, Enum):
    """Machine learning models"""
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"