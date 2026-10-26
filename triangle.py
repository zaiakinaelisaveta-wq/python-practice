import math

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
angle = float(input("Введите угол между сторонами в градусах: "))

c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(angle)))

print("Длина третьей стороны:", round(c, 2))