#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Вводится число экзаменов N<=20. Напечатать фразу "Мы успешно сдали N экзаменов",
# согласовав слово "экзамен" с числом N.

if __name__ == '__main__':
    count = int(input("Введите число экзаменов: "))
    if count <= 0:
        print("Неправильное число")
    elif count == 1:
        print(f"Мы успешно сдали {count} экзамен")
    elif count < 5:
        print(f"Мы успешно сдали {count} экзамена")
    elif count <= 20:
        print(f"Мы успешно сдали {count} экзаменов")
    else:
        print("Слишком много экзаменов")
