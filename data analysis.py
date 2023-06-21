# data analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df2 = pd.read_excel('sresinf.xlsx')
print(df2)
print(df2.describe())

t11 = df2['sigma'] == 0.15
t12 = df2['sigma'] == 0.19
t13 = df2['sigma'] == 0.23
t14 = df2['sigma'] == 0.27
t15 = df2['sigma'] == 0.31
t16 = df2['sigma'] == 0.35
t17 = df2['sigma'] == 0.39
t18 = df2['sigma'] == 0.43

t21 = df2['instants'] == 5
t22 = df2['instants'] == 12
t23 = df2['instants'] == 21
t24 = df2['instants'] == 50


# insec df are names with indexs sigma + instants
# sig = 0.31 different instants
df1521 = df2[np.logical_and(t15, t21)]
df1522 = df2[np.logical_and(t15, t22)]
df1523 = df2[np.logical_and(t15, t23)]
df1524 = df2[np.logical_and(t15, t24)]

# sig = 0.19 different instants
df1221 = df2[np.logical_and(t12, t21)]
df1222 = df2[np.logical_and(t12, t22)]
df1223 = df2[np.logical_and(t12, t23)]
df1224 = df2[np.logical_and(t12, t24)]


# figures
print('\n 21')
df21 = df2[t21]
print(round(df21['discrepancy'].mean(), 5))
print(round(df21['ratio'].mean(), 5))

print('\n 22')
df22 = df2[t22]
print(round(df22['discrepancy'].mean(), 5))
print(round(df22['ratio'].mean(), 5))

print('\n23')
df23 = df2[t23]
print(round(df23['discrepancy'].mean(), 5))
print(round(df23['ratio'].mean(), 5))

print('\n24')
df24 = df2[t24]
print(round(df24['discrepancy'].mean(), 5))
print(round(df24['ratio'].mean(),5))


print('\n\n\nhow volatility affects approximation results')
df11 = df2[t11]
df13 = df2[t13]
df15 = df2[t15]
df17 = df2[t17]
print('\nsig 0.15')
print(round(df11['discrepancy'].mean(), 5))
print(round(df11['ratio'].mean(),5))
print('\nsig 0.23')
print(round(df13['discrepancy'].mean(), 5))
print(round(df13['ratio'].mean(),5))
print('\nsig 0.31')
print(round(df15['discrepancy'].mean(), 5))
print(round(df15['ratio'].mean(),5))
print('\nsig 0.39')
print(round(df17['discrepancy'].mean(), 5))
print(round(df17['ratio'].mean(),5))







# sigma = 0.31 s1 VS ana_prob with different m
plt.plot(df1521['s1'], df1521['continuous'], label='continuous')
plt.plot(df1521['s1'], df1521['ana_prob'], label='instants = 5', linestyle='-')
plt.plot(df1522['s1'], df1522['ana_prob'], label='instants = 12', linestyle='--')
plt.plot(df1523['s1'], df1523['ana_prob'], label='instants = 21', linestyle='-.')
plt.plot(df1524['s1'], df1524['ana_prob'], label='instants = 50', linestyle=':')

plt.xlabel('Time T stock price')
plt.ylabel('Probability')
plt.title("Knock-in probability of sigma = 0.31")
plt.legend(edgecolor='black')
plt.savefig('1_sig_0point3_s1_vs_ana_prob.jpg')
plt.show() # figure 1, sig = 0.3 s1 vs ana_prob with different m
plt.clf() # clear all plots


# sigma = 0.19 s1 VS ana_prob with different m
#
plt.plot(df1221['s1'], df1221['continuous'], label='continuous')
plt.plot(df1221['s1'], df1221['ana_prob'], label='instants = 5', linestyle='-')
plt.plot(df1222['s1'], df1222['ana_prob'], label='instants = 12', linestyle='--')
plt.plot(df1223['s1'], df1223['ana_prob'], label='instants = 21', linestyle='-.')
plt.plot(df1224['s1'], df1224['ana_prob'], label='instants = 50', linestyle=':')

plt.xlabel('Time T stock price')
plt.ylabel('Probability')
plt.title("Knock-in probability of sigma = 0.19")
plt.legend(edgecolor='black')
plt.savefig('2_sig_0point19_s1_vs_ana_prob.jpg')
plt.show() # figure 2, sig = 0.19 s1 vs ana_prob with different m
plt.clf() # clear all plots

#
# m = 21, s1 VS ana_prob with different sigmas
df2311 = df2[np.logical_and(t23, t11)]
df2312 = df2[np.logical_and(t23, t12)]
df2313 = df2[np.logical_and(t23, t13)]
df2314 = df2[np.logical_and(t23, t14)]
df2315 = df2[np.logical_and(t23, t15)]
df2316 = df2[np.logical_and(t23, t16)]
df2317 = df2[np.logical_and(t23, t17)]
df2318 = df2[np.logical_and(t23, t18)]

plt.plot(df2311['s1'], df2311['ana_prob'], label='sigma = 0.15', linestyle='-')
plt.plot(df2312['s1'], df2312['ana_prob'], label='sigma = 0.19', linestyle='--')
plt.plot(df2313['s1'], df2313['ana_prob'], label='sigma = 0.23', linestyle='-.')
plt.plot(df2314['s1'], df2314['ana_prob'], label='sigma = 0.27', linestyle=':')
plt.plot(df2315['s1'], df2315['ana_prob'], label='sigma = 0.31', linestyle='-')
plt.plot(df2316['s1'], df2316['ana_prob'], label='sigma = 0.35', linestyle='--')
plt.plot(df2317['s1'], df2317['ana_prob'], label='sigma = 0.39', linestyle='-.')
# plt.plot(df2318['s1'], df2318['ana_prob'], label='sigma = 0.43', linestyle='')

plt.xlabel('Time T stock price')
plt.ylabel('Probability')
plt.title("Knock-in probability of instants m = 21")
plt.legend(edgecolor='black')
plt.savefig('3_m_21_s1_vs_ana_prob.jpg')
plt.show() # figure 3, m = 21 s1 vs ana_prob with different sigmas
plt.clf() # clear all plots

# m = 21, discrepancy VS s1 different sigmas
plt.plot(df2311['s1'], df2311['discrepancy'], label='sigma = 0.15', linestyle='-')
plt.plot(df2312['s1'], df2312['discrepancy'], label='sigma = 0.19', linestyle='--')
plt.plot(df2313['s1'], df2313['discrepancy'], label='sigma = 0.23', linestyle='-.')
plt.plot(df2314['s1'], df2314['discrepancy'], label='sigma = 0.27', linestyle=':')
plt.plot(df2315['s1'], df2315['discrepancy'], label='sigma = 0.31', linestyle='-')
plt.plot(df2316['s1'], df2316['discrepancy'], label='sigma = 0.35', linestyle='--')
plt.plot(df2317['s1'], df2317['discrepancy'], label='sigma = 0.39', linestyle='-.')
# plt.plot(df2318['s1'], df2318['discrepancy'], label='sigma = 0.43', linestyle='-.')

plt.xlabel('Time T stock price')
plt.ylabel('Approximation error')
plt.title("Approximation error of instants m = 21")
plt.legend(edgecolor='black')
plt.savefig('4_m_21_s1_vs_error.jpg')
plt.show() # figure 4, m = 21 s1 vs ana_prob with different sigmas
plt.clf() # clear all plots


# ratio VS s1 with different sigmas
plt.plot(df2311['s1'], df2311['ratio'], label='sigma = 0.15', linestyle='-')
plt.plot(df2312['s1'], df2312['ratio'], label='sigma = 0.19', linestyle='--')
plt.plot(df2313['s1'], df2313['ratio'], label='sigma = 0.23', linestyle='-.')
plt.plot(df2314['s1'], df2314['ratio'], label='sigma = 0.27', linestyle=':')
plt.plot(df2315['s1'], df2315['ratio'], label='sigma = 0.31', linestyle='-')
plt.plot(df2316['s1'], df2316['ratio'], label='sigma = 0.35', linestyle='--')
plt.plot(df2317['s1'], df2317['ratio'], label='sigma = 0.39', linestyle='-.')
# plt.plot(df2318['s1'], df2318['ratio'], label='sigma = 0.43', linestyle='-.')

plt.xlabel('Time T stock price')
plt.ylabel('Ratio')
plt.title("Approximation error ratio of instants m = 21")
plt.legend(edgecolor='black')
plt.savefig('5_m_21_s1_vs_error_ratio.jpg')
plt.show() # figure 5, m = 21 s1 vs appro error with different sigmas
plt.clf() # clear all plots

# sigma = 0.3, error VS s1 with different m

df1521 = df2[np.logical_and(t15, t21)]
df324 = df2[np.logical_and(t15, t22)]
df322 = df2[np.logical_and(t15, t23)]
df323 = df2[np.logical_and(t15, t24)]

plt.plot(df1521['s1'], df1521['discrepancy'], label='instants = 5', linestyle='-')
plt.plot(df1522['s1'], df1522['discrepancy'], label='instants = 12', linestyle='--')
plt.plot(df1523['s1'], df1523['discrepancy'], label='instants = 21', linestyle='-.')
plt.plot(df1524['s1'], df1524['discrepancy'], label='instants = 50', linestyle=':')

plt.xlabel('Time T stock price')
plt.ylabel('Approximation error')
plt.title("Approximation error of sigma = 0.31")
plt.legend(edgecolor='black')
plt.savefig('6_sig_0p31_s1_vs_error_ratio.jpg')
plt.show() # figure 6, m = 21 s1 vs appro error with different sigmas
plt.clf() # clear all plots

plt.plot(df1521['s1'], df1521['ratio'], label='instants = 5', linestyle='-')
plt.plot(df1522['s1'], df1522['ratio'], label='instants = 12', linestyle='--')
plt.plot(df1523['s1'], df1523['ratio'], label='instants = 21', linestyle='-.')
plt.plot(df1524['s1'], df1524['ratio'], label='instants = 50', linestyle=':')

plt.xlabel('Time T stock price')
plt.ylabel('Ratio')
plt.title("Approximation error ratio of sigma = 0.31")
plt.legend(edgecolor='black')
plt.savefig('7_sig_0p3_s1_vs_error_ratio.jpg')
plt.show() # figure 7, sig = 0.31 s1 vs appro error with different sigmas
plt.clf() # clear all plots
