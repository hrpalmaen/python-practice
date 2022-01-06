def divisors(num: int):
    divisors = list(filter(lambda i: num % i == 0, range(1, num + 1)))
    return divisors

def run():
    num = input("ingrese un número: ")
    assert num.isnumeric(), "Debe ingresar un número entero."
    print(divisors(int(num)))
    print("termino")

if __name__ == '__main__':
    run()