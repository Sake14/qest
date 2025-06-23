def calculate_trip_cost(distance_km, fuel_per_100km, fuel_price):
    """
    Вычисляет стоимость поездки на дачу (туда и обратно).
    distance_km: расстояние до дачи в км (float)
    fuel_per_100km: расход бензина на 100 км (float)
    fuel_price: цена 1 литра бензина (float)
    Возвращает стоимость поездки (float)
    """
    total_distance = distance_km * 2
    fuel_needed = total_distance * fuel_per_100km / 100
    return fuel_needed * fuel_price

def main():
    try:
        distance = float(input("Введите расстояние до дачи (км): "))
        fuel_rate = float(input("Введите расход бензина на 100 км: "))
        price = float(input("Введите цену 1 литра бензина: "))
        if distance < 0 or fuel_rate < 0 or price < 0:
            raise ValueError
    except ValueError:
        print("Ошибка: все значения должны быть неотрицательными числами.")
        return
    cost = calculate_trip_cost(distance, fuel_rate, price)
    print(f"Стоимость поездки на дачу (туда и обратно): {cost:.2f} руб.")

if __name__ == "__main__":
    main() 