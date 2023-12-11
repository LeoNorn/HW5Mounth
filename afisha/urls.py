from django.contrib import admin
from django.urls import path
from movie_app import views
from users.views import register_view, confirm_view, login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.get_director_list),
    path('api/v1/directors/<int:id>/', views.get_director_by_id),
    path('api/v1/movies/', views.get_movie_list),
    path('api/v1/movies/<int:id>/', views.get_movie_by_id),
    path('api/v1/review/', views.get_review_list),
    path('api/v1/review/<int:id>/', views.get_review_by_id),
    path('api/v1/movie/review/', views.review_movie),
    path('api/v1/register_view/', register_view),
    path('api/v1/confirm_view/', confirm_view),
    path('api/v1/login_view/', login_view),
]