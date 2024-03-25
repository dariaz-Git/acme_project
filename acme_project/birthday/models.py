from django.contrib.auth import get_user_model
from django.db import models as m
from django.urls import reverse

from .validators import real_age


User = get_user_model()


class Tag(m.Model):
    tag = m.CharField('Тег', max_length=20)

    def __str__(self):
        return self.tag


class Birthday(m.Model):
    first_name = m.CharField('Имя', max_length=20)
    last_name = m.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20)
    birthday = m.DateField('Дата рождения', validators=(real_age,))
    tags = m.ManyToManyField(
        Tag,
        verbose_name='Теги',
        blank=True,
        help_text='Удерживайте Ctrl для выбора нескольких вариантов'
    )
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


class Congratulation(m.Model):
    text = m.TextField('Текст поздравления')
    birthday = m.ForeignKey(
        Birthday,
        on_delete=m.CASCADE,
        related_name='congratulations',
    )
    created_at = m.DateField(auto_now_add=True)
    author = m.ForeignKey(User, on_delete=m.CASCADE)

    class Meta:
        ordering = ('created_at',)
