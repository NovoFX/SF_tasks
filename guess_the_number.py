"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток

    Суть алгоритма - обновлять минимум и максимум, сужая диапазон поиска
    """
    count = 0
    predict_number = 50
    minimum = 1 #Первоначальный минимум
    maximum = 101 #Первоначальный максимум

    while True:
        count += 1
        
        if predict_number > number:
            maximum = predict_number #Обновляем максимум
            predict_number = int(np.mean([minimum,maximum])) 
            print("Число должно быть меньше!", predict_number)
            

        elif predict_number < number:
            minimum = predict_number #Обновляем миминимум
            predict_number = int(np.mean([minimum,maximum]))
            print("Число должно быть больше!", predict_number)
            


        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)