from django.contrib import admin
from django.urls import path
from movie_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.get_director_list),
    path('api/v1/directors/<int:dir_id>/', views.get_director_list),
    path('api/v1/movies/', views.get_movie_list),
    path('api/v1/movies/<int:movie_id>/', views.get_movie_list),
    path('api/v1/review/', views.get_review_list),
    path('api/v1/review/<int:review_id>/', views.get_review_list),
]