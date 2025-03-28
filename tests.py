import pytest
import os
from main import read_my_file, count_my_words, get_my_top, save_my_stuff, my_main

# Моя штука, щоб зробити файл для тестів
@pytest.fixture
def my_test_input(tmp_path):
    file_path = tmp_path / "test_input.txt"
    my_text = """
    Йо, кодери! Пишу код щодня.
    Код — це моє, код — це топ.
    Йо, люблю свій код!
    """
    file_path.write_text(my_text, encoding='utf-8')
    return str(file_path)

# Мій файл для запису результатів
@pytest.fixture
def my_test_output(tmp_path):
    return str(tmp_path / "test_output.txt")

# Перевіряю, чи читається мій текст
def test_my_reader(my_test_input):
    text = read_my_file(my_test_input)
    what_i_put = """
    Йо, кодери! Пишу код щодня.
    Код — це моє, код — це топ.
    Йо, люблю свій код!
    """.strip()
    assert text.strip() == what_i_put  # чи все так, як я написав
    assert type(text) == str  # чи це точно текст

# Дивлюсь, що буде, якщо файлу нема
def test_no_file_reading():
    result = read_my_file("вигаданий_файл.txt")
    assert result == ""  # має бути пусто, бо нічого нема

# Тестую, як мої слова рахуються
@pytest.mark.parametrize("text_to_check, my_count", [
    ("йо йо код", {"йо": 2, "код": 1}),  # два "йо", один "код"
    ("код. код, код!", {"код": 3}),  # три "код" із крапками
    ("", {}),  # пусто — значить пусто
    ("TOP top Top", {"top": 3}),  # усе маленькими буквами
])
def test_my_counter(text_to_check, my_count):
    result = count_my_words(text_to_check)
    assert result == my_count  # чи правильно порахувало

# Перевіряю, чи топ слів норм вибирається
@pytest.mark.parametrize("words_i_got, how_many, my_best", [
    ({"йо": 2, "код": 4, "топ": 1}, 2, [("код", 4), ("йо", 2)]),  # беру топ-2
    ({"hi": 1, "yo": 3}, 1, [("yo", 3)]),  # тільки одне слово
    ({}, 4, []),  # нічого нема — нічого не беру
    ({"код": 5}, 3, [("код", 5)]),  # більше топ, ніж слів
])
def test_my_best_words(words_i_got, how_many, my_best):
    top_words = get_my_top(words_i_got, how_many)
    assert top_words == my_best  # чи топ такий, як я хочу

# Дивлюсь, чи мої штуки записуються в файл
def test_my_writer(my_test_output):
    my_words = [("код", 4), ("йо", 2)]
    save_my_stuff(my_words, my_test_output)
    
    with open(my_test_output, 'r', encoding='utf-8') as f:
        saved_stuff = f.read().strip()
    assert saved_stuff == "код-4\nйо-2"  # чи все записалось як треба

# Перевіряю, чи вся моя прога працює разом
def test_my_full_run(my_test_input, my_test_output):
    my_main(my_test_input, my_test_output)
    
    with open(my_test_output, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    assert len(lines) <= 10  # не більше 10 рядків, як я задумав
    for line in lines:
        bits = line.strip().split('-')
        assert bits[1].isdigit()  # чи число в кінці норм
