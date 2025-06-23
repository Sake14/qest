def print_price_table(price_per_kg, start_g, end_g, step_g):
    print(f"Цена за 1 кг: {price_per_kg:.2f} руб.")
    print("Вес (г)\tСтоимость (руб)")
    for grams in range(start_g, end_g + 1, step_g):
        cost = price_per_kg * grams / 1000
        print(f"{grams}\t{cost:.2f}")

def main():
    try:
        price = float(input("Введите цену за 1 кг: "))
        a = int(input("Введите начальный вес (г): "))
        b = int(input("Введите конечный вес (г): "))
        c = int(input("Введите шаг (г): "))
        if price < 0 or a < 0 or b < 0 or c <= 0 or a > b:
            raise ValueError
    except ValueError:
        print("Ошибка: некорректные входные данные.")
        return
    print_price_table(price, a, b, c)

if __name__ == "__main__":
    main() 