from pathlib import Path
p=Path(r'C:\Users\Nevo\Downloads\behavioural credit scoring - underwrite to collect rct\series\publications\linkedin\2026-10-08_causal_credit_series\build\appendices\ARTICLE_2_MATHEMATICAL_APPENDIX.md')
s=p.read_text(encoding='utf-8')
a=s.index('From the hazard definition,');b=s.index('For $y_i=',a)
s=s[:a]+'A1.8 derives the hazard-to-survival identity, and A1.7 gives the right-censored event contribution. Substituting the hierarchical hazard above gives the likelihood used here.\n\n'+s[b:]
a=s.index('For competing terminal causes,');b=s.index('## A2.7',a)
s=s[:a]+'For competing terminal causes, each cause retains its own baseline, coefficients and sector, region and vintage effects. A1.8 derives event-free survival, cumulative incidence and probability conservation. For every joint posterior draw, compute those quantities from the complete set of cause-specific hazards before averaging across draws. Default risk is the default cumulative incidence when other terminal exits compete; a single-event model uses one minus survival. Cure followed by re-default uses the intermediate-state transition construction in A1.8. These calculations retain the dependencies represented by the joint posterior.\n\n'+s[b:]
a=s.index('For lawful evaluation group');b=s.index('## A2.9',a)
s=s[:a]+r'''A1.9 defines the group true-positive and false-positive rates and their outcome conventions. Those definitions apply here at the registered decision time, population and horizon. The policy may add a selection-rate ratio:

$$
s_g=\Pr(\widehat Y=1\mid G=g),\qquad
\operatorname{SelectionRatio}_{g,g_0}=s_g/s_{g_0},\quad s_{g_0}>0.
$$

The positive decision and comparison group are declared with the rule. A zero denominator requires a defined review route. Each fairness constraint states whether it applies to a single decision, a cohort or a trajectory; sequential action histories and selective observation determine its estimation and uncertainty. The legal and model-validation process approves the evaluation population, lawful data basis and thresholds.

'''+s[b:]
a=s.index('For $r_j=x_j');b=s.index('For hierarchical logistic Thompson sampling',a)
s=s[:a]+'A1.4 derives the ridge estimate, confidence ellipsoid and Linear UCB action score. That construction supplies the linear benchmark here. '+s[b:]
a=s.index('When behaviour propensity');b=s.index('For trajectories,',a)
s=s[:a]+'A1.5–A1.6 derive the one-step importance-weight identity and doubly robust estimator. Their consistency, exchangeability and support conditions apply at each sequential decision. This subsection extends that evaluation to full action histories.\n\n'+s[b:]
a=s.index('Article 2 references',s.index('## A2.16'));b=s.index('The auxiliary half-t representation',a)
s=s[:a]+"Each subsection identifies its methodological sources in Article 2's reference list. "+s[b:]
start=s.index('Here $p(\\sigma_k)$ is the declared half-t')
insert=r'''Conditioning on the normal–Gamma scale auxiliary variable gives an explicit non-centred block. Define

$$
q_{\sigma k}=v^{\mathsf T}\Omega v+\lambda_{\sigma k}/s_{0,k}^2,
\qquad m_{\sigma k}=q_{\sigma k}^{-1}v^{\mathsf T}(\kappa-\Omega c).
$$

Completing the square yields

$$
\sigma_k\mid z,\omega,\lambda_{\sigma k},D
\sim N(m_{\sigma k},q_{\sigma k}^{-1})\ \text{truncated to }(0,\infty).
$$

This block holds raw non-centred effects $z$ fixed. The centred inverse-Gamma block holds realised effects $u$ fixed. The two auxiliary constructions are alternative implementations of the declared prior; each sampler follows its own consistent conditioning scheme. Integrating Gaussian group effects over a shared half-t standard deviation gives a different mixture from independent Student-t priors on signed fixed coefficients.

'''
s=s[:start]+insert+s[start:]
p.write_text(s,encoding='utf-8')
print('A2 scoped deduplication and prior-role clarification saved.')
