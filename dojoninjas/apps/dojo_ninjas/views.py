from django.shortcuts import render
from . models import Dojo, Ninja

# Create your views here.
def index(request):
    return render(request, 'dojo_ninjas/index.html')

def process(request):
    newdojo = Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
        desc = request.POST['desc']
    )
    return redirect('/')

def create_ninja(request):
    newninja = Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name']
    )
    return redirect('/')
    

    

    return redirect('/')