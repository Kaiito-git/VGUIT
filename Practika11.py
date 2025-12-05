import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from requests.exceptions import RequestException


def get_repo_info():
    repo_name = entry.get().strip()
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите имя репозитория в формате 'owner/repo'")
        return

    try:
        # Получаем информацию о репозитории
        repo_url = f"https://api.github.com/repos/{repo_name}"
        response = requests.get(repo_url, timeout=10)
        response.raise_for_status()
        repo_data = response.json()

        # Получаем информацию о владельце репозитория
        owner_login = repo_data['owner']['login']
        user_url = f"https://api.github.com/users/{owner_login}"
        user_response = requests.get(user_url, timeout=10)
        user_response.raise_for_status()
        user_data = user_response.json()

        # Извлекаем нужные поля
        result = {
            'company': user_data.get('company'),
            'created_at': user_data.get('created_at'),
            'email': user_data.get('email'),
            'id': user_data.get('id'),
            'name': user_data.get('name'),
            'url': user_data.get('url')
        }

        # Сохраняем в файл
        with open('github_info.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        messagebox.showinfo("Успех", f"Данные сохранены в файл 'github_info.json'")

        # Показываем результат в текстовом поле
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, json.dumps(result, indent=2))

    except RequestException as e:  # Используем RequestException
        messagebox.showerror("Ошибка сети", f"Не удалось получить данные: {str(e)}")
    except KeyError as e:
        messagebox.showerror("Ошибка данных", f"Некорректный формат ответа от GitHub: {str(e)}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


# Создание графического интерфейса
root = tk.Tk()
root.title("GitHub Repository Info")
root.geometry("600x400")

# Стилизация
style = ttk.Style()
style.theme_use('clam')

frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

label = ttk.Label(frame, text="Введите имя репозитория (owner/repo):", font=('Arial', 12))
label.pack(anchor=tk.W, pady=(0, 10))

entry_frame = ttk.Frame(frame)
entry_frame.pack(fill=tk.X, pady=(0, 10))

entry = ttk.Entry(entry_frame, font=('Arial', 11))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry.insert(0, "dotnet/runtime")

get_button = ttk.Button(entry_frame, text="Получить информацию", command=get_repo_info)
get_button.pack(side=tk.RIGHT, padx=(10, 0))

note_label = ttk.Label(frame, text="Примеры: microsoft/dotnet, dotnet/corefx, dotnet/runtime",
                       font=('Arial', 9), foreground="gray")
note_label.pack(anchor=tk.W, pady=(0, 20))

# Область для вывода результата
result_frame = ttk.LabelFrame(frame, text="Результат", padding="10")
result_frame.pack(fill=tk.BOTH, expand=True)

result_text = tk.Text(result_frame, height=10, wrap=tk.WORD, font=('Courier', 10))
result_text.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(result_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_text.yview)

root.mainloop()
