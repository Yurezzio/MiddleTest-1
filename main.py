def read_my_file(file_path):
    """Читаю файл і повертаю текст як рядок."""
    try:
        with open(file_path, 'r', encoding='utf-8') as my_file:
            return my_file.read()
    except FileNotFoundError:
        print(f"Ой, файл {file_path} десь загубився!")
        return ""
    except Exception as e:
        print(f"Щось пішло не так: {e}")
        return ""

def count_my_words(text):
    """Рахую слова в тексті, кидаю їх у словник {слово: скільки разів}."""
    text = text.lower()  # все в нижній регістр, щоб не плутатись
    words = text.split()  # розбиваю на слова
    my_word_dict = {}
    
    for word in words:
        word = word.strip('.,!?():;"\'')  # прибираю всяке сміття типу ком
        if word:  # якщо слово не пусте
            if word in my_word_dict:
                my_word_dict[word] += 1  # додаю до лічильника
            else:
                my_word_dict[word] = 1  # перше входження слова
    return my_word_dict

def get_my_top_words(word_dict, how_many=10):
    """Беру топ слів, скільки скажеш (по дефолту 10)."""
    # сортую по кількості, від більшого до меншого
    sorted_stuff = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_stuff[:how_many]

def save_my_results(top_words, output_file):
    """Зберігаю результат у файл, щоб не пропало."""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for word, count in top_words:
                file.write(f"{word}-{count}\n")  # слово і скільки разів
        print(f"Все ок, записав у {output_file}")
    except Exception as e:
        print(f"Не вдалося зберегти, ось помилка: {e}")

def my_main(input_file, output_file):
    """Головний шматок, де все крутиться."""
    text = read_my_file(input_file)  # читаю файл
    if not text:
        print("Нема тексту, нема роботи!")
        return
    
    words = count_my_words(text)  # рахую слова
    top = get_my_top_words(words)  # беру топ-10
    save_my_results(top, output_file)  # зберігаю

if __name__ == "__main__":
    my_input = "input.txt"  # звідки беру текст
    my_output = "output.txt"  # куди пишу результат
    my_main(my_input, my_output)  # запускаю свою прогу