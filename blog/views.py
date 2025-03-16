from django.shortcuts import render, redirect
from .models import Autor, Articulo, Comentario
from .forms import AutorForm, ArticuloForm, ComentarioForm, BusquedaArticuloForm

def inicio(request):
    return render(request, "blog/inicio.html")

def agregar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = AutorForm()
    return render(request, "blog/formulario.html", {"form": form})

def agregar_articulo(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ArticuloForm()
    return render(request, "blog/formulario.html", {"form": form})

def agregar_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ComentarioForm()
    return render(request, "blog/formulario.html", {"form": form})

def buscar_articulo(request):
    form = BusquedaArticuloForm()
    articulos = None
    if request.GET.get("titulo"):
        articulos = Articulo.objects.filter(titulo__icontains=request.GET["titulo"])
    return render(request, "blog/buscar.html", {"form": form, "articulos": articulos})
