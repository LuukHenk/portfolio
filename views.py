import os
import re
from io import BytesIO
from xhtml2pdf import pisa
from markdown import markdown

from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.template.loader import get_template

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MD_FOLDER = PROJECT_ROOT + "/static/md_files/"
RESUME_PDF = PROJECT_ROOT+"/static/resume.pdf"

def index(request):
    context = {
        "biography_text": markdown(open(MD_FOLDER+"biography.md", "r").read())
    }
    return render(request, "myportfolio/index.html", context)

def resume(request):
    return render(request, "myportfolio/resume.html")


def resume_plain(request):
    # Obtain template
    resume_template = get_template("myportfolio/resume.html")
    html_page = resume_template.render()

    # Format template
    resume_start = re.split("<!-- Start resume -->", html_page)[1]
    resume_page = re.split("<!-- End resume -->", resume_start)[0]
    page_head = re.split("</head>", re.split("<head>", html_page)[1])[0]
    full_resume = "<html>{}<body>{}</body></html>".format(page_head, resume_page)

    return HttpResponse(full_resume)
