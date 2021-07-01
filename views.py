from markdown import markdown

from django.urls import reverse
from django.shortcuts import render

MD_FOLDER = "./myportfolio/static/md_files/"

def index(request):
    context = {
        "biography_text": markdown(open(MD_FOLDER+"biography.md", "r").read())
    }
    return render(request, "myportfolio/index.html", context)

def resume(request):
    context = {
        "bioinf_uu_text": markdown(open(MD_FOLDER+"bioinf_uu.md", "r").read())
    }
    return render(request, "myportfolio/resume.html", context)
