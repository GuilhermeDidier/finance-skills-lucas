---
name: valuation-modeling
description: Avalia quanto vale uma empresa usando as metodologias de Investment Banking — DCF, trading comps, transaction comps, sum-of-the-parts — e triangula num football field. Use quando o usuário quiser estimar o valor de uma empresa/ativo, montar ou revisar um DCF, escolher e calcular múltiplos, definir WACC/terminal value, sanity-check de um valuation, ou montar o slide de football field. Gatilhos: "quanto vale", "valuation", "DCF", "WACC", "múltiplos", "comps", "terminal value", "football field", "valor por ação", "enterprise value".
---

# Valuation Modeling

Skill para conduzir um valuation completo no padrão de banco de investimento. O princípio que governa tudo: **valuation é uma faixa, não um número** — você triangula várias metodologias e usa julgamento.

## Quando usar
- Estimar o valor de uma empresa (pública ou privada) ou de um ativo.
- Montar, revisar ou criticar um modelo de DCF.
- Selecionar comparáveis e calcular múltiplos (trading e/ou transaction).
- Definir WACC, cost of equity (CAPM), beta, terminal value.
- Sanity-check de um valuation existente (checar premissas implícitas, ROIIC, g).
- Montar o **football field** (resumo visual das faixas por metodologia).

**Quando NÃO usar:** modelagem de fusão/accretion-dilution → skill de m&a-modeling; construção do 3-statement model → skill de financial-modeling.

## Princípios inegociáveis (leia antes de começar)
1. **Pense em faixa, não em valor único.** Sempre entregue um range.
2. **Olhe pro futuro, não pro passado.** O passado só interessa como guia do futuro.
3. **Triangule.** Nenhuma metodologia sozinha decide. DCF para M&A, comps para IPO.
4. **Trabalhe de trás pra frente.** "O que eu preciso acreditar pra justificar esse valor? É razoável?"
5. **Valor ≠ preço.** Valor é valor; preço é o que se paga. Oportunidade está na divergência.
6. **Não é só número.** Sem entender o negócio e seu ambiente, não há valuation honesto.

## Workflow

### Passo 0 — Enquadrar
Pergunte/defina: **qual o propósito?** (M&A, IPO, fairness opinion, decisão de investimento). Isso decide o peso das metodologias e se transaction comps são aplicáveis. Colete: financials (3–5 anos históricos + projeções), capital structure, shares (diluídas), net debt, setor e comparáveis candidatos.

### Passo 1 — Equity Value vs Enterprise Value
Fixe a base antes de qualquer múltiplo. Ver `references/comparables.md` (seção EV vs Equity). Regra de coerência: múltiplo com EV no numerador exige métrica antes de juros embaixo.

### Passo 2 — DCF (técnica primária na maioria dos casos)
Siga o processo de 5 passos e use as fórmulas de `references/dcf.md` e `references/wacc-capm.md`:
1. Projete o **UFCF** (5–10 anos). Se o forecast cresce rápido, considere horizonte mais longo (o cliff problem).
2. Calcule o **WACC** (CAPM para re; delever/relever beta a partir de comps se preciso).
3. **Terminal value** pelos dois métodos (exit multiple **e** perpetuidade) e **cheque a equivalência** (g implícito vs múltiplo implícito).
4. **Present value** (use mid-year convention quando fizer sentido).
5. **Ajustes** → EV para equity value → valor por ação (diluído).
6. **Rode sensibilidade** em vendas, margens, WACC e terminal value.
7. **Cheque o ROIIC** — se ROIIC implícito >> WACC, as premissas estão furadas. Este passo é obrigatório.

### Passo 3 — Trading Comps
Selecione 1–2 comps realmente bons (mesma natureza de negócio). Calcule EV/EBITDA, EV/EBIT, P/E, PEG (forward). Impute valor multiplicando os resultados do alvo pelos múltiplos. Ver `references/comparables.md`.

### Passo 4 — Transaction Comps (só se for valuation para venda/aquisição)
Transações de M&A na indústria (janela ~5 anos). Captura control premium. **Não use fora desse contexto.**

### Passo 5 — Triangular e montar o Football Field
Junte as faixas (min–max) de cada metodologia num gráfico de barras horizontais, com o preço atual como referência. Calcule os **múltiplos implícitos** de cada faixa para checar razoabilidade. Conclua com uma faixa de valor defensável e o raciocínio.

## Formato da saída
1. **Resumo executivo:** faixa de valor por ação + recomendação em 2–3 linhas.
2. **Football field:** tabela/descrição com a faixa de cada metodologia (DCF perpetuidade, DCF exit multiple, trading comps, transaction comps) e múltiplos implícitos.
3. **DCF:** premissas-chave (WACC, g/exit multiple, margens), valor, e a tabela de sensibilidade.
4. **Comps:** lista de comparáveis, múltiplos e valor implícito.
5. **Sanity checks:** g implícito vs exit multiple, ROIIC vs WACC, valor vs preço de mercado.
6. **Riscos/limitações:** o que mais move o valor e onde estão as fragilidades das premissas.

Sempre declare as premissas explicitamente e prefira faixas a pontos.

## Documentos de apoio
- `references/dcf.md` — DCF completo: UFCF, terminal value (ambos métodos), equivalência, ROIIC, ajustes, sum-of-the-parts, sinergias, sensibilidade.
- `references/wacc-capm.md` — WACC, CAPM, cost of debt/equity, beta delever/relever, exemplos trabalhados.
- `references/comparables.md` — EV vs equity, trading comps, transaction comps, múltiplos, imputação de valores e múltiplos, minority interest.
