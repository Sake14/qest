def count_integers(a, b, c):
    count = 0
    for value in (a, b, c):
        if isinstance(value, int):
            count += 1
    return count

if __name__ == "__main__":
    try:
        a = eval(input("Введите значение a: "))
        b = eval(input("Введите значение b: "))
        c = eval(input("Введите значение c: "))
    except Exception as e:
        print(f"Ошибка ввода: {e}")
        exit(1)
    result = count_integers(a, b, c)
    print(f"Количество целых чисел среди введённых: {result}") 