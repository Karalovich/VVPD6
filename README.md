# Лабораторная работа №6
Документация для результата лабораторных лабораторных работ №4 и №5, созданная по стандарту языка разметки [Markdown](https://ru.wikipedia.org/wiki/Markdown)
Программа позваляет высчитать последовательность по Гипотезе Сиракуз (она же Гипотеза Коллатца) [Гипотеза Коллатца](https://ru.wikipedia.org/wiki/Гипотеза_Коллатца).

## Оглавление

1. [Первая функция](#Первая-функция) 
2. [Вторая функция](#Вторая-функция) 
3. [Результаты](#Результаты) 

## Первая функция
Первая функция *syracuse_sequence* вычисляет последовательность Сиракуз по следующему алгоритму:
1) берём любое натуральное число N;
2) если оно чётное, то делим его на 2;
3) если оно нечётное, то умножаем на 3 и прибавляем 1 (получаем 3N + 1);
4) над полученным числом выполняем те же самые действия, и так далее.
Гипотеза Коллатца заключается в том, что какое бы начальное число n мы
ни взяли, рано или поздно мы получим единицу. 
Код функции:
```python
def syracuse_sequence(n):
    """
    Function to build Syracuse sequence
    :param n: number for building sequence
    :return: list of sequence
    """
    p_list = list()
    p_list.append(n)
    if n == 0:
        return []
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            p_list.append(int(n))
        else:
            n = n * 3 + 1
            p_list.append(int(n))
    return p_list
```
____
[:arrow_up:Оглавление](#Оглавление)
____
## Вторая функция
Вторая функция *syracuse_max* вычисляет максимальный элемент из последовательности Сиракуз по следующему алгоритму:
1) берётся список из элементов последовательности, созданный функцией *syracuse_sequence*;
2) за изначальный максимальный элемент (max_n) берётся 0 (ноль);
3) проходимся по всему списку через цикл for ;
4) если попадается элемент больше max_n (i > max_n) - присваиваем max_n значение i элемента.
Код функции:
```python
def syracuse_max(n):
    """
    Function to find maximal element in Syracuse sequence
    :param n: number for building sequence
    :return: maximal element in Syracuse sequence
    """
    p_list = syracuse_sequence(n)
    max_n = 0
    for i in p_list:
        if i > max_n:
            max_n = i
    return max_n
```
____
[:arrow_up:Оглавление](#Оглавление)
____

## Результаты
Ниже предоставлены результаты тестирования через pytest, а также пример вставки изображения:
![image](https://user-images.githubusercontent.com/90208961/157606781-c57262ec-b69e-415d-856d-76bcfb31fc1d.png)
