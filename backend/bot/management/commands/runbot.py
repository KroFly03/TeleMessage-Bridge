from django.core.management import BaseCommand

from bot.models import TgUser
from bot.tg.schemas import Message
from bot.tg.tg_client import TgClient


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = TgClient()

    def handle(self, *args, **options) -> None:
        offset = 0

        self.stdout.write(self.style.SUCCESS('Bot started'))
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                self.handle_message(item.message)

    def handle_message(self, message: Message) -> None:
        tg_user, _ = TgUser.objects.get_or_create(chat_id=message.chat.id)

        if tg_user.user:
            self.tg_client.send_message(tg_user.chat_id, 'Вы уже успешно подтвердили аккаунт.')
        else:
            self.tg_client.send_message(tg_user.chat_id,
                                        f'Приветствую!\n'
                                        f'Чтобы использовать данного бота, '
                                        f'необходимо подтверидить аккаунт на сайте с помощью кода.')

            tg_user.update_verification_code()
            self.tg_client.send_message(tg_user.chat_id, f'Ваш код подтверждения: {tg_user.verification_code}.')
