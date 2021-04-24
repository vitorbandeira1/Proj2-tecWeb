from django.db import models


class TextField(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return "{}. {}".format(self.id, self.title)

