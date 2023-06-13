from telegram.ext import Updater, MessageHandler, Filters

# Define your bot token here
BOT_TOKEN = "6072381876:AAEmjLaTeWh53X-bjZJpxF762ah8eadUc_s"

# Define your filters and corresponding responses
filters = {
    "hello": "Hello there!",
    "bye": "Goodbye!",
    "cat": "Here's a cute cat picture: [insert cat picture URL]",
    "dog": "Here's an adorable dog picture: [insert dog picture URL]",
    # Add more filters and responses as needed
}

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm Soo Yun 수연. How can I assist you?")

def handle_message(update, context):
    text = update.message.text.lower()
    response = filters.get(text)
    
    if response:
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = MessageHandler(Filters.command("start"), start)
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
