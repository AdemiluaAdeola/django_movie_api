from .models import *
from rest_framework import serializers

class CategoryListSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedIdentityField(
        view_name="movie_list",
        lookup_field = "name",
    )
    
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "movies",
            "series",
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "image",
            "title",
        ]

class MovieDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = [
            "id",
            "image",
            "title",
            "uploaded_at",
            "description",
            "category",
        ]

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "movie_url",
            "title",
            "uploaded_at",
            "description",
        ]

class SeriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = [
            "id",
            "image",
            "title",
        ]

class SeasonListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Season
        fields = [
            "category",
            "id",
            "image",
            "title",
        ]

class EpisodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = [
            "id",
            "image",
            "title",
        ]

class SeasonDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    episodes = EpisodeListSerializer(many=True, read_only=True)
    class Meta:
        model = Season
        fields = [
            "id",
            "image",
            "title",
            "description",
            "category",
            "episodes"
        ]
