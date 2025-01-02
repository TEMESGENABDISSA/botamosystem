from typing import final
from telegram import update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContectTypes

TOKEN: final = '7502488734:AAGF8WNqvwZgZVARkiSftUFHM7mk9moAAsI'
BOT_USESRNAME:final= '@emamu'
#commands
async def  start_command(update:update, context: ContextTypes.DEFAULT_TYPE):

  await update.messsage.reply_text('hello!thanks for chatting with me! I am meraki english !')

async def  help_command(update:update, context: ContextTypes.DEFAULT_TYPE):

     await update.messsage.reply_text('I m a meraki  please type something so I can respond  !')


async def  custom_command(update:update, context: ContextTypes.DEFAULT_TYPE):

    await update.messsage.reply_text('this is  a cusom command  !')

#RESPONSES
def handle_repsonse(text:str) -> str:
    
    Processed: str = text.lower
     
    if 'hello' in processed:
        return  'hey there!'

    if 'how are you'in processed:
          return 'I am good!'
    
    if 'i love python 'in processed:
        return 'remember to subscribe!'
    return 'I do not understand what you wrote...'

    async def handle_message (update:update,context: ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text:str = update.message.text
    print(f'user ({ update.message.chat.id}) in {message_type}:"{text}" ')
    if message_type ='group':
        if BOT_USESRNAME in text:
            new_text:str = text.replace(BOT_USESRNAME,'').strip()
            response: str = handle_repsonse (new_text)
        else: 
            
             return
        
    else:
            response:str = handle_repsonse(text)
            print('bot:', response)
           
            await update.message.reply_text(response)
            
            
