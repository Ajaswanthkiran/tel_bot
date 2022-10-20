import claculater
import telegram
#import sample_qrcode
from telegram.ext import Updater,MessageHandler,Filters
from telegram.ext import CommandHandler

from yt import youtube_search_location

updater=Updater(token='5439158053:AAFjCQVZkSyajpCWfoiwML3N0_n88j7NfVs',use_context=True)
dispatcher=updater.dispatcher

def start(update,context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text="Hello i am a ajk bot i am here to tell the update about the new movies in the ott's\ncan you select your choic your \n 1.Prime\n2.Aha\n3.SunNxt\n4.Netfilx")

def prime(update,context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text="1.Thank You!\n2.Dejavu\n3.Top Gun")
def aha(update,context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text="1.Anjaam Pathiraa\n2.Malik\n3.Shikaru")

def sunnxt(update,context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text="1.Doctor")


# def getqr(update,context):
#     chat_id = update.effective_chat.id
#     q=""
#     for str in range(len(context.args)):
#         q=q+" "+context.args[str]
#     i=sample_qrcode.sender(q)
#     #print(type(i))
#     i.seek(0)
#     context.bot.send_photo(chat_id=chat_id,photo=i)

def netflix(update,context):
    chat_id=update.effective_chat.id
    context.chat.send_message(chat_id=chat_id,text="1.Back to future 1\n2. Back to future 2")

def hello(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello !")



def yt_search(update,context):
    chat_id=update.effective_chat.id
    query=""
    for x in range(len(context.args)):
        query+=" "+context.args[x]
    ans=youtube_search_location(query,1)
    context.bot.send_message(chat_id=chat_id,text="https://www.youtube.com/watch?v="+ans)

dispatcher.add_handler(CommandHandler("start",start))
dispatcher.add_handler(CommandHandler("1",prime))
dispatcher.add_handler(CommandHandler("2",aha))
dispatcher.add_handler(CommandHandler("3",sunnxt))
dispatcher.add_handler(CommandHandler("4",netflix))
#dispatcher.add_handler(CommandHandler("getqr",getqr))
#dispatcher.add_handler(MessageHandler(Filters.all,hello))
dispatcher.add_handler(CommandHandler("yt",yt_search))
updater.start_polling()