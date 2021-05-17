import time
import requests
# api for bot

# 1324149025:AAHpWkMTl4bf44axyMbAUPXDypbpygJ9GqU


def telegram_bot_sendtext(bot_message):

    vacio = {}
    if bot_message != vacio:
        bot_token = '1823351793:AAHWr_BagmrTq1Fn6FUVt51KyKkGG8lG_sc'
        #bot_token = '1324149025:AAHpWkMTl4bf44axyMbAUPXDypbpygJ9GqU'
        #bot_chatID = '558759156'
        bot_chatID = '-540197197'
        send_text = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
            #bot_chatID = '558759156'e
            #send_text = 'https://api.telegram.org/bot' + bot_token + \
                #'/sendMessage?chat_id=' + bot_cheatID + '&parse_mode=Markdown&text=' + bot_message
            #response = requests.get(send_text)eeeeeeeeeeee

        return response.json()
