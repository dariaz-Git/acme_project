from django.db import models as m


class Birthday(m.Model):
    first_name = m.CharField('Имя', max_length=20)
    last_name = m.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20)
    birthday = m.DateField('Дата рождения')


# from django.core.validators import MinValueValidator, MaxValueValidator
# price = m.IntegerField(validators=[MaxValueValidator(100),
    # MinValueValidator(1)])
