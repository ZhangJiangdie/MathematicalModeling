"""
P6, 研究课题1：
【随着汽油价格的上涨，今年你希望买一辆新的（混合动力）汽车，你把选择范围缩小到以下几种2012车型：
  Ford Fiesta, Ford Focus, Chevy Volt, Chevy Cruz, Toyota Camry Hybrid, Toyota Prius, Toyota Corolla.
  每家公司都向你提供如下的“优惠价”。你有能力支付多达60个月的大约500美元的月还款，采用动力系统的方法来确定你
  可以买哪种新的汽车。
  ----------------------------------------------------------------------------
  2012车型               优惠价（美元）       预付款（美元）     利率和贷款持续时间
  ----------------------------------------------------------------------------
  Ford Fiesta            14_200             500             年利率4.5%,60个月
  Ford Focus             20_705             750             年利率4.38%,60个月
  Chevy Volt             39_312             1_000           年利率3.28%,60个月
  Chevy Cruz             16_800             500             年利率4.4%,60个月
  Toyota Camry           22_955             0               年利率4.8%,60个月
  Toyota Camry Hybrid    26_500             0               年利率3%,48个月
  Toyota Corolla         16_500             900             年利率4.25%,60个月
  Toyota Prius           19_950             1_000           年利率4.3%,60个月
  ----------------------------------------------------------------------------
  】
  动力系统模型：
  Delta b_n = rate * b_n - p
  b_0 = cost - prepaid
"""

# (name, cost, prepaid, rate, period)
selections = [("Ford Fiesta", 14_200, 500, 0.045, 60),
              ("Ford Focus", 20_705, 750, 0.0438, 60),
              ("Chevy Volt", 39_312, 1_000, 0.0328, 60),
              ("Chevy Cruz", 16_800, 500, 0.044, 60),
              ("Toyota Camry", 22_955, 0, 0.048, 60),
              ("Toyota Camry Hybrid", 26_500, 0, 0.03, 48),
              ("Toyota Corolla", 16_500, 900, 0.0425, 60),
              ("Toyota Prius", 19_950, 1_000, 0.043, 60)]

P = {}

b_0 = 0
p = 0


def delta_n(n, rate, b_n):
    return round(rate / 12.0 * b_n - p, 2)


for i in range(len(selections)):
    (name, cost, prepaid, rate, period) = selections[i]
    temp_p = []
    b_0 = cost - prepaid
    p = 0
    while True:
        p += 1
        b_i = b_0
        for i in range(period):
            b_i = b_i + delta_n(i, rate, b_i)

        if b_i <= 0:
            if b_i + p > 0:
                temp_p.append(p)
            else:
                break
    P[i] = temp_p
    print("(name, cost, prepaid, rate, period)=", (name, cost, prepaid, rate, period), ", monthly_cost=", P[i])


'''
(name, cost, prepaid, rate, period)= ('Ford Fiesta', 14200, 500, 0.045, 60) , monthly_cost= [256, 257, 258, 259]
(name, cost, prepaid, rate, period)= ('Ford Focus', 20705, 750, 0.0438, 60) , monthly_cost= [371, 372, 373, 374, 375, 376]
(name, cost, prepaid, rate, period)= ('Chevy Volt', 39312, 1000, 0.0328, 60) , monthly_cost= [694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704]
(name, cost, prepaid, rate, period)= ('Chevy Cruz', 16800, 500, 0.044, 60) , monthly_cost= [304, 305, 306, 307]
(name, cost, prepaid, rate, period)= ('Toyota Camry', 22955, 0, 0.048, 60) , monthly_cost= [432, 433, 434, 435, 436, 437]
(name, cost, prepaid, rate, period)= ('Toyota Camry Hybrid', 26500, 0, 0.03, 48) , monthly_cost= [587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598]
(name, cost, prepaid, rate, period)= ('Toyota Corolla', 16500, 900, 0.0425, 60) , monthly_cost= [290, 291, 292, 293]
(name, cost, prepaid, rate, period)= ('Toyota Prius', 19950, 1000, 0.043, 60) , monthly_cost= [352, 353, 354, 355, 356]
所以，除了'Chevy Volt'和'Toyota Camry Hybrid'月还款超过500美元，其它车型都在支付能力范围内。
'''
