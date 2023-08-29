from django.shortcuts import render


# Main page
def index(request):
    return render(request, 'main/index.html', {})
