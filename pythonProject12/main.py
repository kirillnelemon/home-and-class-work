import math

def frange(start,stop,step):
    i=start
    while i < stop:
        yield i
        i += step
#cоздаем значение аргумента x и функции y1 and y2 по формуле
x=[i for i in frange(-6.0,1.0,6.0)]
y1 = [(3+math.sin(i)2)/(1+i2) for i in x]
y2 =[(1/3)*(i**2)*(math.cos(i)**2) for i in x]

filename='data.txt'
with open(filename, 'w') as outfile:
    outfile.write('#значения x, y1 и y2\n')
    for xi, y1i, y2i in zip(x,y1,y2):
        outfile.write('%10.5f %10.5f %10.5f\n' % (xi, y1i, y2i))
outfile.close()

result=map(lambda i1,i2: i1+i2, y1, y2)
y=list(result)

with open(filename, 'a') as  outfile:
    outfile.write('#результат задания')
    for xi, yi in zip (x,y):
        outfile.write('%10.5f %10.5f\n' % (xi, yi))
outfile.close()
print(y)
print(x)
print(xi)
print(yi)