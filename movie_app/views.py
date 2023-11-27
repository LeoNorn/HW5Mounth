from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Director, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer,\
    MovieDetailSerializer, DirectorDetailSerializer, ReviewDetailSerializer



# method GET, POST, PUT, PATCH, DELETE


@api_view(['GET', 'POST'])
def get_director_list(request):
    if request.method == 'GET':
        director = Director.objects.all() \
            .select_related('review') \
            .prefetch_related('director', 'movie')

        search = request.query_params.get('search', None)
        if search is not None:
            name = director.filter(title__icontains=search)

        serializer = DirectorSerializer(instance=name, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.objects.create(
            name=name
        )
        director.name.set(name)

        serializer = DirectorSerializer(instance=name, many=False)

        return Response(
            {
                "message": "Created!",
                "data": serializer.data
            },
            status=201
        )


@api_view(['GET', 'PUT', 'DELETE'])
def get_director_by_id(request, dir_id):
    try:
        director = Director.objects.get(id=dir_id)
    except Director.DoesNotExist:
        return Response({f"Директора с id {dir_id} не существует"}, status=404)

    if request.method == 'GET':
        serializer = DirectorDetailSerializer(instance=director, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        director.name = request.data.get('name', director.name)

        director.save()

        serializer = DirectorDetailSerializer(instance=director, many=False)

        return Response(
            data={
                "message": "updated!",
                "data": serializer.data
            },
            status=200
        )

    if request.method == 'DELETE':
        director.delete()
        return Response(
            data={
                'message': 'deleted'
            },
            status=204
        )


@api_view(['GET','POST'])
def get_movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all() \
            .select_related('review') \
            .prefetch_related('director', 'movie')

        search = request.query_params.get('search', None)
        if search is not None:
            movie = movie.filter(title__icontains=search)

        serializer = MovieSerializer(instance=movie, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        director = request.data.get('director')
        duration = request.data.get('duration', [])

        movie = Movie.objects.create(
            title=title,
            description=description,
            director=director,
        )
        movie.duration.set(duration)

        serializer = MovieSerializer(instance=movie, many=False)

        return Response(
            {
                "message": "Created!",
                "data": serializer.data
            },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
def get_movie_by_id(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({f'Фильма с id {movie_id} не существует'}, status=404)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(instance=movie, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        movie.title = request.data.get('tite', movie.title)
        movie.description = request.data.get('description', movie.description)
        movie.director = request.data.get('director', movie.director)

        duration = request.data.get('duration', movie.duration.all())
        movie.duration.set(duration)

        movie.save()

        serializer = MovieDetailSerializer(instance=movie, many=False)

        return Response(
            data={
                "message": "updated!",
                "data": serializer.data
            },
            status=200
        )

    if request.method == 'DELETE':
        movie.delete()
        return Response(
            data={
                'message': 'deleted'
            },
            status=204
        )

@api_view(['GET', 'POST'])
def get_review_list(request):
    if request.method == 'GET':
        review = Review.objects.all() \
            .select_related('review') \
            .prefetch_related('director', 'movie')

        search = request.query_params.get('search', None)
        if search is not None:
            review = review.filter(title__icontains=search)

        serializer = ReviewSerializer(instance=review, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        rate_stars = request.data.get('stars', [])

        review = Review.objects.create(
            text=text,
            movie=movie,
            rate_stars=rate_stars
        )

        review.rate_stars.set(rate_stars)

        serializer = ReviewSerializer(instance=review, many=False)

        return Response(
            {
                "message": "Created!",
                "data": serializer.data
            },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
def get_review_by_id(request, review_id):
    try:
        review = Review.objects.filter(id=review_id)
    except Review.DoesNotExist:
        return Response({f"Отзыва с id {review_id} не существует"}, status=404)

    if request.method == 'GET':
        serializer = ReviewDetailSerializer(instance=review, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        review.text = request.data.get('text', review.title)
        review.movie = request.data.get('movie', review.content)
        review.rate_stars = request.data.get('rate_stars', review.category_id)

        review.save()

        serializer = ReviewDetailSerializer(instance=review, many=False)

        return Response(
            data={
                "message": "updated!",
                "data": serializer.data
            },
            status=200
        )

    if request.method == 'DELETE':
        review.delete()
        return Response(
            data={
                'message': 'deleted'
            },
            status=204
        )