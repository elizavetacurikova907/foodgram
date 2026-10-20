"""Общие константы проекта Foodgram."""

# Константы приложения recipes_api
NAME_MAX_LENGTH = 256

# Константы приложения tags_api
TAG_NAME_MAX_LENGTH = 32
TAG_SLUG_MAX_LENGTH = 32

# Константы приложения users_api
EMAIL_MAX_LENGTH = 254
USERNAME_MAX_LENGTH = 150
CONFIRMATION_CODE_MAX_LENGTH = 100

# Константы приложения ingredients_api
INGREDIENT_NAME_MAX_LENGTH = 128
MEASUREMENT_UNIT_MAX_LENGHT = 64
MEASUREMENT_CHOICES = [
    ('kg', 'кг'),
    ('g', 'г'),
    ('l', 'л'),
    ('ml', 'мл'),
]
