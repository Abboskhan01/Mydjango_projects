from django.shortcuts import render
from django.http import HttpResponse
from .models import Author


def authors_list(request):
    authors = Author.objects.all()
    print(authors)
    author_list = ""
    for author in authors:
        author_list += f"<li>{author}</li>"
    return HttpResponse(f"<ul>{author_list}</ul>")
