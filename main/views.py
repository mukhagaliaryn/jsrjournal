from django.shortcuts import render, redirect, get_list_or_404
from main.forms import ReviewForm, ArticleForm
from main.models import Publisher, Review

from django.conf import settings
from django.core.mail import EmailMessage


# Main page
def index(request):
    last_publisher = get_list_or_404(Publisher)[:5]
    last_reviews = get_list_or_404(Review)[:3]
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    context = {
        'last_publisher': last_publisher,
        'last_reviews': last_reviews,
        'form': form
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
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            category = request.POST['category']
            item = form.cleaned_data['item']
            file = request.FILES['file']
            subject = full_name
            message = f"""
                ФИО контактного лица: {full_name}
                Email контактного лица: {email}
                Телефон: {phone}
                Научное направление: {category}
                Количество авторов: {item}
            """
            mail = EmailMessage(subject, message, email, [settings.EMAIL_HOST_USER])
            mail.attach(file.name, file.read(), file.content_type)
            mail.send()
            return redirect('pay')

    context = {
        'form': form
    }
    return render(request, 'main/article/create.html', context)


def article_payment(request):
    return render(request, 'main/article/payment.html', {})


# publishers page
def publishers(request):
    all_publisher = get_list_or_404(Publisher)

    return render(request, 'main/publishers.html', {'all_publisher': all_publisher})


# about page
def about(request):
    return render(request, 'main/about.html', {})
