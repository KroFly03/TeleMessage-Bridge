from bot.tg.tg_client import TgClient


def send_telegram_message(chat_id: int, username: str, text: str) -> None:
    TgClient().send_message(chat_id=chat_id, text=f'{username}, я получил от тебя сообщение:\n{text}')
