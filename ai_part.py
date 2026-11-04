import os

from ollama import ResponseError, chat

MODEL = os.getenv("OLLAMA_MODEL", "gemma3:1b")

messages = [{
    "role": "system",
    "content": "Ты учебный помощник. Отвечай кратко и показывай один пример.",
}]

def ai_answer(prompt):

    messages.append({"role": "user", "content": prompt})

    try:
        response = chat(model=MODEL, messages=messages)
        answer = response.message.content
        messages.append({"role": "assistant", "content": answer})
        return answer

    except ConnectionError:
        messages.pop()
        return "Ollama не отвечает. Запустите приложение или сервис."
    except ResponseError as error:
        messages.pop()
        return f"Ошибка Ollama: {error}"