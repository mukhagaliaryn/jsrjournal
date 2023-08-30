from django.shortcuts import render


# Main page
def index(request):
    return render(request, 'main/index.html', {})


# payment page
def payment(request):
    return render(request, 'main/payment.html', {})


# article page
def article(request):
    return render(request, 'main/article.html', {})


# publishers page
def publishers(request):
    return render(request, 'main/publishers.html', {})


# about page
def about(request):
    return render(request, 'main/about.html', {})
