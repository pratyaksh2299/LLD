from enum import Enum

class FeeCalculationType(Enum):
    FLAT_RATE = 'flat_rate'
    HOURLY_RATE = 'hourly_rate'
    