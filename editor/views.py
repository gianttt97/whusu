from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)


def login(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'login.html', {'form': form})
