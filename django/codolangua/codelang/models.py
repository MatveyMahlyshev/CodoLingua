from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.title


class Topic(models.Model):
    topic_title = models.CharField(max_length=255, blank=False)
    topic_content = models.CharField(max_length=255, blank=False)
    topic_slug = models.SlugField(max_length=255, unique=True,blank=False)
    programming_languages = models.ManyToManyField(Language, related_name='topic')

    def __str__(self):
        return self.topic_title