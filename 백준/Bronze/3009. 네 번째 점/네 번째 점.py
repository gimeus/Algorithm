points = []

for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

fourth_x = 0
fourth_y = 0

for x in x_coords:
    if x_coords.count(x) == 1:
        fourth_x = x
        break

for y in y_coords:
    if y_coords.count(y) == 1:
        fourth_y = y
        break

print(fourth_x, fourth_y)