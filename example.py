# Модуль для демонстрации работы math_segment.py


def correct_input(left, right):
    """
    Функция для считывания корректного числового ответа в
    ограниченном диапазоне
    """
    check = 1
    answer = ''
    while check:
        try:
            answer = input()
            if len(answer) == 0:
                print('Вы ничего не ввели')
                continue
            answer = int(answer)
            if answer not in range(left, right + 1):
                print(f'Вы ввели не число от {left} до {right}')
                continue
            check = 0
        except ValueError:
            print('Вы ввели не число')
        else:
            check = 0
    return answer


def answer_1():
    print("""Выберите действие:
0 - Выйти
1 - Ввести промежуток
2 - Узнать принадлежность точки к промежутку
3 - Информация
4 - Удалить промежуток
>2
Введите координату точки: >3
К какому промежутку хотите проверить принадлежность точки?
>example
На данный момент не было введено промежутка с таким именем
Граница - [] или ()
Введите левую границу: >[
Введите правую границу: >]
Введите левую координату: >2
Введите правую координату: >4
Отрезок создан
Принадлежит
""")


def answer_2():
    print("""Выберите действие:
0 - Выйти
1 - Ввести промежуток
2 - Узнать принадлежность точки к промежутку
3 - Информация
4 - Удалить промежуток
>1
Граница - [] или ()
Введите левую границу: >(
Введите правую границу: >]
Введите левую координату: >inf
Введите правую координату: >10
Введите название для промежутка(например AB или h): >example
Отрезок создан
Выберите действие:
0 - Выйти
1 - Ввести промежуток
2 - Узнать принадлежность точки к промежутку
3 - Информация
4 - Удалить промежуток
>3
На данный момент известно следующее:
Название промежутка: example
Его область определения: (inf;10]
Выберите действие:
0 - Выйти
1 - Ввести промежуток
2 - Узнать принадлежность точки к промежутку
3 - Информация
4 - Удалить промежуток
4
Для выхода введите --
Введите название промежутка, который хотите удалить:
>example
Промежуток успешно удалён""")


def answer_3():
    print("""Выберите действие:
0 - Выйти
1 - Ввести промежуток
2 - Узнать принадлежность точки к промежутку
3 - Информация
4 - Удалить промежуток
>1
Граница - [] или ()
Введите левую границу: >[
Введите правую границу: >)
Введите левую координату: >-10
Введите правую координату: >inf
Введите название для промежутка(например AB или h): >example
Отрезок создан
Выберите действие:
0 - Выйти
1 - Ввести промежуток
2 - Узнать принадлежность точки к промежутку
3 - Информация
4 - Удалить промежуток
>2
Введите координату точки: -9
К какому промежутку хотите проверить принадлежность точки?
example
Принадлежит""")


def main():
    """
    Фунция выводит пример входных данных и соответствующего результата
    """
    print('3 примера работы программы math_segments:\n'
          '1 -- Узнать принадлежность точки к промежутку\n'
          '2 -- Ввести промежуток, вывести информацию, удалить введённый промежуток\n'
          '3 -- Ввести промежуток, узнать принадлежность точки к промежутку')
    example_answer = correct_input(1, 3)
    if example_answer == 1:
        answer_1()
    if example_answer == 2:
        answer_2()
    if example_answer == 3:
        answer_3()


if __name__ == "__main__":
    main()
