from django.core.exceptions import ValidationError


class Validations:
    def validate_price(value: float):
        if value < 0:
            raise ValidationError(
                ('%(value)s should not be negative number'), params={'value': value})
