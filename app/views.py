from django.shortcuts import render
from . import forms
def home(request):
    if request.method=="POST":
        form=forms.CoffeForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.CoffeForms
    return render(request,"index.html",{"form":form})
