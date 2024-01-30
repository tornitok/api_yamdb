import datetime as dt

from django.forms import ValidationError


def year_validator(value):
    if value > dt.datetime.now().year:
        raise ValidationError(
            f'Год не может быть больше текущего ({value})',
            params={'value': value},
        )