from django.shortcuts import render

# Create your views here.
def index(request):
    """ 
    View that displays the index page.
    """
    return render(request, "index.html")