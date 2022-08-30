from pydantic import BaseModel, Field
from enum import Enum

class ModelName(str, Enum):
	alexnet = 'alexnet'
	resenet = 'resnet'
	lenet = 'lenet'

class Item(BaseModel):
	name: str
	description: str | None = None
	price: float
	tax: float | None = None
