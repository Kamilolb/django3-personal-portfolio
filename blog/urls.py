from django.urls import path
from . import views              # the . allows the program to import from other files within the same parent folder


app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
    path('<int:blog_id>/', views.detail, name="detail"),
]
