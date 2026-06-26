# Inferência causal — o núcleo da skill

> *Correlação não é causalidade.* Cada método aproxima o **contrafactual**: o que teria acontecido sem o tratamento. Fontes cruzadas: Angrist-Pischke (*Mostly Harmless*), Cunningham (*Causal Inference: The Mixtape*), Callaway-Sant'Anna (2021), de Chaisemartin-D'Haultfœuille (2020), Imbens-Lemieux (RDD), Abadie (synthetic control).

## 0. Potential outcomes (Rubin)

Unidade $i$: $Y_i(1)$ (tratada) e $Y_i(0)$ (não). Só observamos uma → **problema fundamental**. Estimandos:
- **ATE** $=E[Y(1)-Y(0)]$ · **ATT** $=E[Y(1)-Y(0)\mid D=1]$ · **LATE** = efeito nos *compliers* (o que IV identifica).

A diferença de médias observada decompõe em:
$$\underbrace{E[Y\mid D{=}1]-E[Y\mid D{=}0]}_{\text{observado}} = \underbrace{ATT}_{\text{causal}} + \underbrace{E[Y(0)\mid D{=}1]-E[Y(0)\mid D{=}0]}_{\text{viés de seleção}}$$
Todo método ataca o termo de seleção. **SUTVA** (sem interferência entre unidades, um só "tipo" de tratamento) é assumida em todos.

## 1. Difference-in-Differences (DiD)

**Ideia:** compara a *variação* (antes→depois) entre tratados e controles. A tendência do controle é o contrafactual do tratado.

### DiD 2×2 na mão
| | Pré | Pós | Δ |
|---|---|---|---|
| Tratado | 50 | 62 | +12 |
| Controle | 48 | 54 | +6 |

$\hat\delta = (62{-}50)-(54{-}48)=12-6=\mathbf{+6}$. (O +14 bruto e o +12 antes-depois seriam ambos errados — ignoram nível e tendência comum.)

Forma de regressão (two-way fixed effects):
$$Y_{it}=\alpha_i+\lambda_t+\delta\,(Trat_i\times Pós_t)+\varepsilon_{it}$$

- **Hipótese-chave: tendências paralelas** — sem tratamento, tratados e controles evoluiriam igual. Não testável diretamente; *apoie* com **pré-tendências** (event study) e placebos.
- **Inferência:** cluster no nível do tratamento; poucos clusters → wild bootstrap.

### Event study
$$Y_{it}=\alpha_i+\lambda_t+\sum_{k\ne -1}\gamma_k\,\mathbb{1}(t-t^*_i=k)+\varepsilon_{it}$$
$\gamma_k$ pré ($k<0$) ≈ 0 sustenta paralelismo; $\gamma_k$ pós traça a dinâmica. **Omita o período $-1$** (referência) — incluir todos gera colinearidade.

### ⚠️ TWFE com tratamento escalonado é viesado
Com adoção em **momentos diferentes**, o TWFE usa unidades **já-tratadas como controle** ("forbidden comparisons") → pondera efeitos com pesos que podem ser **negativos**.

- **Bacon decomposition** (Goodman-Bacon 2021): o estimador TWFE é uma **média ponderada** de todos os DiD 2×2 possíveis (cedo vs nunca, tarde vs nunca, cedo vs tarde, **tarde vs cedo** ← o problemático). Se o efeito **cresce no tempo**, a comparação "tarde vs cedo" entra com sinal trocado e pode **inverter** o sinal agregado.
- **Estimadores robustos (use estes):**
  - **Callaway & Sant'Anna** (`did` em R, `csdid` em Stata) — ATT(g,t) por coorte×período, agregados depois.
  - **Sun & Abraham** (`sunab()` no `fixest`) — event study com interações coorte×tempo.
  - **de Chaisemartin-D'Haultfœuille** (`did_multiplegt`) — robusto a efeitos heterogêneos, permite tratamento que liga/desliga.
  - **Borusyak-Jaravel-Spiess** (imputation, `did_imputation`) — eficiente sob homocedasticidade.

> Default seguro: adoção escalonada → **nunca** TWFE simples; rode Callaway-Sant'Anna **e** mostre a Bacon decomposition para diagnosticar o peso das comparações ruins.

## 2. Instrumental Variables (IV)

**Para:** endogeneidade (variável omitida, simultaneidade, erro de medida). Instrumento $Z$ afeta $Y$ **só via** $X$.

Duas condições:
1. **Relevância** $Cov(Z,X)\ne 0$ — *testável* (1ª fase).
2. **Exclusão/exogeneidade** $Z$ ⟂ erro e sem outro canal — **não testável**, defenda institucionalmente.

**2SLS:** 1ª fase $X=\pi Z+v$; 2ª fase $Y=\beta\hat X+u$. Com 1 endógena e 1 instrumento, $\hat\beta_{IV}=\frac{Cov(Z,Y)}{Cov(Z,X)}$ (estimador de Wald).

### Mini-exemplo (Wald, instrumento binário)
$Z$ = elegível a programa (sorteado). $E[Y\mid Z{=}1]-E[Y\mid Z{=}0]=4$ (efeito intenção-de-tratar). Adesão: $E[X\mid Z{=}1]-E[X\mid Z{=}0]=0{,}5$. **LATE** $=4/0{,}5=\mathbf{8}$ — efeito nos compliers (os que aderem por serem elegíveis).

- **Instrumento fraco:** 1ª fase fraca → viés (em direção ao OLS) e SE explodindo. **F de 1ª fase > 10** (Stock-Yogo, regra clássica); o limiar moderno é **mais alto** (Lee et al. sugerem ~F>104 p/ t-test válido a 5%). Use **effective F de Montiel-Pflueger** e **IC de Anderson-Rubin** (robusto a weak IV).
- IV identifica o **LATE**, não o ATE (requer **monotonicidade** — sem *defiers*).
- **Sobre-identificação** (mais instrumentos que endógenas): **Hansen J / Sargan** (H0: instrumentos exógenos). Não prova exogeneidade — só checa consistência mútua.

## 3. Regression Discontinuity (RDD)

**Ideia:** tratamento muda descontinuamente num *cutoff* $c$ de uma running variable $X$. Quem está logo acima ≈ quem está logo abaixo → quasi-aleatório na vizinhança.

- **Sharp:** $D=\mathbb{1}(X\ge c)$ determinístico. Efeito $=\lim_{x\downarrow c}E[Y\mid X]-\lim_{x\uparrow c}E[Y\mid X]$.
- **Fuzzy:** prob. de tratamento **salta** (não 0→1) → IV local = (salto em $Y$)/(salto em $D$).
- **Diagnósticos (obrigatórios):**
  - **Bandwidth ótimo** data-driven (Calonico-Cattaneo-Titiunik, `rdrobust`) + **IC robusto a bias** (não use polinômio global de ordem alta — Gelman-Imbens).
  - **McCrary / densidade** (`rddensity`): teste de manipulação da running variable em torno do corte.
  - **Continuidade de covariáveis** pré-tratamento no corte (placebo).
  - **Robustez** a bandwidth e a cutoffs falsos.
- Identifica efeito **local ao cutoff** (validade externa limitada).

## 4. Controle sintético (Synthetic Control)

**Para:** 1 (ou poucas) unidade tratada, painel longo (efeito de política num estado/país — Abadie-Gardeazabal, Abadie-Diamond-Hainmueller).

- Controle sintético = **combinação ponderada** de unidades "doadoras" não-tratadas que replica o tratado **no pré-tratamento** (pesos ≥0 somam 1).
- Efeito = trajetória real − sintética no pós.
- **Inferência por placebo/permutação:** aplica o método a cada doador; o efeito do tratado deve ser **extremo** vs a distribuição placebo (RMSPE ratio).
- Extensões: **Synthetic DiD** (Arkhangelsky et al. 2021 — combina pesos de unidade e de tempo), augmented SC, generalized SC.

## 5. Matching / Propensity Score / DML

**Para:** seleção em **observáveis** (CIA/unconfoundedness: $Y(0),Y(1)\perp D\mid X$). O mais **fraco** — exige que controlar por $X$ elimine o viés.

- **PSM:** estima $p(X)=P(D{=}1\mid X)$ (logit); casa tratados/controles por escore. Cheque **balanceamento** (diferenças padronizadas <0,1) e **suporte comum/overlap**.
- **Pesagem (IPW):** pondera por $1/p(X)$ (tratados) e $1/(1-p)$ (controles).
- **Doubly robust / AIPW:** combina modelo de outcome + propensity; consistente se **um dos dois** estiver certo.
- **Double/Debiased ML** (Chernozhukov et al.; `DoubleML`): usa ML (forests, lasso) para os *nuisance* (propensity e outcome) com **cross-fitting** e score de Neyman-ortogonal → permite muitos controles sem viés de regularização. Estado da arte para seleção em observáveis de alta dimensão.
- ⚠️ Nada disso resolve **variável omitida não-observada** — é "controlar melhor", não identificação por desenho.

## Como escolher (árvore de decisão)
- Aleatorização? → **RCT** (compare médias).
- Tratamento muda num corte de variável contínua? → **RDD**.
- Grupo de comparação + antes/depois? → **DiD/event study** (cheque escalonamento → Callaway-Sant'Anna).
- Instrumento crível (exógeno, relevante)? → **IV**.
- 1 unidade tratada, painel longo? → **Controle sintético**.
- Só observáveis (muitos)? → **DML/AIPW/matching** (seja humilde quanto a não-observáveis).

## Armadilhas
- ❌ TWFE com adoção escalonada (use Callaway-Sant'Anna/Sun-Abraham + Bacon).
- ❌ Justificar exclusão de IV com "parece exógeno" sem argumento institucional.
- ❌ F>10 como garantia (limiar moderno é mais alto; use Anderson-Rubin se fraco).
- ❌ RDD com polinômio global de ordem alta ou sem McCrary.
- ❌ Apresentar PSM/DML como solução de endogeneidade não-observada.
- ❌ DiD sem mostrar pré-tendências/placebos.

## Fontes
Angrist-Pischke MHE (IV/LATE, DiD) · Cunningham Mixtape (potential outcomes, RDD, synthetic) · Goodman-Bacon (2021), Callaway-Sant'Anna (2021), de Chaisemartin-D'Haultfœuille (2020), Sun-Abraham (2021) · Calonico-Cattaneo-Titiunik (RDD robusto) · Abadie-Diamond-Hainmueller (synthetic) · Chernozhukov et al. (DML).
