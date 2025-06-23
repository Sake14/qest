def seconds_to_time(k):
    """
    Преобразует k-ю секунду суток в количество полных часов и минут.
    Возвращает (часы, минуты).
    """
    if not (0 <= k < 86400):
        raise ValueError("k должно быть в диапазоне от 0 до 86399")
    hours = k // 3600
    minutes = (k % 3600) // 60
    return hours, minutes

def main():
    try:
        k = int(input("Введите k (номер секунды от 0 до 86399): "))
        h, m = seconds_to_time(k)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return
    print(f"С начала суток прошло {h} полных часов и {m} полных минут.")

if __name__ == "__main__":
    main() 