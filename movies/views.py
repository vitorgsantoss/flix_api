from django.db.models import Count, Avg
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from app.permissions import GlobalDefaultPermission
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieDetailSerializer
from reviews.models import Review


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer
        return MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = Movie.objects.all().count()
        movies_by_genres = Movie.objects.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.all().count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        return Response(
            data={
                'total_movies': total_movies,
                'movies_by_genres': movies_by_genres,
                'total_reviews': total_reviews,
                'average_stars': round(average_stars, 1) if average_stars else 0
            },
            status=200
        )
