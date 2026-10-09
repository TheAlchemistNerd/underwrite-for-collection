# Mathematical appendix to Article 4

## A4.1 Scope, units and notation

This appendix derives Article 4’s economic-value, earnings, pricing, deposit, liquidity, collateral and control formulations. Numerical inputs are hypothetical. Additional assumptions introduced to complete a calculation are identified explicitly. A symbol is local to the section in which it is defined; amounts are in Kenyan shillings (KES), rates are annual decimal rates, and a basis point is $10^{-4}$ of a rate.

| Symbol | Meaning and unit |
|---|---|
| $t=0,\ldots,T$ | Decision or cash-flow index; the timetable states its actual dates |
| $\tau_t$ | Accrual fraction of a year for interval $t$ |
| $s$ | A declared economic and behavioural scenario |
| $P_s(0,t)$ | Discount factor to date $t$, dimensionless |
| $CF^A_{t,s},CF^L_{t,s}$ | Asset receipts and liability payments, KES |
| $B^A_{t,s},B^L_{t,s}$ | Relevant average accrual balances, KES |
| $r^A_{t,s},r^L_{t,s}$ | Asset and liability annual interest rates |
| $x_t,a_t,w_{t+1}$ | Decision state, action and next exogenous shock |
| $\pi,\gamma$ | Policy and one-period discount factor |
| $\mathbb E,\Pr$ | Expectation and probability under the specified model |

Currencies are converted using a declared convention before aggregation. Accrual profit, cash availability and present value are separate outputs. External funding expense and internal FTP are reconciled rather than charged twice to the consolidated bank.

## A4.2 From dated cash flows to EVE and duration

The value and earnings risk perspectives follow [1], [2].

Let $N_{t,s}=CF^A_{t,s}-CF^L_{t,s}$ be the net banking-book cash flow, augmented by relevant off-balance-sheet flows. With one reporting currency,

$$
\operatorname{EVE}_s=\sum_{t=1}^{T}P_s(0,t)N_{t,s},
\qquad
\Delta\operatorname{EVE}_s=\operatorname{EVE}_s-\operatorname{EVE}_0.
$$

The scenario affects both discount factors and behavioural flows. For a single parallel continuously compounded yield $y$, fixed $N_t$, and elapsed time $u_t$ in years,

$$
V(y)=\sum_t N_t e^{-yu_t},\qquad
V'(y)=-\sum_t u_tN_t e^{-yu_t}.
$$

Define $D(y)=-V'(y)/V(y)$ when $V(y)\ne0$. Taylor expansion gives

$$
V(y+\Delta y)-V(y)
=V'(y)\Delta y+\frac12V''(y)(\Delta y)^2+O((\Delta y)^3),
$$

$$
\Delta V\approx-D(y)V(y)\Delta y.
$$

This is the article’s first-order duration approximation. A finite-difference effective duration, allowing the valuation engine to re-estimate behavioural cash flows, is

$$
D_{\mathrm{eff}}=
\frac{V(y-h)-V(y+h)}{2hV(y)},
$$

where $h>0$ is a small yield shock. Net EVE can be close to zero or negative, making duration normalised by EVE unstable. In that case report dollar sensitivity $V'(y)$ and direct scenario changes. With a vector of curve nodes $\boldsymbol y$, the corresponding first-order expression is $\Delta V\approx\nabla V^{\mathsf T}\Delta\boldsymbol y$. Separate spread and basis shocks add their own derivatives. This prevents a single parallel duration from standing in for all rate, basis, option and credit-spread effects.

## A4.3 Earnings over an explicit horizon

For scenario $s$, a simple accrual representation is

$$
\operatorname{NII}_s(H)=
\sum_{t=1}^{H}\tau_t
\left(B^A_{t,s}r^A_{t,s}-B^L_{t,s}r^L_{t,s}\right)
+\sum_{t=1}^{H}J_{t,s}.
$$

Here $J_{t,s}$ contains only fees or hedge effects classified within the institution’s stated NII definition, including any required effective-interest treatment. Other fee income and valuation effects remain separately classified. Each interest term has units KES times annual rate times years, hence KES. Balances and rates can change with amortisation, repricing, deposit migration and new business. A run-off scenario sets new production to zero; constant-book and dynamic scenarios define their replacement rules. These assumptions explain why two NII projections can differ even when they share the same market-rate shock.

For an action comparison, compute $\Delta\operatorname{NII}_s=\operatorname{NII}_s^{\mathrm{candidate}}-\operatorname{NII}_s^{\mathrm{baseline}}$ using the same scenario and accounting perimeter. Principal receipts affect liquidity and balances; they are not interest income.

## A4.4 Curves, overnight compounding and FTP

The customer benchmark and pricing conventions follow [3], [4], [5].

A fixed-cash-flow instrument with quoted value $V^{\mathrm{quote}}$ supplies an equation

$$
V^{\mathrm{quote}}=\sum_{j=1}^{m}CF_jP(0,t_j).
$$

If earlier discount factors have already been obtained and $CF_m\ne0$, bootstrapping solves

$$
P(0,t_m)=
\frac{V^{\mathrm{quote}}-\sum_{j=1}^{m-1}CF_jP(0,t_j)}{CF_m}.
$$

Floating instruments require projected coupons as well as discount factors. Under a single-curve, simple-forward convention,

$$
F(0;t_{j-1},t_j)=
\frac{P(0,t_{j-1})/P(0,t_j)-1}{\tau_j}.
$$

A multi-curve framework uses a separately calibrated projection curve in the forward formula and the appropriate discount curve for valuation. Repricing checks compare each reconstructed value with its quotation under specified tolerances.

For overnight observations $k_j$, each applying to $d_j$ calendar days, and an applicable day-count denominator $B$, an illustrative compounded rate over the accrual period is

$$
\tau=\sum_j\frac{d_j}{B},\qquad
k_{\mathrm{comp}}=
\frac{\prod_j(1+k_jd_j/B)-1}{\tau}.
$$

The contract determines observation dates, holidays, lags, any floors and how the premium is applied. Where it specifies an annual additive premium $K$, a schematic rate is $r^{\mathrm{customer}}=k_{\mathrm{comp}}+K$. The benchmark is an input to contractual pricing; an internal FTP curve separately allocates the bank’s funding and liquidity economics. CBK’s revised pricing framework and the product’s actual terms determine the customer-facing application.

For an amortising product, period FTP charges are

$$
\operatorname{FTP}_t=B^{\mathrm{FTP}}_tf^{\mathrm{FTP}}_t\tau_t,
$$

where $B^{\mathrm{FTP}}_t$ is the approved chargeable balance and $f^{\mathrm{FTP}}_t$ the corresponding transfer rate. An equivalent flat transfer rate, when that reporting convention is useful, satisfies

$$
\bar f=
\frac{\sum_t d_t B^{\mathrm{FTP}}_tf^{\mathrm{FTP}}_t\tau_t}
{\sum_t d_t B^{\mathrm{FTP}}_t\tau_t},
$$

with declared reporting discount factors $d_t$. The weighting reflects cash-flow timing and balances; a one-year rate cannot automatically price every later exposure in a revolving facility.

## A4.5 Reproduce the KES 10 million contribution bridge

Assume the balance remains KES 10,000,000 for one year and every quoted component uses that same balance and annual basis. Treat the 9.4% funding component and 0.6% liquidity term component as non-overlapping allocations. Then

$$
\begin{aligned}
\operatorname{Contribution}
&=10{,}000{,}000
(0.130-0.094-0.006-0.003-0.012-0.008)\\
&=10{,}000{,}000(0.007)
=70{,}000\ \mathrm{KES}.
\end{aligned}
$$

The components are KES 1,300,000 customer interest, KES 940,000 funding, KES 60,000 liquidity allocation, KES 30,000 operating allocation, KES 120,000 expected credit cost and KES 80,000 capital-return allocation. Their residual is KES 70,000. The capital-return allocation is a management profitability charge; the expected credit cost is a pricing estimate. Mapping them to accounting expense requires the institution’s approved methodology.

To quantify the article’s repricing-lag example, add the following assumptions: twelve equal months, unchanged balance, funding cost immediately up 120 basis points for all twelve months, customer rate up 100 basis points only after the first month, and all other components unchanged. Incremental annual contribution is

$$
\Delta\operatorname{Contribution}
=10{,}000{,}000
\left(0.010\frac{11}{12}-0.012\right)
=-28{,}333.33\ \mathrm{KES}.
$$

The new contribution is KES 41,666.67. Of the reduction, KES 20,000 reflects the additional 20-basis-point annual mismatch and KES 8,333.33 the one-month customer repricing lag. An amortising or capped contract requires period-by-period recalculation.

For internal reconciliation, business-line contribution subtracts the FTP charge and Treasury receives the corresponding internal credit. Summing the two units eliminates the internal transfer; external funding expense remains in consolidated profit. Expected and realised credit costs are compared on consistent definitions rather than deducted together as if they were separate losses.

## A4.6 Deposit beta, migration and replication

Deposit beta is a rate sensitivity. In a simple sample regression,

$$
\Delta r^{\mathrm{dep}}_t
=\alpha+\beta\Delta r^{\mathrm{market}}_t+\varepsilon_t,
$$

where $\alpha$ is an intercept and $\varepsilon_t$ the residual. With an intercept, least-squares estimation gives

$$
\widehat\beta=
\frac{\sum_t(\Delta r^{\mathrm{market}}_t-\overline{\Delta r^{\mathrm{market}}})
(\Delta r^{\mathrm{dep}}_t-\overline{\Delta r^{\mathrm{dep}}})}
{\sum_t(\Delta r^{\mathrm{market}}_t-\overline{\Delta r^{\mathrm{market}}})^2}.
$$

This descriptive estimate needs uncertainty and regime checks. For the article’s KES 100 million deposits, initial rate 3%, and a one-percentage-point market increase, beta 0.35 implies a rate of 3.35% and annual interest expense KES 3.35 million at unchanged balances. Under beta 0.60, the rate becomes 3.60%. If 20% migrates out immediately, remaining expense is $80{,}000{,}000(0.036)=2{,}880{,}000$ KES, alongside a KES 20 million liquidity outflow. If the bank replaces that balance at annual rate $f$, total expense is $2{,}880{,}000+20{,}000{,}000f$ KES. For an explicitly added illustration $f=11\%$, it is KES 5.08 million.

A replication portfolio can approximate repricing cash flows through weights $w_j$ on approved tenors $j$. One transparent fitting objective is

$$
\min_{\boldsymbol w}\sum_{t\in\mathcal T}
\left(z_t-\sum_jw_jg_{jt}\right)^2,
\qquad w_j\ge0,\quad\sum_jw_j=1,
$$

where $z_t$ is the selected deposit-rate or cash-flow target and $g_{jt}$ the corresponding instrument response. The measurement target, balance perimeter and out-of-sample period must be fixed before fitting. This approximation describes behaviour; withdrawal remains available according to the deposit contract.

## A4.7 Liquidity ratios and the article’s 106.5% result

The illustrative ratio definitions follow [6], [7].

At a simplified level,

$$
\operatorname{LCR}=\frac{H}{O-\min(I,0.75O)},
$$

where $H$ is eligible HQLA after the applicable adjustments, $O$ weighted stressed outflows and $I$ eligible weighted inflows. The displayed 75% cap is the Basel standard convention, subject to applicable provisions; an institution applies its actual domestic requirements and classifications. Inputs must avoid double-counting pledged assets or the same cash movement.

Article 4 supplies net outflows directly: $H=120$ and $N=100$, in KES billions. After the stated changes, $H'=115$ and $N'=108$; therefore

$$
\operatorname{LCR}_0=\frac{120}{100}=1.20,
\qquad
\operatorname{LCR}_1=\frac{115}{108}=1.0648148\approx106.5\%.
$$

This assumes the KES 8 billion increase is already the net-outflow increment after all applicable classification and cap calculations. The KES 5 billion reduction is an independently identified loss of available eligible HQLA. A real hedge package must reconcile their overlap rather than applying both numbers mechanically.

The structural funding ratio is

$$
\operatorname{NSFR}
=\frac{\operatorname{ASF}}{\operatorname{RSF}},\qquad
\operatorname{ASF}=\sum_i a_iL_i,\qquad
\operatorname{RSF}=\sum_j b_jA_j+\operatorname{RSF}^{\mathrm{off}}.
$$

$L_i$ are eligible funding and capital amounts, $a_i$ their available-stable-funding factors, $A_j$ asset amounts, $b_j$ required-stable-funding factors, and $\operatorname{RSF}^{\mathrm{off}}$ the relevant off-balance-sheet requirement. The article provides no NSFR balance inventory or factor assignments, so it supports this calculation structure rather than a numerical NSFR. Numerical implementation requires institution-specific classification, residual maturities and the applicable rules.

## A4.8 Hedging, collateral and cash availability

The article’s hedge reduces the selected EVE loss from KES 2.0 billion to KES 1.2 billion: an improvement of KES 0.8 billion. Peak modelled collateral needs rise from KES 1 billion to KES 4 billion: an increase of KES 3 billion. The two differences have distinct horizons and meanings; their subtraction would not produce a well-defined net benefit.

For a simplified collateral agreement, let $V_t$ be the derivative mark-to-market value to the bank and $H_t$ a posting threshold. Required collateral posted by the bank can be represented schematically as

$$
C_t^{\mathrm{req}}=\max(-V_t-H_t,0)+IM_t,
\qquad
\Delta C_t=C_t^{\mathrm{req}}-C_{t-1}^{\mathrm{held}},
$$

where $IM_t$ is applicable initial margin and held collateral is adjusted for returns, haircuts and settlement. Minimum transfer amounts, netting, independent amounts and eligible collateral terms must be included when applicable. A signed positive $\Delta C_t$ is an additional posting in this simplified representation.

A cash ledger over period $t$ is

$$
K_{t+1}=K_t+\operatorname{receipts}_t
+\operatorname{funding}_t-\operatorname{payments}_t
-\operatorname{drawings}_t-\operatorname{collateral\ posted}_t
+\operatorname{collateral\ returned}_t.
$$

Every item uses actual availability dates. Peak collateral demand is $\max_t C_t^{\mathrm{req}}$, while liquidity stress may measure $\max_t\max(K_t^{\mathrm{minimum}}-K_t,0)$. These path measures expose a funding problem that can coexist with improved EVE sensitivity.

## A4.9 Finite-horizon stochastic control and Bellman recursion

The recursion follows the dynamic-programming framework in [12], connected to bank balance-sheet control in [9].

Represent the next state by $x_{t+1}=F_t(x_t,a_t,w_{t+1})$. Integrating over the conditional shock distribution defines the transition kernel

$$
K_t(dx'\mid x,a)
=\Pr\{F_t(x,a,w_{t+1})\in dx'\mid x,a\}.
$$

The article’s conditional notation involving both a state kernel and $w_{t+1}$ can be interpreted through this transition mechanism. A finite-horizon objective with terminal value $g$ is

$$
J(\pi)=\mathbb E_\pi\left[
\sum_{t=0}^{T}\gamma^tr_t(x_t,a_t,x_{t+1})
+\gamma^{T+1}g(x_{T+1})\right].
$$

Setting $g=0$ gives the displayed article objective. The policy $\pi$ selects an allowed action using information available at $t$, and $0<\gamma\le1$ discounts consistently with the period length. Rewards and terminal values require one declared unit and economic accounting convention.

Split the first reward from later rewards and condition on $x_{t+1}$:

$$
V_{T+1}(x)=g(x),
$$

$$
V_t(x)=\max_{a\in\mathcal A_t^{\mathrm{feas}}(x)}
\int\left[r_t(x,a,x')+\gamma V_{t+1}(x')\right]
K_t(dx'\mid x,a).
$$

This is the Bellman recursion under the Markov and measurability assumptions. The feasible set includes mandate, counterparty, currency, concentration and operational restrictions. It also includes the modelled LCR, NSFR, capital, EVE and cash-stress checks. For example, $\operatorname{LCR}\ge\ell_t$, $\operatorname{NSFR}\ge n_t$, $C_t^{\mathrm{capital}}\ge c_t$, $|\Delta\operatorname{EVE}|\le e_t$ and $\operatorname{CashStress}\le q_t$, with each threshold’s units declared. A ratio-based capital constraint uses a ratio threshold; an absolute-capital constraint uses KES.

If feasibility is tested across a scenario set $\Omega_t$, write $g_k(x,a,\omega)\le0$ for every required constraint $k$ and $\omega\in\Omega_t$. A statistical chance constraint, $\Pr(g_k>0)\le\epsilon_k$, is a separate modelled risk control and does not relax a binding legal limit. Finite scenario coverage establishes compliance within those scenarios; it does not prove compliance for every future state. An empty feasible set invokes the defined contingency and escalation process.

## A4.10 Partial observation, predictive cash and policy evaluation

The belief-state update follows [12].

For hidden economic state $z_t$, let $b_t(z)=\Pr(z_t=z\mid h_t)$ be the belief after observed history $h_t$. With hidden-state transition $K(z'\mid z,a)$ and observation likelihood $O(y\mid z',a)$,

$$
b_{t+1}(z')=
\frac{O(y_{t+1}\mid z',a_t)\sum_zK(z'\mid z,a_t)b_t(z)}
{\sum_{u}O(y_{t+1}\mid u,a_t)\sum_zK(u\mid z,a_t)b_t(z)}.
$$

Replace sums by integrals for continuous states. The denominator is the predictive probability of the observation. A belief-state Bellman equation uses expected reward $\bar r(b,a)$ and the update map $\mathcal B$:

$$
V_t(b)=\max_{a\in\mathcal A_t^{\mathrm{feas}}(b)}
\left\{\bar r_t(b,a)+\gamma\sum_y
\Pr(y\mid b,a)V_{t+1}(\mathcal B(b,a,y))\right\}.
$$

Behavioural parameters, deposit persistence and latent stress states require an identified observation process and validation. Cash forecasts supplied by borrower hierarchies preserve shared sector, region and vintage effects. For total portfolio cash $C=\sum_i C_i$,

$$
\operatorname{Var}(C)
=\sum_i\operatorname{Var}(C_i)
+2\sum_{i<j}\operatorname{Cov}(C_i,C_j).
$$

Scenario generation must retain those dependencies and any declared common shocks. Summing independently generated customer distributions would generally discard them.

For $M$ common simulated scenarios, a paired policy comparison is

$$
\widehat{\Delta J}=\frac1M\sum_{m=1}^{M}
\left(G_m^{\mathrm{candidate}}-G_m^{\mathrm{baseline}}\right),
$$

where $G_m$ is the discounted return. Its Monte Carlo standard error is the sample standard deviation of paired differences divided by $\sqrt M$ when scenarios are independent. This quantifies simulation sampling error, separately from parameter, simulator and policy-identification uncertainty. All comparisons also report constraint breaches, tail outcomes and implementation feasibility.

### Sources supporting this appendix

The financial context follows Article 4’s cited primary materials: the IRRBB standard [1], LCR and NSFR definitions [6], [7], revised customer-pricing framework [4], and bank Treasury control study [9]. Algebraic examples above are fully specified illustrations. Applicable Kenyan prudential requirements and institution-approved measurement conventions determine operational use.

### Further methodological reading

Additional sources retained from the article bibliography: [13].
