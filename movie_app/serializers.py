from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'director'


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id', 'name'

class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'rating')

        def get_rating(self, obj):
            review_all = obj.movie_review.all()
            rate = [i.rate_stars for i in review_all]
            rate_avg = sum(rate) / len(rate)
            return rate_avg


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'rate_stars')

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie')

    class DirectorSerializer(serializers.ModelSerializer):
        movie_count = serializers.SerializerMethodField()

        class Meta:
            model = Director
            fields = ('id', 'name', 'movie_count')

        def get_movie_count(self, obj):
            return obj.movie_director.count()
