from django.db import models
from django.urls import reverse


class Language(models.Model):
    title = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.title


class Topic(models.Model):
    topic_title = models.CharField(max_length=255, blank=False)
    topic_content = models.CharField(max_length=255, blank=False)
    topic_slug = models.SlugField(max_length=255, unique=True, db_index=True)
    topic_text = models.TextField(blank=True)
    programming_languages = models.ManyToManyField(Language, related_name='topic')

    def __str__(self):
        return self.topic_title

    def get_absolute_url(self):
        return reverse('python_topic', kwargs={'python_slug': self.topic_slug})