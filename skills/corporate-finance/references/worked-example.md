# Exemplo trabalhado — Decisão de Capital Allocation

> A empresa gerou **$500M de FCF** e o CEO precisa decidir o que fazer. WACC = 10%. Mostra a régua "ROIC vs custo de capital + preço vs valor". Valores em $ milhões.

## As 5 opções na mesa
| Opção | Detalhe |
|---|---|
| A) Reinvestir organicamente | $500M em projetos com ROIC esperado de **18%** |
| B) Adquirir um concorrente | $500M por um alvo que gera **$40M de NOPAT** (ROIC 8%) |
| C) Recomprar ações | ação negocia a **$40**, valor intrínseco (DCF) **$50** |
| D) Dividendo especial | devolver $500M |
| E) Pagar dívida | dívida a 6% pré-imposto (4,5% após imposto, t=25%) |

## Quantificando a criação de valor (economic profit perpétuo)
Valor criado ≈ Investimento × (ROIC − WACC) / WACC

**A) Reinvestir a 18%:**
```
EP anual = 500 × (18% − 10%) = $40 → PV = 40 / 0,10 = +$400M criados
```
✅ Maior criação de valor. Reinveste enquanto houver projetos com ROIC > WACC.

**B) Aquisição a ROIC 8%:**
```
EP anual = 500 × (8% − 10%) = −$10 → PV = −10 / 0,10 = −$100M destruídos
```
❌ Destrói valor — e ainda **antes** do prêmio de controle (que pioraria). "Comprar receita" abaixo do custo de capital queima dinheiro.

**C) Recompra com ação barata (preço $40 < valor $50):**
```
Ações recompradas = 500 / $40 = 12,5M
Valor intrínseco do que comprou = 12,5M × $50 = $625M
Ganho p/ acionistas que ficam = 625 − 500 = +$125M criados
```
✅ Cria valor porque compra $1 de valor por $0,80. (Se a ação estivesse a $60 > $50, **destruiria** valor.)

**D) Dividendo especial:** devolve caixa; neutro a preço. Bom se não há projeto com ROIC > WACC e a ação não está barata. ~$0 de valor criado/destruído (além de impostos do investidor).

**E) Pagar dívida (4,5% após imposto):** reduz risco; por *conservation of value*, ~neutro em valor puro (a menos que reduza risco de distress materialmente).

## Ranking e decisão
```
A (+400)  >  C (+125)  >  E (~0) ≈ D (~0)  >  B (−100)
```
**Decisão disciplinada:** priorizar **reinvestimento orgânico** (maior valor), depois **recomprar** (ação subvalorizada), **evitar** a aquisição que destrói valor. Se faltassem projetos com ROIC > WACC e a ação estivesse a fair value, a resposta seria devolver caixa (dividendo/buyback).

## A lição (os 5 princípios em ação)
- **Zero-based:** avaliar todas as opções de novo, não repetir o do ano passado.
- **ROIC > WACC** decide reinvestimento e M&A.
- **Preço vs valor** decide recompra.
- **Não destruir valor** com M&A "estratégico" que não cobre o custo de capital.
- A pior resposta comum na prática: fazer a aquisição (B) por "crescimento", destruindo $100M+ — exatamente o erro que [[mna-modeling]] e a disciplina de capital allocation existem para evitar.
