from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Validations:
    def validate_price(value: float):
        if value < 0:
            raise ValidationError(
                ('%(value)s should not be negative number'), params={'value': value})
