from datetime import datetime

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import LoginUserForm, RegisterUserForm
from notes.forms import NoteForm
from notes.models import NoteContent


# Create your views here.
class HomePage(CreateView):
    form_class = NoteForm
    model = NoteContent
    template_name = 'main/account.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        user_notes = NoteContent.objects.filter(user=self.request.user.id)
        form = NoteForm()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Дневник'
        context['user_notes'] = user_notes
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = NoteForm(request.POST)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            self.object.save()
            return HttpResponseRedirect('account')
        return render(request, 'main/account.html', context={'form': form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')



def main(request):
    return render(request, 'main/main.html')


def auth(request):
    return render(request, 'main/login.html')


def index(request):
    return render(request, 'main/account.html')