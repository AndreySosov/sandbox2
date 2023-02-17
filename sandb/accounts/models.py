from django.contrib.auth.models import User
from PIL import Image
from django.db import models

# Create your models here.
class About(models.Model):
    birth_day = models.DateField()
    sex = models.CharField(max_length=1)
    city = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "О пользователе"


class Education(models.Model):
    edu = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Образование"


class Hobbies(models.Model):
    hobby = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Увлечения"


class Targets(models.Model):
    target = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Цели"


class Contacts(models.Model):
    contact = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Контакты"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')

    def __str__(self):
        return f'{self.user.username}'


    # resizing images
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.img.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.img.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'