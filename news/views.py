from django.shortcuts import render
from .models import News

# Create your views here.


def NewsIndex(request):
    right_nav_news = News.objects.filter('pub_date')[:3]
    return render(request, 'pages/index.html', {'right_nav_news': right_nav_news})
