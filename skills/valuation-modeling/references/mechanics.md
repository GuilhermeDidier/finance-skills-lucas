# Mecânica de Comps & Valuation (grunt work banker-grade)

> Fonte: Rosenbaum & Pearl, *Investment Banking* (3ª ed.), Cap. 1. É a mecânica braçal que sustenta qualquer comp/DCF feito num banco. O DCF conceitual está em `dcf.md`; aqui é o "como spread" de verdade.

## 1. Equity Value e Fully Diluted Shares
```
Equity Value = Current Share Price × Fully Diluted Shares Outstanding
Fully Diluted Shares = Basic Shares + In-the-Money Options/Warrants (via TSM) + Convertibles in-the-money (if-converted ou NSS)
```
- **Basic shares:** primeira página do 10-K/10-Q mais recente (ou proxy, se mais atual).
- Para trading comps, use o **preço de fechamento do dia anterior**.
- Convenção de conservadorismo: muitos bancos usam todas as opções **outstanding** in-the-money (não só as exercisable) — cenário mais dilutivo.

### Treasury Stock Method (TSM) — opções e warrants
Assume que todas as tranches in-the-money são exercidas ao strike médio ponderado e os proceeds recompram ações ao preço atual. Como strike < preço, recompra-se menos do que entra → emissão líquida (dilutiva).
```
Option Proceeds          = In-the-Money Options × Weighted Avg Exercise Price
Shares Repurchased       = Option Proceeds / Current Share Price
Net New Shares           = In-the-Money Options − Shares Repurchased
Fully Diluted Shares     = Basic Shares + Net New Shares
```
**Exemplo (Rosenbaum 1.7):** preço $20, basic 100M, 5M opções @ strike $18.
Proceeds = 5M×$18 = $90M → recompra = $90M/$20 = 4,5M → net new = 5−4,5 = **0,5M** → FD = **100,5M**.

### Convertibles — If-Converted vs Net Share Settlement
Primeiro cheque se o convert está in-the-money (preço atual > conversion price). Se out-of-the-money, **continua tratado como dívida**. Leia os footnotes do 10-K/prospecto.

**If-Converted** (physical settlement): trata o convert como equity.
```
Incremental Shares = Amount Outstanding / Conversion Price
```
- Adiciona as shares à contagem; remove o convert do total debt.
- Ajuste o net income pra cima pelo **juro economizado** (tax-effected) do cupom.
- **Exemplo (1.8):** $150M convert, conversion price $15, preço $20 → 150/15 = **10M shares** → FD = 100 + 0,5 + 10 = **110,5M**.

**Net Share Settlement (NSS):** só o excesso do valor de conversão sobre o par vira ação (menos diluição; comum em emissores maiores). O principal **permanece como dívida** (liquidado em caixa no vencimento).
```
Conversion Value   = Incremental Shares (=Amt/Conv Price) × Current Share Price
Excess Over Par    = Conversion Value − Par
Incremental Shares = Excess Over Par / Current Share Price
```
- **Exemplo (1.9):** mesmo convert → if-converted dá 10M; NSS dá só (200−150)/20 = **2,5M**.

> ⚠️ Tratamento contábil de converts mudou (FASB 2008 bifurcou em dívida+equity; proposta de eliminar em 2019). Para shares outstanding, ainda se usa TSM/NSS — mas consulte um especialista de ECM em casos materiais.

## 2. Enterprise Value — o bridge completo
```
Enterprise Value = Equity Value
                 + Total Debt (short + long term)
                 + Preferred Stock
                 + Noncontrolling (Minority) Interest
                 − Cash & Cash Equivalents (excess)
```
- **Net Debt** = Total Debt − Cash & equivalents (− short-term investments, se aplicável).
- Some pensão sub-financiada e capital/finance leases (ver nota IFRS 16 abaixo) ao "debt-like".
- Subtraia equity em afiliadas não-consolidadas (trate como cash).
- **Regra de coerência:** EV no numerador → métrica pré-juros (Sales/EBITDA/EBIT) no denominador. Equity value → métrica pós-juros (Net Income/EPS).

> **IFRS 16 / ASC 842 (2019+):** operating leases agora vão pro balanço como lease liability + right-of-use asset. A regra antiga de "capitalizar = 8× aluguel" está **superada** para reportantes sob esses padrões — use a lease liability reportada. Cheque a consistência entre os comps (uns sob IFRS 16, outros não) e, se preciso, padronize via EBITDAR.

## 3. LTM — Last Twelve Months
Para medir performance no período de 12 meses mais recente:
```
LTM = Prior Fiscal Year + Current Stub − Prior Stub
```
- **Current stub** = YTD do ano corrente; **Prior stub** = mesmo YTD do ano anterior.
- Se o trimestre mais recente for o **Q4** (fim do FY), não precisa calcular LTM — o FY reportado já é o LTM.
- **Exemplo:** FY2018 = $1.000; current stub (9M 2019) = $850; prior stub (9M 2018) = $750 → LTM 9/30/2019 = 1.000 + 850 − 750 = **$1.100**.
- Antes do 10-Q/10-K, o earnings release (8-K) já traz dados pra atualizar comps.

## 4. Calendarização
Comps com fiscal years diferentes não são "apples-to-apples". Ajuste todos pro mesmo CY end:
```
CY Sales (próximo) = (Month# × FYA) / 12 + ((12 − Month#) × NFY) / 12
```
- **Month#** = mês em que o FY termina (FY abril → 4). FYA = fiscal year atual; NFY = próximo fiscal year.
- **Exemplo:** FY 4/30/2019A = $1.000, FY 4/30/2020E = $1.150 → CY2019E = (4/12)×1.000 + (8/12)×1.150 = **$1.100**.
- Se houver estimativas trimestrais, use-as como base (mais preciso).

## 5. Scrubbing — ajuste por itens não-recorrentes
Para normalizar a performance ("sanitizar" os financials). Não fazer = múltiplos enganosos.
- **Add-back de charges one-time:** reestruturação (fechamento de lojas/plantas, demissões), perdas em venda de ativos, mudança de princípio contábil, write-off de estoque, goodwill impairment, extinção de dívida, litígios.
- **Eliminar gains one-time:** venda de ativos, acordos favoráveis, ajustes fiscais.
- **Tax-effecte** os ajustes que entram acima do net income.
- Fontes: MD&A e footnotes do 10-K/10-Q, earnings releases, relatórios de equity research.
- Resultado: **Adjusted EBITDA / Adjusted EBIT / Adjusted EPS** — a base "clean" pros múltiplos.

## Erros clássicos a evitar (Rosenbaum)
- Comps mal calendarizados ou sem LTM consistente.
- Falha em scrubar não-recorrentes → múltiplos distorcidos.
- Misturar EV com métrica pós-juros (ou equity com pré-juros).
- Ignorar opções/converts in-the-money na contagem de shares.
