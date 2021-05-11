from django.db import models


class Production(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=500)
    genres = models.CharField(max_length=100)
    rating = models.IntegerField()
    link = models.TextField(max_length=500)

    TYPES = (
        ('M', 'Movie'),
        ('TV', 'TV Show'),
    )
    type_of = models.CharField(max_length=2, choices=TYPES)


    def __str__(self):
        return "{}. {}".format(self.id, self.title)

