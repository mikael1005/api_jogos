from datetime import date
from rest_framework import serializers
from .models import Jogo


class JogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jogo
        fields = [
            "id",
            "titulo",
            "genero",
            "plataforma",
            "ano_lancamento",
            "preco",
            "disponivel",
        ]
        read_only_fields = ["id"]

    def validate_ano_lancamento(self, valor):
        if valor > date.today().year:
            raise serializers.ValidationError(
                "O ano não pode estar no futuro."
            )
        return valor

    def validate_preco(self, valor):
        if valor < 0:
            raise serializers.ValidationError(
                "O preço não pode ser negativo."
            )
        return valor