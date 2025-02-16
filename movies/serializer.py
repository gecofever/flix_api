from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None

        # reviews = obj.reviews.all()

        # if reviews:
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count = reviews.count()

        #     return round(sum_reviews / reviews_count, 1)
        
        # return None

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError("Favor não lançar filmes antes de 1980")
        return value
    
    def validate_resume(self, value):
        if len(value) > 300:
            raise serializers.ValidationError("Resumo não suporta mais de 200 caracteres.")
        return value