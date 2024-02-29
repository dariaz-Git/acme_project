from django.db import models as m

from .validators import real_age


class Birthday(m.Model):
    first_name = m.CharField('Имя', max_length=20)
    last_name = m.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20)
    birthday = m.DateField('Дата рождения', validators=(real_age,))
    image = m.ImageField(
        'Фото',
        upload_to='birthdays_images',
        blank=True)

    class Meta():
        constraints = (
            m.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )


# from django.core.validators import MinValueValidator, MaxValueValidator
# price = m.IntegerField(validators=[MaxValueValidator(100),
    # MinValueValidator(1)])
