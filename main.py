import parsingProxy
import telepot
import time
from telepot.loop import MessageLoop
import urllib3

import test_model

global token
global result
global flag

flag = None

token='921261036:AAEc45igFmQDo2BtHp_lpk9jBmLq_vDhy00'




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
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

    if content_type == 'photo':
        print(msg["photo"])
        # bot.sendMessage(chat_id, "You said '{}'".format(msg["photo"]))
        bot.download_file(msg['photo'][0]['file_id'], 'file.png')
        # flaf = 1
        bot.sendMessage(chat_id, "Обрабатываю")
        result = test_model.recognition("file.png")
        # if flag == 0:
        bot.sendMessage(chat_id, str(result))

    # if content_type == 'document':
    #     # print()
    #     print(msg["document"])
    #     bot.download_file(msg['document'][0]['message']['document']['thumb']['file_id'], 'file.png')




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
        print (bot.getUpdates())

    except:
        print('Ошибка. Перезапуск proxy.')
        logWrite('Ошибка. Перезапуск proxy.')
        i=get_proxy()
        telepot.api.set_proxy(i)
        bot = telepot.Bot(token)
        print (bot.getMe())





    time.sleep(1)
