print('Введите длинну шоколадки')
n = int(input())
print('Введите ширину шоколадки')
m = int(input())
print('Введите количество желаемых кусочков')
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
