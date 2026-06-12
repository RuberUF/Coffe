from django.shortcuts import render
from . import forms
import pandas as pd
def home(request):
    exito="inicio"
    descripcion=""
    if request.method=="POST":
        form=forms.CoffeForms(request.POST,request.FILES)
        if form.is_valid():
            exito="exito"
            reporte=form.save()
            df=pd.read_csv(reporte.csv.path)
            descripcion=df.describe().to_json()
        else:
            exito="error"
    else:
        form=forms.CoffeForms()
    return render(request,"index.html",{"form":form,"exito":exito,"descripcion":descripcion})
