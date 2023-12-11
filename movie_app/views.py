from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Director, Review
from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieDetailSerializer, \
    DirectorDetailSerializer, \
    ReviewDetailSerializer, DirValidateSerializer, MovieReviewSerializer


@api_view(['GET', 'POST'])
def get_director_list(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True).data
        return Response(data=serializer, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_director_by_id(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response({f"Директора с id {id} не существует"}, status=404)

    if request.method == 'GET':
        serializer = DirectorDetailSerializer(instance=director, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DirValidateSerializer(instance=director, data=request.data)
        serializer.is_valid(raise_exception=True)
        director = serializer.update(instance=director, validated_data=serializer.validated_data)

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
        movie = Movie.objects.all()

        search = request.query_params.get('search', None)
        if search is not None:
            movie = movie.filter(title__icontains=search)

        serializer = MovieSerializer(instance=movie, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DirValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = serializer.save()

        serializer = MovieSerializer(instance=movie, many=False)

        return Response(
            {
                "message": "Created!",
                "data": serializer.data
            },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
def get_movie_by_id(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response({f'Фильма с id {id} не существует'}, status=404)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(instance=movie, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MovieDetailSerializer(instance=movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = serializer.update(instance=movie, validated_data=serializer.validated_data)

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
        review = Review.objects.all()

        search = request.query_params.get('search', None)
        if search is not None:
            review = review.filter(title__icontains=search)

        serializer = ReviewSerializer(instance=review, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()

        serializer = ReviewSerializer(instance=review, many=False)

        return Response(
            {
                "message": "Created!",
                "data": serializer.data
            },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
def get_review_by_id(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response({f"Отзыва с id {id} не существует"}, status=404)

    if request.method == 'GET':
        serializer = ReviewDetailSerializer(instance=review, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ReviewDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save()

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


@api_view(['GET'])
def review_movie(request):
    review_m = Movie.objects.all()
    serializer = MovieReviewSerializer(review_m, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)