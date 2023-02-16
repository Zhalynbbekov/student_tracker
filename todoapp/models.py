from django.db import models


# Create your models here.
class Information(models.Model):
    name_and_surname = models.CharField('name_and_surname', max_length=50)
    group = models.CharField('group', max_length=50)
    gpa = models.FloatField(verbose_name='gpa')
    attendance = models.CharField('attendace', max_length=50)

    def __str__(self):
        return self.name_and_surname
