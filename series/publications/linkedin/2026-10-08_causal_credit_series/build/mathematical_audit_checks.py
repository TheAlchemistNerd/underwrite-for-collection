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

# Finite-action Boltzmann checks with fixed illustrative action values.
def probability_vector(p):
    p = tuple(p)
    if (not p or any(not math.isfinite(x) or not 0 <= x <= 1 for x in p)
            or not math.isclose(math.fsum(p), 1., rel_tol=0., abs_tol=1e-12)):
        raise ValueError('A finite nonnegative probability vector summing to one is required')
    return p


def admissible_mask(mask, size):
    mask = tuple(True for _ in range(size)) if mask is None else tuple(mask)
    if len(mask) != size or any(not isinstance(ok, bool) for ok in mask) or not any(mask):
        raise ValueError('At least one admissible action and a matching boolean mask are required')
    return mask


def stable_boltzmann(q, temperature, mask=None):
    q = tuple(q)
    if not q or any(not math.isfinite(x) for x in q):
        raise ValueError('Action values must be a nonempty finite sequence')
    if not math.isfinite(temperature) or temperature <= 0:
        raise ValueError('Temperature must be finite and positive')
    mask = admissible_mask(mask, len(q))
    peak = max(x for x, ok in zip(q, mask) if ok)
    weights = tuple(math.exp((x - peak) / temperature) if ok else 0.
                    for x, ok in zip(q, mask))
    total = math.fsum(weights)
    return tuple(w / total for w in weights)


def masked_uniform_mix(p, epsilon, mask=None):
    p = probability_vector(p)
    mask = admissible_mask(mask, len(p))
    if not math.isfinite(epsilon) or not 0 <= epsilon <= 1:
        raise ValueError('Epsilon must be finite and lie between zero and one')
    if any(x != 0 for x, ok in zip(p, mask) if not ok):
        raise ValueError('Input policy must already respect the mask')
    k = sum(mask)
    return tuple((1 - epsilon) * x + epsilon / k if ok else 0.
                 for x, ok in zip(p, mask))


def entropy_nats(p):
    p = probability_vector(p)
    return -math.fsum(x * math.log(x) for x in p if x > 0)


def entropy_objective(p, q, temperature):
    p, q = probability_vector(p), tuple(q)
    if (len(p) != len(q) or any(not math.isfinite(x) for x in q)
            or not math.isfinite(temperature) or temperature <= 0):
        raise ValueError('Matching finite action values and positive finite temperature are required')
    return (math.fsum(x * y for x, y in zip(p, q))
            + temperature * entropy_nats(p))


def vector_check(name, actual, expected, atol=1e-14):
    actual, expected = tuple(actual), tuple(expected)
    if len(actual) != len(expected):
        check(name + '_length', len(actual), len(expected), atol=0., rtol=0.)
        return
    for i, (a, e) in enumerate(zip(actual, expected)):
        check(name + '_' + str(i), a, e, atol=atol, rtol=1e-12)


def expect_value_error(name, fn):
    try:
        fn()
    except ValueError:
        check(name, 1., 1.)
    else:
        check(name, 0., 1.)


BQ = (5000., 4000., 2000.)
BT = 1000.
BP = stable_boltzmann(BQ, BT)
vector_check('Boltzmann_known_probabilities', BP,
             (.7053845126982412, .25949646034241913, .03511902695933973))
check('Boltzmann_probability_mass', math.fsum(BP), 1., atol=1e-14, rtol=0.)
vector_check('Boltzmann_large_translation',
             stable_boltzmann(tuple(x + 1e6 for x in BQ), BT), BP)
vector_check('Boltzmann_joint_positive_scaling',
             stable_boltzmann(tuple(7 * x for x in BQ), 7 * BT), BP)
vector_check('Boltzmann_low_temperature', stable_boltzmann(BQ, 1.), (1., 0., 0.))
vector_check('Boltzmann_high_temperature',
             stable_boltzmann(BQ, 1e12), (1 / 3,) * 3, atol=6e-10)
vector_check('Boltzmann_tied_max_low_temperature',
             stable_boltzmann((5000., 5000., 2000.), 1.), (.5, .5, 0.))

BM = (False, True, True)
BMP = stable_boltzmann(BQ, BT, BM)
vector_check('Boltzmann_masked_probabilities', BMP,
             (0., .8807970779778823, .11920292202211755))
check('Boltzmann_masked_probability_mass', math.fsum(BMP), 1., atol=1e-14, rtol=0.)
retained = math.fsum(x for x, ok in zip(BP, BM) if ok)
vector_check('Boltzmann_mask_then_renormalize', BMP,
             tuple(x / retained if ok else 0. for x, ok in zip(BP, BM)))

BEP = masked_uniform_mix(BP, .1)
vector_check('Boltzmann_epsilon_mixture', BEP,
             (.6681793947617505, .2668801476415106, .06494045759673908))
check('Boltzmann_epsilon_mass', math.fsum(BEP), 1., atol=1e-14, rtol=0.)
checks.append(dict(name='Boltzmann_epsilon_floor', actual=min(BEP),
                   floor=.1 / 3, passed=min(BEP) >= .1 / 3))
BMEP = masked_uniform_mix(BMP, .1, BM)
vector_check('Boltzmann_masked_epsilon_mixture', BMEP,
             (0., .8427173701800942, .15728262981990582))
check('Boltzmann_masked_epsilon_mass', math.fsum(BMEP), 1., atol=1e-14, rtol=0.)
checks.append(dict(name='Boltzmann_masked_floor',
                   actual=min(x for x, ok in zip(BMEP, BM) if ok), floor=.05,
                   passed=all(x >= .05 if ok else x == 0 for x, ok in zip(BMEP, BM))))
check('Boltzmann_expected_reward',
      math.fsum(x * y for x, y in zip(BP, BQ)), 4635.146458779562)
check('Boltzmann_entropy_nats', entropy_nats(BP), .7138657579886247,
      atol=1e-14, rtol=1e-12)
BF = entropy_objective(BP, BQ, BT)
logz = max(BQ) / BT + math.log(math.fsum(math.exp((x - max(BQ)) / BT) for x in BQ))
check('Boltzmann_entropy_optimum_known', BF, 5349.012216768187)
check('Boltzmann_log_partition_identity', BF, BT * logz)
for label, r in (('greedy', (1., 0., 0.)), ('uniform', (1 / 3,) * 3),
                 ('nonuniform', (.5, .3, .2)), ('epsilon_mixture', BEP)):
    kl = math.fsum(x * math.log(x / y) for x, y in zip(r, BP) if x > 0)
    gap = BF - entropy_objective(r, BQ, BT)
    check('Boltzmann_fixed_Q_KL_gap_' + label, gap, BT * kl, atol=1e-9, rtol=1e-12)
    checks.append(dict(name='Boltzmann_nonnegative_gap_' + label,
                       actual=gap, passed=gap >= -1e-9))
check('Boltzmann_greedy_raw_reward_advantage',
      max(BQ) - math.fsum(x * y for x, y in zip(BP, BQ)), 364.853541220438)
check('Boltzmann_epsilon_objective_gap',
      BF - entropy_objective(BEP, BQ, BT), 11.202237994601091)

for label, fn in (
    ('empty', lambda: stable_boltzmann((), BT)),
    ('zero_temperature', lambda: stable_boltzmann(BQ, 0.)),
    ('negative_temperature', lambda: stable_boltzmann(BQ, -1.)),
    ('nan_temperature', lambda: stable_boltzmann(BQ, float('nan'))),
    ('infinite_temperature', lambda: stable_boltzmann(BQ, float('inf'))),
    ('nan_value', lambda: stable_boltzmann((0., float('nan')), BT)),
    ('infinite_value', lambda: stable_boltzmann((0., float('inf')), BT)),
    ('empty_admissible_set', lambda: stable_boltzmann(BQ, BT, (False,) * 3)),
    ('mask_length', lambda: stable_boltzmann(BQ, BT, (True,))),
    ('epsilon_below_zero', lambda: masked_uniform_mix(BP, -.1)),
    ('epsilon_above_one', lambda: masked_uniform_mix(BP, 1.1)),
    ('epsilon_nan', lambda: masked_uniform_mix(BP, float('nan'))),
    ('unmasked_mixture_input', lambda: masked_uniform_mix(BP, .1, BM)),
    ('empty_probability_vector', lambda: masked_uniform_mix((), .1)),
    ('negative_probability', lambda: masked_uniform_mix((-.1, .5, .6), .1)),
    ('probability_above_one', lambda: masked_uniform_mix((1.1, 0., 0.), .1)),
    ('probability_sum', lambda: masked_uniform_mix((.2, .2, .2), .1)),
    ('probability_nan', lambda: masked_uniform_mix((float('nan'), 1.), .1)),
    ('probability_infinite', lambda: masked_uniform_mix((float('inf'), 0.), .1)),
    ('nonboolean_mask', lambda: stable_boltzmann(BQ, BT, (1, 1, 0))),
    ('objective_dimension', lambda: entropy_objective(BP, (1., 2.), BT)),
    ('entropy_invalid_probability', lambda: entropy_nats((-.5, 1.5))),
):
    expect_value_error('Boltzmann_invalid_' + label, fn)

sources=[]
source_paths = [ROOT/'ARTICLE_2_CONTEXTUAL_BANDITS_AND_SEQUENTIAL_COLLECTION.md']
source_paths.extend(ROOT/'build'/'appendices'/f'ARTICLE_{num}_MATHEMATICAL_APPENDIX.md'
                    for num in (2,5))
for path in source_paths:
    data=path.read_bytes()
    if b'\0' in data:
        raise ValueError('NUL byte in source '+str(path))
    sources.append(dict(path=str(path.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))

report=dict(status='passed' if all(c['passed'] for c in checks) else 'failed',
            check_count=len(checks),passed_count=sum(c['passed'] for c in checks),
            scope='Deterministic mathematical identities and synthetic numerical examples in Article 2 and appendices 2 and 5, including finite-action Boltzmann policy arithmetic. Empirical fitting, causal identification and production validation require their respective evidence.',
            sources=sources,checks=checks,
            manual_review=dict(boltzmann='Fixed-Q softmax, admissible-action masking, uniform exploration floor and entropy-regularized objective are checked separately from raw expected reward and sequential policy performance.',
                               hierarchy='Logistic and hazard models use distinct coefficient sets, shared sector/region/vintage hierarchy pattern, half-t SD priors and a declared hazard baseline.',
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
