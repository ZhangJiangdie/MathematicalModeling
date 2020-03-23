import matplotlib.pyplot as plt

'''
P4, 例2：
【六年前，你的父母筹措月利率为1%,、每月还款为880.87美元的20年贷款资金80000美元买了房子，他们已经还款72个月，
  同时想知道他们还欠多少抵押贷款。】
  动力系统模型：
  Delta b_n = 0.01b_n - 880.87
  b_0 = 80000
'''

b_0 = 80000


def delta_n(n, b_n):
    return round(0.01 * b_n - 880.87, 2)


N = 20 * 12
B = [b_0, ]
b_i = b_0
for i in range(N):
    b_i = b_i + delta_n(i, b_i)
    if b_i <= 0:
        b_i = 0
        B.append(b_i)
        break
    else:
        B.append(b_i)

for i in range(len(B)):
    print("\nn=%d,b_n=%.2f" % (i, B[i]))

plt.figure()
plt.scatter(range(len(B)), B)
plt.show()
