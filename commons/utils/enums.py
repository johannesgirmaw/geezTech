from django.db import models


class COURSE_TYPE(models.IntegerChoices):
    FREE = 100
    PREMIUM = 101
    SPONSORED = 102


class COURSE_LEVEL(models.IntegerChoices):
    BEGINNER = 100
    INTERMEDIATE = 101
    ADVANCED = 102


CONTENT_TYPE = [
    (100, 'content'),
    (101, 'question'),
]


CART_STATUS = [
    (100, 'ordered'),
    (101, 'enrolled'),
]

RATING_VALUES = [
    (100, 'excellent'),
    (101, 'very good'),
    (102, 'good'),
    (103, 'not bad'),
    (104, 'bad'),
]


class PROGRESS_STATUS(models.IntegerChoices):
    STARTED = 100
    ON_PROGRESS = 101
    FINISHED = 102


class CONTENT_TYPE(models.IntegerChoices):
    VIDEO = 100
    IMAGE = 101
    DOCUMENT = 102
    QUESTION = 103
    YOUTUBE_VIDEO = 104


class COURSE_STATUS(models.IntegerChoices):
    CREATED = 100
    PUBLISHED = 101


class EDUCATIONAL_LEVEL(models.IntegerChoices):
    Elementary = 100
    Secondary = 101
    Level_III_Diploma_TVET = 102
    Bachelor_of_Education = 103
    Bachelor_of_Arts_or_Science = 104
    Master = 105
    Doctorate = 106
