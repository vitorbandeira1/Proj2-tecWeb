from django.db import models


class Production(models.Model):
    id_api = models.IntegerField(default=None)
    title = models.CharField(max_length=100)
    rating = models.IntegerField(default=None)
    link = models.TextField(max_length=600)
    img = models.TextField(max_length=600, default="") 
    TYPES = (
        ('M', 'Movie'),
        ('TV', 'TV Show'),
    )
    type_of = models.CharField(max_length=10, choices=TYPES)


    def __str__(self):
        return "{}. {}".format(self.id, self.title)

