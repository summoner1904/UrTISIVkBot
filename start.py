from server import Server

if __name__ == "__main__":
    bot = Server()
    COMMAND_LIST = {
        "привет": bot.command_hi,
        "понедельник": bot.command_raspisanie,
        "вторник": bot.command_raspisanie,
        "среда": bot.command_raspisanie,
        "четверг": bot.command_raspisanie,
        "пятница": bot.command_raspisanie,
        "суббота": bot.command_raspisanie,
        "клавиатура": bot.command_raspisanie,
        "ошибка": bot.command_error
    }
    bot.start(COMMAND_LIST)
