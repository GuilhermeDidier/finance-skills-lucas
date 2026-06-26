# Worked example — VAR Selic × IPCA × câmbio (dado REAL do BCB)

> Rodado com **dado real do BCB-SGS, 2004–2026 (mensal, n=268)** via `python-bcb`. Fluxo completo: **dados → estacionariedade → especificação → IRF → validação out-of-sample**. O resultado real revela os clássicos **price puzzle / exchange-rate puzzle** — uma lição que os números "de livro-texto" escondem. Script reprodutível ao final.

## Pergunta
Como um **choque de juros (Selic)** se propaga sobre **câmbio (BRL/USD)** e **inflação (IPCA)** ao longo do tempo? E qual a defasagem da política monetária no Brasil?

## Passo 1 — Dados
Mensais, fev/2004–mai/2026 (n=268), SGS via `python-bcb`:
- `selic` — Selic meta (% a.a.), SGS **432** (diária → fim de mês).
- `cambio` — R$/US$ venda, SGS **1** (diária → fim de mês).
- `ipca` — variação mensal do IPCA (%), SGS **433**.

> ⚠️ Séries **diárias** no SGS (432, 1) têm limite de **10 anos por consulta** — puxe em janelas e concatene (ver script).

Transformações: `d_selic = Δselic`; `dlcambio = 100·Δlog(câmbio)` (variação % ≈ depreciação quando positivo).

## Passo 2 — Estacionariedade (ADF / KPSS) — valores reais

| Série | ADF p (H0: raiz unit.) | KPSS p (H0: estac.) | Conclusão |
|---|---|---|---|
| `ipca` | **0,000** | 0,100 | **I(0)** — usar em nível |
| `selic` (nível) | 0,005 | 0,031 | ambíguo/persistente → diferenciar |
| `d_selic` | **0,000** | 0,100 | **I(0)** ✔️ |
| `log(câmbio)` | 0,915 | 0,010 | **I(1)** — não-estacionária |
| `dlcambio` | **0,000** | 0,100 | **I(0)** ✔️ |

Leitura: IPCA já é estacionário; câmbio e Selic em nível **não** são (Selic é muito persistente — ADF e KPSS discordam, sinal de quase-raiz-unitária). Johansen no período não dá cointegração robusta entre os três → seguimos com **VAR nas variáveis estacionárias** `[ipca, d_selic, dlcambio]`. (Se houvesse cointegração, seria **VECM** — ver `macro-timeseries.md`.)

## Passo 3 — Especificação do VAR
Seleção de lags (real): **AIC = 4**, BIC = 3, HQIC = 4 → escolhemos **VAR(4)**.
```python
from statsmodels.tsa.api import VAR
res = VAR(data[["ipca","d_selic","dlcambio"]]).fit(4)
```

## Passo 4 — Identificação (Cholesky)
Ordem econômica **mais lenta → mais rápida**: `[ipca → d_selic → dlcambio]` — inflação reage com defasagem, juro responde à inflação, câmbio é o preço mais rápido. (IRFs ortogonalizadas; **a ordem importa** — reportá-la é obrigatório.)

## Passo 5 — IRF real: resposta a um choque de +1 d.p. em `d_selic`

| Horizonte (meses) | 0 | 3 | 6 | 12 | 18 | 24 |
|---|---|---|---|---|---|---|
| **Câmbio** (cumul., %) | −0,01 | +0,12 | +0,48 | **+0,78** | +0,92 | +0,99 |
| **IPCA** (p.p.) | 0,000 | +0,039 | +0,019 | +0,008 | +0,004 | +0,002 |

Pico da resposta do IPCA: **mês 2 (+0,051 p.p.)**, depois decai.

### ⚠️ Os números reais contam uma história "errada" — e isso é a lição
O livro-texto prevê: aperto de juros → câmbio **aprecia** e inflação **cai**. O dado real mostra o **oposto** no curto prazo:
- **Exchange-rate puzzle:** câmbio **deprecia** ~+0,8% em 12m após alta de juros.
- **Price puzzle (Sims):** inflação **sobe** (+0,05 p.p.) logo após o aperto.

Por que acontece (e por que **não** é erro de código):
1. **Endogeneidade / variável omitida.** O Copom sobe a Selic *justamente quando* há choque de risco/inflação à frente. O VAR recursivo, sem controlar o risco, atribui ao juro o que é do choque que o motivou. Falta uma variável de **risco/expectativas** (EMBI+, Focus) e/ou commodities.
2. **Identificação ingênua.** Cholesky impõe uma ordem contemporânea forte; o puzzle costuma sumir com **restrições de sinal**, **proxy-SVAR** ou incluindo expectativas — exatamente o que `macro-timeseries.md` recomenda.
3. **Contexto BR / dominância fiscal.** Sob prêmio de risco fiscal elevado, alta de juros pode de fato coincidir com depreciação — o canal cambial "limpo" não opera. Isso conecta com a ressalva de **dominância fiscal** em `brazilian-macro.md`.

> **Esta é a moral do exemplo:** uma IRF é tão boa quanto sua identificação. O VAR recursivo "cru" produz puzzles bem documentados; o trabalho sério é **consertar a identificação**, não confiar no primeiro gráfico.

## Passo 6 — Validação out-of-sample (real)
Prever `ipca` 1 passo à frente, **janela expansiva** (treino = 70% inicial, n_teste = 80), vs **random walk** (último IPCA):

| Modelo | RMSE |
|---|---|
| **VAR(4)** | **0,362** |
| Random walk | 0,419 |

→ O VAR **bate o random walk em +13,6%** na previsão 1 passo à frente. Ou seja: para *forecast* de curto prazo o modelo tem valor mesmo com a identificação estrutural problemática — **previsão e identificação causal são objetivos diferentes** (um VAR pode prever bem e ainda assim dar IRF sem sentido estrutural).

## Leitura final (formato de saída da skill)
1. **Modelo:** VAR(4) em `[ipca, d_selic, dlcambio]` (estacionárias), Cholesky `[ipca→selic→câmbio]`, dado real SGS 2004–2026.
2. **IRF:** choque de juros → câmbio **deprecia** (+0,8%/12m) e inflação **sobe** levemente — **puzzles** por endogeneidade/identificação, não por código.
3. **Validação:** VAR vence random walk em 13,6% (RMSE 0,362 vs 0,419) na previsão 1 passo.
4. **Contexto BR:** o puzzle é coerente com **prêmio de risco fiscal/dominância fiscal**; identificação limpa exige incluir risco/expectativas ou usar restrições de sinal.
5. **Próximo passo metodológico:** re-estimar com EMBI+/Focus no sistema e/ou SVAR com restrições de sinal → o puzzle deve atenuar.

## Reprodutibilidade
Script `var-real.py` (no material da skill): puxa SGS em janelas de 10 anos, testa ADF/KPSS, seleciona lags, estima o VAR, extrai IRF ortogonalizada e roda a validação OOS. Dependências: `python-bcb`, `statsmodels`, `pandas`, `numpy`.

## A enriquecer (roadmap)
- [x] Rodar com dado real do SGS e colar IRF/OOS verdadeiros. ✅ *(feito — revelou os puzzles)*
- [ ] Adicionar **EMBI+/Focus** ao VAR e mostrar o puzzle atenuando.
- [ ] Versão **SVAR com restrições de sinal** (Uhlig) como contraste ao Cholesky.
- [ ] Versão com **cointegração** → VECM (Selic curta × DI longo).
- [ ] Caso de **previsão de IPCA**: SARIMA vs VAR vs mediana do Focus (quem ganha?).
