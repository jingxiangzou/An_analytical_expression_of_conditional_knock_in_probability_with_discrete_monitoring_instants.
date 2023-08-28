# An analytical expression of knock-in probability under discrete monitoring
The question is as follows:

Suppose a stock follows Geometric Brownian Motion, with a dividend rate of $q$, the risk-free interest rate being $r$ and the stock's volatility being $\sigma$. Define 'knock-in price' $KI$ as the price the stock reaches when it constitutes a 'knock-in'.  Suppose the time zero price of the stock is $S_0$ and the price in a month is $S_1; S_1 > KI$; Please calculate the knock-in probability when the stock price is monitored once per day.


The following is my idea


I am first enlightened by the Theorem 10.3 from Sheldon Ross's Book \textit{Introduction to probability models}
which states that for 
\[
M(t) = \max\limits_{0\leq y \leq t} X(y)
\]
where $X(y)$ follows Brownian Motion. For $ y > x $ the conditional distribution of $M(t)$ should satisfy 
\begin{equation}
P(M(t) \ge y | X(t) = x) = e^{-2y (y-x) / {t\sigma ^2}}
\end{equation}

Ross proved that the conditional distribution of $M(t)$ given the value of $X(t)$ does not depend on value of the drift term. 

We also learn from the symmetry of Brownian Motion that for the scenario where the 'knock-in price' being $-KI$, the time zero price being $-S_0$ and the price in one month being $-S_1$, the knock-in probability would be the same. Now that the drift term is  irrelevant, we can obtain $y$ and $x$ in (1) from:

\[
- KI  = -S_0 e^y
\]
\[
-S_1 = -S_0 e^x 
\]
thus we have the knock-in probability under continuous monitoring:

\[
e^{- \frac{2}{t\sigma^2}log(\frac{KI}{S_0})log(\frac{KI}{S_1})}
\]

However, our question features monitoring in a discrete manner. I immediately think of your 1997 paper published on \textit{Mathematical Finance} which proposed a continuity correction for discrete barrier option pricing. The paper says and I quote, 'the correction shifts the barrier away from the underlying by a factor of $exp(\pm\beta\sigma \sqrt{\frac{T}{m}})$' In our case, apply the continuity correction and we arrive at the following expression:

\[
e^{- \frac{2}{t\sigma^2}log(\frac{KI exp(-\beta\sigma \sqrt{\frac{T}{m}})}{S_0})log(\frac{KI exp(-\beta\sigma \sqrt{\frac{T}{m}})}{S_1})}
\]

I wish applying this continuity correction to the conditional probability under the continuous case would arrive at a solution to the original problem. I am yet to mathematically justify my guess.


To justify the validity of formula (1), one proper measure is to compare the results produced by the formula to those produced by simulation. The reasons are as follows. If our assumptions for the dynamics of the simulation were correct, then the simulation results should not be far from the true ones, with the former converging to the latter as more paths are considered. And if it so happens that our approximation formula were correct, then the simulated results and the ones by the formula should not be significantly far from each other. It is worth noting though, that since the formula itself yields an \emph{approximation} of the knock-in probability instead of an exact result, we rightfully expect a certain level of discrepancy between the two types of results for any case where the number of instants $m < \infty$.
