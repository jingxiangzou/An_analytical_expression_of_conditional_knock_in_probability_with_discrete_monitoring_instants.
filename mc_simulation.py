import numpy as np
import pandas as pd
import random
import scipy as sp
from scipy.special import zeta
import matplotlib.pyplot as plt
import time


class testclass:
    def __init__(self, sigma, duration, instants, s0, s1, ki):
        """
        :param sigma: volatility
        :param duration: duration, T
        :param instants: number of monitoring instants
        :param s0: starting price
        :param s1: ending price
        """
        self.sig = sigma
        self.T = duration
        self.m = instants
        self.s0 = s0
        self.s1 = s1
        self.ki = ki

    def ana_appro(self):
        beta = -1 * zeta(1/2) / np.sqrt(2 * np.pi)
        adj_ki = self.ki * np.exp(-1 * beta * self.sig * np.sqrt(self.T/self.m))
        return np.exp((-2.0)/ (self.T * self.sig * self.sig) * np.log(adj_ki / self.s0) * np.log(adj_ki / self.s1))

    def ana_cont(self):
        return np.exp(-2 * np.log(self.ki/self.s1) * np.log(self.ki/self.s0) / (self.T * self.sig * self.sig))

    def mc_sim(self, nsim):
        count = 0
        for isim in range(nsim):
            a = np.random.normal(0, self.sig * np.sqrt(self.T/self.m), self.m)
            b = [0] * (self.m + 1)

            for i in range(self.m):
                b[i+1] = a[i] + b[i] # b is the BM
            c = [0] * (self.m + 1)

            for j in range(self.m + 1):
                c[j] = b[j] - (j / self.m) * b[-1] # the brownian bridge

            dd = [np.log(self.s1 / self.s0) * (ii / self.m) for ii in range(self.m + 1)]
            d = np.add(c, dd)
            e = [self.s0 * np.exp(d[jj]) for jj in range(self.m + 1)]
            if min(e) < self.ki:
                count += 1

        return (1.0000000 * count) / nsim

    def mot_sim(self, nsim):
        a = np.random.normal(0, self.sig * np.sqrt(self.T / self.m), self.m * nsim)
        b = a.reshape((nsim, self.m))
        c = np.cumsum(b, axis=1) # sum over columns for each row

        # we get the vmt which translate brownian motion into brownian bridge
        vmt = np.eye(self.m)
        ary = np.zeros(self.m)
        ary[:-1] = -1/self.m * np.arange(1, self.m)
        vmt[-1, :] = ary
        mat = c @ vmt

        # dd = [np.log(self.s1 / self.s0) * (ii / self.m) for ii in range(self.m + 1)]
        d = np.array(list(np.log(self.s1 / self.s0) / self.m * np.arange(1, self.m + 1)) * nsim)
        e = d.reshape((nsim, self.m))
        nmat = np.add(mat, e)
        return sum(nmat.min(axis=1) < np.log(self.ki / self.s0)) / nsim


if __name__ == '__main__':
    test1 = testclass(0.3, 1/12, 21, 100, 95, 90)
    print(test1.ana_appro())
    start = time.time()
    print(test1.mot_sim(1000000)) # 100万
    end = time.time()
    print(end - start)

    df =pd.DataFrame(columns=['instants', 'sigma', 's1', 'ana_prob', 'mc_prob', 'discrepancy', 'continuous'])
    tme = 0
    for sig in np.arange(0.15, 0.45, 0.02):
        for s in np.arange(91, 96, 0.1):
            for m in np.array([5, 12, 21, 50]):
                tc = testclass(sig, 1/12, m, 100, s, 90)
                ana_p = tc.ana_appro()
                mc_p = tc.mot_sim(5000000)
                tme += 1
                print(tme)
                new_row = pd.DataFrame({'instants': m, 'sigma': sig, 's1': s, 'ana_prob': ana_p, 'mc_prob': mc_p,
                                        'discrepancy': abs(ana_p - mc_p), 'continuous': tc.ana_cont()},
                                        index=[0])
                df = pd.concat([new_row, df.loc[:]]).reset_index(drop=True)

    df.to_excel('sresinf.xlsx')




