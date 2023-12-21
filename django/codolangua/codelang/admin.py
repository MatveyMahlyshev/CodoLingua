from django.contrib import admin, messages
from .models import Language, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    fields = ['topic_title', 'topic_content', 'topic_slug', 'programming_languages', 'topic_text', 'topic_code']
    list_display = ['topic_title', 'topic_content', 'topic_slug', 'get_programming_languages']
    list_display_links = ['topic_title']
    filter_vertical = ('programming_languages',)
    ordering = ['programming_languages']

    def get_programming_languages(self, obj):
        return ", ".join([p.title for p in obj.programming_languages.all()])


