fSeries = []
a = 0
b = 1
for _ in range(10):
    a, b = b, a+b
    fSeries.append(a)
print(fSeries)
