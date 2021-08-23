import json

from django.contrib import admin
from django.contrib.admin.models import LogEntry

from boards.models import Board
from boards.models import Topic
from boards.models import Post
from import_export import resources

# Register your models here.


admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Topic)


