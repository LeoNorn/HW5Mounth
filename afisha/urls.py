from django.contrib import admin
from django.urls import path
from movie_app import views
from users.views import RegisterAPIView, ConfirmAPIView, LoginAPIView
from movie_app.views import DirectorAPIView, MovieAPIView, ReviewAPIView, ReviewMovieAPIView,\
    DirectorDetailAPIVIew, MovieDetailAPIVIew, ReviewDetailAPIView
from afisha.drf_yasg import urlpatterns as yasg_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIVIew.as_view()),
    path('api/v1/movies/', views.MovieAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailAPIVIew.as_view()),
    path('api/v1/review/', views.ReviewAPIView.as_view()),
    path('api/v1/review/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('api/v1/movie/review/', views.ReviewMovieAPIView.as_view()),
    path('api/v1/register_view/', RegisterAPIView.as_view()),
    path('api/v1/confirm_view/', ConfirmAPIView.as_view()),
    path('api/v1/login_view/', LoginAPIView.as_view()),
] + yasg_patterns