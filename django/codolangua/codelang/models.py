from django.db import models


class Topics(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title
