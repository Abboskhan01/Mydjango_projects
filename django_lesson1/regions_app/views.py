from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def main(request, main=None):
    html = f"""
    <h1>About Uzbekstan</h1>
    """
    return HttpResponse(f"Salom {main}")


def regionsVIEW(request, region):
    return HttpResponse(f"Region {region}")

