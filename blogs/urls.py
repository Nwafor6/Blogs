from .import views
from django.urls import path 
app_name = 'blogs'
urlpatterns = [
    

    path('', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('post_detil/<str:pk>/', views.post_detil, name='post_detil'),
    path('update_detil/<str:pk>/', views.updatecomment, name='update_detil'),
    path('comment_reply/<str:pk>/', views.replycomment, name='comment_reply'),

 ]