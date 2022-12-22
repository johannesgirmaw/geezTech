from django.db import models

COURSE_TYPE = [
    (100, 'free'),
    (101, 'premium'),
    (102, 'sponsord'),
]

COURE_LEVEL = [
    (100, 'biginner'),
    (101, 'intermediate'),
    (102, 'advanced'),
]

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

class EDUCATIONAL_LEVEL(models.IntegerChoices):
    Elementary = 100
    Secondary = 101
    Level_III_Diploma_TVET = 102
    Bachelor_of_Education = 103
    Bachelor_of_Arts_or_Science = 104
    Master = 105
    Doctorate = 106