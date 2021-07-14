from django.contrib import admin
from boards.models import Board
from boards.models import Topic
from boards.models import Post
from import_export import resources


# Register your models here.
class TopicR(resources.ModelResource):
    pass


admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Topic)
