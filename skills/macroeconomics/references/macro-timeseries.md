# Séries temporais macro — VAR, cointegração e previsão

> A peça que **não existia pronta** no mercado de skills. Regra de ouro: **estacionariedade primeiro, validação fora-da-amostra depois.** Fontes cruzadas: Hamilton (*Time Series Analysis*), Enders (*Applied Econometric Time Series*), Lütkepohl (*New Introduction to Multiple Time Series*), Kilian-Lütkepohl (*Structural VAR*), Jordà (2005, local projections).

## 1. Estacionariedade — o ponto de partida
Série estacionária = média, variância e autocovariância constantes. Regredir séries não-estacionárias gera **correlação espúria** (R² alto, tudo "significante", nada real — Granger-Newbold).

- **Testes de raiz unitária:**
  - **ADF** (Augmented Dickey-Fuller): H0 = raiz unitária (não-estacionária). Rejeitar = estacionária. Inclua tendência se a série tem trend.
  - **KPSS:** H0 = estacionária (**invertido**). Use os dois: ADF rejeita **e** KPSS não rejeita → confiança em I(0). Discordância → quase-raiz-unitária/baixa potência.
  - **Phillips-Perron** (robusto a hetero/autocorrelação não-paramétrico).
- **Ordem de integração I(d):** nº de diferenças para estacionar. Maioria das séries macro em nível é **I(1)**; em log-diferença (≈ crescimento %) costuma ser **I(0)**.
- **Cuidados:** **quebra estrutural** imita raiz unitária (Perron 1989) → teste de **Zivot-Andrews** (quebra endógena). Sazonalidade → dessazonalizar (X-13-ARIMA-SEATS) ou SARIMA. Não diferencie demais (over-differencing cria MA não-invertível).

## 2. ARIMA / SARIMA (univariado)
$ARIMA(p,d,q)$: $d$ diferenças, $p$ termos AR, $q$ MA.
- **Identificação:** ACF/PACF (PACF corta em $p$ p/ AR puro; ACF corta em $q$ p/ MA puro) **ou** minimizar **AIC/BIC** (`auto.arima`/`pmdarima`). BIC penaliza mais → modelos parcimoniosos.
- **SARIMA** $(p,d,q)(P,D,Q)_s$: sazonalidade de período $s$ (12 mensal, 4 trimestral).
- **Diagnóstico de resíduos:** ruído branco (Ljung-Box não rejeita); sem ARCH remanescente.
- Bom **benchmark univariado**; previsão converge p/ média/tendência, intervalos alargam com o horizonte.
- Extensões: **ARIMAX/transfer function** (regressores exógenos), **ETS** (suavização exponencial — frequentemente competitivo).

## 3. VAR (Vector Autoregression)
$$\mathbf{y}_t = \mathbf{c} + A_1\mathbf{y}_{t-1} + \dots + A_p\mathbf{y}_{t-p} + \mathbf{u}_t$$
- **Use com séries estacionárias** (I(0)) — ou em diferenças, ou **VECM** se cointegradas.
- **Seleção de lags:** AIC/BIC/HQ; cheque resíduos sem autocorrelação (LM test) e **estabilidade** (raízes do polinômio característico dentro do círculo unitário).
- **Saídas:**
  - **IRF (resposta a impulso):** resposta de uma variável a um choque de 1 d.p. em outra ao longo do tempo — o produto principal. Bandas por bootstrap.
  - **FEVD (decomposição da variância):** que fração da variância do erro de previsão de cada variável vem de choques de cada outra → mede a "potência" relativa.
  - **Causalidade de Granger:** lags de X ajudam a prever Y? **Precedência temporal, NÃO causalidade estrutural.**

### Identificação estrutural (SVAR) — onde mora a suposição
A IRF depende de como se recuperam os **choques estruturais** dos resíduos reduzidos ($\mathbf{u}_t = B\boldsymbol{\varepsilon}_t$):
- **Cholesky (recursivo):** impõe ordem de contemporaneidade (a 1ª variável afeta as demais no impacto, não o contrário). **Resultado muda com a ordem** → ordene por argumento econômico (mais lenta/exógena primeiro: atividade → preços → juros → câmbio). Gera os clássicos **price puzzle / exchange-rate puzzle** quando há variável de risco omitida (ver `worked-example.md`).
- **Restrições de sinal** (Uhlig 2005): impõe apenas o **sinal** das respostas por algumas defasagens (ex.: choque monetário contracionista → juro sobe, preço cai, atividade cai) e aceita todo o conjunto de IRFs compatível. Mais agnóstico; entrega um **intervalo** de respostas, não um ponto.
- **Restrições de longo prazo** (Blanchard-Quah 1989): choque de demanda não tem efeito permanente no produto; só de oferta tem.
- **Proxy-SVAR / external instruments** (Stock-Watson, Mertens-Ravn): usa um instrumento de fora (surpresa de política via high-frequency) para identificar **um** choque sem ordenar tudo.
- > A IRF é tão crível quanto a história de identificação. **Sempre reporte a suposição** e, idealmente, mostre robustez a esquemas alternativos.

## 4. Cointegração e VECM (relações de longo prazo)
Se séries são I(1) mas existe combinação linear delas que é I(0), são **cointegradas** — têm **equilíbrio de longo prazo** comum (juro curto×longo, consumo×renda, câmbio×diferencial de preços/PPP).

- **Engle-Granger** (2 variáveis): regride uma na outra, testa se o resíduo é estacionário (ADF com valores críticos próprios). Simples, assimétrico, só 1 relação.
- **Johansen** (multivariado): testa o **número de vetores de cointegração** $r$ via **trace** e **max-eigenvalue**.
  - Leitura prática: testa H0: rank ≤ 0, depois ≤ 1, etc. **Pare no primeiro que não rejeita.** Ex.: 3 variáveis, trace rejeita r=0 mas não r=1 → **1 vetor de cointegração** (uma relação de equilíbrio).
- **VECM** = VAR em diferenças + **termo de correção de erro**:
  $$\Delta\mathbf{y}_t = \alpha\,\underbrace{(\beta'\mathbf{y}_{t-1})}_{\text{desvio do equilíbrio}} + \sum\Gamma_i\Delta\mathbf{y}_{t-i} + \mathbf{u}_t$$
  - $\beta$ = relação de **longo prazo** (cointegração); $\alpha$ = **velocidade de ajuste** (quão rápido cada variável corrige o desvio; sinal deve "puxar de volta"). $\alpha$ próximo de 0 → ajuste lento.
- **Regra de decisão:** I(1) + cointegradas → **VECM**; I(1) sem cointegração → **VAR em diferenças**; I(0) → **VAR em nível**.

## 5. Previsão honesta (anti-overfitting)
- **Out-of-sample sempre.** Treino/teste ou **janela rolante/expansível** (re-estima a cada passo, prevê o seguinte).
- **Benchmark ingênuo obrigatório:** random walk (último valor) ou média. Modelo que não bate o RW não tem valor. (Câmbio: bater RW em horizonte curto é notoriamente difícil — Meese-Rogoff 1983.)
- **Métricas:** RMSE, MAE, MAPE. **Diebold-Mariano** testa se a diferença de acurácia entre dois modelos é significativa; **Clark-West** para modelos aninhados.
- **Intervalos / fan chart:** reporte incerteza, não só ponto.
- **Real-time / vintage data** (ALFRED): para replicar uma decisão histórica, use o dado **como era na época** (PIB é revisado) — senão há look-ahead por revisão.
- **Combinação de previsões** (média de modelos) costuma bater qualquer modelo isolado (Bates-Granger).

## 6. Além do básico
- **Volatilidade — ARCH/GARCH:** clusters de volatilidade (câmbio, ativos). GARCH(1,1) é o cavalo de batalha; EGARCH/GJR p/ assimetria (alavancagem). Ver também skill **derivatives-modeling** (vol).
- **Mudança de regime — Markov-switching** (Hamilton 1989): recessão vs expansão, alta vs baixa vol, com probabilidades de transição.
- **Frequências mistas — MIDAS / bridge equations:** usar dado mensal/diário para prever variável trimestral (PIB).
- **Nowcasting — dynamic factor models / Kalman** (Giannone-Reichlin-Small): extrai um fator comum de muitas séries de alta frequência; atualiza a previsão do trimestre corrente a cada novo dado.
- **Local projections** (Jordà 2005): estima a IRF regredindo $y_{t+h}$ no choque, **um horizonte por vez** — mais robusto a má especificação que o VAR, integra bem com identificação por instrumentos (LP-IV); custo: menos eficiente.
- **Bayesian VAR (BVAR):** prioris (Minnesota) domam VARs grandes (muitas variáveis, poucos dados); padrão em bancos centrais. Large BVAR (Bańbura et al.) para dezenas de séries.

## Ferramentas
- **R:** `urca` (ADF/KPSS/Johansen), `vars` (VAR/SVAR/IRF/FEVD), `tsDyn`/`urca` (VECM), `forecast`/`fable` (ARIMA/ETS), `rugarch` (GARCH), `BVAR`/`bvartools`, `lpirfs` (local projections).
- **Python:** `statsmodels.tsa` (adfuller/kpss, ARIMA/SARIMAX, VAR, VECM, `coint_johansen`), `pmdarima` (auto-arima), `arch` (GARCH), `statsmodels` Markov-switching, `localprojections`.

## Armadilhas
- ❌ VAR/regressão em níveis I(1) sem checar cointegração → espúrio.
- ❌ IRF sem explicitar identificação (ordem de Cholesky muda tudo).
- ❌ Confundir Granger com causalidade econômica.
- ❌ Avaliar previsão **in-sample** (overfitting garantido).
- ❌ Não comparar com random walk.
- ❌ Ignorar quebras estruturais e revisões de dados.
- ❌ Over-differencing (cria MA não-invertível e infla a variância).

## Fontes
Hamilton (VAR, Markov-switching, Kalman) · Enders (ARIMA, cointegração, prático) · Lütkepohl (VAR/VECM, referência técnica) · Kilian-Lütkepohl (SVAR, identificação) · Uhlig (sign restrictions) · Blanchard-Quah (restrições de longo prazo) · Jordà (local projections) · Giannone-Reichlin-Small (nowcasting) · Diebold-Mariano (avaliação de previsão).
