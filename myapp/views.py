from django.shortcuts import render
from .models import People
from myapp.filters import PeopleFilter
# Create your views here.

def index(request):
    #all_people = People.objects.all()
    people_filter = PeopleFilter(request.GET)
    #return render(request, 'index.html', {'all_people':all_people})
    return render(request, 'index.html', {'people_filter':people_filter})