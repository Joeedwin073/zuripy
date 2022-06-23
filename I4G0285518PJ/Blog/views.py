from django import views
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from python_assignments.zuripy.I4G0285518PJ.Blog.models import Post


# Create your views here.

class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy("blog:all")

