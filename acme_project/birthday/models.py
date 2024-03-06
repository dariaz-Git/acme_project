from django.contrib.auth import get_user_model
from django.db import models as m
from django.urls import reverse

from .validators import real_age


User = get_user_model()


class Birthday(m.Model):
    first_name = m.CharField('Имя', max_length=20)
    last_name = m.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20)
    birthday = m.DateField('Дата рождения', validators=(real_age,))
    image = m.ImageField(
        'Фото',
        upload_to='birthdays_images',
        blank=True)
    author = m.ForeignKey(
        User, verbose_name='Автор записи', on_delete=m.CASCADE, null=True
    )

    class Meta():
        constraints = (
            m.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    def get_absolute_url(self):
        return reverse("birthday:detail", kwargs={"pk": self.pk})

# from django.core.validators import MinValueValidator, MaxValueValidator
# price = m.IntegerField(validators=[MaxValueValidator(100),
    # MinValueValidator(1)])
