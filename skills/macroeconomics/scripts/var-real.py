"""Valida o worked-example de macroeconomics com dado REAL do BCB-SGS."""
import warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from bcb import sgs
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.api import VAR

# ---- 1. Dados reais (SGS). Séries diárias (Selic 432, câmbio 1) têm limite de
#         10 anos por consulta -> puxa em janelas e concatena.
def fetch_chunked(code, name, start="2004-01-01"):
    out = []
    yr0 = int(start[:4])
    for y in range(yr0, 2027, 9):
        s = f"{y}-01-01"; e = f"{min(y+8,2026)}-12-31"
        try:
            out.append(sgs.get({name: code}, start=s, end=e))
        except Exception:
            pass
    return pd.concat(out).sort_index()[~pd.concat(out).sort_index().index.duplicated()]

selic = fetch_chunked(432, "selic")
cambio = fetch_chunked(1, "cambio")
ipca = sgs.get({"ipca": 433}, start="2004-01-01")
raw = selic.join(cambio, how="outer").join(ipca, how="outer")
df = raw.resample("ME").last()
df["d_selic"] = df["selic"].diff()
df["dlcambio"] = np.log(df["cambio"]).diff() * 100
data = df[["ipca", "d_selic", "dlcambio"]].dropna()
print(f"Amostra: {data.index.min():%Y-%m} a {data.index.max():%Y-%m}  (n={len(data)})\n")

# ---- 2. Estacionariedade
def adf_p(s): return adfuller(s.dropna(), autolag="AIC")[1]
def kpss_p(s):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return kpss(s.dropna(), regression="c", nlags="auto")[1]
print("Estacionariedade (ADF H0=raiz unit; KPSS H0=estacionária)")
for name, s in [("ipca", df["ipca"]), ("selic(nivel)", df["selic"]),
                ("d_selic", df["d_selic"]), ("log_cambio", np.log(df["cambio"])),
                ("dlcambio", df["dlcambio"])]:
    print(f"  {name:14s} ADF p={adf_p(s):.3f}  KPSS p={kpss_p(s):.3f}")
print()

# ---- 3. Seleção de lags
sel = VAR(data).select_order(12)
print("Seleção de lags (AIC/BIC/HQIC):")
print(f"  AIC={sel.aic}  BIC={sel.bic}  HQIC={sel.hqic}\n")
p = sel.aic
res = VAR(data).fit(p)

# ---- 4. IRF: resposta a choque em d_selic (ordem Cholesky = colunas do data)
irf = res.irf(24)
idx = {n: i for i, n in enumerate(data.columns)}
cum_cambio = irf.orth_cum_effects[:, idx["dlcambio"], idx["d_selic"]]  # cumul. nivel cambio
resp_ipca = irf.orth_irfs[:, idx["ipca"], idx["d_selic"]]
print(f"VAR({p}) | ordem Cholesky: {list(data.columns)}")
print("IRF a choque de +1 d.p. em d_selic:")
print("  h(meses):     0      3      6     12     18     24")
print("  cambio(cum%): " + " ".join(f"{cum_cambio[h]:6.2f}" for h in [0,3,6,12,18,24]))
print("  ipca(p.p.):   " + " ".join(f"{resp_ipca[h]:6.3f}" for h in [0,3,6,12,18,24]))
mx = int(np.argmax(np.abs(resp_ipca)))
print(f"  -> pico |resposta IPCA| no mes {mx} ({resp_ipca[mx]:+.3f} p.p.)\n")

# ---- 5. Validação OOS: prever ipca 1 passo, janela expansiva, vs random walk
start = int(len(data) * 0.7)
err_var, err_rw = [], []
for t in range(start, len(data) - 1):
    tr = data.iloc[:t]
    try:
        fc = VAR(tr).fit(p).forecast(tr.values[-p:], 1)[0][idx["ipca"]]
    except Exception:
        continue
    actual = data["ipca"].iloc[t]
    err_var.append(actual - fc)
    err_rw.append(actual - data["ipca"].iloc[t-1])  # RW: ultimo valor
rmse_var = np.sqrt(np.mean(np.square(err_var)))
rmse_rw  = np.sqrt(np.mean(np.square(err_rw)))
print(f"Validacao OOS (IPCA, 1 passo, n={len(err_var)}):")
print(f"  RMSE VAR = {rmse_var:.4f}  |  RMSE random walk = {rmse_rw:.4f}")
print(f"  VAR {'BATE' if rmse_var < rmse_rw else 'NAO bate'} o random walk "
      f"({(rmse_rw-rmse_var)/rmse_rw*100:+.1f}% vs RW)")
