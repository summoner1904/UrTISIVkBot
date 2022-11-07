from server import Server

if __name__ == "__main__":
    bot = Server()
    COMMAND_LIST = {
        "привет": bot.command_hi,
        "понедельник": bot.command_monday,
        "вторник": bot.command_tuesday,
        "среда": bot.command_wednesday,
        "четверг": bot.command_thursday,
        "пятница": bot.command_friday,
        "суббота": bot.command_saturday,
        "клавиатура": bot.command_keyboard,
        "ошибка": bot.command_error,
    }
    bot.start(COMMAND_LIST)
