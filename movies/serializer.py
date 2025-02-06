from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def get_rate(self, obj):
        reviews = obj.reviews.all()
        return 5

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError("Favor não lançar filmes antes de 1980")
        return value
    
    def validate_resume(self, value):
        if len(value) > 300:
            raise serializers.ValidationError("Resumo não suporta mais de 200 caracteres.")
        return value