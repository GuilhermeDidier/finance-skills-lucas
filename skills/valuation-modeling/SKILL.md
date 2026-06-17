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
- Valuar empresas **difíceis**: alto crescimento, jovens, prejuízo, tech/intangível pesado, ou em **mercado emergente/Brasil** (ver `references/growth-and-emerging-markets.md`).
- Decompor criação de valor (**ROIC × crescimento**, economic profit) e entender o que um múltiplo embute (ver `references/value-drivers.md`).

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

### Passo 1 — Mecânica: Equity Value, Fully Diluted Shares e EV
Fixe a base antes de qualquer múltiplo (ver `references/mechanics.md`):
- **Fully diluted shares:** basic + opções/warrants in-the-money via **TSM** + converts in-the-money (if-converted ou NSS). Não pule isso.
- **Enterprise Value bridge:** Equity + Total Debt + Preferred + Minority Interest − Excess Cash (+ pensão/leases debt-like).
- **Regra de coerência:** múltiplo com EV no numerador exige métrica pré-juros embaixo (Sales/EBITDA/EBIT); equity value usa pós-juros (Net Income/EPS).

### Passo 2 — DCF (técnica primária na maioria dos casos)
Siga o processo de 5 passos e use as fórmulas de `references/dcf.md` e `references/wacc-capm.md`:
1. Projete o **UFCF** (5–10 anos). **Decomponha o crescimento em ROIC × investment rate** (não só "receita +X%") e cheque se a empresa cria valor hoje (ROIC vs WACC) — ver `references/value-drivers.md`. Se o forecast cresce rápido, considere horizonte mais longo (cliff problem). **Empresa de alto crescimento/jovem/sem lucro:** use o caminho receita → margem-alvo → sales-to-capital de `references/growth-and-emerging-markets.md`.
2. Calcule o **WACC** sobre a **estrutura de capital-alvo** (não a atual por default). CAPM para re; delever/relever beta a partir de comps; some **size premium** (small/mid cap) e **country risk premium** se for EM/Brasil. **Consistência de moeda:** FCF e WACC na mesma moeda.
3. **Terminal value** pelos dois métodos (exit multiple **e** perpetuidade) e **cheque a equivalência** (g implícito vs múltiplo implícito).
4. **Present value** (use mid-year convention quando fizer sentido).
5. **Ajustes** → EV para equity value → valor por ação (diluído).
6. **Rode sensibilidade** (tabela 2-D) em vendas, margens, WACC e terminal value.
7. **Cheque o ROIIC / value driver formula** — se o ROIC implícito no terminal value >> WACC para sempre, exige moat; senão as premissas estão furadas. Cross-check com economic profit (`value-drivers.md`). Este passo é obrigatório.

### Passo 3 — Trading Comps
Selecione 1–2 comps realmente bons (mesma natureza de negócio). Antes de calcular múltiplos, faça a **mecânica** (ver `references/mechanics.md`): **LTM** (prior FY + current stub − prior stub), **calendarização** ao mesmo CY end, e **scrubbing** dos não-recorrentes (Adjusted EBITDA/EBIT/EPS). Só então calcule EV/EBITDA, EV/EBIT, P/E, PEG (forward) e impute valor.

### Passo 4 — Transaction Comps (só se for valuation para venda/aquisição)
Transações de M&A na indústria (janela ~5 anos). Captura control premium. **Não use fora desse contexto.**

### Passo 4.5 — LBO como "floor" (quando relevante)
Em situações de sponsor/take-private, a análise de LBO define um **piso de valuation** (o máximo que um financial sponsor pagaria para atingir o IRR-alvo). Detalhe → skill **lbo-modeling**; aqui entra como uma das faixas do football field quando aplicável.

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

> 💡 Para um caso completo de referência (mecânica → DCF → comps → football field, com toda a aritmética fechando), veja `references/worked-example.md`.

## Documentos de apoio
- `references/worked-example.md` — caso end-to-end "ExemploCo" amarrando tudo, com sanity checks (equivalência TV, ROIIC) e football field.
- `references/mechanics.md` — grunt work: fully diluted shares (TSM, if-converted, NSS), EV bridge, LTM, calendarização, scrubbing de não-recorrentes, nota IFRS 16.
- `references/dcf.md` — DCF completo: UFCF, terminal value (ambos métodos), equivalência, ROIIC, ajustes, sum-of-the-parts, sinergias, sensibilidade, calibração de g em juro alto/BRL.
- `references/wacc-capm.md` — WACC, CAPM, cost of debt/equity, beta delever/relever; camada avançada (target structure, size premium, country risk premium Damodaran, predicted beta, sensibilização).
- `references/comparables.md` — EV vs equity, trading & transaction comps, múltiplos, imputação, minority interest, múltiplos como atalho de DCF + intangíveis (Mauboussin).
- `references/value-drivers.md` — criação de valor (ROIC × crescimento), value driver formula, economic profit (EVA), conservation of value, o que os múltiplos escondem. (McKinsey/Koller + Mauboussin)
- `references/growth-and-emerging-markets.md` — valuar alto crescimento/jovens/sem-lucro/intangível e mercados emergentes; country risk premium e consistência de moeda. (Damodaran)
- `references/moat.md` — sustentabilidade do ROIC (spread ROIC−WACC), competitive advantage period, Five Forces, barreiras de entrada, WTP/WTS e checklist — justifica (ou não) o ROIIC/CAP do terminal value. (Mauboussin, Measuring the Moat)
- `references/pitfalls-and-football-field.md` — checklist de pitfalls de comps, "red lights" de sanidade, e como montar o football field (com exemplo real e múltiplos implícitos). (Credit Suisse Handbook)
