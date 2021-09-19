import telebot
import cv2
import numpy as np
from keras.models import load_model

model = load_model("/content/model.h5")
bot =telebot.TeleBot("1998425031:AAEO7yJO_KGEbwiiPjo-ZzDfY-OoS1sbhtI")

width = height = 224

@bot.message_handler(commands=['start'])
def say_welcome(messages):
    bot.send_message(messages.chat.id, f'سلام خوش اومدی صفا آوردی {messages.from_user.first_name}')
    bot.send_message(messages.chat.id,f' اینجا شما می تونی تشخیص بدی شیخ، رو از افرادی که شیخ نیستن') 
    bot.send_message(messages.chat.id,f'اکنون بفرست یک عکس برای من') 


  


# @bot.message_handler(commands=['help'])
# def komak(message):
#     bot.send_message(message.chat.id,"من برای کمک به شما آماده هستم")


# buttons =telebot.types.ReplyKeyboardMarkup(row_width=2)
# btn1 =telebot.types.KeyboardButton('🎬فیلم')
# btn2 =telebot.types.KeyboardButton('🎧موسیقی')
# btn3 =telebot.types.KeyboardButton('📷عکس')
# buttons.add(btn1,btn2,btn3)
# @bot.message_handler(commands=['download'])
# def mydownload(message):
#     bot.send_message(message.chat.id," چی دوست داری برات بیارم؟",reply_markup=buttons)


# @bot.message_handler(func=lambda message:True)
# def send_normal_message(message):
#     bot.send_message(message.chat.id," شما یک پیام عادی فرستادی")


# @bot.message_handler(func=lambda message:True)
# def send_normal_message(message):
#     if message.text =="سلام":
#         bot.reply_to(message," علیک  سلام")

#     elif message.text =="خوبی":
#          bot.reply_to(message," نه تو خوبی ")

#     elif message.text =="چه خبر؟":
#          bot.reply_to(message,"سلامتی رهبر ")

#     elif message.text =="چی پوشیدی؟":
#         photo =open("shomiz.jpg","rb")
#         bot.send_photo(message.chat.id,photo)
         
#     else :
#          bot.reply_to(message,"نمی فهمم چی می گی!")




@bot.message_handler(content_types=['photo'])
def photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    s = file_info.file_path
    with open("/content/" + s, 'wb') as new_file:
        new_file.write(downloaded_file)

    image = cv2.imread("/content/" + s)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (width, height))
    image = image/255
    image = image.reshape(1, width, height, 3)
    pred = model.predict([image])

    r= np.argmax(pred)
    if r == 0:
      bot.reply_to(message, 'شیخ نیست')
    else:
      bot.reply_to(message, 'شیخ ')

bot.polling()







