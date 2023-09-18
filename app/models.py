from django.db import models

class ToDo(models.Model):
    stat = [
        ('Done' , 'Done'),
        ('Bajarilmadi', 'Bajarilmadi')
        ('Bajarilmoqda','Bajarilmoqda')
    ]

    title = models.CharField(max_length=100)
    time = models.DateTimeField()
    desc = models.TextField()
    status = models.CharField(choices=stat)

    def __str__(self):
        return self.title