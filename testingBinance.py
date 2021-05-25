import sendMessages as sm
import time
import core as bot



if __name__ == '__main__':
    while True:
        alert_list = []
        i = 0
        for coin in futures_coin_list:
            i = i+1
            bot.get_signal(symbol=coin)
            if(len(alert_list)) > 10:
                sm.telegram_bot_sendtext(str(alert_list))
                alert_list = []
            if(i >= max_stock_number):
                sm.telegram_bot_sendtext(str(alert_list))
                break

    print("list:"+str(alert_list))
    time.sleep(300)





