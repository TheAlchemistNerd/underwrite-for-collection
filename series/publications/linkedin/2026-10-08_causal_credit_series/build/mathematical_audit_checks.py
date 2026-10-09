"""Deterministic checks for the mathematical appendix examples; standard library only.
Recovered after a power interruption. This verifies identities and illustrative
arithmetic, not empirical model fit or causal identification.
"""
from pathlib import Path
import hashlib
import json
import math
import os
from statistics import NormalDist

ROOT = Path(__file__).resolve().parents[1]
checks = []

def check(name, actual, expected, atol=1e-9, rtol=1e-8):
    error = abs(actual - expected)
    passed = error <= atol + rtol * abs(expected)
    checks.append(dict(name=name, actual=actual, expected=expected,
                       absolute_error=error, absolute_tolerance=atol,
                       relative_tolerance=rtol, passed=passed))
    return passed

def simpson(f, lo, hi, n=8000):
    h = (hi-lo)/n
    return h/3*(f(lo)+f(hi)+4*sum(f(lo+h*j) for j in range(1,n,2))
                +2*sum(f(lo+h*j) for j in range(2,n,2)))

def loggamma_density(x, a, b):
    return a*math.log(b)-math.lgamma(a)+(a-1)*math.log(x)-b*x

def logig_density(x, a, b):
    return a*math.log(b)-math.lgamma(a)-(a+1)*math.log(x)-b/x

def normal_density(x, variance):
    return math.exp(-x*x/(2*variance))/math.sqrt(2*math.pi*variance)

def student_density(x, nu, scale):
    return math.exp(math.lgamma((nu+1)/2)-math.lgamma(nu/2)) / (
        math.sqrt(nu*math.pi)*scale)*(1+x*x/(nu*scale*scale))**(-(nu+1)/2)

nu, scale = 3., 1.7
for q in (0., .8, 4.):
    def normal_gamma_integrand(t):
        lam = math.exp(t)
        return normal_density(q, scale*scale/lam)*math.exp(loggamma_density(lam,nu/2,nu/2)+t)
    check('normal_Gamma_Student_t_marginal_q_'+str(q),
          simpson(normal_gamma_integrand,-35,12), student_density(q,nu,scale))
for sigma in (.2, 1., 4.):
    variance = sigma*sigma
    def auxiliary_integrand(t):
        aux = math.exp(t)
        return math.exp(logig_density(variance,nu/2,nu/aux)
                        +logig_density(aux,.5,1/(scale*scale))+t)*2*sigma
    check('inverse_Gamma_auxiliary_half_t_sigma_'+str(sigma),
          simpson(auxiliary_integrand,-20,35), 2*student_density(sigma,nu,scale))

# The log-density ratios remove normalising constants and check full conditionals.
uvec = [.1,-.4,.3]
aux, sig2a, sig2b = .8, .5, 1.3
j = len(uvec)
sumsq = sum(x*x for x in uvec)
def centred_variance_kernel(v):
    return logig_density(v,nu/2,nu/aux)-j/2*math.log(v)-sumsq/(2*v)
check('centred_variance_IG_full_conditional',
      centred_variance_kernel(sig2a)-centred_variance_kernel(sig2b),
      logig_density(sig2a,(nu+j)/2,nu/aux+sumsq/2)-logig_density(sig2b,(nu+j)/2,nu/aux+sumsq/2))
def auxiliary_kernel(a):
    return logig_density(sig2a,nu/2,nu/a)+logig_density(a,.5,1/scale**2)
check('auxiliary_IG_full_conditional', auxiliary_kernel(.4)-auxiliary_kernel(2.),
      logig_density(.4,(nu+1)/2,nu/sig2a+1/scale**2)-logig_density(2.,(nu+1)/2,nu/sig2a+1/scale**2))

# PG transform: E[exp(-omega*eta^2/2)] = cosh(eta/2)^(-b).
for b,y,eta in ((1,0,-2.),(1,1,1.3),(5,2,.4)):
    actual=2**(-b)*math.exp((y-b/2)*eta)/math.cosh(eta/2)**b
    expected=math.exp(y*eta)/(1+math.exp(eta))**b
    check('PG_likelihood_identity_'+str((b,y,eta)),actual,expected)

# Gaussian precision and offset: compare original and completed-square differences.
z=[(1.,-.4),(1.,.7),(1.,1.2)]
omega=[.2,.24,.16]
kappa=[-.5,.5,.5]
offset=[.1,-.2,.05]
q0=(.6,1.1); m0=(.1,-.2)
precision=[[sum(omega[i]*z[i][a]*z[i][b] for i in range(3))+(q0[a] if a==b else 0.) for b in range(2)] for a in range(2)]
rhs=[sum(z[i][a]*(kappa[i]-omega[i]*offset[i]) for i in range(3))+q0[a]*m0[a] for a in range(2)]
det=precision[0][0]*precision[1][1]-precision[0][1]*precision[1][0]
mean=[(precision[1][1]*rhs[0]-precision[0][1]*rhs[1])/det,
      (precision[0][0]*rhs[1]-precision[1][0]*rhs[0])/det]
def original_kernel(theta):
    eta=[sum(z[i][a]*theta[a] for a in range(2))+offset[i] for i in range(3)]
    return sum(kappa[i]*eta[i]-.5*omega[i]*eta[i]**2 for i in range(3))-.5*sum(q0[a]*(theta[a]-m0[a])**2 for a in range(2))
def square_kernel(theta):
    d=[theta[a]-mean[a] for a in range(2)]
    return -.5*sum(d[a]*precision[a][b]*d[b] for a in range(2) for b in range(2))
a=(.3,.1); b=(-.2,.8)
check('PG_Gaussian_block_with_offset',original_kernel(a)-original_kernel(b),square_kernel(a)-square_kernel(b))

# Non-centred sigma kernel holds z fixed, unlike centred IG full conditional.
v=[-.4,.7,1.2]
def direct_scale_kernel(s):
    eta=[offset[i]+s*v[i] for i in range(3)]
    return sum(kappa[i]*eta[i]-.5*omega[i]*eta[i]**2 for i in range(3))
def expanded_scale_kernel(s):
    return -.5*s*s*sum(v[i]**2*omega[i] for i in range(3))+s*sum(v[i]*(kappa[i]-omega[i]*offset[i]) for i in range(3))
check('noncentred_scale_kernel',direct_scale_kernel(.4)-direct_scale_kernel(1.2),expanded_scale_kernel(.4)-expanded_scale_kernel(1.2))

G,O,L=1200.,0.,18800.
threshold=(G+O)/(G+O+L)
check('fixed_payoff_risk_threshold',threshold,.06)
check('fixed_payoff_expected_value',.96*G-.04*L,400.)
check('indifference_at_threshold',(1-threshold)*G-threshold*L+(1-threshold)*O,0.)
check('cash_limit_headroom_existing',500000.-300000.,200000.)
check('cash_limit_headroom_revised',600000.-300000.,300000.)

def beta_survival(x,alpha=4,beta=96):
    n=alpha+beta-1
    return sum(math.comb(n,k)*x**k*(1-x)**(n-k) for k in range(alpha))
def beta_quantile(p):
    lo,hi=0.,1.
    for _ in range(90):
        mid=(lo+hi)/2
        if 1-beta_survival(mid)<p:lo=mid
        else:hi=mid
    return (lo+hi)/2
check('Beta_posterior_mean',4/100,.04)
check('Beta_posterior_variance',4*96/(100**2*101),.0003801980198019802)
check('Beta_95CI_lower',beta_quantile(.025),.0111167488,atol=1e-10)
check('Beta_95CI_upper',beta_quantile(.975),.0860112643,atol=1e-10)
check('Beta_cap_exceedance',beta_survival(.06),.1483731733,atol=1e-10)
normal=NormalDist()
z95=normal.inv_cdf(.95)
check('causal_average_contrast_90CI_lower',8000-4000*z95,1420.585492,atol=1e-5)
check('causal_average_contrast_90CI_upper',8000+4000*z95,14579.414508,atol=1e-5)
check('causal_average_contrast_probability_positive',normal.cdf(2),.9772498681,atol=1e-10)
values=[20000.,100000.,180000.]; weights=[.3,.5,.2]
mean_cash=sum(v*w for v,w in zip(values,weights))
second_cash=sum(v*v*w for v,w in zip(values,weights))
check('predictive_cash_mean',mean_cash,92000.)
check('predictive_cash_second_moment',second_cash,11600000000.)
check('predictive_cash_variance',second_cash-mean_cash**2,3136000000.)
check('predictive_cash_standard_deviation',math.sqrt(second_cash-mean_cash**2),56000.)
check('predictive_obligation_shortfall_probability',sum(w for v,w in zip(values,weights) if v<70000),.3)
check('predictive_obligation_shortfall_amount',sum(w*max(70000-v,0) for v,w in zip(values,weights)),15000.)

# Continuous-time hazard / competing-risk probability conservation example.
lambdas=[.025,.04]; horizon=12
survival=math.exp(-sum(lambdas)*horizon)
cifs=[lam/sum(lambdas)*(1-survival) for lam in lambdas]
check('competing_risk_probability_conservation',survival+sum(cifs),1.)
# Posterior prediction averages survival, preserving parameter uncertainty.
posterior_rates=[.01,.12]
mean_survival=sum(math.exp(-l*horizon) for l in posterior_rates)/2
plug_survival=math.exp(-sum(posterior_rates)/2*horizon)
checks.append(dict(name='posterior_survival_Jensen_inequality',actual=mean_survival,
                   plug_in_survival=plug_survival,passed=mean_survival>=plug_survival))

for name,actual,expected in [('pilot_day60_difference',46/50-38/50,.16),
                              ('pilot_day90_difference',41/50-34/50,.14),
                              ('illustrative_RAROC',850/5000,.17)]:
    check(name,actual,expected)

sources=[]
for num in (2,5):
    path=ROOT/'build'/'appendices'/f'ARTICLE_{num}_MATHEMATICAL_APPENDIX.md'
    data=path.read_bytes()
    if b'\0' in data:
        raise ValueError('NUL byte in source '+str(path))
    sources.append(dict(path=str(path.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))

report=dict(status='passed' if all(c['passed'] for c in checks) else 'failed',
            check_count=len(checks),passed_count=sum(c['passed'] for c in checks),
            scope='Deterministic mathematical identities and synthetic numerical examples in appendices 2 and 5; not empirical fitting, causal identification, legal approval or a production model audit.',
            sources=sources,checks=checks,
            manual_review=dict(hierarchy='Logistic and hazard models use distinct coefficient sets, shared sector/region/vintage hierarchy pattern, half-t SD priors and a declared hazard baseline.',
                               scale_updates='Centred inverse-Gamma and non-centred scale kernels are separately stated; no Gaussian full conditional is claimed for the half-t SD from the normal-Gamma identity alone.',
                               causal_uncertainty='Average-effect and policy-value posterior contrasts are distinguished from unidentifiable individual cross-potential-outcome covariance.',
                               limits='Fixed payoff threshold and posterior exceedance gate are separated; actual limit changes use incremental action values with joint uncertainty.'))
output=ROOT/'build'/'mathematical_audit.json'
temp=output.with_suffix('.json.tmp')
with temp.open('w',encoding='utf-8',newline='\n') as handle:
    json.dump(report,handle,ensure_ascii=False,indent=2)
    handle.write('\n')
    handle.flush()
    os.fsync(handle.fileno())
os.replace(temp,output)
print(json.dumps(dict(status=report['status'],checks=len(checks),passed=report['passed_count'],path=str(output))))
if report['status']!='passed':
    print(json.dumps([c for c in checks if not c['passed']],indent=2))
    raise SystemExit(1)
