from django.shortcuts import render

def index(request):
    """Home page for the BoardgameForum."""
    return render(request, 'main/index.html')
