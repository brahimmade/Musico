import requests
from .models import TeleSettings


def sendTelegram(tg_text, tg_name, tg_email):
    if TeleSettings.objects.get():
        settings = TeleSettings.objects.get()
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}') + 1:text.rfind('{')]
            part_3 = text[text.rfind('}'): -1]

            text_slise = part_1 + tg_text + part_2 + tg_name + part_3
        else:
            text_slise = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slise,
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки!')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Все ОК, сообщение отправлено')
    else:
        pass
