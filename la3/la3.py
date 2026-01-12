import os

def file_read(file_path, mode='full'):

    try:
        if not os.path.exists(file_path):
            return f"Файл '{file_path}' не найден"

        if mode.lower() == 'full':
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        elif mode.lower() == 'line-by-line':
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
                return lines
        else:
            return "Неправильный режим. Используйте 'full' или 'line-by-line'"
    except Exception as e:
        return f"Ошибка при чтении файла: {e}"


import os


def add_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text + '\n')
            return f"Text add was complete in file{file_path}."
    except Exception as e:
        return f"Add error:{e}"


import os
def file_read(file_path, mode='full'):

    try:
        if not os.path.exists(file_path):
            return f"File '{file_path}' not found"

        if mode.lower() == 'full':
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        elif mode.lower() == 'line-by-line':
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
                return lines
        else:
            return "Choose ('full' or 'line-by-line'):"
    except Exception as e:
        return f"Error read: {e}"

def add_file(file_path,text):
    try:
        with open(file_path, 'w') as file:
            file.write(text+'\n')
            return f"Text add was complete in file {file_path}."
    except Exception as e:
        return f"Add error:{e}"

if __name__ == "__main__":
    while True:
        menu = input('You can (Read,Write,Add new text,Exit):').strip().lower()

        if menu == 'read':
            file_name = input('Write your file name:')
            mod = input("How you can read file(Full | Line-by-line):")
            if mod not in ['full', 'line-by-line']:
                print('Choose correct mode("Full or Line by line"')
                continue
            result = file_read(file_name, mod)
            if isinstance(result, str):
                print(result)
            elif isinstance(result, list):
                for i, line in enumerate(result, start=1):
                    print(f"{i}. {line}")

        elif menu == 'write':
            file_name = input("Enter the file name: ")
            new_text = input("Enter the text: ")
            result = add_file(file_name, new_text)
            print(result)

        elif menu == 'add':
            file_name = input("Enter the file name for the attachment: ")
            new_text = input("Enter text for addition: ")
            result = add_file(file_name, new_text)
            print(result)

        elif menu == 'exit':
            print("Work completed.")
            break
        else:
            print("Command not found. Try again.")