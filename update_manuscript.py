with open('/home/user/Claude/manuscript_corrected_text.txt') as f:
    text = f.read()

# Fix AgtNrs references
text = text.replace('AgtNrs (B = 0.004, p > .05)', 'AgtNrs (B = -0.021, SE = 0.015, p = .163)')
text = text.replace('.004 (.012)', '-.021 (.015)')

# ThirdParty footnote
old_tp = ('ThirdParty Involvement: a binary indicator coded from PA-X mediation variables, '
          'identifying whether a formal mediator or international organization was present '
          'in a facilitative role (65.3% of processes in the sample meet this criterion).')
new_tp = ('ThirdParty Involvement: a binary indicator coded from PA-X v.8 mediation variables, '
          'identifying whether a formal mediator or international organization was present '
          'in a facilitative role (65.3% of processes in the sample meet this criterion). '
          '[Footnote: ThirdParty_Involvement was derived directly from PA-X Version 8 '
          'mediation-related variables and coded 1 if any agreement within the process '
          'contained evidence of formal third-party mediator or international organization '
          'involvement in a facilitative role, 0 otherwise. This variable was not stored '
          'in the PP-X SPSS dataset file; it was computed from PA-X v.8 source data prior '
          'to process-level aggregation and merged for use in Models 8-9 only.]')
text = text.replace(old_tp, new_tp)

# Table 2
old_t2 = ('Table 2: Robustness Check — Logistic Regression with Contextual Controls (N=150)\n\n'
           'Note: Values are B (SE). * p<.05.')
new_t2 = """Table 2: Robustness Check - Logistic Regression with Contextual Controls (N=150)

Variable                  | Model 8            | Model 9
--------------------------|--------------------|-----------------
TjMech                    | 0.700 (0.187)*     | 0.556 (0.207)*
TjVic                     |                    | 0.165 (0.243)
TjPrire                   |                    | 0.123 (0.191)
TjNR                      |                    | 0.229 (0.243)
Conflict_Intensity (z)    | -0.240 (0.210)     | -0.191 (0.218)
ThirdParty_Involvement    | 1.492 (0.469)*     | 1.354 (0.483)*
AgtNrs                    | -0.022 (0.013)     | -0.029 (0.016)
Is_Local                  | .077 (.505)        | .077 (.505)
Constant                  | -1.942 (0.414)*    | -2.164 (0.450)*

Note: Values are B (SE). * p<.05. Model 8 includes TjMech plus contextual controls.
Model 9 adds all four theorized TJ provisions simultaneously. ThirdParty_Involvement
derived from PA-X v.8 mediation variables (see footnote in Section 5.3).
Conflict_Intensity is z-scored UCDP conflict type code."""
text = text.replace(old_t2, new_t2)

# New sections 6.5-6.7
new_sections = """
6.5 Limitations and Future Research Directions
While this study makes important theoretical and methodological contributions, several limitations warrant discussion and suggest directions for future research. The primary methodological contribution is the temporal freezing procedure rather than the PP-X reorganization itself. By ensuring that all predictors are derived exclusively from pre-outcome data, this approach offers a transferable solution to hindsight bias in peace process research applicable to any process-level dataset, not only PA-X.

Endogeneity and Causal Inference

As discussed in Section 5.2, our findings represent robust associations rather than definitive causal effects. The temporal freezing design strengthens causal inference by ensuring predictors reflect only information available before final outcomes were determined, thus avoiding hindsight bias and establishing temporal precedence. However, this design does not fully eliminate endogeneity concerns. Selection bias persists because underlying factors that lead some processes to include TJ provisions during partial stages may also independently predict success. Additionally, reverse causality within stages remains possible if negotiators perceiving positive momentum include more ambitious provisions precisely because they anticipate success.

The literature identifies the balance of power between parties as a theoretically important predictor of peace agreement provision and durability. We use the standardized UCDP conflict type code as the closest available proxy for conflict severity, and note the absence of a direct power-balance measure as a boundary condition on the generalizability of our results.

As noted in Section 6.4, the highest-coding procedure does not preserve information about the order in which TJ provisions appeared within the partial stage. The Online Appendix reports an exploratory first-agreement analysis testing whether first-agreement inclusion predicted outcomes differently from later inclusion. Results are preliminary and largely inconclusive. A properly powered sequencing analysis would require dedicated first-appearance coding across all agreements in all processes, which we recommend for future work.

Our control variables, robustness checks, and methodological triangulation partially address these concerns, but future research could strengthen causal inference through instrumental variable designs, matching methods, and qualitative process tracing in selected cases.

Defining and Categorizing Peace Processes

Our analysis inherits the PA-X database's definitions of what constitutes a peace process and how processes are bounded in time. As Kapshuk (2021) discusses, defining peace processes involves difficult choices about when a process begins and ends, and how to treat negotiations that resume after breakdown. Future research could develop typologies of peace processes based on structural characteristics and temporal patterns, examining whether the factors predicting success differ across process types.

Contextual Variation

Our sample encompasses peace processes from diverse conflicts including interstate, intrastate, and local disputes. This diversity strengthens generalizability but also means our findings represent average associations across heterogeneous contexts. Future research could examine whether the importance of truth mechanisms varies with conflict intensity, international involvement, or regional norms through interaction analyses or stratified samples.

Scope of Provisions Examined

While we examined TJ provisions comprehensively using all available PA-X variables, peace agreements address numerous other issues that influence success. D'Amico, Sosa, and Melin (2025) find that private goods embedded in peace agreements significantly improve the durability of peace, complementing our TJ-focused results by suggesting different categories of provisions operate through distinct mechanisms. Future research should extend the process-level, temporal freezing approach to these other domains, and examine how interim provisions relate to outcomes beyond comprehensive agreement including peace durability, implementation quality, and human rights improvements.

6.6 The Null Finding: Why Amnesties, Courts, and Vetting Do Not Predict Success
Among the most substantively significant findings of this analysis is a null result. Amnesties (TjAm), courts and prosecutions (TjCou), and vetting (TjVet), the three TJ mechanisms most prominent in the peace-versus-justice debate, demonstrate no significant independent association with whether peace processes achieve comprehensive settlement. In the Random Forest analysis, all three rank below the median in variable importance. In logistic regression, none approaches statistical significance across any model specification.

These provisions were not incorporated into the theoretical hypotheses of Section 2.3 because the peace-versus-justice literature characterizes courts and vetting primarily as impediments rather than facilitators, while the empirical role of amnesty provisions remains contested. All three were retained in the exploratory Random Forest analysis to assess whether they would exhibit limited predictive power. The null finding substantiates this expectation, yet warrants explicit interpretation.

The result challenges both positions in the peace-versus-justice debate. The absence of a negative association between courts or vetting and process success contradicts the skeptical argument that accountability mechanisms undermine negotiations. The absence of a positive association for amnesties contradicts the argument that impunity provisions are necessary to facilitate agreement. TjAm does exhibit a modest bivariate association with comprehensive settlement (B = 0.293, p = .042), but this association is entirely attenuated when TjMech is held constant (B = 0.071, p = .697), indicating that amnesty provisions co-occur with broader TJ engagement rather than independently predicting outcomes.

The determinative factor for whether processes reach comprehensive settlement appears to be the presence of truth-seeking and acknowledgment mechanisms, not the choice between retributive and amnesiac approaches to justice. This finding is consistent with Olsen et al.'s (2010) conclusion that combinations of mechanisms outperform single approaches. For practitioners, deliberations over amnesty versus prosecution, however consequential for post-agreement legitimacy and human rights, may not constitute the primary determinant of negotiation success. The inclusion of truth-seeking provisions in partial agreements is a more robust predictor of process success than the accountability architecture adopted.

6.7 Implications for Policy and Practice
Our findings offer several practical insights for negotiators, mediators, and policymakers engaged in peace processes. Most fundamentally, the results suggest that including mechanisms to deal with the past during interim stages is associated with successful progression to comprehensive settlement. This finding challenges perspectives that view justice provisions as obstacles to peace or issues best deferred until after conflict ends. Our analysis indicates that establishing truth mechanisms during partial stages may facilitate rather than impede reaching final agreements.

For practitioners, this suggests that frameworks addressing past abuses should be considered early in negotiations rather than postponed. The political feasibility of including such mechanisms during interim stages, combined with their strong association with success, makes them valuable tools for peace process design. Importantly, mechanisms for dealing with the past appear to function most effectively when combined with other provisions such as prisoner releases and victim participation. The interaction patterns identified in our analysis point toward comprehensive justice packages rather than isolated provisions as the most promising approach.

However, our findings also counsel careful attention to which justice mechanisms are employed and when. Truth commissions show strong positive associations with success, while more retributive measures like vetting and prosecutions showed limited predictive importance in our models. Provisions that establish principles of justice without immediately threatening current leaders may be more suitable for interim stages, with decisions about prosecutions or vetting potentially deferred to later phases or post-agreement contexts.

Finally, our methodological approach demonstrates the value of process-level analysis for understanding peace negotiations. Rather than evaluating agreements in isolation, practitioners might benefit from thinking systematically about entire negotiation trajectories. Which issues should be addressed in what sequence? How do early agreements create foundations for later ones? What combinations of provisions demonstrate genuine commitment to transformation? These process-design questions, informed by systematic analysis of historical patterns, can complement the case-specific knowledge and context-sensitivity that effective peacemaking requires.
"""

# Insert after section 6.4
marker = "understanding these different roles is essential for both theoretical development and practical peacemaking."
idx = text.lower().find(marker.lower())
if idx >= 0:
    insert_at = idx + len(marker)
    text = text[:insert_at] + '\n' + new_sections + text[insert_at:]
    print("Inserted after 6.4")
else:
    text = text + '\n' + new_sections
    print("Appended (marker not found)")

# Pronoun fixes
pronoun_map = [
    ('the author addresses', 'we address'),
    ('the author shows', 'we show'),
    ('the author argues', 'we argue'),
    ('the author uses', 'we use'),
    ('the author employs', 'we employ'),
    ('the author frames', 'we frame'),
    ('the author finds', 'we find'),
    ('the author provides', 'we provide'),
    ('the author describes', 'we describe'),
    ('the author notes', 'we note'),
    ('the author introduces', 'we introduce'),
    ('the author characterizes', 'we characterize'),
    ('The author addresses', 'We address'),
    ('The author shows', 'We show'),
    ('The author argues', 'We argue'),
    ('The author uses', 'We use'),
    ('The author employs', 'We employ'),
    ('The author finds', 'We find'),
    ('The author provides', 'We provide'),
    ('The author describes', 'We describe'),
    ('The author notes', 'We note'),
]
# Handle possessives separately to avoid syntax issues
text = text.replace("the author's analysis", "our analysis")
text = text.replace("the author's approach", "our approach")
text = text.replace("the author's dataset", "our dataset")
text = text.replace("the author's findings", "our findings")
text = text.replace("the author's contribution", "our contribution")
text = text.replace("The author's analysis", "Our analysis")
text = text.replace("The author's approach", "Our approach")
for old, new in pronoun_map:
    text = text.replace(old, new)

with open('/home/user/Claude/manuscript_corrected_text.txt', 'w') as f:
    f.write(text)

print(f"Done: {len(text)} chars")
for needle, label in [
    ('6.5 Limitations', 'Section 6.5'),
    ('6.6 The Null Finding', 'Section 6.6'),
    ('6.7 Implications for Policy', 'Section 6.7'),
    ('PA-X Version 8 mediation-related variables', 'ThirdParty footnote'),
    ('1.492 (0.469)*', 'Table 2 values'),
    ('B = 0.071, p = .697', 'TjAm null finding'),
    ('TjGar', 'No TjGar remaining'),
]:
    found = needle in text
    print(f'  {"[OK] FOUND" if found else "[MISS] NOT FOUND"}: {label}')
