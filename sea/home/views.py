from django.shortcuts import render

# Create your views here.
#create a view for home page of the website with some context paased with it
def home(request):
    context = {'home': 'active'}
    return render(request, 'home/home.html', context)
