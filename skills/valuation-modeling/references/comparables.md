# Comparables — Trading Comps e Transaction Comps (referência detalhada)

> Fonte: Merrill Lynch IBD Analyst Training — Valuation Overview (2007).

## Equity Value vs Enterprise Value (a base de tudo)
- **Equity Value** = valor para os "donos" após dívida e preferred. ≈ Shares Outstanding × Preço.
- **Enterprise Value (EV)** = valor de todo o capital investido:
  ```
  EV = Market Value of Equity + Minority Interest + Preferred Stock + Net Debt
  Net Debt = Short-Term Debt + Long-Term Debt + Capitalized Leases − Excess Cash
  ```
- **Regra de coerência numerador/denominador:** múltiplo com dívida no numerador (EV) exige métrica **antes dos juros** no denominador (EBITDA, EBIT, Sales). P/E usa equity em cima e net income embaixo.

---

## 1) Trading Comps (Publicly-Traded Comparable Companies)
Compara estatísticas operacionais e de trading de empresas similares. Dá o **"public market value"** (investimento minoritário e passivo).

### Por que usar
- Benchmark via empresas similares; capta info de um mercado eficiente; revela múltiplos-chave da indústria.

### O que faz uma empresa ser comparável
- **O mais importante: a natureza do negócio.** Mesma indústria? Mesmos tipos de cliente, produtos e drivers econômicos?
- Tamanho, crescimento e margens importam, mas não isoladamente.
- Melhor focar **1–2 comps realmente bons** do que 6–8 mais ou menos. Exclua outliers; use bom senso.

### Múltiplos principais
| Enterprise Value | Equity Value |
|---|---|
| EV/EBITDA | P/E (Price/EPS) |
| EV/EBIT | PEG (P/E ÷ crescimento) |
| EV/Revenues | P/Book |
| EV/métrica (subscribers, barris…) | |

**Quais usar?** Todos — são fáceis de calcular. Enfatize **P/E, EV/EBITDA, EV/EBIT e PEG**, e foque em múltiplos **forward** (preço atual ÷ EPS/EBITDA projetado).
- EBIT costuma ser melhor proxy de FCF que EBITDA (capex > depreciação na maioria), mas EBITDA é mais usado — olhe os dois.
- EV/Revenues: só quando não há lucro/EBITDA (empresas jovens). Ignora rentabilidade.
- **PEG:** PE forward ÷ (crescimento de 5 anos × 100). Conceito relativo (S&P ≈ 1.8x). Validade intelectual duvidosa, mas muito usado.
- **P/Book:** o mais frágil; só faz mais sentido em serviços financeiros. Desenfatize.

### Vantagens das razões de EV
- Minimizam efeito de alavancagem entre empresas com estruturas de capital diferentes.
- Eliminam diferenças contábeis de D&A e impostos.

### Limitações honestas
- **E se os comps estiverem errados?** Análise é puramente relativista — assume que os comparáveis estão corretos.
- Ruim para ações thinly traded / small cap / sub-cobertas.
- Mais vulnerável a questões contábeis que o DCF.
- Não foca em FCF; não captura control premium nem sinergias.

### Imputando valores (passo a passo)
1. Multiplique o resultado operacional do alvo pelo múltiplo relevante dos comps (LTM e ano projetado).
2. Múltiplos de **net income / EPS / book** → dão direto **equity value**.
3. Múltiplos de **Sales / EBITDA / EBIT** → dão **enterprise value** → subtraia Net Debt para chegar a equity.
4. Valor por ação = equity value ÷ diluted shares (em M&A, ajuste net debt por conversíveis e proceeds de opções/warrants).

**Fórmulas de valor implícito por ação:**
```
EPS:    Target EPS × múltiplo
EBIT:   (múltiplo × Target EBIT − Net Debt) / Shares
EBITDA: (múltiplo × Target EBITDA − Net Debt) / Shares
Sales:  (múltiplo × Target Sales − Net Debt) / Shares
```

**Exemplo (Rookie Enterprises):** Dec-98 EPS $3.31 × 8.7x = **$28.80/ação**. LTM EBITDA $87M × 6.2x = $539.4M − Net Debt $88M = $451.4M ÷ 14.6M ações = **$30.92/ação**.

### Multiplos forward — timing
Investidores rolam o ano-base na primavera. Ex.: por maio/2007 já olham Preço/EPS 2008. Use o ano que o mercado está precificando.

### Trading Comps × DCF (prós e contras)
| | Prós | Contras |
|---|---|---|
| **Trading Multiples** | Fácil; sem terminal value; capta mercado eficiente; bom crosscheck | Comps puros raros; distorção contábil; não foca em caixa; esconde premissas do mercado |
| **DCF** | Dirigido por caixa; teoricamente correto; foco explícito no futuro do negócio | Sensível a WACC e TV; range amplo de forecasts |

---

## 2) Transaction Comps (Comparable Acquisition Transactions)
Transações de M&A na mesma indústria. Dá o **"private market value" / control value** — captura o **control premium** pago.

### Características
- Ainda mais difícil achar comparáveis verdadeiros.
- Janela típica: **5 anos** (complica — juros e bolsa variam muito no tempo).
- Anote: status (Completed/Pending/Withdrawn), consideração (Cash vs Stock), Hostile vs Friendly.

### Objetivos
- Medir **private market value (control value)**.
- **Não** captura diretamente o valor das sinergias (o principal driver econômico do M&A).
- Entender atividade de M&A da indústria: quem compra, o quê (share, tecnologia), quanto pagam.

> ⚠️ **Não confie em transaction comps a não ser que você esteja valorando a empresa exatamente para esse fim (uma venda/aquisição).**

### Fatores que influenciam o preço pago
Número de compradores, sinergias, alternativas de target, competição entre investidores, valores de DCF, comps, governança, estrutura da transação, questões fiscais/contábeis/legais.

---

## Imputando múltiplos (cross-check após DCF)
Depois de ter um range de valores por várias metodologias, calcule os **múltiplos implícitos** para checar se o preço faz sentido:
```
EPS:    Valor por ação / Target EPS
EBIT:   (Valor/ação × Shares + Net Debt) / Target EBIT
EBITDA: (Valor/ação × Shares + Net Debt) / Target EBITDA
Sales:  (Valor/ação × Shares + Net Debt) / Target Sales
```

## Minority interest e equity em afiliadas não-consolidadas
Mantenha numerador e denominador "apples-to-apples":
- **Minority interest:** some ao firm value (numerador); denominador usa resultado consolidado.
- **Equity interest (stake minoritária que você detém):** subtraia do firm value (trate como cash); denominador NÃO inclui a afiliada.
