from django.core.exceptions import ValidationError


def validate_len_of_email(value):
    if len(value) < 8:
        raise ValidationError('Email Should be at least 8 characters long!')