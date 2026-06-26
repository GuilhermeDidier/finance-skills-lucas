# Worked example — DiD com event study (ponta a ponta)

> Caso fictício, números fechando na mão. Substituível por dado real depois. Objetivo: mostrar o fluxo **identificação → estimação → diagnóstico → leitura**.

## Cenário
Em 2018, **6 estados** (grupo de tratamento) adotaram um incentivo fiscal a startups; **6 estados** não adotaram (controle). Temos emprego em tech (`emp`, em milhares) por estado-ano, 2015–2021. Pergunta: **o incentivo aumentou o emprego em tech?**

- Identificação: **DiD**. Fonte de variação exógena = timing da adoção (assumimos não correlacionado com choques de tendência do emprego).
- Ameaça principal: **tendências paralelas** — e se estados que adotaram já estivessem crescendo mais rápido? → checamos com **pré-tendências**.

## Passo 1 — DiD 2×2 na mão (médias)

|  | Pré (2015–17, média) | Pós (2019–21, média) | Δ |
|---|---|---|---|
| Tratados | 50,0 | 62,0 | **+12,0** |
| Controles | 48,0 | 54,0 | **+6,0** |

$$\hat\delta_{DiD} = (62{-}50) - (54{-}48) = 12 - 6 = \mathbf{+6{,}0 \text{ mil empregos}}$$

Leitura: o incentivo está associado a **+6 mil empregos** acima do que teria acontecido seguindo a tendência dos controles. (O efeito "bruto" pós-tratamento de +14 vs controle seria errado — ignora que tratados já partiam de nível maior; o +12 antes-depois do tratado seria errado — ignora a tendência comum de +6.)

## Passo 2 — Regressão TWFE

$$emp_{it} = \alpha_i + \lambda_t + \delta\,(Trat_i\times Pós_t) + \varepsilon_{it}$$

```r
library(fixest)
m <- feols(emp ~ i(trat_post) | estado + ano, data = df, cluster = ~estado)
# δ̂ ≈ 6.0 (SE clusterizado por estado)
```
Como a adoção foi **simultânea** (todos em 2018), o TWFE simples é válido aqui. *Se* fosse escalonada (estados adotando em anos diferentes), trocaríamos por `sunab()`/Callaway-Sant'Anna (ver `causal-inference.md`).

## Passo 3 — Event study (pré-tendências + dinâmica)

$$emp_{it} = \alpha_i+\lambda_t+\sum_{k\ne 2017}\gamma_k\mathbb{1}(ano=k)\times Trat_i+\varepsilon_{it}$$

Coeficientes $\hat\gamma_k$ (ref. = 2017) — **valores recuperados pelo código** (painel calibrado, cluster por estado):

| Ano | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 |
|---|---|---|---|---|---|---|---|
| $\hat\gamma_k$ | −0,03 | −0,23 | 0 (ref) | +2,29 | +4,58 | +6,23 | +7,26 |
| signif. (5%) | não | não | — | sim | sim | sim | sim |

- **Pré-tratamento (2015–16) ≈ 0 e não-significante** → sustenta tendências paralelas. ✔️
- **Pós cresce gradualmente** (+2,3 → +7,3): efeito acumula com o tempo, coerente com adoção de política.

```r
es <- feols(emp ~ i(ano, trat, ref = 2017) | estado + ano, df, cluster = ~estado)
iplot(es, main = "Event study: emprego tech")
```

> ✅ **Validado em código** (`scripts/did-check.py`, statsmodels): o painel sintético calibrado reproduz o 2×2 (tratado 49,7→61,7; controle 48,0→53,9) e o **TWFE recupera δ̂ = 6,11** (= DiD das médias). O event study recupera as pré-tendências nulas e a rampa pós-tratamento acima. *Aviso:* aqui o SE é minúsculo (ruído baixo, p/ a aritmética fechar); **com ruído realista o SE cresce** e vale o alerta de poucos clusters (12 < 40 → wild bootstrap).

## Passo 4 — Diagnóstico e robustez
- **Clustering:** por estado (nível da atribuição) — 12 clusters é **pouco** (<40): reporte **wild cluster bootstrap** (`fwildclusterboot`/`boottest`) para o p-valor de $\delta$.
- **Placebo temporal:** finja tratamento em 2016 → efeito deve ser ≈0 (e é: pré-tendências nulas confirmam).
- **Placebo de grupo:** atribua tratamento a controles aleatórios → distribuição de efeitos centrada em 0.
- **Sensibilidade:** dropar um estado por vez (o resultado não pode depender de 1 unidade).

## Passo 5 — Leitura final (formato de saída da skill)
1. **Identificação:** DiD, variação = adoção do incentivo em 2018; ameaça = tendências paralelas, sustentada por pré-tendências nulas.
2. **Especificação:** TWFE (estado + ano FE), cluster por estado; event study para dinâmica.
3. **Resultado:** **+6 mil empregos** (≈ +12% sobre a base de 50 mil), crescendo de +2,1 (ano 1) a +7,0 (ano 3).
4. **Diagnóstico:** pré-tendências ≈0; wild bootstrap por poucos clusters; placebos ok.
5. **Robustez/ressalvas:** efeito **local** a esses estados/período; não captura migração de empregos de outros estados (efeito líquido nacional pode ser menor).

## Reprodutibilidade
Script `scripts/did-check.py` (statsmodels): gera o painel calibrado, calcula o DiD 2×2, roda o TWFE com cluster por estado e o event study com dummies de ano relativo. Dependências: `statsmodels`, `pandas`, `numpy`.

## A enriquecer (roadmap)
- [x] Validar a aritmética/código (TWFE = 2×2; event study com pré-tendências). ✅
- [ ] Versão com dados reais (RAIS/CAGED por UF, ou painel internacional).
- [ ] Versão escalonada para demonstrar Bacon/Sun-Abraham na prática.
- [ ] Output real do `fixest` + figura do event study.
