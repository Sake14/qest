import math

def distance(x, y):
    """
    Вычисляет расстояние от точки (x, y) до начала координат.
    """
    return math.sqrt(x ** 2 + y ** 2)

def main():
    try:
        x1 = float(input("Введите x координату точки A: "))
        y1 = float(input("Введите y координату точки A: "))
        x2 = float(input("Введите x координату точки B: "))
        y2 = float(input("Введите y координату точки B: "))
    except ValueError:
        print("Ошибка: координаты должны быть числами.")
        return
    dist_a = distance(x1, y1)
    dist_b = distance(x2, y2)
    print(f"Расстояние от A до начала координат: {dist_a:.3f}")
    print(f"Расстояние от B до начала координат: {dist_b:.3f}")
    if dist_a < dist_b:
        print("Точка A ближе к началу координат.")
    elif dist_b < dist_a:
        print("Точка B ближе к началу координат.")
    else:
        print("Обе точки на одинаковом расстоянии от начала координат.")

if __name__ == "__main__":
    main() 