from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test_response(request):
    return HttpResponse("To jest nasz pierwszy test")