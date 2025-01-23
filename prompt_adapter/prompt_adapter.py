import os
import pandas as pd


class PromptAdapter:
    """Адаптер для работы с промптами, хранящимися в CSV-файле.

    Attributes:
        _prompts (dict): Словарь для хранения промптов.
        file_path (str): Путь к файлу с промптами.  
    """

    def __init__(self, file_path: str, file_dir='prompts'):
        """Инициализирует экземпляр PromptAdapter.

        Args:
            file_path (str): Имя файла с промптами, который находится в папке 'prompts'.
        """
        self.file_path = os.path.join(file_dir, file_path)
        self.__read_data()

    def __read_data(self) -> None:
        """Читает данные из CSV-файла и сохраняет их в виде словаря.

        Raises:
            Exception: Если произошла ошибка при чтении файла.
        """
        try:
            self.file_path = pd.read_csv(
                self.file_path,
                sep=';',
                encoding='utf-8-sig'
            )
        except Exception as e:
            print(e)

    def get_prompt(self, doc_class: str, question_type: str) -> str:
        """Возвращает промпт для заданного класса документа и типа вопроса.

        Args:
            doc_class (str): Класс документа.
            question_type (str): Тип вопроса.

        Returns:
            str: Строка с промптом.

        Raises:
            ValueError: Если промпт для заданного класса документа и типа вопроса не найден.
        """
        prompt = f'{doc_class} {question_type}'

        if prompt not in list(self.file_path['doc_class_question_type']):
            raise ValueError(f"Prompt '{prompt}' not found in data.")

        result = self.file_path[self.file_path['doc_class_question_type'] == prompt]['prompt'].iloc[0]

        return result