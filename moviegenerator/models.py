from django.db import models


class Production(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=500)
    gender = models.CharField(max_length=100)

    TYPES = (
        ('M', 'Movie'),
        ('TV', 'TV Show'),
    )
    type = models.CharField(max_length=2, choices=TYPES)

    rating = models.IntegerField()
    link = models.TextField(max_length=500)

    def __str__(self):
        return "{}. {}".format(self.id, self.title)

