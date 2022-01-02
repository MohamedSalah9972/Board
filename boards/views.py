from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from .serializers import TopicSerializer


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    print(request.POST)
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            user = User.objects.first()
            topic.creator = user
            topic.save()
            message = form.cleaned_data.get('message')
            post = Post.objects.create(
                message=message,
                topic=topic,
                creator=user
            )
            return redirect('board_topics', board_id=board_id)

    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


@api_view(['GET'])
def topic_list(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def topic_detail(request, pk):
    topics = Topic.objects.get(pk=pk)
    serializer = TopicSerializer(topics, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def topic_create(request):
    serializer = TopicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("invalid ya m3lm")
    return Response(serializer.data)


@api_view(['POST'])
def topic_update(request, pk):
    topic = Topic.objects.get(pk=pk)
    serializer = TopicSerializer(instance=topic, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def topic_delete(request, pk):
    topic = Topic.objects.get(pk=pk)
    if topic:
        topic.delete()
        return Response('Deleted')
    else:
        return Response('not found')
