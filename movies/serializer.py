from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1980:
            raise serializers.ValidationError("Favor não lançar filmes antes de 1980")
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("Resumo não suporta mais de 200 caracteres.")
        return value