from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm


# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        form=NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            user = User.objects.first()
            topic.creator = user
            topic.save()
            message =form.cleaned_data.get('message')
            post = Post.objects.create(
                message=message,
                topic=topic,
                creator=user
            )
            return redirect('board_topics', board_id=board_id)

    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
