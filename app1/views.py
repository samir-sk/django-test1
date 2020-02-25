from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView
from django.http.response import HttpResponseRedirect
from app1.models import MyProfile, MyPost, PostComment, PostLike, FollowUser




class HomeView(TemplateView):
    template_name="app1/home.html"


class AboutView(TemplateView):
    template_name="app1/about.html"


class ContactView(TemplateView):
    template_name="app1/contact.html"














