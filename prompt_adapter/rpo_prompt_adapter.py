import os


class TXTPromptAdapter:
    """Адаптер для работы с промптами, хранящимися в txt-файле.

    Атрибуты:
        _prompt (str): Текст системного промпта, прочитанного из файла.
        file_path (str): Полный путь к файлу с промптом.
    """

    def __init__(self, file_path: str, file_dir: str = 'prompts') -> None:
        """Инициализирует экземпляр TXTPromptAdapter.

        Аргументы:
            file_path (str): Имя файла с промптами.
            file_dir (str, optional): Директория, в которой находится файл с промптом. 
                                     По умолчанию 'prompts'.

        Исключения:
            FileNotFoundError: Если файл с промптами не найден.
            IOError: Если произошла ошибка при чтении файла.
        """
        self._prompt: str = None
        self.file_path: str = os.path.join(file_dir, file_path)
        self.__read_data()

    def __read_data(self) -> None:
        """Читает данные из txt-файла и сохраняет их в атрибуте _prompt.

        Исключения:
            FileNotFoundError: Если файл с промптом не найден.
            IOError: Если произошла ошибка при чтении файла.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self._prompt = file.readline()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден.")
        except IOError as e:
            raise IOError(f"Ошибка при чтении файла {self.file_path}: {e}")

    def get_prompt(self) -> str:
        """Возвращает промпт.

        Возвращает:
            str: Текст промпта.

        Исключения:
            ValueError: Если промпт не был прочитан (равен None).
        """
        if self._prompt is None:
            raise ValueError("Промпт не был прочитан из файла.")
        return self._prompt
