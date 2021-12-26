import telebot

token="5010861931:AAH6cfS6eLVGNP6tEen3EkoWKwdyLmRBJ8M"
bot=telebot.TeleBot(token)


# Объявления переменных
smile='📩'
jija_now='  '
basket_real=[" "]
basket_real_str=" "
id_SLAVA=1213080030
id_MY=858375713


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row("Продолжить")

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row("Каталог")

keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row("Rick and Morty")
keyboard3.row("Mad")
keyboard3.row("Boshki")
keyboard3.row("Одноразка 'elf bar'")
keyboard3.row("Очистить корзину")
keyboard3.row("Показать корзину")
keyboard3.row("Отправить заказ"+smile)

keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row("🔙")
keyboard4.row("Лесные ягоды", "Киви+кактус+яблоко")
keyboard4.row("Смородина+черника+гранат+земляника")
keyboard4.row("Мишки желейные", "Апельсин+помело")
keyboard4.row("Клюква", "Ягодный пирог")
keyboard4.row("Фруктовый лимонад", "Грейпфрут+черника")
keyboard4.row("Очистить корзину")
keyboard4.row("Показать корзину")
keyboard4.row("Отправить заказ"+smile)

array_rick_and_morty=["Лесные ягоды", "Киви+кактус+яблоко", "Смородина+черника+гранат+земляника", "Мишки желейные", "Апельсин+помело", "Клюква", "Ягодный пирог", "Фруктовый лимонад", "Грейпфрут+черника"]

keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
keyboard5.row("🔙")
keyboard5.row("Яблоко", "Бабл-гам")
keyboard5.row("Киви", "Манго ледяное")
keyboard5.row("Виноград", "Личи")
keyboard5.row("Лесные ягоды", "Тропический микс")
keyboard5.row("Очистить корзину")
keyboard5.row("Показать корзину")
keyboard5.row("Отправить заказ"+smile)

array_mad=["Яблоко", "Бабл-гам", "Киви", "Манго ледяное", "Виноград", "Личи", "Лесные ягоды", "Тропический микс"]

keyboard6 = telebot.types.ReplyKeyboardMarkup(True)
keyboard6.row("Минск", "Червень")

keyboard7 = telebot.types.ReplyKeyboardMarkup(True)
keyboard7.row("🔙")
keyboard7.row("Добрые", "Злые")
keyboard7.row("Бодрые", "Сладкие")
keyboard7.row("Очистить корзину")
keyboard7.row("Показать корзину")
keyboard7.row("Отправить заказ"+smile)

array_boshki=["Добрые", "Злые", "Бодрые", "Сладкие"]



def send(id, text, keyboard):
    bot.send_message(id, text, reply_markup = keyboard)

def send_photo(id):
    bot.send_photo(id, photo=open('photo5348309529038799169.jpg', 'rb'), caption="Жидкость 'Rick and Morty' \n 50 солей\n 2% никотина\n Цена: 14.50 BYN")
    bot.send_photo(id, photo=open('photo5348309529038799170.jpg', 'rb'), caption="Жидкость 'Mad' \n 60 солей\n 6% никотина\n Цена: 14.00 BYN")
    bot.send_photo(id, photo=open('photo5350561328852482244.jpg', 'rb'), caption="Жидкость 'Boshki' \n 45 солей\n 6% никотина\n Цена: 15.00 BYN")
    bot.send_photo(id, photo=open('photo5350561328852482246.jpg', 'rb'), caption="Одноразка 'Elf Bar' \n 1500 lux (оригинал)\n Цена: 17.00 BYN")

@bot.message_handler(commands = ['start'])
def start(message):
     send(message.chat.id, "Привет. Я бот, который поможет тебе найти подходящую жидкость и оформить заказ. Работаю в Минске и Червене.", keyboard1)


@bot.message_handler(commands = ['clean'])
def start(message):
     send(message.chat.id, "Корзина очищена", keyboard1)



@bot.message_handler(content_types = ['text'])
def text(message):
    global basket_real, jija_now, basket_real_str, smile, id_SLAVA
    chat_id = message.chat.id
    msg = message.text

    if msg =="Продолжить":
        send(message.chat.id, "Далее тебе будет представлен каталог для выбора. Для отправки заказа вызови функцию <отправить заказ> снизу.", keyboard2)
    

    if msg =="Каталог":
        send(message.chat.id, "Каталог:", keyboard3)
        send_photo(chat_id)

    if msg =="Rick and Morty":
        send(message.chat.id, "Вкусы:", keyboard4)
        # Эта переменная показывает вкусы какой жижы сейчас смотрят
        jija_now='Rick and Morty'

    if msg =="Mad":
        send(message.chat.id, "Вкусы:", keyboard5)
        jija_now='Mad'

    if msg =="Boshki":
        send(message.chat.id, "Вкусы:", keyboard7)
        jija_now='Boshki'

    if msg =="Одноразка 'elf bar'":
        send(message.chat.id, "Добавлено в корзину:"+" " +msg, keyboard3)
        jija_now="Одноразка 'elf bar'"
        u="Одноразка 'elf bar'"
        basket_real.append(u)
        basket_real_str=" "


    if (msg in array_rick_and_morty)and (jija_now=='Rick and Morty') :
        x="Rick and Morty"+"  "+msg
        send(message.chat.id, "Добавлено в корзину:"+" " +x, keyboard4)
        basket_real.append(x)
        basket_real_str=" "

    if (msg in array_mad) and (jija_now=='Mad'):
        y="Mad"+"  "+msg
        send(message.chat.id, "Добавлено в корзину:"+" " +y, keyboard5)
        basket_real.append(y)
        basket_real_str=" "

    if (msg in array_boshki) and (jija_now=='Boshki'):
        z="Boshki"+"  "+msg
        send(message.chat.id, "Добавлено в корзину:"+" " +z, keyboard7)
        basket_real.append(z)
        basket_real_str=" "

    if msg =="Очистить корзину":
        send(message.chat.id, "Корзина очищена", keyboard3)
        jija_now=' '
        basket_real=[" "]
        basket_real_str=" "

    if msg =="Показать корзину":
        if len(basket_real)==1:
            send(message.chat.id, "Корзина пуста..." , keyboard3)
        else:
            for i in basket_real:
                basket_real_str=basket_real_str+"\n\n"+i
            send(message.chat.id, "В корзине сейчас:"+"  "+basket_real_str , keyboard3)
        jija_now=' '
        basket_real_str=" "

    if msg =="Отправить заказ"+smile:
        send(message.chat.id, "Выберите город", keyboard6)
        basket_real_str=" "

    if msg=="Минск"  or msg=="Червень":
        for i in basket_real:
                basket_real_str=basket_real_str+"\n\n"+i
        end_message=msg + "     " + "@" + message.chat.username+ "\n" + basket_real_str
        send(message.chat.id, "Заказ успешно отправлен, продавец скоро с вами свяжется в Telegram." , keyboard3)
        send(id_SLAVA, end_message, keyboard3)
        send(id_MY, "@" + message.chat.username, keyboard3)
        jija_now=' '
        basket_real=[" "]
        basket_real_str=" "

    if msg =="🔙":
        send(message.chat.id, "Каталог: ", keyboard3)
        basket_real_str=" "
        jija_now=' '
    


bot.polling(none_stop = True)
 
