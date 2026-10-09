"""Prepare TeX mathematics for the PDF, preserving the Unicode article sources."""
from pathlib import Path
import hashlib
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Explicit transcriptions preserve the notation and mathematical meaning.
FORMULAS = {
    'R = cash received − funding cost − servicing cost − realized loss': r'\begin{aligned}R={}&\text{cash received}-\text{funding cost}\\&-\text{servicing cost}-\text{realized loss}\end{aligned}',
    'V(a,x)=E[∑ₜ₌₁ᵀ dₜ(CFₜ(a)−OPEXₜ(a)) − L(a) | X=x]': r'V(a,x)=\mathbb{E}\!\left[\sum_{t=1}^{T}d_t\bigl(\mathrm{CF}_t(a)-\mathrm{OPEX}_t(a)\bigr)-L(a)\,\middle|\,X=x\right]',
    'μ(x,a)=E[R|X=x,A=a]': r'\mu(x,a)=\mathbb{E}[R\mid X=x,A=a]',
    'πₜ(a|x)=(1−εₜ)π̂ₜ(a|x)+εₜq(a|x)': r'\pi_t(a\mid x)=(1-\varepsilon_t)\widehat{\pi}_t(a\mid x)+\varepsilon_t q(a\mid x)',
    'μ(x,a)=xᵀθₐ': r'\mu(x,a)=x^{\mathsf T}\theta_a',
    'λ(t|x,a)=λ₀(t)exp(xᵀβ+g(a,x))': r'\lambda(t\mid x,a)=\lambda_0(t)\exp\!\bigl(x^{\mathsf T}\beta+g(a,x)\bigr)',
    'S(t|x,a)=exp(−∫₀ᵗλ(u|x,a)du)': r'S(t\mid x,a)=\exp\!\left(-\int_0^t\lambda(u\mid x,a)\,\mathrm{d}u\right)',
    'Fᴰ(τ | x,a) = Pr(T ≤ τ, J = D | X = x, A = a)': r'F^D(\tau\mid x,a)=\Pr(T\le\tau,J=D\mid X=x,A=a)',
    'λₖ(t | x,a) = lim₍Δt→0₎ Pr(t ≤ T < t+Δt, J = k | T ≥ t, X = x, A = a) / Δt': r'\begin{aligned}\lambda_k(t\mid x,a)={}&\lim_{\Delta t\to0}\frac{1}{\Delta t}\\&\quad\times\Pr\!\bigl(t\le T<t+\Delta t,J=k\mid T\ge t,X=x,A=a\bigr)\end{aligned}',
    'V̂_IPS(π)=n⁻¹∑ᵢ [π(Aᵢ|Xᵢ)/π₀(Aᵢ|Xᵢ)]Rᵢ': r'\widehat{V}_{\mathrm{IPS}}(\pi)=\frac{1}{n}\sum_i\frac{\pi(A_i\mid X_i)}{\pi_0(A_i\mid X_i)}R_i',
    'V̂_DR(π)=n⁻¹∑ᵢ[∑ₐπ(a|Xᵢ)m(Xᵢ,a)+π(Aᵢ|Xᵢ)/π₀(Aᵢ|Xᵢ)(Rᵢ−m(Xᵢ,Aᵢ))]': r'\begin{aligned}\widehat{V}_{\mathrm{DR}}(\pi)=\frac{1}{n}\sum_i\Biggl[&\sum_a\pi(a\mid X_i)m(X_i,a)\\&+\frac{\pi(A_i\mid X_i)}{\pi_0(A_i\mid X_i)}\bigl(R_i-m(X_i,A_i)\bigr)\Biggr]\end{aligned}',
    '58/72 = 80.6%': r'\frac{58}{72}=80.6\%',
    '64/75 = 85.3%': r'\frac{64}{75}=85.3\%',
    'Vₜ(s) = maxₐ∈A(s) E[rₜ(s,a,Sₜ₊₁) + γVₜ₊₁(Sₜ₊₁)]': r'V_t(s)=\max_{a\in A(s)}\mathbb{E}\!\left[r_t(s,a,S_{t+1})+\gamma V_{t+1}(S_{t+1})\right]',
    'bₜ(z)=Pr(zₜ=z | o₁:ₜ,a₁:ₜ₋₁)': r'b_t(z)=\Pr(z_t=z\mid o_{1:t},a_{1:t-1})',
    'λᵢ(t)=λ₀(t)exp(xᵢᵀβ+u_group)': r'\lambda_i(t)=\lambda_0(t)\exp\!\bigl(x_i^{\mathsf T}\beta+u_{\mathrm{group}}\bigr)',
    'logit(pᵢ)=α+xᵢᵀβ+u_group': r'\operatorname{logit}(p_i)=\alpha+x_i^{\mathsf T}\beta+u_{\mathrm{group}}',
    'Dᵢ(τ) ∼ Bernoulli(pᵢ,τ)': r'D_i(\tau)\sim\operatorname{Bernoulli}(p_{i,\tau})',
    'logit(pᵢ,τ)=α+Xᵢᵀβ+u_sector[i]+v_region[i]+w_vintage[i]': r'\begin{aligned}\operatorname{logit}(p_{i,\tau})={}&\alpha+X_i^{\mathsf T}\beta\\&+u_{\mathrm{sector}[i]}+v_{\mathrm{region}[i]}+w_{\mathrm{vintage}[i]}\end{aligned}',
    'λᵢ(t|Xᵢ)=λ₀(t)exp(Xᵢᵀβ+u_group[i])': r'\lambda_i(t\mid X_i)=\lambda_0(t)\exp\!\bigl(X_i^{\mathsf T}\beta+u_{\mathrm{group}[i]}\bigr)',
    'Sᵢ(t)=exp(−∫₀ᵗλᵢ(u)du)': r'S_i(t)=\exp\!\left(-\int_0^t\lambda_i(u)\,\mathrm{d}u\right)',
    'maxπ Eπ[∑ₜγᵗrₜ]': r'\max_{\pi}\mathbb{E}_{\pi}\!\left[\sum_t\gamma^t r_t\right]',
    'Eπ[∑ₜcₖ,ₜ] ≤ Bₖ': r'\mathbb{E}_{\pi}\!\left[\sum_t c_{k,t}\right]\le B_k',
    'EL ≈ PD×LGD×EAD': r'\mathrm{EL}\approx\mathrm{PD}\times\mathrm{LGD}\times\mathrm{EAD}',
    'EL≈PD×LGD×EAD': r'\mathrm{EL}\approx\mathrm{PD}\times\mathrm{LGD}\times\mathrm{EAD}',
    'ECₐ = VaRₐ(L) − E[L]': r'\mathrm{EC}_a=\operatorname{VaR}_a(L)-\mathbb{E}[L]',
    'ESₐ(L) − E[L]': r'\operatorname{ES}_a(L)-\mathbb{E}[L]',
    'RAROC = (risk-adjusted income − expected loss − funding cost − operating cost − tax adjustments) / economic capital': r'\mathrm{RAROC}=\frac{\begin{gathered}\text{risk-adjusted income}-\text{expected loss}-\text{funding cost}\\-\text{operating cost}-\text{tax adjustments}\end{gathered}}{\text{economic capital}}',
    'KES 850/KES 5,000 = 17%': r'\frac{\text{KES }850}{\text{KES }5{,}000}=17\%',
    'θ>0': r'\theta>0',
    'λ_L=2^(−1/θ)': r'\lambda_L=2^{-1/\theta}',
    'τ=θ/(θ+2)': r'\tau=\frac{\theta}{\theta+2}',
    'yᵢ∈{0,1}': r'y_i\in\{0,1\}',
    'ηᵢ=xᵢᵀβ': r'\eta_i=x_i^{\mathsf T}\beta',
    'κᵢ=yᵢ−1/2': r'\kappa_i=y_i-\frac{1}{2}',
    'ωᵢ∼PG(1,ηᵢ)': r'\omega_i\sim\operatorname{PG}(1,\eta_i)',
    'Σ⁎=(XᵀΩX+Σ₀⁻¹)⁻¹': r'\Sigma^{\ast}=\left(X^{\mathsf T}\Omega X+\Sigma_0^{-1}\right)^{-1}',
    'xₜ = φ(Gₜ)': r'x_t=\varphi(G_t)',
    'UCBₜ(x,a) = xₜ(a)ᵀ θ̂ₜ + α √(xₜ(a)ᵀ Aₜ⁻¹ xₜ(a))': r'\operatorname{UCB}_t(x,a)=x_t(a)^{\mathsf T}\widehat{\theta}_t+\alpha\sqrt{x_t(a)^{\mathsf T}A_t^{-1}x_t(a)}',
    'θ̃ₜ ∼ p(θ | Dₜ);   p̃ₜ(a) = σ(xₜ(a)ᵀ θ̃ₜ)': r'\widetilde{\theta}_t\sim p(\theta\mid D_t),\qquad\widetilde{p}_t(a)=\sigma\!\bigl(x_t(a)^{\mathsf T}\widetilde{\theta}_t\bigr)',
    'aₜ = arg max₍a ∈ A_safe₎ Q̃ₜ(a)': r'a_t=\operatorname*{arg\,max}_{a\in A_{\mathrm{safe}}}\widetilde{Q}_t(a)',
    'U_MCTS(s,a) = Q(s,a) + c √(ln N(s) / N(s,a))': r'U_{\mathrm{MCTS}}(s,a)=Q(s,a)+c\sqrt{\frac{\ln N(s)}{N(s,a)}}',
    'Q_H(s,a) = E[Σₖ₌₀ᴴ γᵏ rₜ₊ₖ | sₜ=s, aₜ=a, model]': r'Q_H(s,a)=\mathbb{E}\!\left[\sum_{k=0}^{H}\gamma^k r_{t+k}\,\middle|\,s_t=s,a_t=a,\text{model}\right]',
    'KES 1,100 − KES 250 = KES 850 per assigned case': r'\text{KES }1{,}100-\text{KES }250=\text{KES }850\quad\text{per assigned case}',
    'Sᵢ=1': r'S_i=1',
    'Dᵢᵃ(τ)=1': r'D_i^a(\tau)=1',
    'pᵢ,τ(a)=Pr(Dᵢᵃ(τ)=1 | Xᵢ)': r'p_{i,\tau}(a)=\Pr(D_i^a(\tau)=1\mid X_i)',
    'Tᵢᵃ=1': r'T_i^a=1',
    'Dᵢᵃ(τ) ∼ Bernoulli(pᵢ,τ(a))': r'D_i^a(\tau)\sim\operatorname{Bernoulli}\!\bigl(p_{i,\tau}(a)\bigr)',
    'logit(pᵢ,τ(a)) = α + u_sector[i] + v_region[i] + w_vintage[i] + f(Xᵢ) + h(a,Xᵢ)': r'\begin{aligned}\operatorname{logit}\!\bigl(p_{i,\tau}(a)\bigr)={}&\alpha+u_{\mathrm{sector}[i]}+v_{\mathrm{region}[i]}\\&+w_{\mathrm{vintage}[i]}+f(X_i)+h(a,X_i)\end{aligned}',
    'λᵢ(t|Xᵢ,a)=λ₀(t)exp(Xᵢᵀβ + q(a,Xᵢ)+u_group[i])': r'\lambda_i(t\mid X_i,a)=\lambda_0(t)\exp\!\bigl(X_i^{\mathsf T}\beta+q(a,X_i)+u_{\mathrm{group}[i]}\bigr)',
    'e(x)=Pr(S=1|X=x)': r'e(x)=\Pr(S=1\mid X=x)',
    '0<e(x)<1': r'0<e(x)<1',
    'Dᵃ(τ) ⫫ S | X': r'D^a(\tau)\mathrel{\perp\!\!\!\perp}S\mid X',
    'e(x)=0': r'e(x)=0',
    'logit Pr(Dᵃ=1|X,S=0) = logit Pr(Dᵃ=1|X,S=1)+δ_g': r'\begin{aligned}\operatorname{logit}\Pr(D^a=1\mid X,S=0)={}&\operatorname{logit}\Pr(D^a=1\mid X,S=1)\\&+\delta_g\end{aligned}',
    'Bernoulli(pᵢ)': r'\operatorname{Bernoulli}(p_i)',
    '4/80=5%': r'\frac{4}{80}=5\%',
    'xₜ₊₁ ~ P(· | xₜ, aₜ, wₜ₊₁)': r'x_{t+1}\sim P(\,\cdot\mid x_t,a_t,w_{t+1})',
    'ΔEVE = EVE(shocked curves, behavioural cash flows) − EVE(base curves, behavioural cash flows)': r'\begin{aligned}\Delta\mathrm{EVE}={}&\mathrm{EVE}(\text{shocked curves, behavioural cash flows})\\&-\mathrm{EVE}(\text{base curves, behavioural cash flows})\end{aligned}',
    'ΔEVE ≈ −Dₑff × EVE₀ × Δr': r'\Delta\mathrm{EVE}\approx-D_{\mathrm{eff}}\times\mathrm{EVE}_0\times\Delta r',
    'NIIₛ(H) = Σₜ₌₁ᴴ [interest incomeₜ,s − interest expenseₜ,s] + relevant fee and hedge effects': r'\begin{aligned}\mathrm{NII}_s(H)={}&\sum_{t=1}^{H}\bigl[\text{interest income}_{t,s}-\text{interest expense}_{t,s}\bigr]\\&+\text{relevant fee and hedge effects}\end{aligned}',
    '13.0% − 9.4% − 0.6% − 0.3% − 1.2% − 0.8% = 0.7%': r'13.0\%-9.4\%-0.6\%-0.3\%-1.2\%-0.8\%=0.7\%',
    '(120 − 5) / (100 + 8) = 106.5%': r'\frac{120-5}{100+8}=106.5\%',
    'J(π) = Eπ[Σₜ₌₀ᵀ γᵗ r(xₜ, aₜ, xₜ₊₁)]': r'J(\pi)=\mathbb{E}_{\pi}\!\left[\sum_{t=0}^{T}\gamma^t r(x_t,a_t,x_{t+1})\right]',
    'aₜ ∈ A(xₜ), LCRₜ ≥ ℓₜ, NSFRₜ ≥ nₜ, capitalₜ ≥ cₜ, |ΔEVEₜ| ≤ eₜ, liquidity stressₜ ≤ qₜ': r'\begin{aligned}a_t&\in A(x_t),&\mathrm{LCR}_t&\ge\ell_t,\\\mathrm{NSFR}_t&\ge n_t,&\text{capital}_t&\ge c_t,\\|\Delta\mathrm{EVE}_t|&\le e_t,&\text{liquidity stress}_t&\le q_t\end{aligned}',
}

SYMBOLS = {
    'Aₜ':r'A_t','CFₜ':r'\mathrm{CF}_t','C_A':r'C_A','C_B':r'C_B','Dᵢᵃ(τ)':r'D_i^a(\tau)',
    'OPEXₜ':r'\mathrm{OPEX}_t','Rₜ':r'R_t','Xₜ':r'X_t','dₜ':r'd_t','m(x,a)':r'm(x,a)',
    'εₜ':r'\varepsilon_t','π':r'\pi','π(a|x)':r'\pi(a\mid x)','π̂ₜ':r'\widehat{\pi}_t',
    'π₀':r'\pi_0','πₜ(a|x)':r'\pi_t(a\mid x)','τ':r'\tau','A(sₜ)':r'A(s_t)',
    'Gₜ':r'G_t','P(sₜ₊₁ | sₜ,aₜ)':r'P(s_{t+1}\mid s_t,a_t)','Xᵀκ':r'X^{\mathsf T}\kappa',
    'aₜ':r'a_t','oₜ':r'o_t','rₜ':r'r_t','sₜ':r's_t','xₜ':r'x_t','zₜ':r'z_t','β':r'\beta',
    'φ':r'\varphi','ω':r'\omega','Xᵢ':r'X_i','e(x)':r'e(x)','yᵢ':r'y_i','δ_g':r'\delta_g',
    'wₜ₊₁':r'w_{t+1}','A(xₜ)':r'A(x_t)','γ':r'\gamma','ℓₜ':r'\ell_t','nₜ':r'n_t',
    'cₜ':r'c_t','eₜ':r'e_t','qₜ':r'q_t','bₜ':r'b_t',
}
SYMBOLS.update({x:x for x in ['A','B','J','L','T','N','Q','X','a','c','f','h','k','q','s','t','x']})


FORMULAS.update({
    'uⱼ = σzⱼ;   zⱼ ∼ Normal(0,1)': r'u_j=\sigma z_j,\qquad z_j\sim\mathcal{N}(0,1)',
    'σ ∼ Half-Student-t(ν=3, scale=s₀)': r'\sigma\sim\operatorname{Half\!\text{-}\!Student\!\text{-}t}(\nu=3,\mathrm{scale}=s_0)',
    'λ ∼ Gamma(shape=3/2, rate=3/2)': r'\lambda\sim\operatorname{Gamma}(\mathrm{shape}=3/2,\mathrm{rate}=3/2)',
    'q | λ ∼ Normal(0, s₀²/λ);   σ = |q|': r'q\mid\lambda\sim\mathcal{N}(0,s_0^2/\lambda),\qquad\sigma=|q|',
    'p̄ = E[p | D]': r'\bar p=\mathbb{E}[p\mid D]',
    'E[V(extend) | D] = (1−p̄)G − p̄L': r'\mathbb{E}[V(\mathrm{extend})\mid D]=(1-\bar p)G-\bar pL',
    'E[V(decline) | D] = −(1−p̄)O': r'\mathbb{E}[V(\mathrm{decline})\mid D]=-(1-\bar p)O',
    'p* = (G+O)/(G+O+L)': r'p^{\ast}=\frac{G+O}{G+O+L}',
    'p* = 1,200/(1,200+18,800) = 6%': r'p^{\ast}=\frac{1{,}200}{1{,}200+18{,}800}=6\%',
    'E[V(extend) | D] = 0.96×1,200 − 0.04×18,800 = KES 400': r'\mathbb{E}[V(\mathrm{extend})\mid D]=0.96\times1{,}200-0.04\times18{,}800=\text{KES }400',
    'Pr(p > p_cap | D) > ε   ⇒   apply the approved uncertainty-review route': r'\begin{gathered}\Pr(p>p_{\mathrm{cap}}\mid D)>\varepsilon\\\Longrightarrow\text{apply the approved uncertainty-review route}\end{gathered}',
    'qₚ = Pr(p₁₂(a) > p_max | D)': r'q_p=\Pr(p_{12}(a)>p_{\max}\mid D)',
    'q_Δ = Pr(Δ(a, a₀) > δ | D, identification assumptions)': r'q_{\Delta}=\Pr\!\bigl(\Delta(a,a_0)>\delta\mid D,\text{identification assumptions}\bigr)',
    'q_C = Pr(C₃₀(a) < B₃₀ | D, a)': r'q_C=\Pr(C_{30}(a)<B_{30}\mid D,a)',
})
SYMBOLS.update({'uⱼ':r'u_j','σ':r'\sigma','zⱼ':r'z_j','s₀':r's_0','λ':r'\lambda','ν':r'\nu','p̄':r'\bar p','ε':r'\varepsilon','δ':r'\delta','qₚ':r'q_p','p₁₂(a)':r'p_{12}(a)','a₀':r'a_0','C₃₀(a)':r'C_{30}(a)','B₃₀':r'B_{30}','Δ(a, a₀)':r'\Delta(a,a_0)','Dₑff':r'D_{\mathrm{eff}}','Δr':r'\Delta r'})

FORMULAS.update({
    'R = cash received − initial advance − funding cost − servicing cost': r'\begin{aligned}R={}&\text{cash received}-\text{initial advance}\\&-\text{funding cost}-\text{servicing cost}\end{aligned}',
    'V(a,x)=E[−P₀(a)+∑ₜ₌₁ᵀ dₜ(Qₜ(a)−OPEXₜ(a)) | X=x]': r'V(a,x)=\mathbb E\!\left[-P_0(a)+\sum_{t=1}^{T}d_t\{Q_t(a)-\operatorname{OPEX}_t(a)\}\,\middle|\,X=x\right]',
    'λᵢ(t|Xᵢ,a)=λ₀(t)exp(Xᵢᵀβᴴ+gᴴ(a,Xᵢ)+uᴴ_sector[i]+vᴴ_region[i]+wᴴ_vintage[i])': r'\begin{aligned}\lambda_i(t\mid X_i,a)=\lambda_0(t)\exp\bigl(&X_i^{\mathsf T}\beta^H+g^H(a,X_i)\\&+u^H_{s(i)}+v^H_{r(i)}+w^H_{c(i)}\bigr)\end{aligned}',
    'Sᵢ(t|Xᵢ,a)=exp(−∫₀ᵗλᵢ(u|Xᵢ,a)du)': r'S_i(t\mid X_i,a)=\exp\!\left[-\int_0^t\lambda_i(u\mid X_i,a)\,du\right]',
    'λᵢ(t)=λ₀(t)exp(xᵢᵀβᴴ+uᴴ_sector[i]+vᴴ_region[i]+wᴴ_vintage[i])': r'\lambda_i(t)=\lambda_0(t)\exp\!\bigl(x_i^{\mathsf T}\beta^H+u^H_{s(i)}+v^H_{r(i)}+w^H_{c(i)}\bigr)',
    'logit(pᵢ,τ)=αᴸ+xᵢᵀβᴸ+uᴸ_sector[i]+vᴸ_region[i]+wᴸ_vintage[i]': r'\begin{aligned}\operatorname{logit}(p_{i,\tau})={}&\alpha^L+x_i^{\mathsf T}\beta^L\\&+u^L_{s(i)}+v^L_{r(i)}+w^L_{c(i)}\end{aligned}',
    'logit(pᵢ,τ)=αᴸ+Xᵢᵀβᴸ+uᴸ_sector[i]+vᴸ_region[i]+wᴸ_vintage[i]': r'\begin{aligned}\operatorname{logit}(p_{i,\tau})={}&\alpha^L+X_i^{\mathsf T}\beta^L\\&+u^L_{s(i)}+v^L_{r(i)}+w^L_{c(i)}\end{aligned}',
    'λᵢ(t|Xᵢ)=λ₀(t)exp(Xᵢᵀβᴴ+uᴴ_sector[i]+vᴴ_region[i]+wᴴ_vintage[i])': r'\lambda_i(t\mid X_i)=\lambda_0(t)\exp\!\bigl(X_i^{\mathsf T}\beta^H+u^H_{s(i)}+v^H_{r(i)}+w^H_{c(i)}\bigr)',
    'uᵐ_s = σᵐ_u zᵐ_us;   zᵐ_us ∼ Normal(0,1)': r'u_s^m=\sigma_u^m z_{us}^m,\qquad z_{us}^m\sim N(0,1)',
    'vᵐ_r = σᵐ_v zᵐ_vr;   zᵐ_vr ∼ Normal(0,1)': r'v_r^m=\sigma_v^m z_{vr}^m,\qquad z_{vr}^m\sim N(0,1)',
    'wᵐ_c = σᵐ_w zᵐ_wc;   zᵐ_wc ∼ Normal(0,1)': r'w_c^m=\sigma_w^m z_{wc}^m,\qquad z_{wc}^m\sim N(0,1)',
    'σᵐ_k ∼ Half-Student-t(ν=3, scale=s₀,kᵐ),   k ∈ {u,v,w}, m ∈ {L,H}': r'\begin{gathered}\sigma_k^m\sim\operatorname{HalfStudentT}(3,s_{0,k}^m),\\ k\in\{u,v,w\},\quad m\in\{L,H\}\end{gathered}',
    'αᴸ ∼ Normal(0,sα²);   βᵐ ∼ MVNormal(0,Bᵐ)': r'\alpha^L\sim N(0,s_\alpha^2),\qquad\beta^m\sim N(0,B^m)',
    'λ₀,ℓ ∼ Gamma(shape=aℓ, rate=bℓ)': r'\lambda_{0,\ell}\sim\operatorname{Gamma}(\mathrm{shape}=a_\ell,\mathrm{rate}=b_\ell)',
    'logit(pᵢ,τ(a)) = αᴸ + uᴸ_sector[i] + vᴸ_region[i] + wᴸ_vintage[i] + fᴸ(Xᵢ) + hᴸ(a,Xᵢ)': r'\begin{aligned}\operatorname{logit}(p_{i,\tau}(a))={}&\alpha^L+u^L_{s(i)}+v^L_{r(i)}+w^L_{c(i)}\\&+f^L(X_i)+h^L(a,X_i)\end{aligned}',
    'λᵢ(t|Xᵢ,a)=λ₀(t)exp(Xᵢᵀβᴴ+qᴴ(a,Xᵢ)+uᴴ_sector[i]+vᴴ_region[i]+wᴴ_vintage[i])': r'\begin{aligned}\lambda_i(t\mid X_i,a)=\lambda_0(t)\exp\bigl(&X_i^{\mathsf T}\beta^H+q^H(a,X_i)\\&+u^H_{s(i)}+v^H_{r(i)}+w^H_{c(i)}\bigr)\end{aligned}',
})
SYMBOLS.update({'P₀':r'P_0','Qₜ':r'Q_t','αᴸ':r'\alpha^L','βᴸ':r'\beta^L','βᴴ':r'\beta^H','βᵐ':r'\beta^m','σᵐ_k':r'\sigma_k^m','s₀,kᵐ':r's_{0,k}^m'})

def main():
    source=Path(sys.argv[1]).resolve()
    destination=source.with_name(source.stem+'_TYPESET.md')
    text=source.read_text(encoding='utf-8')
    original_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in source.parent.parent.glob('ARTICLE_*.md')}
    used={}
    in_code=False
    in_display=False
    lines=[]
    def count(key): used[key]=used.get(key,0)+1
    for line in text.splitlines():
        if line.strip() == '$$':
            in_display=not in_display
            lines.append(line)
            continue
        if in_display:
            lines.append(line)
            continue
        if line.lstrip().startswith('```'):
            in_code=not in_code
            lines.append(line)
            continue
        if in_code:
            lines.append(line)
            continue
        stripped=line.strip()
        # Standalone formulas become displayed mathematics with their punctuation.
        found=False
        for key,value in sorted(FORMULAS.items(),key=lambda kv:len(kv[0]),reverse=True):
            for token in (f'**{key}**',key):
                if stripped.startswith(token):
                    tail=stripped[len(token):]
                    if not tail or tail in (',','.',';') or tail.startswith(', and applicable'):
                        punctuation=tail if tail in (',','.',';') else ''
                        lines.extend(['','$$',value+punctuation,'$$',''])
                        if tail.startswith(', and applicable'): lines.append(tail[2:])
                        count(key); found=True; break
            if found: break
        if found: continue
        # Convert marked inline variables and equations, retaining surrounding prose.
        def bold(match):
            key=match[1]
            value=FORMULAS.get(key,SYMBOLS.get(key))
            if value is None: return match[0]
            count(key)
            return '$'+value+'$'
        line=re.sub(r'\*\*(.+?)\*\*',bold,line)
        # Article 4 has unmarked mathematical notation in its prose.
        fragments=re.split(r'(\$[^$]*\$)',line)
        for i,fragment in enumerate(fragments):
            if fragment.startswith('$'): continue
            pending={}
            for key,value in sorted({**SYMBOLS,**FORMULAS}.items(),key=lambda kv:len(kv[0]),reverse=True):
                if not any(ord(c)>127 for c in key): continue
                pattern=re.escape(key)
                def substitute(match):
                    token=f'@@MATH{len(pending)}@@'
                    pending[token]='$'+value+'$'
                    count(key)
                    return token
                fragment=re.sub(pattern,substitute,fragment)
            for token,value in pending.items(): fragment=fragment.replace(token,value)
            fragments[i]=fragment
        line=''.join(fragments)
        # Let Pandoc's URL handling wrap long DOI identifiers in references.
        line=re.sub(r'doi:\s*(10\.[0-9]{4,9}/[A-Za-z0-9./_-]+)',
                    lambda m: 'doi: <https://doi.org/'+m.group(1).rstrip('.')+'>'+('.' if m.group(1).endswith('.') else ''),
                    line)
        lines.append(line)
    result='\n'.join(lines)+'\n'
    destination.write_text(result,encoding='utf-8')
    for name,digest in original_hashes.items():
        assert hashlib.sha256((source.parent.parent/name).read_bytes()).hexdigest()==digest
    report={'display_equations':result.count('$$')//2,'math_transcriptions':sum(used.values()),'used':used,'unchanged_article_hashes':original_hashes}
    (source.parent/'math_typesetting_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{report["display_equations"]} display equations; {report["math_transcriptions"]} mathematical expressions; source article hashes unchanged')

if __name__=='__main__': main()
