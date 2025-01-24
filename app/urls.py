from django.contrib import admin
from django.urls import path, include
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetriveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetriveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('genres.urls')),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),

    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetriveUpdateDestroyView.as_view(), name='movie-detail-view'),

    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetriveUpdateDestroyView.as_view(), name='review-detail-view'),
]
