from telemessage_bridge.celery import app

from users.services import send_telegram_message


@app.task
def send_message(chat_id: int, username: str, text: str) -> None:
    send_telegram_message(chat_id, username, text)
