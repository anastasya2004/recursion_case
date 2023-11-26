from turtle import *

print("Привет! Какой фрактал вы хотите посмотреть? Выберите число")
print("1 Рекурсивная функция")
print("2 Построение двоичного дерева")
print("3 Фрактал Ветка")
print("4 Кривая Коха")
print("5 Снежинка Коха")
print("6 Кривая Минковского")
print("7 Первая ледяная фигура")
print("8 Вторая ледяная фигура")
print("9 Кривая Леви")
print("10 Фрактал Алёны")
print("11 Фрактал Ангелины")
print("12 Фрактал Анастасии")

choice = input("\n")

if choice == "1":
    print(  for _ in range(4):
    forward(n)
    left(-90)

    def rec_square(n):
      if n <= 1:
        return None
      square(n)
      left(-5)
      return rec_square(0.9*n)
    
    rec_square(100)
    done())

elif choice == "2":
    print("тут будет код")

elif choice == "3":
    print("тут будет код")

elif choice == "4":
    print("тут будет код")

elif choice == "5":
    print(def koch(order, size):
    if order == 0:          
        forward(size)
    else:
        koch(order-1, size/3)   
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)

    def main():
        up()
        goto(-100,0)
        down()
        n = int(input('Глубина рекурсии:'))
        a = int(input('Длина стороны:'))
        for _ in range(3):
          koch(n, a)
          right(120)
    
    if __name__ == '__main__':
        main())

elif choice == "6":
    print("тут будет код")

elif choice == "7":
    print(def ice(order, size):
    if order == 0:          
        forward(size)
    else:
        ice(order-1, size/2)   
        left(90)
        ice(order-1, size/4)
        right(180)
        ice(order-1, size/4)
        left(90)
        ice(order-1, size/2)

    def main():
        up()
        goto(-100,0)
        down()
        n = int(input('Глубина рекурсии:'))
        a = int(input('Длина стороны:'))
        ice(n, a)
    
    if __name__ == '__main__':
        main())

elif choice == "8":
    print("тут будет код")

elif choice == "9":
    print("тут будет код")

elif choice == "10":
    print("тут будет код")

elif choice == "11":
    print("тут будет код")

elif choice == "12":
    print(    if size > 0:
        circle(size)
        draw_circle(size-10)

    draw_circle(100)
    done())
