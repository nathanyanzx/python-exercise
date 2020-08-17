def triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        s=(p*(p-a)*(p-b)*(p-c))**0.5
        return '三角形的面积是：', s
    else:
        raise ValueError('两边之和必须大于第三边')
print(triangle(5,5,6))