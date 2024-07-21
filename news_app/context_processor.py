from .models import News, Categories


def latest_news(request):
    latest_news = News.published.all().order_by('-published_time')[:10]
    categories = Categories.objects.all()

    context = {
        'latest_news': latest_news,
        'categories': categories
    }
    return context