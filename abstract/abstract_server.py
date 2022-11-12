from abc import ABC, abstractmethod


class AbstractBaseServer(ABC):
    @abstractmethod
    def start(self) -> None:
        """
        Метод отвечает за инициализацию command_list. Слушает longpoll.
        Работает с классом Today - запрашивает дату. Вызывает метод command_worker
        и передает ему event.

        :return: None
        """
        pass

    @abstractmethod
    def command_worker(self) -> None:
        """
        Сравнивает сообщение пользователя с ключами из словаря command_list.
        Если находит ключ - выполняет команду.
        :return: None
        """
        pass


class AbsctractKeyboardMixin(ABC):
    @abstractmethod
    def get_standart_keyboard(self) -> None:
        """
        Стандартная клавиатура со всеми днями недель.
        :return: None
        """
        pass
