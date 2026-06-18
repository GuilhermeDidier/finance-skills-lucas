---
name: corporate-finance
description: Cobre as decisões financeiras da empresa — estrutura de capital (Modigliani-Miller, trade-off, pecking order), capital allocation (reinvestir/M&A/dividendos/buybacks/dívida), política de payout, custo de capital, criação de valor (ROIC vs WACC) e a estratégia/vantagem competitiva que sustenta o ROIC (7 Powers, barreiras de entrada, disrupção). Use quando o usuário discutir quanto endividamento ter, o que fazer com o caixa, dividendos vs recompras, se um investimento cria valor, custo de capital, ou a sustentabilidade da vantagem competitiva. Gatilhos: "estrutura de capital", "capital allocation", "alocação de capital", "dividendos", "buyback/recompra", "Modigliani-Miller", "WACC", "ROIC", "criação de valor", "vantagem competitiva", "7 powers", "moat", "pecking order", "payout".
---

# Corporate Finance

Skill para as grandes decisões financeiras da empresa: **como financiar, o que fazer com o caixa, e o que sustenta o valor**. O fio condutor: valor é criado quando **ROIC > custo de capital**, de forma **sustentável** (moat) — e destruído quando se aloca capital abaixo do custo de capital.

## Quando usar
- **Estrutura de capital:** quanta dívida vs equity; estrutura ótima; debt capacity.
- **Capital allocation:** reinvestir, adquirir, pagar dividendo, recomprar, ou amortizar dívida.
- **Política de payout:** dividendos vs buybacks; quando cada um cria valor.
- **Custo de capital** e **criação de valor** (ROIC vs WACC, economic profit).
- **Estratégia/vantagem competitiva:** o que sustenta o ROIC (7 Powers, barreiras, disrupção).

**Quando NÃO usar:** valuation de uma empresa específica → valuation-modeling; modelar uma fusão → mna-modeling; LBO → lbo-modeling. (Esta skill é a teoria/decisão que informa todas elas.)

## Princípios inegociáveis
1. **Valor = ROIC vs custo de capital.** Investir/crescer só cria valor se ROIC > WACC.
2. **Conservation of value:** engenharia financeira (recap, buyback, troca contábil) não cria valor por si — só muda quem fica com fluxos/risco.
3. **Preço ≠ valor** — recomprar cria valor só com ação abaixo do intrínseco.
4. **Estrutura de capital ótima** equilibra tax shield vs custos de distress (não é "máximo de dívida").
5. **Sustentabilidade exige barreira** — ROIC alto sem moat é arbitrado pela concorrência.
6. **Disciplina de alocação** — zero-based, sair de negócios que não criam valor, agir no gap preço/valor.

## Roteiro de análise
1. **Diagnóstico de valor:** a empresa gera ROIC > WACC? Subindo/caindo? (ver `../valuation-modeling/references/value-drivers.md`).
2. **Sustentabilidade:** que Power/barreira sustenta o ROIC? É frágil a disrupção? (`references/strategy-and-power.md` e `../valuation-modeling/references/moat.md`).
3. **Estrutura de capital:** está perto da ótima? Debt capacity, coverage, rating? (`references/capital-structure.md`).
4. **Capital allocation:** ranqueie os usos do caixa por valor criado (reinvestir > M&A > buyback/dividendo > dívida, conforme ROIC e preço/valor) (`references/capital-allocation.md`).
5. **Payout:** dividendo vs buyback dado preço/valor, sinalização e estabilidade do caixa (`references/payout-policy.md`).

## Formato da saída
1. **Diagnóstico:** cria ou destrói valor hoje (ROIC vs WACC) e por quê.
2. **Sustentabilidade:** o moat/Power e os riscos (disrupção).
3. **Recomendação de estrutura de capital** (com a lógica trade-off).
4. **Capital allocation ranqueada** por valor criado, com números.
5. **Payout** recomendado e justificativa.

Sempre quantifique a criação de valor (economic profit / NPV) e seja explícito sobre premissas.

## Documentos de apoio
- `references/capital-structure.md` — Modigliani-Miller (I/II, com impostos), trade-off, custos de distress, pecking order, estrutura ótima/WACC. (Strategic Issues + McKinsey)
- `references/capital-allocation.md` — o menu de usos do caixa, régua ROIC vs WACC, 5 princípios, disciplina de buyback. (Mauboussin Capital Allocation + McKinsey)
- `references/payout-policy.md` — dividend irrelevance (MM), Gordon, Lintner (smoothing), dividendos vs buybacks, sinalização e impostos.
- `references/strategy-and-power.md` — 7 Powers (benefit+barrier), barreiras de entrada (Greenwald), disrupção (Christensen). (7 Powers + Competition Demystified + Innovator's Dilemma)
- `references/worked-example.md` — decisão de capital allocation com 5 opções e o valor criado por cada uma.

> 🔗 Reaproveita `value-drivers.md` e `moat.md` da skill valuation-modeling. Conecta com lbo-modeling (debt capacity) e mna-modeling (disciplina de M&A).
