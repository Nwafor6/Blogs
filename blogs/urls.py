from .import views
from django.urls import path 
app_name = 'blogs'
urlpatterns = [
    
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('post_detil/<str:pk>/', views.post_detil, name='post_detil'),
    path('update_detil/<str:pk>/', views.updatecomment, name='update_detil'),
    path('comment_reply/<str:pk>/', views.replycomment, name='comment_reply'),
    path('delete_comment/<str:pk>/', views.deletecomment, name='delete_comment'),
    path('delete_reply/<str:pk>/', views.deletereply, name='delete_reply'),
    path('update_reply/<str:pk>/', views.updatereply, name='update_reply'),
    # Help section urls
    path('Edu-help/', views.roomMate, name='Edu-help'),
    path('Edu-help-del/<str:pk>/', views.roommateDelete, name='Edu-help-del'),
    path('Edu-help-edit/<str:pk>/', views.editroommatePost, name='Edu-help-edit'),
    # Advertisment Urls
    path('carousel/', views.carousel, name='carousel'),



 ]