import os
from telegram.ext import CommandHandler, MessageHandler, Filters
from settings import WELCOME_MESSAGE, TELEGRAM_SUPPORT_CHAT_ID, TELEGRAM_TOKEN
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    
    update.message.reply_text(WELCOME_MESSAGE)
    user_info = update.message.from_user.to_dict()

    context.bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=f"""
        
📞 Новый пользователь начал диалог с Ботом {user_info}.
        """,
    )

  def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu
button_list = [
    InlineKeyboardButton("col1", callback_data=...),
    InlineKeyboardButton("col2", callback_data=...),
    InlineKeyboardButton("row 2", callback_data=...)
]

# сборка клавиатуры из кнопок `InlineKeyboardButton`
reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
# отправка клавиатуры в чат
 context.bot.send_message(chat_id=chat_id, text="Меню из двух столбцов", reply_markup=reply_markup)  


def about(update, context):
    update.message.reply_text('\n С помощью комплексного интернет-маркетинга внедряем эффективные решения, позволяющие достичь максимальных имиджевых и финансовых результатов для Клиентов в России 🇷🇺, странах СНГ 🇵🇬, США 🇺🇸 и Европе 🇪🇺🤝 \n \n При формировании наших решений мы учитываем поставленные перед нами бизнес-задачи, состояние и перспективы развития сайтов, последние технологические разработки алгоритмов поисковых систем 🤖 и тенденции развития интернет-маркетинга 👾🤓')

def why(update, context):
    update.message.reply_text('Спрашивайте, мы ответим через минуту')

def catalog(update, context):
    update.message.reply_text('Наши услуги: \n 😏 Seo-продвижение сайтов \n 😁 Управление репутацией в интернете \n 😉 Создание сайтов\n ☺️ E-mail маркетинг \n 😋 Конкурентная разведка \n 😎 Техническая поддержка сайтов \n \n Если хотите узнать подробнее, напишите нам, и мы подберем предложение идивидуально для Вас 🤩')

def help(update, context):
    update.message.reply_text('Мне жаль, что мы доставили Вам неудобство. Опишите ситуацию и мы обязательно все исправим')



def forward_to_chat(update, context):
   
    update.message.forward(chat_id=TELEGRAM_SUPPORT_CHAT_ID)


def forward_to_user(update, context):
    
    user_id = update.message.reply_to_message.forward_from.id
    context.bot.copy_message(
        message_id=update.message.message_id,
        chat_id=user_id,
        from_chat_id=update.message.chat_id
    )


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('about', about))
    dp.add_handler(CommandHandler('why', why))
    dp.add_handler(CommandHandler('catalog', catalog))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))
    dp.add_handler(MessageHandler(Filters.chat(TELEGRAM_SUPPORT_CHAT_ID) & Filters.reply, forward_to_user))
    return dp


                   


