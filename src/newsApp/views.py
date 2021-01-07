from django.shortcuts import render
# from newsapi.newsapi_client import NewsApiClient
from newsapi import NewsApiClient
# Create your views here.


def index(request):
    newsApi = NewsApiClient(api_key='aa6faeccad2842839353d4b050bb5768')
    headLines = newsApi.get_top_headlines(sources='ign, cnn')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, "newsApp/index.html", context={"mylist": mylist})
