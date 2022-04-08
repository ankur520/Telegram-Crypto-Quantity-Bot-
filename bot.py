import datetime as dt
import logging
import gspread
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = 'Your TOKEN '

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    global user
    user =  str(update.message.from_user.username)
    """Send a message when the command /start is issued."""
    example_signal_post = "To calculate the trade amount the bot needs the following inputs\n\n1) Entry\n2) Stop Loss\n3) Leverage\n4) Your Portfolio\n5) Risk Percentage\n\nTo get trade amount put the requested data in this format\n\nEntry/Stop Loss/Leverage/Your Portfolio/Risk Percentage\n\nAnd Click on 'Send'\n\nYou should get your trade amount. Set your risk percentage based on your risk appetite. Don't overexpose your funds.\n\nMessage @moontrades0 for premium details and queries"

    update.message.reply_text(example_signal_post)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Sorry for error. Type /start if I am not responding.\n\n Contact @sinbit007')

def echo(update, context):
    """Echo the user message."""
    
    signals_data = update.message.text
    
    '''try:
        ins_val = [update.message.from_user.username + ' sinbit', str(dt.datetime.now()), signals_data]

        gc = gspread.service_account(filename = 'cred.json')
        sh = gc.open_by_key('1OoYjFbW8G1C7IOJErXLouOxHH236JzU_j7etUsdxz9Y')
        worksheet = sh.sheet1

        worksheet.insert_row(ins_val,2)
    except:
        pass'''
    msz = signals_data
    if (signals_data.count('/')== 4):

        Entry = float(msz.split('/')[0])
        sLoss = float(msz.split('/')[1])
        Levrage = msz.split('/')[2]
        Port = msz.split('/')[3]
        rpt = msz.split('/')[4]

        #Margin  = msz.split(':')[5]
        if(Levrage.endswith('x') or Levrage.endswith('X')):
            Levrage = Levrage[:-1]
        if(risk.endswith('%')):
            risk = risk[:-1]

        # slPercent = (abs(Entry - sLoss)*100) / Entry
        # slPercent = slPercent * float(Levrage)
        # USDt = float(Port) * (float(risk)/100)
        # amount = (USDt / slPercent) * 100
        # #print(amount)


        usdtPercent = int(float(Port) * rpt / 100)
        slDifference = Entry - sLoss
        # quantity
        calculateQuantity = abs(usdtPercent / (slDifference * Levrage))
        formatted_calculateQuantity = "{:.5f}".format(calculateQuantity)
        # trade amount 
        calQuanTradeAmount = abs(int(calculateQuantity * Entry))
        # sl Percent 
        slDifferencePercent =   float(slDifference / Entry * 100)
        formatted_slDifferencePercent = "{:.2f}".format(slDifferencePercent)


        #  loss Dollars 
        lossDollars = abs(calculateQuantity * (slDifference * Levrage ))
        # formatted_lossDollars = "{:.2f}".format(lossDollars)


        # total profit % with leverage 
        profitPercent = abs(slDifferencePercent * Levrage)
        formatted_profitPercent = "{:.2f}".format(profitPercent)


        messageRPT = "Your RPT is --> " + str(usdtPercent) + " $ "
        messageQuantity =  "Quantity --> " + str(formatted_calculateQuantity) 
        messageTradeAmount = "Trade Amount --> " + str(calQuanTradeAmount) + "$" 
        messageLossDollars = "LossDollars --> "  + str(lossDollars) 
        messageProfitPercent = "% Profit on "+ str( Levrage) + "X --> " + str(formatted_profitPercent) + " %"
        # messageProfitDollar =  "Profit --> " + str(profitDollar) +" $"

        reply = messageRPT + "\n" + messageTradeAmount  + "\n" + messageQuantity + "\n" +  messageLossDollars + "\n" +  messageProfitPercent  


        update.message.reply_text(reply)





def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('app Link' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
