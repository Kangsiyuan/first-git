import random
def ra():
    list1 = []
    for i in range(10):
        x = random.randint(0,10)
        list1.append(x)
    return set(list1)
a = ra();
b = ra();
print("A矩阵:",a,"矩阵长度：",len(a),"最大值：",max(a),"最小值：",min(a))
print("B矩阵:",b,"矩阵长度：",len(b),"最大值：",max(b),"最小值：",min(b))
print("A、B的并集",a|b)
print("A、B的交集",a&b)
print("A、B的差集",a-b)