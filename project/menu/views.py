from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html', {'title': 'Home'})


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def services(request):
    return render(request, 'services.html', {'title': 'Services'})


def web_development(request):
    return render(request, 'web_development.html', {'title': 'Web Development'})


def seo(request):
    return render(request, 'seo.html', {'title': 'SEO'})
