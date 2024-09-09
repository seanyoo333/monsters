# 원뿔 구하는 방법, 반지름(r)과 높이(h)는  1<= r, h <= 100
PI = 3.14152653589793
radius = int(input())
height = int(input())

cone_volume = (PI * radius**2 * height / 3)

print(cone_volume)
