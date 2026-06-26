# Variáveis dependentes limitadas (binárias, contagem, censuradas, seleção)

> Quando $y$ **não** é contínuo e irrestrito, OLS não basta. Mapa de modelos de máxima verossimilhança (MLE) e como **interpretá-los** sem errar. Fontes: Wooldridge (*Cross Section & Panel*, cap. 15–19), Cameron-Trivedi (*Microeconometrics*), Greene (*Econometric Analysis*).

## 1. Desfecho binário (0/1): Logit e Probit

$$P(y=1\mid x)=G(x'\beta), \quad G=\begin{cases}\Lambda(z)=\dfrac{e^z}{1+e^z} & \text{logit}\\ \Phi(z) & \text{probit (normal)}\end{cases}$$

- **Coeficientes ≠ efeitos marginais.** O sinal de $\beta_j$ indica direção; a magnitude depende de onde se avalia (G é não-linear).
- **Reporte efeitos marginais:**
  - **AME** (average marginal effect) — média do efeito sobre a amostra. **Preferido.**
  - **MEM** (marginal effect at means) — avaliado nas médias (pode ser irrealista).
  - $\dfrac{\partial P}{\partial x_j}=g(x'\beta)\,\beta_j$, com $g$ a densidade.
- **Logit — odds ratio:** $e^{\beta_j}$ = razão de chances por +1 de $x_j$. Ex.: $\beta=0{,}69\Rightarrow e^{0{,}69}\approx 2$ → dobra a chance.
- **LPM (Linear Probability Model)** — OLS em $y$ binário: coeficientes já são efeitos marginais (fáceis, robustos a especificação, ótimos com FE/IV), mas prevê fora de [0,1] e é heterocedástico por construção (use SE robusto). **Angrist-Pischke defendem LPM** para efeitos causais; logit/probit quando se quer probabilidades bem-comportadas.
- Logit vs probit: resultados quase idênticos (coefs logit ≈ 1,6× probit); escolha por convenção da área.
- **Ajuste:** pseudo-$R^2$ (McFadden), % corretamente classificado, **AUC/ROC**, Hosmer-Lemeshow (calibração).

### Mini-exemplo
Logit de inadimplência, $\beta_{\text{dívida/renda}}=0{,}8$. Odds ratio $=e^{0{,}8}=2{,}23$ → cada +1 na razão dívida/renda **dobra** as chances de default. AME pode ser, digamos, +12 p.p. na probabilidade avaliada na amostra.

## 2. Contagens: Poisson e Binomial Negativa

$y\in\{0,1,2,\dots\}$ (nº de eventos). $E[y\mid x]=e^{x'\beta}$, então $\beta_j$ = **variação proporcional** (semi-elasticidade): +1 de $x_j$ → $100(e^{\beta_j}-1)$% em $E[y]$.

- **Poisson** assume $Var=E$ (equidispersão). Quase sempre violado (**overdispersion** $Var>E$).
- **Binomial Negativa:** acrescenta parâmetro de dispersão (teste de overdispersion vs Poisson).
- **PPML (Poisson Pseudo-ML):** consistente **mesmo sem ser Poisson de verdade**, só precisa da média certa — padrão moderno para **log-gravidade com zeros** (Santos Silva-Tenreyro, comércio internacional). Resolve o viés de fazer log(y) com muitos zeros.
- Excesso de zeros estrutural → **zero-inflated** (ZIP/ZINB) ou hurdle.

## 3. Censura e canto: Tobit

$y$ observado só num intervalo (ex.: gasto ≥0, com massa em 0; salário top-coded). OLS é **viesado** (a censura distorce).
- **Tobit (tipo I):** modela a variável latente $y^*=x'\beta+u$, observando $y=\max(0,y^*)$. Efeito marginal decompõe em (prob. de estar acima do limite) × (efeito condicional).
- Sensível a normalidade/homocedasticidade do latente.

## 4. Seleção amostral: Heckman

Quando a amostra observada é **selecionada** de forma não-aleatória relacionada ao desfecho (ex.: salário só de quem trabalha → viés de seleção de Gronau-Heckman).
- **Heckit (two-step):** (1) probit de seleção → **inverse Mills ratio** $\lambda$; (2) regressão do desfecho **incluindo $\lambda$**. Coeficiente de $\lambda$ significativo = havia viés de seleção.
- **Identificação:** idealmente uma **exclusion restriction** (variável que afeta seleção mas não o desfecho) — sem ela, identifica só pela não-linearidade de $\lambda$ (frágil).

## 5. Multinomial e ordenado
- **Multinomial logit** (categorias sem ordem: meio de transporte). Assume **IIA** (independência de alternativas irrelevantes — teste de Hausman-McFadden); se violado → **nested logit** ou **mixed/random-parameters logit**.
- **Ordered logit/probit** (categorias ordenadas: rating AAA>AA>A; escala Likert). Modela limiares (cutpoints); pressupõe **proportional odds** (teste de Brant).

## 6. Painel não-linear (rápido)
- **FE logit** (conditional logit de Chamberlain): elimina efeito fixo, mas só usa unidades que "mudam" de desfecho e **não dá efeitos marginais** diretos.
- **Probit FE** sofre **incidental parameters problem** (viés com T pequeno) → use correlated random effects (Mundlak) ou probit de efeitos aleatórios.
- Alternativa pragmática para efeito causal: **LPM com FE** (e cluster), aceitando as limitações.

## Tabela-resumo

| $y$ | Modelo | $\beta_j$ significa | Cuidado |
|---|---|---|---|
| binário | logit/probit (ou LPM) | direção; reporte AME | coef ≠ efeito marginal |
| binário causal | **LPM** | efeito marginal direto | fora de [0,1], heterocedástico |
| contagem | Poisson/NB/**PPML** | % em $E[y]$ | overdispersion; zeros |
| censurado | Tobit | efeito no latente | normalidade |
| selecionado | Heckman | + correção de viés | precisa exclusion restriction |
| categórico | multinomial/ordered logit | log-odds relativo | IIA / proportional odds |

## Armadilhas
- ❌ Ler coeficiente de logit/probit como efeito marginal (reporte **AME**).
- ❌ `log(y)` com muitos zeros → use **PPML**.
- ❌ Poisson sem checar overdispersion.
- ❌ OLS em variável censurada (use Tobit) ou em amostra selecionada (use Heckman).
- ❌ Probit FE com T pequeno (incidental parameters).
- ❌ Multinomial logit sem testar IIA.

## Fontes
Wooldridge (cap. 15–19, painel não-linear) · Cameron-Trivedi (contagens, MLE) · Greene · Angrist-Pischke (defesa do LPM) · Santos Silva-Tenreyro (PPML).
