from prompt_adapter.rpo_prompt_adapter import TXTPromptAdapter  # Импортируем класс TXTPromptAdapter


if __name__ == "__main__":
    # Путь к файлу с промптами
    file_path = 'example_rpo_prompt.txt'  

    # Путь к папке с файлами
    file_dir = 'example_docs' # по умолчанию 'prompts'

    # Создаем экземпляр TXTPromptAdapter
    txt_adapter = TXTPromptAdapter(file_path, file_dir)

    # Пример использования: получаем промпт из .txt файла
    try:
        prompt = txt_adapter.get_prompt()
        print(prompt)
    except ValueError as e:
        print(e)