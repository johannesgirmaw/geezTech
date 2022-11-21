import enum

class CourseType(enum.Enum):
    free = 100
    premium = 101
    sponsord = 102



class CourseLevel(enum.Enum):
    biginner = 100
    intermediate = 101
    advanced = 102

CART_STATUS = [
   (100,'ordered'),
   (101,'enrolled'),
]