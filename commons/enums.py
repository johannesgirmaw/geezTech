import enum


class CourseType(enum.Enum):
    free = 100
    premium = 101
    sponsord = 102


class CourseLevel(enum.Enum):
    biginner = 100
    intermediate = 101
    advanced = 102


class ContentType(enum.Enum):
    content = 100
    question = 101
