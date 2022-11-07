import random
import vk_api
from database import *
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from config import TOKEN
from abstract.abstract_server import AbstractBaseServer, AbsctractKeyboardMixin


class BaseServer(AbstractBaseServer):
    """
    Класс, отвечающий за авторизацию в лице сообщества ВК.
    """

    vk = vk_api.VkApi(token=TOKEN)
    longpoll = VkLongPoll(vk)

    def start(self, COMMAND_LIST: dict):
        """
        Работает с классом Today - получает актуальную дату. Инициализирует command_list.
        :param command_list (Словарь с командами)
        :return: None
        """
        self.commands = COMMAND_LIST
        for event in self.longpoll.listen():
            Today.today = datetime.datetime.now()
            Today.today_str = Today.today.strftime("%d-%m-%y")
            Today.today_lst = Today.today_str.split("-")
            Today.day = Today.today_lst[0]
            Today.mounth = Today.today_lst[1]
            self.command_worker(event)

    def command_worker(self, event):
        """
        Обрабатывает сообщения пользователя. Если находит сообщение пользоваля в command_list, то выполняет команду.
        Если сообщения пользователя нет в command_list, то обращается к ключу "ошибка" в словаре command_list.
        :param event
        :return: None
        """
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if self.commands.get(event.text.lower()):
                self.commands[event.text.lower()](event)
            else:
                self.commands["ошибка"](event)


class UtilsServer(BaseServer):
    """
    Класс, отвечающий за отправку сообщения пользователю от лица сообщества.
    """

    def send_msg(self, user_id, message, keyboard=None):
        """
        Отправляет сообщение пользователю.
        :param user_id (id пользователя, кому отправить сообщение)
        :param message (сообщение, которое нужно отправить пользователю)
        :param keyboard
        :return: None
        """
        if keyboard:
            params = {
                "user_id": user_id,
                "message": message,
                "random_id": random.randint(1, 10000),
                "keyboard": keyboard.get_keyboard(),
            }
        else:
            params = {
                "user_id": user_id,
                "message": message,
                "random_id": random.randint(1, 10000),
            }
        self.vk.method("messages.send", params)


class Server(UtilsServer):
    """
    Класс с командами.
    """

    def __init__(self):
        """
        Инициализация клавиатуры
        :return: None
        """
        self.keyboard = KeyboardMixin()

    def command_error(self, event):
        """
        Команда, подсказывающая пользователю о том, что необходимо написать/выбрать.
        :param event
        :return: Возвращает метод send_msg с сообщением "Введите или выберите день недели!".
        """
        self.send_msg(
            event.user_id,
            "Введите или выберите день недели!",
            keyboard=self.keyboard.get_standart_keyboard(),
        )

    def command_hi(self, event):
        """
        Команда, передающая сообщение "Привет!" в метод send_msg.
        :param event
        :return: Возвращает метод send_msg с сообщением "Привет!".
        """
        self.send_msg(
            event.user_id, "Привет!", keyboard=self.keyboard.get_standart_keyboard()
        )

    def command_keyboard(self, event):
        """
        Команда, отвечающая за вывод клавиатуры в боте.
        :param event
        :return: Возвращает клавиатуру и сообщение "Держи клавиатуру!" (str).
        """
        self.send_msg(
            event.user_id,
            "Держи клавиатуру!",
            keyboard=self.keyboard.get_standart_keyboard(),
        )

    def command_monday(self, event):
        """
        Команда, формирующая расписание на понедельник.
        :param event
        :return: Возвращает метод send_msg с расписанием на понедельник (list) и стандартную клавиатуру.
        """
        self.send_msg(
            event.user_id,
            "\n".join(monday_upd),
            keyboard=self.keyboard.get_standart_keyboard(),
        )

    def command_tuesday(self, event):
        """
        Команда, формирующая расписание на вторник.
        :param event
        :return: Возвращает метод send_msg с расписанием на вторник (list) и стандартную клавиатуру.
        """
        self.send_msg(
            event.user_id,
            "\n".join(tuesday_upd),
            keyboard=self.keyboard.get_standart_keyboard(),
        )

    def command_wednesday(self, event):
        """
        Команда, формирующая расписание на среду.
        :param event
        :return: Возвращает метод send_msg с расписанием на среду (list) и стандартную клавиатуру.
        """
        self.send_msg(
            event.user_id,
            "\n".join(wednesday_upd),
            keyboard=self.keyboard.get_standart_keyboard(),
        )

    def command_thursday(self, event):
        """
        Команда, формирующая расписание на четверг.
        :param event
        :return: Возвращает метод send_msg с расписанием на четверг (list) и стандартную клавиатуру.
        """
        self.send_msg(
            event.user_id,
            "\n".join(thursday),
            keyboard=self.keyboard.get_standart_keyboard(),
        )

    def command_friday(self, event):
        """
        Команда, формирующая расписание на пятницу.
        :param event
        :return: Возвращает метод send_msg с расписанием на пятницу (list) и стандартную клавиатуру.
        """
        self.send_msg(
            event.user_id,
            "\n".join(friday_upd),
            keyboard=self.keyboard.get_standart_keyboard(),
        )

    def command_saturday(self, event):
        """
        Команда, формирующая расписание на субботу.
        :param event
        :return: Возвращает метод send_msg с расписанием на субботу (list) и стандартную клавиатуру.
        """
        self.send_msg(
            event.user_id,
            "\n".join(saturday),
            keyboard=self.keyboard.get_standart_keyboard(),
        )


class KeyboardMixin(VkKeyboard, AbsctractKeyboardMixin):
    """
    Класс, отвечающий за клавиатуру.
    :return: keyboard
    """

    def get_standart_keyboard(self):
        """
        Стандартная клавиатура (со всеми днями недели).
        :return: Возвращает стандартную клавиатуру.
        """
        keyboard = VkKeyboard()
        keyboard.add_button(label="Понедельник", color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(label="Вторник", color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(label="Среда", color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(label="Четверг", color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(label="Пятница", color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(label="Суббота", color=VkKeyboardColor.PRIMARY)
        return keyboard
