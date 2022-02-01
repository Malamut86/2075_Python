def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
a = ("Процент")
b = ("Процента")
c = ("Процентов")
N = input("Введите любой N")
numbers = {11,12,13,14}
for N in range(100):
    N = N + 1
    if N in numbers:
        print("У Вас ", N, "процентов")
    elif N % 10 == 1:
        print("У Вас ",N, "процент")
    elif N % 10 > 1 and N % 10 <5:
        print("У Вас ",N, "процента")
    else:
        print("У Вас ",N, "процентов")

