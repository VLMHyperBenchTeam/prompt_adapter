# PromptAdapter

`PromptAdapter` — это класс для работы с промптами, хранящимися в CSV-файле.  

## Формат CSV-файла  
Файл должен содержать два столбца:
- `doc_class_question_type` — ключ, объединяющий класс документа и тип вопроса.
- `prompt` — текст соответствующего промпта.

## Использование  

### Использование `PromptAdapter`

Убедитесь, что в папке `prompts` находится соответствующий CSV-файл.

1. **Создайте экземпляр `PromptAdapter`**, указав имя CSV-файла (по умолчанию файл ищется в папке `prompts`):
   ```python
   adapter = PromptAdapter("qwen2_5_plus.csv")
   ```

2. **Получите промпт по классу документа и типу вопроса**:
   ```python
   prompt = adapter.get_prompt("passport_HD", "Пол")
   ```

### Использование `TXTPromptAdapter`

Убедитесь, что в папке `prompts` находится соответствующий txt-файл.

`TXTPromptAdapter` — это класс для работы с промптами, хранящимися в txt-файле.

1. **Создайте экземпляр `TXTPromptAdapter`**, указав имя txt-файла (по умолчанию файл ищется в папке `prompts`):
   ```python
   txt_adapter = TXTPromptAdapter("example_rpo_prompt.txt")
   ```

2. **Получите промпт**:
   ```python
   prompt = txt_adapter.get_prompt()
   ```
   
## Обработка ошибок  
- Если файл не найден или не загружен, будет выведено сообщение об ошибке.
- Если запрошенный `doc_class_question_type` отсутствует в файле, выбрасывается `ValueError`.

