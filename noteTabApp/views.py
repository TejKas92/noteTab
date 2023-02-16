from django.shortcuts import render
from .models import Note
from .forms import NoteForm

def landingView(request):
    context = {}

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            new_score = Note()
            new_score.student = form.cleaned_data.get('student')
            new_score.note = form.cleaned_data.get('note')

    context['notes'] = Note.objects.all()
    context['form'] = NoteForm()

    return render(request, 'noteTabApp/index.html', context)