from django.urls import path
from .views import homePageView, ContactPageView, errorPageView, news_detail, HomePageView, news_list,  \
    LocalNewsView, ForeignNewsView, TechnologyNewsView, SportNewsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('error/', errorPageView, name='error_page'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('news/', news_list, name='all_news_list'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_news_page'),
    path('technology/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
]