from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import NewsHeader,News



def news(request):
    news_header = NewsHeader.objects.first()
    all_news = News.objects.all()
    latest_news = News.objects.order_by('-publish_date')[:3]

    paginator = Paginator(all_news, 4)  # 4 news per page
    page = request.GET.get('page')

    try:
        news_page = paginator.page(page)
    except PageNotAnInteger:
        news_page = paginator.page(1)
    except EmptyPage:
        news_page = paginator.page(paginator.num_pages)

    context = {
        'news_header': news_header,
        'news_list': news_page,  # paginated news list
        'latest_news': latest_news,
    }
    return render(request, 'news.html', context)



def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    latest_news = News.objects.order_by('-publish_date')[:3]

    context = {
        'news': news_item,
        'latest_news': latest_news,
    }
    return render(request, 'news_detail.html', context)

