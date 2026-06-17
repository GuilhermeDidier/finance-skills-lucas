---
name: lbo-modeling
description: Modela leveraged buyouts (LBO) — estrutura de financiamento por tranches, sources & uses, debt schedule, análise de retornos (IRR, MOIC/cash return), os 3 motores de retorno (debt paydown, EBITDA growth, multiple expansion), e o preço-máximo que um sponsor paga (floor de valuation). Use quando o usuário quiser montar/avaliar um LBO, calcular IRR/MOIC de um buyout, dimensionar dívida vs equity, achar o preço máximo de um financial sponsor, avaliar se uma empresa é bom candidato a LBO, ou entender retornos de private equity. Gatilhos: "LBO", "leveraged buyout", "buyout", "private equity", "sponsor", "IRR", "MOIC", "cash return", "alavancagem", "dividend recap", "financial buyer", "preço máximo".
---

# LBO Modeling

Skill para modelar leveraged buyouts no padrão de private equity / IB. Pergunta central: **dado um preço e uma estrutura de dívida, o sponsor atinge o IRR-alvo no exit?** — e, invertendo, **qual o preço máximo** que ele pode pagar. Constrói-se sobre o 3-statement (financial-modeling) e conecta com valuation (floor) e mna (financial buyer).

## Quando usar
- Montar/avaliar um **LBO model** (entrada, hold, exit).
- Calcular **IRR e MOIC** de um buyout.
- Dimensionar **dívida vs equity** e a pilha de capital (tranches).
- Achar o **preço máximo** de um financial sponsor (floor de valuation).
- Avaliar se uma empresa é **bom candidato** a LBO.
- Analisar **dividend recap** e estratégias de saída.

**Quando NÃO usar:** valuation standalone (DCF/comps) → valuation-modeling; merger/accretion-dilution (strategic buyer) → mna-modeling; o 3-statement em si → financial-modeling.

## Princípios inegociáveis
1. **IRR é a métrica primária** (threshold típico 15–20% em ~5 anos); MOIC complementa (não considera tempo).
2. **Retorno vem de 3 motores:** debt paydown, EBITDA growth, multiple expansion. Os dois primeiros são sólidos; **multiple expansion é otimista** — não conte com ele no base case.
3. **Alavancagem amplifica retorno E risco.** Menos equity = IRR maior, mas caixa mais apertado.
4. **O caixa tem que servir a dívida** em todos os anos (stress-test obrigatório).
5. **Equity é o plug** do sources & uses, depois de definir quanta dívida o negócio aguenta.
6. **Bom candidato** = caixa forte e previsível, posição defensável, baixo capex, base de ativos, management provado.

## Workflow (5 passos — Rosenbaum)
1. **Reunir informação** — financials, projeções, capital de mercado de dívida alcançável, tese.
2. **Pre-LBO model** — projetar o alvo standalone (3-statement; skill financial-modeling).
3. **Input da transação** — purchase price (múltiplo × EBITDA), **sources & uses** (dívida por tranche + equity plug + fees), purchase accounting, link ao balanço pro forma.
4. **Post-LBO model** — **debt schedule** (juros, mandatório + cash sweep, revolver, circularidade), pro forma IS/BS/CF.
5. **Returns analysis** — EV de saída (múltiplo × EBITDA exit) → equity de saída (− dívida líquida) → **IRR e MOIC**; sensibilidade 2-D; **value creation bridge**.

Ver detalhes em `references/lbo-model-build.md`.

## Para achar o preço máximo
Inverta: fixe o **IRR-alvo** e o exit (múltiplo/ano) e resolva para o **preço de entrada máximo**. Esse é o **floor** no football field (valuation-modeling) e o lance do financial buyer (mna-modeling).

## Formato da saída
1. **Veredito:** IRR e MOIC vs threshold; o deal funciona?
2. **Sources & Uses:** dívida por tranche, equity, alavancagem (Debt/EBITDA).
3. **Returns:** IRR, MOIC, e **value creation bridge** (quanto de cada motor).
4. **Sensibilidade:** IRR/MOIC vs múltiplo de entrada/saída, alavancagem, ano de exit.
5. **Stress-test:** a empresa serve a dívida no downside? Covenants ok?
6. **Preço máximo** para o IRR-alvo (se relevante).

Sempre mostre o bridge (de onde vem o retorno) e sensibilize entrada/saída/alavancagem.

## Documentos de apoio
- `references/lbo-fundamentals.md` — o que é LBO, candidato ideal, participantes, estratégias de saída (sale/IPO/dividend recap).
- `references/lbo-economics.md` — IRR, MOIC/cash return, os 3 motores de retorno, efeito da alavancagem, value creation bridge.
- `references/financing-structure.md` — pilha de capital (revolver→TLB→bonds→mezz→equity), níveis de alavancagem, sources & uses.
- `references/lbo-model-build.md` — os 5 passos de build, link ao debt schedule e ao preço-máximo.
- `references/worked-example.md` — LBO da AlvoCo: IRR ~22%, MOIC 2,73x, value bridge e sensibilidade.

> 🔗 Debt schedule/circularidade → skill financial-modeling. Floor de valuation → valuation-modeling. Financial buyer → mna-modeling. Purchase accounting → mna-modeling.
