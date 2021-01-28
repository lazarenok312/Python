from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import RegistrationForm

from .models import Post, Comment

# Create your views here.
class IndexView(generic.ListView):
    template_name = "blog/index.html"

    def get_queryset(self):
        return None
    

class PostView(generic.ListView):
    template_name = "blog/posts.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=context["post"]) 
        return context

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

class RegisterView(generic.edit.FormView):
    form_class = RegistrationForm
    success_url = "blog/login/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)
    
    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)


def create_comment(request):
    return redirect("/posts")
