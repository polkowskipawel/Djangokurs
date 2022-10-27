from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wszystkie_filmy(request):
    # return HttpResponse("To jest nasz pierwszy test")

    return render(request, 'filmy.html', {'filmy': ['Avatar','Titanic']})