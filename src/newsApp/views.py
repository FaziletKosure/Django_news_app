from django.shortcuts import render
# from newsapi.newsapi_client import NewsApiClient
from newsapi import NewsApiClient
from decouple import config
# Create your views here.


def index(request):
    API_KEY = config("API_KEY")

    newsApi = NewsApiClient(api_key=API_KEY)
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
