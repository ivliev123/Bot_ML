import parsingProxy
import telepot
import time
from telepot.loop import MessageLoop
import urllib3
import pickle
import numpy as np

import test_model

global token

import argparse






ap = argparse.ArgumentParser()
ap.add_argument("-t", "--token", default='',
	help="token of telegram bot")

args = vars(ap.parse_args())


print(args["token"])


flag = None

token=args["token"]


with open('/home/ivliev/Bot_ML/label_class.pickle', 'rb') as f:
    label_class = pickle.load(f)


def logWrite(n):
    try:
        file=open('log.txt','a')
    except:
        file=open('log.txt','w')
    if n!='-------------------------':
        file.write(str(n)+' | '+time.ctime(time.time())+'\n\n')
    else:
        file.write(str(n)+'\n\n')
    file.close()

def handle(msg):
    global label_class
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    # if content_type == 'text':
    #     bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

    if content_type == 'photo':
        print(msg["photo"])
        file_name_ ='_' + str(chat_id) + "file.png"
        bot.download_file(msg['photo'][0]['file_id'], file_name_)

        bot.sendMessage(chat_id, "Обрабатываю")
        time.sleep(3)
        # result = test_model.recognition("file.png")
        #
        # label_class = np.array(label_class)
        # label = label_class[:,0]
        # label = list(label)
        # i_nn = label.index(str(result))

        result = test_model.predictions_out(file_name_, label_class)
        str_out = ''
        for i in range(len(result)):
            str_out += str(result[i][0]) + ' - ' + str(round(result[i][1],2)) + '%; '


        bot.sendMessage(chat_id, str_out)
        # bot.sendMessage(chat_id, str(label_class[i_nn][1]))





def get_proxy():
    print('Запрос списка proxy')
    urls=parsingProxy.search()
    for i in urls:
        print('Проверяем proxy ',i)
        telepot.api.set_proxy(i)
        bot = telepot.Bot(token)
        try:
            bot.getMe()
        except:
            print('Ошибка')
        else:
            logWrite('*Готово '+i)
            print('Готово')
            return i
    logWrite('Ошибка подключения к proxy')
    return 'none'

i=get_proxy()
telepot.api.set_proxy(i)
bot = telepot.Bot(token)

MessageLoop(bot, handle).run_as_thread()
logWrite('Ожидание...')
print('Ожидание...')

while True:
    # if flag == 1:
    #     result = test_model.recognition("file.png")
    #     flag = 0

    try:
        bot.getMe()
        print (bot.getMe())
        # print (bot.getUpdates())

    except:
        print('Ошибка. Перезапуск proxy.')
        logWrite('Ошибка. Перезапуск proxy.')
        i=get_proxy()
        telepot.api.set_proxy(i)
        bot = telepot.Bot(token)
        print (bot.getMe())





    time.sleep(1)
