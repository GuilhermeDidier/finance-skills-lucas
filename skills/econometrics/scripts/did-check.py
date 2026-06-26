"""Valida o worked-example de econometrics: DiD TWFE + event study + cluster SE.
Painel sintético calibrado para REPRODUZIR a tabela documentada:
  tratado 50->62, controle 48->54, DiD=6; efeito cresce no pos."""
import warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
rng = np.random.default_rng(7)

states = [f"S{i:02d}" for i in range(12)]
treated = set(states[:6])
years = list(range(2015, 2022))
t_star = 2018
# efeito verdadeiro por ano (trajetória da skill); 2018 = adoção/transição
true_gamma = {2018: 2.1, 2019: 4.5, 2020: 6.2, 2021: 7.0}
trend = lambda y: 1.5 * (y - 2016)          # tendência comum (paralela)
NOISE = 0.25

rows = []
for s in states:
    base = (50 if s in treated else 48) + rng.normal(0, 0.4)
    for y in years:
        eff = true_gamma.get(y, 0.0) if s in treated else 0.0
        emp = base + trend(y) + eff + rng.normal(0, NOISE)
        rows.append((s, y, emp, int(s in treated)))
df = pd.DataFrame(rows, columns=["estado","ano","emp","trat"])
# 'pos' = efeito plenamente ativo a partir de 2019 (anúncio 2018)
df["pos"] = (df["ano"] >= 2019).astype(int)
df["trat_pos"] = df["trat"] * df["pos"]

# --- DiD 2x2 por médias (pre=2015-17, pos=2019-21; 2018 = transição, fora) ---
m22 = df[df.ano != 2018].copy()
g = m22.groupby(["trat","pos"])["emp"].mean()
did = (g[(1,1)]-g[(1,0)]) - (g[(0,1)]-g[(0,0)])
print("== DiD 2x2 (pre 2015-17 vs pos 2019-21) ==")
print(f"  tratado:  pre={g[(1,0)]:.1f}  pos={g[(1,1)]:.1f}  Δ={g[(1,1)]-g[(1,0)]:.1f}")
print(f"  controle: pre={g[(0,0)]:.1f}  pos={g[(0,1)]:.1f}  Δ={g[(0,1)]-g[(0,0)]:.1f}")
print(f"  DiD = {did:.2f}\n")

# --- TWFE com cluster por estado (exclui 2018 p/ casar com 2x2) ---
m = smf.ols("emp ~ trat_pos + C(estado) + C(ano)", m22).fit(
        cov_type="cluster", cov_kwds={"groups": m22["estado"]})
print("== TWFE (estado+ano FE, cluster por estado) ==")
print(f"  δ̂ = {m.params['trat_pos']:.2f}  SE={m.bse['trat_pos']:.2f}  "
      f"t={m.tvalues['trat_pos']:.2f}  p={m.pvalues['trat_pos']:.3f}\n")

# --- Event study com dummies explícitas (ref = 2017) ---
es_df = df.copy()
for y in years:
    if y == 2017: continue
    es_df[f"g{y}"] = ((es_df.ano == y) & (es_df.trat == 1)).astype(int)
gcols = [f"g{y}" for y in years if y != 2017]
es = smf.ols(f"emp ~ {' + '.join(gcols)} + C(estado) + C(ano)", es_df).fit(
        cov_type="cluster", cov_kwds={"groups": es_df["estado"]})
print("== Event study (γ_k, ref=2017) ==")
print("  ano    γ̂      SE    signif(5%)")
for y in years:
    if y == 2017:
        print(f"  {y}   0.00   (ref)"); continue
    c, se, pv = es.params[f"g{y}"], es.bse[f"g{y}"], es.pvalues[f"g{y}"]
    print(f"  {y}  {c:+.2f}  {se:.2f}   {'sim' if pv<0.05 else 'não'}")
