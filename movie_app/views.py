from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Director, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer



# method GET, POST, PUT, PATCH, DELETE


@api_view(['GET'])
def get_director_list(request):
    director = Director.objects.all()
    serializer = DirectorSerializer(director, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_director_by_id(request, dir_id):
    director = Director.objects.get(id=dir_id)
    serializer = Director(director)
    return Response(serializer.data)


@api_view(['GET'])
def get_movie_list(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_movie_by_id(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    serializer = Movie(movie)
    return Response(serializer.data)


@api_view(['GET'])
def get_review_list(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_review_by_id(request, review_id):
    review = Review.objects.get(id=review_id)
    serializer = Review(review)
    return Response(serializer.data)