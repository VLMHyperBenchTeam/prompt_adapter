from prompt_adapter.prompt_adapter import PromptAdapter  # Импортируем класс PromptAdapter


if __name__ == "__main__":
    # Путь к файлу с промптами
    file_path = 'qwen2_5_plus.csv'  

    # Путь к папке с файлами
    file_dir = 'example_docs' # по умолчанию 'prompts'

    # Создаем экземпляр PromptAdapter
    adapter = PromptAdapter(file_path, file_dir)

    # Пример использования: получаем промпт для определенного класса документа и типа вопроса
    try:
        doc_class = 'passport_HD'  # Пример класса документа
        question_type = 'Пол'  # Пример типа вопроса
        prompt = adapter.get_prompt(doc_class, question_type)
        print(f"Prompt for {doc_class} and {question_type}: {prompt}")
    except ValueError as e:
        print(e)
