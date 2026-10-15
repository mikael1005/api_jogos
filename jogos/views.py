from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Jogo
from .serializers import JogoSerializer


class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all().order_by("titulo")
    serializer_class = JogoSerializer


@api_view(["GET"])
def estatisticas(request):
    total = Jogo.objects.count()

    disponiveis = Jogo.objects.filter(
        disponivel=True
    ).count()

    return Response({
        "total_jogos": total,
        "disponiveis": disponiveis,
        "indisponiveis": total - disponiveis,
    })