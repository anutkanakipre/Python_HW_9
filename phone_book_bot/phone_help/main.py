import export_1
import export_2
import import1
import inter_data
import view
import data

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
table_1 = []
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Введите цифру с необходимым действием")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[/0] Ввести данные в базу вручную: ")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[/1] Ввести данные в базу (экспорт_1): ")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[/2] Ввести данные в базу (экспорт_2): ")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[/3] Показать данные: ")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[/4] Импортировать данные: ")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[/5] Выход: ")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global result
    global table_1
    if result == 1:
        table_1=[]
        table_1.append(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Введите имя")
        result = 102
    elif result == 102:
        table_1.append(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Введите Телефон")
        result = 103  
    elif result == 103:
        table_1.append(update.message.text)
        data.phone_help.append(table_1)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Запись добавлена")
        result = 999    

result=111
async def start1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global result
    await  context.bot.send_message(chat_id=update.effective_chat.id, text="[/1] ВЫБРАНО 1: ЭКСПОРТ 1 ")
    await  context.bot.send_message(chat_id=update.effective_chat.id, text="Начинаю экспорт")
    my_file = open("phone_book_bot\Export1_File.txt", "w+")
    count = 0
    for record in data.phone_help:
        my_file.write(str(record).strip('[]'))
        count+=1
    my_file.close()   
    await  context.bot.send_message(chat_id=update.effective_chat.id, text=f"Экспортировано {count} записей")
    result=1


async def start2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global result
    await  context.bot.send_message(chat_id=update.effective_chat.id, text="[/2] ВЫБРАНО 2: ЭКСПОРТ 2 ")
    await  context.bot.send_message(chat_id=update.effective_chat.id, text="Начинаю экспорт")
    my_file = open("phone_book_bot\Export2_File.txt", "w+")
    count = 0
    for record in data.phone_help:
        my_file.write(str(record).strip('[]'))
        my_file.write('\n')
        count+=1
    my_file.close()   
    await  context.bot.send_message(chat_id=update.effective_chat.id, text=f"Экспортировано {count} записей")
    result=2

async def start3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global result
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[/3] Показываю данные: ")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(data.phone_help)) 
    await context.bot.send_message(chat_id=update.effective_chat.id, text="КОНЕЦ ДАННЫХ")
    result = 3
async def start4(update: Update, context: ContextTypes.DEFAULT_TYPE):
   global result
   await context.bot.send_message(chat_id=update.effective_chat.id, text="[/4] Импортирую данные: ")
   f = open("phone_book_bot\import1_data.txt")
   count = 0
   for line in f:
        print(line)
        table_1 = []
        table_1.append(line.strip('\n'))
        data.phone_help.append(table_1)
        count = count+1
   f.close()
   await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Данные импортинрованны. Добавлено {count} записей")
   result = 4



async def start5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global result
    await context.bot.send_message(chat_id=update.effective_chat.id, text="[/5] Выход: ")
    result = 5

async def start0(update: Update, context: ContextTypes.DEFAULT_TYPE):
   global result
   await context.bot.send_message(chat_id=update.effective_chat.id, text="[/0] Ввести данные в базу вручную: ") 
   await context.bot.send_message(chat_id=update.effective_chat.id, text=" Введите Фамилию: ") 
   result = 1
# ==================================================================
        
# ==================================================================
if __name__ == '__main__':
    application = ApplicationBuilder().token('6185766163:AAHyKX_B2oUQDYSTeXadbi-UXDIz-hWdU18').build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    start_handler = CommandHandler('start', start)
    start_handler1 = CommandHandler('1', start1)
    start_handler2 = CommandHandler('2', start2)
    start_handler3 = CommandHandler('3', start3)
    start_handler4 = CommandHandler('4', start4)
    start_handler5 = CommandHandler('5', start5)
    start_handler0 = CommandHandler('0', start0)

    application.add_handler(echo_handler)
    application.add_handler(start_handler)
    application.add_handler(start_handler0)
    application.add_handler(start_handler1)
    application.add_handler(start_handler2)
    application.add_handler(start_handler3)
    application.add_handler(start_handler4)
    application.add_handler(start_handler5)
    application.run_polling()


data.init()



# while result != 5:   
    
#     if result == 0:
#        inter_data.interdata()
#     elif result == 1:
#         export_1.export_1_data()
#     elif result == 2:
#         export_2.export_2_data()
#     elif result == 3:
#         view.view_data()
#     elif result == 4:
#         import1.import_data()
