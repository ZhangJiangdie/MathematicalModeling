"""
P6, 研究课题2：
【你正在考虑月利率为0.4%的250_000美元的30年抵押贷款。
  a). 确定360个月还清贷款的月还款p
  b). 现在假设你已经还了8年的月还款，而且你现在有机会来重新制定还款计划。你可以在以下两种情况下进行选择：
  或者是年利率为4%的每月还款的20年贷款，或者是年利率为3.8%的每月还款的15年贷款。每种贷款都要支付2500美元
  的交易费。确定20年和15年贷款的月还款，你认为重新指定还款计划正确吗？如果正确的话，你喜欢20年还是15年的选择？】

  动力系统模型：
  delta a_n = 0.004 * a_n - p
  a_0 = 250_000
  a_360 = 0
"""


class DynamicsModel:
    """
    动力系统模型：
      delta a_n = rate * a_n - p
      a_0
      N: 还款周期
    """

    def __init__(self, name, a_0, rate, p, N):
        self.name = name
        self.a_0 = a_0
        self.rate = rate
        self.p = p
        self.N = N
        self.P = []
        self.A = {}

    def resolve_p(self):
        self.p = 0
        while True:
            self.p += 1
            temp_A = []
            a_i = self.a_0
            temp_A.append(a_i)
            for i in range(self.N):
                a_i = a_i + self.delta_n(i, a_i)
                temp_A.append(a_i)
            if a_i <= 0:
                if a_i + self.p > 0:
                    self.P.append(self.p)
                    temp_A[-1] = 0
                    self.A[self.p] = temp_A
                else:
                    temp_A[-1] = 0
                    break

    def delta_n(self, i, a_i):
        return round(self.rate * a_i - self.p, 2)

    def total_cost(self, p, left_index=0, right_index=None):
        # total cost in the half-open region: [left_index, right_index)
        A = self.A[p]
        sum = 0
        if A is None:
            return sum

        if right_index is None:
            right_index = len(A)

        if left_index < 0 or right_index > len(A) or left_index >= right_index:
            return sum

        for i in range(left_index, right_index - 1):
            sum += (A[i + 1] - A[i])

        if right_index == len(A):
            sum += A[-1]

        print("name=%s,p=%d,region[%d,%d),total_cost=%d" % (self.name, p, left_index, right_index, sum))
        return sum

    def print(self):
        print("name=%s,a_0:%d,rate=%f,P=" % (self.name, self.a_0, self.rate), self.P)
        for pi in self.P:
            print("name=%s,p=%d,A=" % (self.name, pi), self.A[pi])


model_30 = DynamicsModel("model_30", 250_000, 0.004, 0, 30 * 12)
model_30.resolve_p()
model_30.print()

for pi in model_30.P:
    a_n = model_30.A[pi][8 * 12]
    model_20 = DynamicsModel("model_20", a_n + 2_500, 0.04 / 12.0, 0, 20 * 12)
    model_20.resolve_p()
    model_20.print()

    model_15 = DynamicsModel("model_15", a_n + 2_500, 0.038 / 12.0, 0, 15 * 12)
    model_15.resolve_p()
    model_15.print()

    model_30.total_cost(pi)
    model_30.total_cost(pi, 8 * 12)
    for pii in model_20.P:
        model_20.total_cost(pii)
    for piii in model_15.P:
        model_15.total_cost(piii)

    del model_20
    del model_15

del model_30
