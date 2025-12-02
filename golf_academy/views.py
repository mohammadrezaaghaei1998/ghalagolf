from django.shortcuts import render

# Create your views here.
def golf_academy(request):
   

    # context = {
    #     'news': news_item,
    #     'latest_news': latest_news,
    # }
    return render(request, 'golf_academy.html')

