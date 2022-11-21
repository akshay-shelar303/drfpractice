from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def myView(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show")
    template_name  = "demoproject.html"
    context = {"form": form}
    return render(request, template_name, context)

def showView(request):
    projects = Project.objects.all()
    template_name = "show.html"
    context = {"projects": projects}
    return render(request, template_name, context)

