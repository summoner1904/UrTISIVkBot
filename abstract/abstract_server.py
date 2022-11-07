from abc import ABC, abstractmethod


class AbstractBaseServer(ABC):
    @abstractmethod
    def start(self) -> None:
        """
        Метод работает с командами из словаря и классом Today.
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