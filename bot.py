import telebot
bot =telebot.TeleBot("1998425031:AAEO7yJO_KGEbwiiPjo-ZzDfY-OoS1sbhtI")

@bot.message_handler(commands=['start'])
def say_welcome(message):
    bot.send_message(message.chat.id,"سلام خوش اومدی صفا آوردی") 

@bot.message_handler(commands=['help'])
def komak(message):
    bot.send_message(message.chat.id,"من برای کمک به شما آماده هستم")


buttons =telebot.types.ReplyKeyboardMarkup(row_width=2)
btn1 =telebot.types.KeyboardButton('🎬فیلم')
btn2 =telebot.types.KeyboardButton('🎧موسیقی')
btn3 =telebot.types.KeyboardButton('📷عکس')
buttons.add(btn1,btn2,btn3)
@bot.message_handler(commands=['download'])
def mydownload(message):
    bot.send_message(message.chat.id," چی دوست داری برات بیارم؟",reply_markup=buttons)


# @bot.message_handler(func=lambda message:True)
# def send_normal_message(message):
#     bot.send_message(message.chat.id," شما یک پیام عادی فرستادی")


@bot.message_handler(func=lambda message:True)
def send_normal_message(message):
    if message.text =="سلام":
        bot.reply_to(message," علیک  سلام")

    elif message.text =="خوبی":
         bot.reply_to(message," نه تو خوبی ")

    elif message.text =="چه خبر؟":
         bot.reply_to(message,"سلامتی رهبر ")

    # elif message.text =="چی پوشیدی؟":
    #     photo =open("zahra.jpg","rb")
    #     bot.send_photo(message.chat.id,photo)
         
    else :
         bot.reply_to(message,"نمی فهمم چی می گی!")

bot.polling()