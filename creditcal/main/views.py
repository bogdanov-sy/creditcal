from django.shortcuts import render
from django.http import HttpResponse

from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def main(request):
    return render(request, 'main/index.html', {})