# Fundamentos: modelo linear, inferência e erros-padrão

> Base para todo o resto. O objetivo: **inferência correta** — o coeficiente certo *e* o erro-padrão certo. Fontes cruzadas: Wooldridge (*Introductory* e *Cross Section & Panel*), Angrist-Pischke (*Mostly Harmless*, cap. 3), Cameron-Trivedi (*Microeconometrics*), Cunningham (*Mixtape*).

## 1. Modelo linear e o que OLS estima

$$y_i = \beta_0 + \beta_1 x_{1i} + \dots + \beta_k x_{ki} + u_i, \qquad \hat\beta = (X'X)^{-1}X'y$$

**Interpretação de $\beta_j$:** efeito de 1 unidade de $x_j$ sobre $y$, **mantendo os demais regressores fixos** (ceteris paribus parcial — teorema de Frisch-Waugh-Lovell: $\beta_j$ é a regressão de $y$ na parte de $x_j$ ortogonal aos outros regressores).

| Forma | Modelo | Leitura de $\beta_1$ |
|---|---|---|
| nível-nível | $y=\beta_0+\beta_1x$ | Δ$y$ por +1 de $x$ |
| log-nível | $\ln y=\beta_0+\beta_1x$ | +1 de $x$ → ~$100\beta_1$ % em $y$ |
| nível-log | $y=\beta_0+\beta_1\ln x$ | +1% em $x$ → $\beta_1/100$ em $y$ |
| log-log | $\ln y=\beta_0+\beta_1\ln x$ | **elasticidade** (% por %) |

> Semi-elasticidade exata (log-nível, dummy): $100\,(e^{\beta_1}-1)$, não $100\beta_1$, quando $\beta_1$ é grande.

## 2. Hipóteses de Gauss-Markov (e o que cada quebra causa)

| Hipótese | Significa | Se quebra |
|---|---|---|
| Linearidade nos parâmetros | modelo correto | viés de especificação |
| Amostragem aleatória | i.i.d. | SE/inferência errados |
| **Exogeneidade** $E[u\mid X]=0$ | regressores ⟂ erro | **viés** (a ameaça central) |
| Sem multicolinearidade perfeita | $X$ posto cheio | não estima |
| Homocedasticidade $Var(u\mid X)=\sigma^2$ | variância constante | OLS não-viesado, mas SE clássico errado → robusto |
| Normalidade de $u$ (opcional) | só p/ amostra pequena | irrelevante em amostra grande (TCL) |

Sob 1–4, OLS é **não-viesado e consistente**; somando homocedasticidade, é **BLUE** (Gauss-Markov: menor variância entre lineares não-viesados).

## 3. Viés de variável omitida (OVB) — a ameaça nº 1

Modelo verdadeiro $y=\beta_0+\beta_1x+\beta_2z+u$; estimamos sem $z$. O plim do coeficiente de $x$:

$$\text{plim }\hat\beta_1 = \beta_1 + \beta_2\,\underbrace{\delta_{zx}}_{\text{coef. de } x \text{ em } z\sim x}, \qquad \text{viés}=\beta_2\,\frac{Cov(x,z)}{Var(x)}$$

**Regra do sinal:** sinal(viés) = sinal($\beta_2$) × sinal(corr($x,z$)).

### Mini-exemplo numérico (faça sempre o sinal antes de rodar)
Salário ~ educação, omitindo **habilidade**. $\beta_2>0$ (habilidade ↑ salário) e corr(educação, habilidade) > 0 → **viés positivo**: OLS **superestima** o retorno da educação. Se o retorno "verdadeiro" é 7%/ano e a habilidade some no erro, você pode ler 10%. → motiva IV (proximidade de faculdade, Card) ou efeitos fixos de gêmeos.

**Soluções:** incluir $z$ (se observável); **efeitos fixos** (se $z$ é invariante no tempo/grupo — ver `panel-data.md`); **IV**; desenho quasi-experimental.

## 4. Bad controls e colisores — o erro oposto ao OVB

Controlar **demais** também enviesa. Um **bad control** é uma variável afetada pelo tratamento (pós-tratamento) ou um **colisor** (causa comum de tratamento e desfecho condicionada).

- Ex.: efeito de educação no salário **controlando ocupação** → ocupação é *canal* (pós-tratamento); controlar bloqueia parte do efeito e cria viés de seleção. (Angrist-Pischke §3.2.3.)
- Mini-DAG: $T \to M \to Y$ e $T\to Y$. Controlar $M$ (mediador) remove o efeito indireto. Controlar um **colisor** $C$ com $T\to C\leftarrow Y$ **abre** um caminho espúrio.
- **Regra:** só controle por **pré-tratamento** (confundidores), nunca por consequências do tratamento.

## 5. Erros-padrão: o ponto que mais se erra

Ponto estimado pode estar certo e a inferência errada pelo SE.

| Tipo | Corrige | Quando usar |
|---|---|---|
| Clássico (homocedástico) | nada | quase nunca válido com dado real |
| **Robusto HC** (White) | heterocedasticidade | *default mínimo* em cross-section |
| **Clusterizado** | correlação intra-grupo | **no nível da atribuição do tratamento** |
| **HAC** (Newey-West) | hetero + autocorrelação | séries temporais |

**Variantes HC** (amostra pequena): HC0 (White cru) → HC1 (×$n/(n-k)$, default do Stata `robust`) → HC2/HC3 (ajuste por leverage; **HC3 recomendado** com $n$ pequeno — MacKinnon-White). Em amostra grande convergem.

**Clustering — é decisão de desenho, não estatística.** Pergunte "onde estão correlacionados os choques?". Política por estado → cluster por estado. **Poucos clusters (<~40):** o SE clusterizado **subestima** → use **wild cluster bootstrap** (Cameron-Gelbach-Miller; `fwildclusterboot` em R, `boottest` em Stata).

## 6. Inferência

- **t** = $\hat\beta_j/SE$; |t|>1,96 ≈ 5% bicaudal (amostra grande). **F** p/ restrições conjuntas.
- Reporte **IC e magnitude econômica**, não só estrelas. "Significante" ≠ "importante" — em amostra grande quase tudo rejeita; foque no **tamanho do efeito**.
- **Multiple testing / p-hacking:** muitas especificações inflam falsos positivos. Pré-registre a spec principal; o resto é robustez. Correções: Bonferroni (conservador), Romano-Wolf, FDR (Benjamini-Hochberg).

## 7. Além do OLS (mapa — detalhe em `limited-dependent-variables.md`)
- **GLS/WLS:** estrutura de variância conhecida (eficiência).
- **Logit/Probit (MLE):** $y$ binário — coeficientes **não** são efeitos marginais (reporte **AME**).
- **Poisson/PPML:** contagens e log-gravidade com zeros.
- **Quantílica:** efeito em quantis, não na média.

## Armadilhas
- ❌ SE clássico com heterocedasticidade/clusters → inferência inválida.
- ❌ Clusterizar no nível errado (observação em vez de tratamento).
- ❌ **Bad controls** (variáveis pós-tratamento) → reintroduz viés.
- ❌ Interpretar coeficiente de logit/probit como efeito marginal.
- ❌ Confundir significância estatística com relevância econômica.
- ❌ Poucos clusters sem wild bootstrap.

## Fontes
Wooldridge (OVB, FE, robustez) · Angrist-Pischke MHE cap. 3 (bad controls, FWL, robustez) · MacKinnon-White (HC2/HC3) · Cameron-Gelbach-Miller (wild cluster) · Cunningham Mixtape (DAGs, colisores).
