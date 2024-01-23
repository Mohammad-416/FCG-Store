from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path('blog/<int:num>/', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('game-single', views.game_single, name='game-single'),
    path('games', views.games, name='games'),
    path('review', views.review, name='review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
