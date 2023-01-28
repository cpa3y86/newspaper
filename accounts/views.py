from django.shortcuts import render


def default_page(request):
    return render(request, 'default.html')


def contacts(request):
     return render(request, 'contacts.html')


def news(request):
    return render(request, 'news.html')

def articles(request):
     return render(request, 'articles.html')

def about(request):
    return render(request, 'about.html')