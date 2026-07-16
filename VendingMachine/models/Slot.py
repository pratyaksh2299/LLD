
from .Product import Product,field
from dataclasses import dataclass
from typing  import Dict

@dataclass
class Slot:
    items : Dict[Product,int] = field(default_factory=dict)