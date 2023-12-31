'''
Anastasya Osokina 72%
Alena Kareva 85%

'''
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
    def square(n):
        for _ in range(4):
            forward(n)
            left(-90)

    def rec_square(n):
        if n <= 1:
            return None
        square(n)
        forward(0.1*n)
        left(-10)
        return rec_square(0.9*n)

    rec_square(100)
    done()


elif choice == "2":
    def tree(height, size, corner):
        if height == 0:
            return None
        if height > 0:
            forward(size)
            right(corner)
            tree(height - 1, size / 2, corner)
            left(corner * 2)
            tree(height - 1, size / 2, corner)
            right(corner)
            backward(size)

    def main():
        left(90)
        tree(height, size, corner)

    height = int(input("Введите высоту дерева: "))
    size = int(input("Введите длину стороны дерева: "))
    corner = int(input("Введите угол между ветвями: "))

    main()
    mainloop()

elif choice == "3":
        def draw(l, n):
            if n == 0:
                left(180)
                return

            x = l / (n + 1)
            for i in range(n):
                forward(x)
                left(45)
                draw(0.5 * x * (n - i - 1), n - i - 1)
                left(90)
                draw(0.5 * x * (n - i - 1), n - i - 1)
                right(135)

            forward(x)
            left(180)
            forward(l)


        left(90)
        draw(400, 5)
    

elif choice == "4":
    def koch(n, size):
        if n == 0:
            forward(size)
        else:
            koch(n - 1, size / 3)
            left(60)
            koch(n - 1, size / 3)
            right(120)
            koch(n - 1, size / 3)
            left(60)
            koch(n - 1, size / 3)

    def main():
        up()
        goto(-100, 0)
        down()
        koch(n, size)

    n = int(input("Введите глубину рекурсии: "))
    size = int(input("Введите длину стороны: "))

    main()
    mainloop()

elif choice == "5":
    def koch(order, size):
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
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        for _ in range(3):
          koch(n, a)
          right(120)
    
    main()
    done()
    

elif choice == "6":
    def mino_curve(order, size):
        if order == 0:
            forward(size)
        else:
            mino_curve(order-1, size/4)
            left(90)
            mino_curve(order-1, size/4)
            right(90)
            mino_curve(order-1, size/4)
            right(90)
            mino_curve(order-1, size/4)
            mino_curve(order-1, size/4)
            left(90)
            mino_curve(order-1, size/4)
            left(90)
            mino_curve(order-1, size/4)
            right(90)
            mino_curve(order-1, size/4)

    speed(0)
    up()
    goto(-150, 0)
    down()

    mino_curve(3, 300)

    done()


elif choice == "7":
    def ice(order, size):
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
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        ice(n, a)

    main()
    done()



elif choice == "9":
    def levi(n, size):
        if n == 0:
            forward(size)
        else:
            left(45)
            levi(n - 1, size / 2)
            right(90)
            levi(n - 1, size / 2)
            left(45)

    def main():
        up()
        goto(-100, 0)
        down()
        levi(n, size)

    n = int(input("Введите глубину рекурсии: "))
    size = int(input("Введите размер стороны: "))

    main()
    mainloop()

elif choice == "10":
    def balls(n, radius):
        if n == 0:
            circle(radius)
        else:
            circle(radius)
            left(45)
            balls(n - 1, radius * 0.5)
            right(90)
            balls(n - 1, radius * 0.5)
            left(45)

    def main():
        up()
        goto(-100, 0)
        down()
        balls(n, radius)

    n = int(input("Введите глубину рекурсии: "))
    radius = int(input("Введите радиус кружка: "))

    main()
    mainloop()

elif choice == "11":
    def draw_flower(x, y, size, depth):
        if depth > 0:
            turtle.up()
            turtle.goto(x, y - size)
            turtle.down()
            turtle.circle(size)
            draw_flower(x - size, y, size/2, depth-1)
            draw_flower(x + size, y, size/2, depth-1)
            draw_flower(x, y - size, size/2, depth-1)
            draw_flower(x, y + size, size/2, depth-1)

    turtle.speed(0)
    draw_flower(0, 0, 100, 5)
    turtle.done()


elif choice == "12":
    def snow(order, size):
        if order == 0:
            forward(size)
        else:
            left(90)
            snow(order-1, size/3)
            right(60)
            snow(order-1, size/3)
            left(120)
            snow(order-1, size/3)
            right(60)
            snow(order-1, size/3)
            right(90)

    def main():
        up()
        goto(0,0)
        down()
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        for _ in range(8):
            snow(n, a)
            right(45)

    main()
    done()

    
