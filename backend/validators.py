from django.core.validators import RegexValidator

username_regex = RegexValidator(
    regex=r'^[\w.@+-]+\z',
    message='Недопустимые символы.'
)

slug_regex = RegexValidator(
    regex=r'^[-a-zA-Z0-9_]+$',
    message='Слаг может содержать только латинские буквы и цифры.'
)