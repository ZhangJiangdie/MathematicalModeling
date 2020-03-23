import matplotlib.pyplot as plt

'''
P6, exercise-12,13：
【你当前的信用卡欠款余额为12_000美元，而当前的利率为19.9%，利息是按月计算的，确定什么样的月还款p美元才能在
  以下情况下还清欠款：
  a). 2年，假定有新的信用卡支付k美元
  b). 4年，假定有新的信用卡支付k美元
  】
  动力系统模型：
  Delta b_n = 0.199/12.0 * b_n - p + k
  b_0 =12_000
  b_24 = 0 (b_48 = 0)
'''

b_0 = 12_000
p = 0
k = 0


def delta_n(n, b_n):
    return round(0.199 / 12.0 * b_n - p + k, 2)


def showArray(B):
    for i in range(len(B)):
        print("\nn=%d,b_n=%.2f" % (i, B[i]))

    plt.figure()
    plt.scatter(range(len(B)), B)
    plt.show()


P = []  # p的数值解的集合
B = [b_0, ]
b_i = b_0
N = 24
# N = 48
# k = 0
k = 105
while True:
    p += 1
    b_i = b_0
    for i in range(N):
        b_i = b_i + delta_n(i, b_i)
    print("p=%d,N=%d,b_n=%.2f" % (p, N, b_i))
    if b_i <= 0:
        if b_i + p - k > 0:
            P.append(p)
        else:
            break

print("P:", P)
