from django.shortcuts import render, redirect, get_list_or_404

from main.forms import ArticleForm
from main.models import Publisher


# Main page
def index(request):
    last_publisher = get_list_or_404(Publisher)[:5]

    context = {
        'last_publisher': last_publisher
    }

    return render(request, 'main/index.html', context)


# payment page
def payment(request):
    return render(request, 'main/payment.html', {})


# article page
def article(request):
    return render(request, 'main/article/index.html', {})


def article_create(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {
        'form': form
    }
    return render(request, 'main/article/create.html', context)


# publishers page
def publishers(request):
    all_publisher = get_list_or_404(Publisher)

    return render(request, 'main/publishers.html', {'all_publisher': all_publisher})


# about page
def about(request):
    return render(request, 'main/about.html', {})
