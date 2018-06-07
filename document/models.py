from django.db import models

# Create your models here.


class Document(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField(default=None)
    # pub_date = models.DateTimeField(default=None)


    def __str__(self):
        return self.title