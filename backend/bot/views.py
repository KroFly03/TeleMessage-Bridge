from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response

from bot.models import TgUser
from bot.serializers import TgUserSerializer
from bot.tg.tg_client import TgClient


class VerificationView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TgUserSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        tg_user: TgUser = serializer.save(user=request.user)

        TgClient().send_message(tg_user.chat_id, 'Код подтвержден')

        return Response(serializer.data)
