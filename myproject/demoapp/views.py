from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def myView(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pform")
    template_name  = "demoproject.html"
    context = {"form": form}
    return render(request, template_name, context)
