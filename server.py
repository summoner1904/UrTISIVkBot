import random
import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from config import TOKEN
from database import *
from abstract.abstract_server import AbstractBaseServer, AbsctractKeyboardMixin


class BaseServer(AbstractBaseServer):
    """
    Класс, отвечающий за авторизацию в лице сообщества ВК.
    """

    _vk = vk_api.VkApi(token=TOKEN)
    __longpoll = VkLongPoll(_vk)

    def start(self, COMMAND_LIST: dict):
        """
        Работает с классом Today - получает актуальную дату. Инициализирует command_list.
        Вызывает метод command_worker.
        :param command_list (Словарь с командами)
        :return: None
        """
        self.commands = COMMAND_LIST
        for event in self.__longpoll.listen():
            Today.update_date()
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
        params = {
            "user_id": user_id,
            "message": message,
            "random_id": random.randint(1, 10000),
            "keyboard": keyboard.get_keyboard(),
        }
        self._vk.method("messages.send", params)


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
        buttons = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота")
        for i in buttons:
            if i in buttons[2::2]:
                keyboard.add_line()
            keyboard.add_button(label=i, color=VkKeyboardColor.PRIMARY)
        return keyboard


class Server(UtilsServer):
    """
    Класс с командами.
    """

    keyboard = KeyboardMixin()

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

    def command_raspisanie(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(raspisanie_dict[event.text.lower()]),
            keyboard=self.keyboard.get_standart_keyboard(),
        )
