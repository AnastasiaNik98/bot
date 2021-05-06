import os
from telegram.ext import CommandHandler, MessageHandler, Filters
from settings import WELCOME_MESSAGE, TELEGRAM_SUPPORT_CHAT_ID, MARKUP

def start(update, context):
    update.message.reply_text(WELCOME_MESSAGE, MARKUP)

    user_info = update.message.from_user.to_dict()

    context.bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=f"""
📞 Connected {user_info}.
        """,
    )
    
    
def about(update, context):
    update.message.reply_text('\n С помощью комплексного интернет-маркетинга внедряем эффективные решения, позволяющие достичь максимальных имиджевых и финансовых результатов для Клиентов в России 🇷🇺, странах СНГ 🇵🇬, США 🇺🇸 и Европе 🇪🇺🤝 \n \n При формировании наших решений мы учитываем поставленные перед нами бизнес-задачи, состояние и перспективы развития сайтов, последние технологические разработки алгоритмов поисковых систем 🤖 и тенденции развития интернет-маркетинга 👾🤓')

def why(update, context):
    update.message.reply_text('Спрашивайте, мы ответим через минуту')

def catalog(update, context):
    update.message.reply_text('Наши услуги: \n 😏 Seo-продвижение сайтов \n 😁 Управление репутацией в интернете \n 😉 Создание сайтов\n ☺️ E-mail маркетинг \n 😋 Конкурентная разведка \n 😎 Техническая поддержка сайтов \n \n Если хотите узнать подробнее, напишите нам, и мы подберем предложение идивидуально для Вас 🤩')

def help(update, context):
    update.message.reply_text('Мне жаль, что мы доставили Вам неудобство. Опишите ситуацию и мы обязательно все исправим')



def forward_to_chat(update, context):
    """{ 
        'message_id': 5, 
        'date': 1605106546, 
        'chat': {'id': 49820636, 'type': 'private', 'username': 'danokhlopkov', 'first_name': 'Daniil', 'last_name': 'Okhlopkov'}, 
        'text': 'TEST QOO', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'username': 'danokhlopkov', 'language_code': 'en'}
    }"""
    update.message.forward(chat_id=TELEGRAM_SUPPORT_CHAT_ID)


def forward_to_user(update, context):
    """{
        'message_id': 10, 'date': 1605106662, 
        'chat': {'id': -484179205, 'type': 'group', 'title': '☎️ SUPPORT CHAT', 'all_members_are_administrators': True}, 
        'reply_to_message': {
            'message_id': 9, 'date': 1605106659, 
            'chat': {'id': -484179205, 'type': 'group', 'title': '☎️ SUPPORT CHAT', 'all_members_are_administrators': True}, 
            'forward_from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'danokhlopkov': 'okhlopkov', 'language_code': 'en'}, 
            'forward_date': 1605106658, 
            'text': 'g', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 
            'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
            'from': {'id': 1440913096, 'first_name': 'SUPPORT', 'is_bot': True, 'username': 'lolkek'}
        }, 
        'text': 'ggg', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 
        'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 
        'from': {'id': 49820636, 'first_name': 'Daniil', 'is_bot': False, 'last_name': 'Okhlopkov', 'username': 'danokhlopkov', 'language_code': 'en'}
    }"""
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


                   


