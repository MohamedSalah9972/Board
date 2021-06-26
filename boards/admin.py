from django.contrib import admin
from boards.models import Board
from boards.models import Topic
from boards.models import Post
# Register your models here.

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Topic)