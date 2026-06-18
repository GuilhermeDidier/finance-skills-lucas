# Technical Calculations — Q&A de Cálculo (estilo entrevista)

> Fonte: 400 Questions IB Interview Guide (2025), seções de *Calculations*. Os problemas de cálculo rápidos que bancos pedem (mental math). As mecânicas completas vivem nas skills profundas; aqui é o treino de resposta rápida. Tax = 25% por padrão (média de países desenvolvidos — confirme).

## A. Accounting — walk-throughs das 3 demonstrações
**Método (sempre nesta ordem):** 1) DRE → 2) DFC (incluindo deferred taxes) → 3) Balanço (e **por que fecha**). Pergunte se querem mudança **única** ou **combinada** (ex.: emitir dívida vs emitir dívida + juros + amortização no ano).

**1) Contrata funcionário a $100K/ano (OpEx):**
- DRE: OpEx +100 → pré-imposto −100 → **NI −75**.
- DFC: NI −75, sem outros → caixa **−75**.
- Balanço: caixa −75 (ativo); equity −75 (lucros retidos) → fecha. Intuição: gastou 100, economizou 25 de imposto.

**2) Depreciação CAI $10** (a pegadinha do clássico invertido):
- DRE: pré-imposto +10 → **NI +7,5**.
- DFC: NI +7,5, mas add-back de depreciação é **$10 menor** → caixa **−2,5**.
- Balanço: caixa −2,5 e PP&E +10 → ativos +7,5; equity +7,5 → fecha. Intuição: perde $2,5 de benefício fiscal.

**3) Vende fábrica de book $100 por $140** (ganho realizado $40):
- DRE: ganho +40 → **NI +30**.
- DFC: NI +30; **reverte o ganho de 40 no CFO**; em CFI entra o **total de proceeds +140** → caixa = +30 − 40 + 140 = **+130**.
- Balanço: caixa +130, PP&E −100 (book) → ativos +30; equity +30 (NI) → fecha.
> Regra do ganho/perda de ativo: o **ganho** sai do lucro mas é **revertido no CFO** (não é caixa operacional); os **proceeds inteiros** entram no **CFI**.

## B. Merger — accretion/dilution na cabeça
**Atalho:** accretive se **Weighted Cost of Acquisition < Yield do Seller** (= NI / Purchase Equity Value). Custo do stock = 1/(P/E do comprador); custo da dívida/caixa = taxa × (1−t).

**1) 100% stock, mental math:** A: 10 ações @ $25, NI $10 (EPS $1,00). Compra B por $150 (NI $10), tax 25%.
- Ações emitidas = 150/25 = 6 → total 16. Combined NI = 10+10 = 20. **Combined EPS = 20/16 = $1,25 → +25% accretive.**

**2) Mesmo deal, 100% cash vs 100% debt** (caixa 4%, dívida 10%):
- After-tax cash = 4%×0,75 = 3%; after-tax debt = 10%×0,75 = 7,5%. Yield do Seller = 10/150 = **6,7%**.
- **Cash: accretive** (3% < 6,7%); **Debt: dilutive** (7,5% > 6,7%).

**3) Mix 1/3-1/3-1/3:** A P/E 11x, debt 8%, cash 4%, t 25%; compra B a purchase P/E 20x.
- Custo stock = 1/11 ≈ 9%; debt = 6%; cash = 3%. Weighted = (9+6+3)/3 = **6%**. Yield B = 1/20 = 5%. **6% > 5% → dilutive.**

**4) Que taxa de dívida torna dilutivo?** A P/E 20x compra B a P/E 10x, 100% dívida.
- Yield B = 1/10 = 10% → after-tax cost of debt > 10% para diluir → pré-imposto > 10%/0,75 = **~13,3%**. Como ninguém paga 13%, 100% dívida quase sempre é accretive.

**5) Quanta sinergia p/ virar accretive?** A: equity $2.000, NI $200 (P/E 10x → cost stock 10%). B: purchase equity $1.200, NI $100 (purchase P/E 12x → yield 8,3%). 100% stock.
- Sem sinergia: levemente dilutivo. Yield de B precisa passar de 10% → NI de B > $120 → precisa de **$20 de sinergia after-tax** (≈ **$27 pré-imposto** a 25%).

> **Regras de combinada:** Combined Equity Value = Equity do A + valor de mercado das ações emitidas. Combined EV = EV do A + Purchase EV do alvo. Múltiplos de EV combinados ficam **entre** os do comprador e os de compra do alvo. (Mecânica completa → skill **mna-modeling**.)

## C. LBO — IRR/MOIC na cabeça
**Rules of thumb (decore):**
| MOIC | 3 anos | 5 anos |
|---|---|---|
| **2x** | ~25% IRR | ~15% IRR |
| **3x** | ~45% IRR | ~25% IRR |

**1) IRR de um deal:** EBITDA $100, 10x → EV $1.000; 60% dívida ($600), 40% equity (**$400**). Sai com EBITDA $150 × 9x = **$1.350**; repaga $250 de dívida → restam $350. Equity proceeds = 1.350 − 350 = **$1.000**. MOIC = 1.000/400 = **2,5x** → entre 2x(15%) e 3x(25%) em 5 anos → **~20% IRR**.

**2) Exit multiple p/ 25% IRR:** compra 12x, 5x dívida/EBITDA, EBITDA $100→$200, sem repagamento. EV compra $1.200 (dívida $500, equity **$700**). 25% em 5 anos = **triplicar** → proceeds $2.100. Sem repagamento → Exit EV = $2.100 + $500 = $2.600 → exit multiple = 2.600/200 = **13x**.

**3) Com 75% da dívida repaga:** restam $125. Proceeds $2.100 → Exit EV = 2.100 + 125 = $2.225 → 2.225/200 = **~11x**.

**4) Quanto de dívida foi repaga?** IRR 20% em 5 anos ≈ MOIC 2,5x. Compra EBITDA $100×10x = $1.000, dívida 5x = $500, equity **$500**. Proceeds = 500×2,5 = $1.250. Exit EV = $150×11x = $1.650 → net debt no exit = 1.650 − 1.250 = $400 → repagou **$100** (de $500).

> Método: ache o equity de entrada (EV − dívida); aplique a regra MOIC↔IRR para os proceeds-alvo; o exit EV = proceeds + dívida no exit; resolva para a incógnita. (Mecânica completa → skill **lbo-modeling**.)

## D. Dica de execução em entrevista
Vá devagar e **declare cada passo** (entrada → exit → proceeds). Use as rules of thumb para evitar conta de IRR na mão. Se pedirem precisão, diga a faixa e ofereça o cálculo exato. O avaliador quer ver o **método**, não decoreba.
