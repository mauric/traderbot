import time
import requests


def telegram_bot_sendtext(bot_message):

    vacio = {}
    if bot_message != vacio:
        bot_token = '1660167981:AAHMCMZ3lMdq3bv8SuCg727MsSpAheY2OMk'
        bot_chatID = '-584004372'
        send_text = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)

        return response.json()
