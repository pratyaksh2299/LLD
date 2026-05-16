from abc import ABC,abstractmethod
from enum import Enum
class VehicleType(Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK ="truck"

class DurationType(Enum):
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
