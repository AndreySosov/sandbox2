from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class NoteContent(models.Model):
    date = models.DateTimeField(blank=True, auto_now=True)
    note = models.TextField()
    condition = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Заметки"
        ordering = ['-date']


    def get_absolute_url(self):
        return '/account'