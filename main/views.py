from django.shortcuts import render, redirect
# from .models import Task
from .forms import UserForm
from django.http import HttpResponse
from .models import Post

def index(request):
	return render(request, 'main/Simple Resume.html')

def about(request):
	return render(request, 'main/Adaptive Resume.html')

def paint(request):
	return render(request, 'main/Творче резюме.html')

def paintAdaptive(request):
	return render(request, 'main/Творче Адаптивне резюме.html')






def post_list(request):
	post = Post.objects.filter()
	return render(request, "main/post_list.html", {"posts": post})
