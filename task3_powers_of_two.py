def print_powers_of_two(n):
    print("Степени двойки от 0 до", n)
    for i in range(n + 1):
        print(f"2^{i} = {2 ** i}")

def main():
    try:
        n = int(input("Введите n (целое неотрицательное число): "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Ошибка: n должно быть целым неотрицательным числом.")
        return
    print_powers_of_two(n)

if __name__ == "__main__":
    main() 