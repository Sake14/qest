import math

def distance(x1, y1, x2, y2):
    """
    Вычисляет расстояние между двумя точками (x1, y1) и (x2, y2).
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    try:
        x1 = float(input("Введите x1: "))
        y1 = float(input("Введите y1: "))
        x2 = float(input("Введите x2: "))
        y2 = float(input("Введите y2: "))
    except ValueError:
        print("Ошибка: координаты должны быть числами.")
        return
    d = distance(x1, y1, x2, y2)
    print(f"Расстояние между точками: {d:.3f}")

if __name__ == "__main__":
    main() 