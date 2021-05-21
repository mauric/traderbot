import time
import requests


def telegram_bot_sendtext(bot_message):

    vacio = {}
    if bot_message != vacio:
        bot_token = '1823351793:AAHWr_BagmrTq1Fn6FUVt51KyKkGG8lG_sc'
        bot_chatID = '-540197197'
        send_text = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        return response.json()
