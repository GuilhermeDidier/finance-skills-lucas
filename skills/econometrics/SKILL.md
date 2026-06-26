---
name: econometrics
description: Econometria aplicada — estimação e inferência (OLS/GLS, erros-padrão robustos e clusterizados, testes de hipótese), dados em painel (efeitos fixos/aleatórios, within/between, painel dinâmico Arellano-Bond), e inferência causal (DiD/diferenças-em-diferenças, event study, IV/variáveis instrumentais, RDD/regressão descontínua, controle sintético, matching), com diagnósticos (heterocedasticidade, autocorrelação, multicolinearidade, instrumentos fracos, testes de especificação) e a implementação prática em R (fixest), Python (linearmodels/statsmodels) e Stata (reghdfe/ivreg2). Use quando o usuário quiser estimar um modelo, identificar um efeito causal, escolher estratégia de identificação, rodar regressão com painel, clusterizar erros-padrão, interpretar coeficientes/diagnósticos, ou gerar código econométrico reprodutível. Gatilhos: "econometria", "regressão", "OLS", "efeito causal", "identificação", "DiD", "diferenças em diferenças", "event study", "IV", "variável instrumental", "RDD", "descontinuidade", "controle sintético", "matching", "painel", "efeitos fixos", "clusterizar", "erro-padrão robusto", "endogeneidade", "instrumento fraco", "fixest", "linearmodels", "reghdfe".
---

# Econometrics (Econometria Aplicada)

Skill para **estimar relações e identificar efeitos causais** a partir de dados. O fio condutor: *correlação não é causalidade* — toda estimativa séria começa por uma **estratégia de identificação** (o que torna a variação explorada "as-good-as-random") antes de qualquer regressão. Forte ênfase em **inferência causal moderna** e na **implementação correta** (erros-padrão no nível certo, diagnósticos, robustez). Séries temporais macro (VAR/cointegração/forecast) → skill **macroeconomics**.

## Quando usar
- **Estimar** um modelo (OLS/GLS, logit/probit) e **interpretar** coeficientes e significância.
- **Identificar um efeito causal**: escolher entre DiD, IV, RDD, controle sintético, matching.
- Rodar **dados em painel** (efeitos fixos/aleatórios, two-way, painel dinâmico).
- **Clusterizar/robustecer** erros-padrão no nível correto do desenho.
- **Diagnosticar** problemas (endogeneidade, heterocedasticidade, autocorrelação, instrumento fraco) e testar robustez.
- Gerar **código reprodutível** (R/Python/Stata) com tabelas publication-ready.

**Quando NÃO usar:** previsão/modelagem de séries temporais macro (ARIMA, VAR/SVAR, cointegração/VECM), nowcasting e dados macro → skill **macroeconomics**; backtest de estratégia de trading → skill **backtest**/**crypto**; modelagem financeira de 3 demonstrações → **financial-modeling**.

## Princípios
1. **Identificação antes de estimação.** Pergunte sempre: *qual é a fonte de variação exógena?* Sem isso, o coeficiente é só correlação.
2. **O desenho dita o estimador**, não o contrário. Aleatorização > descontinuidade/IV > seleção em observáveis (matching/controles) > correlação simples.
3. **Erro-padrão no nível da atribuição do tratamento** (cluster). SE errado → inferência errada, mesmo com ponto estimado certo.
4. **Endogeneidade é a regra, não a exceção** (variável omitida, simultaneidade, erro de medida, seleção). Nomeie a ameaça específica.
5. **Robustez > significância.** Um efeito que só aparece numa especificação não é um efeito. Reporte pré-tendências, placebos, especificações alternativas.
6. **TWFE com tratamento escalonado é viesado** (Goodman-Bacon, de Chaisemartin-D'Haultfœuille); use estimadores robustos (`sunab`, Callaway-Sant'Anna).

## Roteiro
1. **Formule a pergunta causal** e a unidade de observação; declare a **ameaça à identificação** — ver `references/foundations.md`.
2. **Escolha a estratégia** (DiD, IV, RDD, sintético, matching) pelo desenho disponível — `references/causal-inference.md`.
3. **Estruture os dados** (cross-section vs painel; balanceado?) e o **modelo** (FE/RE, two-way) — `references/panel-data.md`.
4. **Estime** com SE corretos e **rode os diagnósticos** da estratégia (1ª-fase F, pré-tendências, densidade) — `references/diagnostics.md`. Se $y$ for binário/contagem/censurado → `references/limited-dependent-variables.md`.
5. **Implemente** em R/Python/Stata e exporte tabelas/figuras — `references/tooling.md`.
6. **Robustez**: especificações alternativas, placebos, sensibilidade a clustering.

## Formato da saída
1. **Estratégia de identificação** em uma frase (fonte de variação exógena + ameaça principal).
2. **Especificação** (equação, fixed effects, nível de cluster) e por que cada escolha.
3. **Resultado**: coeficiente-chave, SE/IC, interpretação econômica (magnitude, não só sinal/estrelas).
4. **Diagnósticos** da estratégia (ex.: F de 1ª fase >10 p/ IV; gráfico de pré-tendências p/ DiD).
5. **Robustez** e ameaças remanescentes.
6. **Código** reprodutível (pacote idiomático) + premissas explícitas.

## Documentos de apoio
- `references/foundations.md` — modelo linear, hipóteses de Gauss-Markov, inferência, erros-padrão robustos/clusterizados, viés de variável omitida, MLE/logit-probit.
- `references/causal-inference.md` — potential outcomes, DiD/event study (+ problema do TWFE escalonado), IV, RDD, controle sintético, matching/PSM. **Núcleo da skill.**
- `references/panel-data.md` — within/between, efeitos fixos vs aleatórios (Hausman), two-way FE, painel dinâmico (Arellano-Bond/Blundell-Bond), clustering.
- `references/limited-dependent-variables.md` — logit/probit e efeitos marginais (AME), LPM, contagens (Poisson/NB/PPML), censura (Tobit), seleção (Heckman), multinomial/ordenado, painel não-linear.
- `references/diagnostics.md` — heterocedasticidade, autocorrelação, multicolinearidade, especificação (RESET), endogeneidade (Hausman/Durbin-Wu), instrumento fraco, testes de sobre-identificação.
- `references/tooling.md` — receitas idiomáticas em R (`fixest`), Python (`linearmodels`/`statsmodels`) e Stata (`reghdfe`/`ivreg2`); tabelas com `modelsummary`/`esttab`.
- `references/worked-example.md` — um DiD com efeitos fixos two-way e event study, validado em código (TWFE recupera o DiD das médias), com `scripts/did-check.py`.
