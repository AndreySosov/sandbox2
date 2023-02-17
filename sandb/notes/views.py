from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, ListView
from notes.forms import NoteForm
from notes.models import NoteContent
from django.http import JsonResponse


# Create your views here.
class UpdatePage(UpdateView):
    form_class = NoteForm
    model = NoteContent
    template_name = 'notes/editing_post.html'
    context_object_name = 'note'
    success_url = 'edit'

    def get_context_data(self, *, object_list=None, **kwargs):
        user_notes = NoteContent.objects.filter(user=self.request.user.id)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Дневник'
        context['user_notes'] = user_notes
        return context

class DeleteNote(DeleteView):
    form_class = NoteForm
    model = NoteContent
    template_name = 'main/account.html'
    context_object_name = 'note'
    success_url = '/account'

    def get(self, requests, *args, **kwargs):
        return self.delete(requests, *args, **kwargs)


def write_note(request):
    user_notes = NoteContent.objects.all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.date = datetime.today().strftime('%Y-%m-%d')
            form.save()
            return HttpResponseRedirect('account')
    else:
        form = NoteForm()
    return render(request, 'main/account.html', context={'form1': form, 'user_notes': user_notes})


class NotesList(LoginRequiredMixin, ListView):
    model = NoteContent
    template_name = 'main/account.html'
    context_object_name = 'notes'


def editing_note(request, pk):
    user_notes = NoteContent.objects.filter(user=request.user.id).reverse()
    reversed_result = reversed(list(user_notes))
    note = NoteContent.objects.get(id=pk)
    return render(request, 'notes/editing_post.html', context={'user_notes': reversed_result, 'note': note})


def delete_note(request, pk):
    user_note = NoteContent.object.get(id=pk)
    user_note.delete()
    return redirect('/accaunt')


def delete_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        NoteContent.objects.filter(id=post_id).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def post_search(request):
    query = request.GET.get('query')
    if query:
        results = NoteContent.objects.filter(title__icontains=query)
    else:
        results = []
    return render(request, 'notes/note_search.html', {'query': query, 'results': results})