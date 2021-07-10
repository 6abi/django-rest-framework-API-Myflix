from rest_framework import serializers
from myflix.models import Programa

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = ['titulo', 'tipo', 'data_lancamento', 'likes']