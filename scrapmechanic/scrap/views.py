from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import *
from .utils import *

class mod (ListView):
    model = mods
    extra_context = {'title':'Моды'}
    template_name = 'scrap/mods.html'



def main(request):
    return render(request, 'scrap/main.html')

def test(request):
    return render(request, 'scrap/base.html')

def profile(request):
    return render(request, 'scrap/profile.html')

def about(request,slug):
    post = mods.objects.get(slug=slug)
    comments = post.comments.filter(active=True).order_by('-created')
    if request.method == 'POST':

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user.username
            new_comment.email = request.user.email
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'scrap/about.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'scrap/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('mainpage')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'scrap/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'логин'
        return context
    # def get_success_url(self):
    #     return reverse_lazy('mainpage')

def LogoutUser(request):
    logout(request)
    return redirect('mainpage')


