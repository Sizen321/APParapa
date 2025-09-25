from django.urls import path
app_name = 'main'


from main import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
]