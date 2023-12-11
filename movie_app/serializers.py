from rest_framework import serializers
from movie_app.models import Director, Movie, Review, stars


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'rate_stars')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director']



class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class MovieReviewSerializer(serializers.ModelSerializer):
        reviews = ReviewDetailSerializer(many=True, read_only=True)
        rating = serializers.SerializerMethodField()
        class Meta:
            model = Movie
            fields = ['id', 'title', 'description', 'duration', 'director', 'reviews', 'rating']
        def get_rating(self, obj):
            review_all = obj.reviews.all()
            rate = [i.rate_stars for i in review_all]
            rate_avg = sum(rate) / len(rate)
            return rate_avg

class DirValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)

    def validate_dir(self, value: int):
        try:
            Director.objects.get(id=value)
        except Director.DoesNotExist:
            raise serializers.ValidationError('Режиссер не найден!')
        return value

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Укажите режиссера!')
        return value

    def create(self, validated_data):
        name = validated_data.get('name')

        name = Director.objects.create(
            name=name
        )

        return name

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()

        return instance


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=10)
    description = serializers.CharField()
    duration = serializers.CharField(max_length=10)
    director = serializers.CharField()

    def validate_movie(self, value: int):
        try:
            Movie.objects.get(id=value)
        except Movie.DoesNotExist:
            raise serializers.ValidationError('Фильм не найден!')
        return value

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Длина заголовка должна быть больше 10 символов')
        return value

    def create(self, validated_data):
        title = validated_data.get('title')
        description = validated_data.get('description')
        duration = validated_data.get('duration', [])
        director = validated_data.get('director')

        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director=director
        )

        movie.duration.set(duration)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.director = validated_data.get('director', instance.director)

        duration = validated_data.get('duration', instance.duration.all())
        instance.duration.set(duration)

        instance.save()

        return instance


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.CharField()

    def validate_review(self, value: int):
        try:
            Review.objects.get(id=value)
        except Review.DoesNotExist:
            raise serializers.ValidationError('Обзор не найден!')
        return value

    def validate_text(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Длина заголовка должна быть больше 10 символов')
        return value

    def create(self, validated_data):
        rate_stars = validated_data.get('rate_stars')
        text = validated_data.get('text')
        movie = validated_data.get('movie')

        review = Review.objects.create(
            rate_stars=rate_stars,
            text=text,
            movie=movie,
        )

        review.review.set(review)

        return review

    def update(self, instance, validated_data):
        instance.rate_stars = validated_data.get('rate_stars', instance.rate_stars)
        instance.text = validated_data.get('text', instance.text)
        instance.movie = validated_data.get('movie', instance.movie)

        instance.save()

        return instance
