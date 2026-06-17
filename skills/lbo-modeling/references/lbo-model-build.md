# Construindo o LBO Model (passo a passo)

> Fonte: Rosenbaum & Pearl, Cap. 5 (LBO Analysis). O processo de montar o modelo do sponsor.

## Os 5 passos (Rosenbaum)
### Step I — Reunir e analisar a informação
Financials históricos, projeções de management, estrutura de capital atual, dados de comps/mercado de dívida (leverage e pricing alcançáveis), e a tese (crescimento, eficiência, exit).

### Step II — Pre-LBO Model (standalone)
Projete o alvo standalone (3-statement; ver skill financial-modeling): receita, margens, EBITDA, capex, NWC, FCF. É a base operacional sobre a qual a estrutura de LBO é aplicada.

### Step III — Input da estrutura da transação
- **Purchase price:** múltiplo de entrada × EBITDA → Enterprise Value de compra.
- **Sources & Uses:** define a dívida (por tranche, dentro do que o negócio aguenta e os lenders aceitam) e o **equity do sponsor como plug**. Inclua fees (transaction + financing). Ver `financing-structure.md`.
- **Link ao balanço pro forma:** purchase accounting (goodwill, write-ups, DTL — mesma lógica da skill mna-modeling), nova estrutura de capital, eliminação do equity antigo.

### Step IV — Post-LBO Model (debt schedule + pro forma)
- **Debt schedule:** saldos por tranche, juros (SOFR+spread / cupom fixo), repagamentos mandatórios + **cash sweep** opcional, revolver como válvula. (Mecânica e **circularidade** → skill financial-modeling, `references/debt-schedule.md`.)
- Complete a DRE pro forma (EBIT → juros → net income), o balanço (dívida e equity) e a DFC (financing).
- **Cash available for debt repayment** alimenta a desalavancagem ano a ano.

### Step V — Returns Analysis
- Calcule o **EV de saída** = múltiplo de saída × EBITDA do ano de exit.
- **Equity de saída** = EV de saída − dívida líquida no exit.
- **MOIC** = equity de saída / equity de entrada; **IRR** dos fluxos de equity.
- **Sensibilidade (2-D):** IRR/MOIC vs múltiplo de entrada, múltiplo de saída, alavancagem e ano de exit.
- **Value creation bridge:** decomponha o ganho em EBITDA growth + multiple expansion + debt paydown (ver `lbo-economics.md`).

## Para achar o preço máximo (uso comum)
Inverta o modelo: fixe o **IRR-alvo** (ex.: 20%) e o múltiplo/ano de saída, e resolva para o **preço de entrada máximo** que ainda atinge o IRR. Esse é o **floor de valuation** no football field e o lance do financial buyer no M&A.

## Checagens
- A empresa serve a dívida em todos os anos (sem caixa negativo; revolver cobre apertos)?
- Covenants respeitados (leverage e coverage)?
- O retorno depende demais de multiple expansion (frágil) ou vem de desalavancagem/crescimento (sólido)?
- Sources = Uses; balanço pro forma fecha.
