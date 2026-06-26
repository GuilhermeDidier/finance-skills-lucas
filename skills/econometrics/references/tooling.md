# Implementação: R, Python e Stata

> Receitas idiomáticas. Default por linguagem: **R = `fixest`**, **Python = `linearmodels`/`statsmodels`**, **Stata = `reghdfe`/`ivreg2`**.

## R — `fixest` (rápido, multi-FE, IV, clustering nativo)

```r
library(fixest); library(modelsummary)

# OLS robusto
feols(y ~ x1 + x2, data = df, vcov = "hetero")

# Two-way fixed effects + cluster
feols(y ~ x | firm + year, data = df, cluster = ~firm)

# IV (endógena ~ instrumentos)
feols(y ~ exog | firm + year | x_endog ~ z1 + z2, data = df)
fitstat(m, ~ ivf)   # F de 1ª fase (instrumento fraco)

# DiD / event study (Sun-Abraham para tratamento escalonado)
feols(y ~ sunab(cohort, year) | id + year, data = df, cluster = ~id)
iplot(m)            # plota o event study

# Tabela publication-ready (LaTeX)
modelsummary(list(m1, m2), stars = c('*'=.1,'**'=.05,'***'=.01),
             output = "results/tab.tex")
```
Callaway-Sant'Anna: pacote `did` (`att_gt()` → `aggte()`). RDD: `rdrobust`. Controle sintético: `tidysynth`/`Synth`; Synthetic DiD: `synthdid`.

## Python — `linearmodels` + `statsmodels`

```python
import pandas as pd, statsmodels.formula.api as smf
from linearmodels.panel import PanelOLS
from linearmodels.iv import IV2SLS

# OLS robusto
smf.ols("y ~ x1 + x2", df).fit(cov_type="HC3")

# Two-way FE + cluster (índice MultiIndex: entidade, tempo)
df = df.set_index(["firm", "year"])
PanelOLS.from_formula("y ~ x + EntityEffects + TimeEffects", df)\
        .fit(cov_type="clustered", cluster_entity=True)

# IV 2SLS:  IV2SLS(dep, exog, endog, instruments)
res = IV2SLS.from_formula("y ~ 1 + exog + [x_endog ~ z1 + z2]", df).fit(
        cov_type="clustered", clusters=df["firm"])
print(res.first_stage)          # diagnóstico de 1ª fase
```
DiD escalonado: `differences` (Callaway-Sant'Anna) ou `pyfixest` (porta o `fixest`/`sunab`). RDD: `rdrobust` (tem versão Python). Double ML: `DoubleML`.

## Stata — `reghdfe` + `ivreg2`

```stata
* OLS robusto
reg y x1 x2, robust

* Multi-FE + cluster
reghdfe y x, absorb(firm year) vce(cluster firm)

* IV com diagnósticos de instrumento fraco/sobre-id
ivreg2 y exog (x_endog = z1 z2), cluster(firm) first
* -> Kleibergen-Paap F (weak IV), Hansen J (overid)

* DiD escalonado robusto
csdid y, ivar(id) time(year) gvar(first_treat)      // Callaway-Sant'Anna
eventstudyinteract ... (Sun-Abraham);  did_multiplegt (dCDH)

* Tabelas
esttab using tab.tex, star(* .1 ** .05 *** .01) se
```
RDD: `rdrobust`. PSM: `psmatch2`/`teffects`. Painel dinâmico: `xtabond2` (Roodman).

## Tabela de equivalência rápida

| Tarefa | R | Python | Stata |
|---|---|---|---|
| OLS robusto | `feols(...,vcov="hetero")` | `.fit(cov_type="HC3")` | `reg, robust` |
| Multi-FE + cluster | `feols(y~x\|fe, cluster=)` | `PanelOLS` | `reghdfe, absorb() vce(cluster)` |
| IV/2SLS | `feols(y~\|fe\|x~z)` | `IV2SLS` | `ivreg2` |
| DiD escalonado | `sunab()` / `did` | `differences`/`pyfixest` | `csdid` |
| RDD | `rdrobust` | `rdrobust` | `rdrobust` |
| Tabela | `modelsummary` | `stargazer`/`pystout` | `esttab` |

## Boas práticas de reprodutibilidade
1. Script único e ordenado: setup → load → clean → descritivas → spec principal → robustez → export.
2. Seeds fixas; versões de pacotes registradas (`renv`/`pip freeze`).
3. Nunca editar dado bruto à mão; toda transformação no código.
4. Exportar tabelas/figuras direto p/ `results/` (sem copiar-colar números).

## Wild cluster bootstrap (poucos clusters)
Quando há **< ~40 clusters**, o SE clusterizado subestima e o p-valor é inválido. Receita:
```r
# R
library(fwildclusterboot)
m <- feols(y ~ treat | fe, data = df, cluster = ~estado)
boottest(m, param = "treat", clustid = ~estado, B = 9999)
```
```stata
* Stata
reghdfe y treat, absorb(fe) vce(cluster estado)
boottest treat, reps(9999)
```

## Callaway-Sant'Anna (DiD escalonado) nas 3 linguagens
```r
library(did); att <- att_gt(yname="y", tname="ano", idname="id",
        gname="primeiro_trat", data=df); aggte(att, type="dynamic")
```
```python
from differences import ATTgt
att = ATTgt(data=df, cohort_name="primeiro_trat").fit(formula="y")
```
```stata
csdid y, ivar(id) time(ano) gvar(primeiro_trat) agg(event)
```

## Estrutura de projeto reprodutível
```
projeto/
├── data/raw/        (nunca editar à mão)
├── data/clean/      (gerado por código)
├── code/  01_clean.R  02_descritivas.R  03_main.R  04_robustez.R
├── results/  tables/  figures/
└── renv.lock | requirements.txt   (versões travadas)
```

## Fontes
`fixest` (Bergé) · `linearmodels` (Sheppard) · `reghdfe` (Correia) · `did` (Callaway-Sant'Anna) · `fwildclusterboot`/`boottest` (Roodman et al.) · Gentzkow-Shapiro (*Code and Data for the Social Sciences*).
