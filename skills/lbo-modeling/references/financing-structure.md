# Estrutura de Financiamento do LBO e Sources & Uses

> Fonte: Rosenbaum & Pearl, Cap. 4–5. As camadas de capital, sua senioridade/custo, e como montar o sources & uses.

## A pilha de capital (do mais seguro/barato ao mais arriscado/caro)
| Camada | Senioridade | Garantia | Custo | Características |
|---|---|---|---|---|
| **Revolving Credit Facility** | Sênior secured | Sim (1st lien) | Baixo (flutuante, ex.: S+325) | Linha rotativa p/ working capital; geralmente não sacada no closing |
| **Term Loan A (TLA)** | Sênior secured | 1st lien | Baixo (flutuante) | Amortização linear; bancos |
| **Term Loan B (TLB)** | Sênior secured | 1st lien | Flutuante (S+spread) | Amortização mínima (~1%/ano), bullet no fim; investidores institucionais |
| **Second Lien** | Secured subordinada | 2nd lien | Maior | Entre senior e high yield |
| **Senior Notes / High Yield Bonds** | Sênior unsecured | Não | Cupom fixo, alto | Bonds; covenants mais leves (incurrence) |
| **Senior Subordinated / Subordinated Notes** | Subordinada | Não | Mais alto | Abaixo dos senior notes |
| **Mezzanine Debt** | Subordinada | Não | Mais alto (+ warrants/PIK) | Híbrido dívida-equity; "equity kicker" |
| **Contributed Equity** | Residual | — | — | Equity do sponsor (+ rollover do management) |

- **Floating vs fixed:** revolver e term loans flutuam (SOFR + spread); bonds têm cupom fixo. (Antes LIBOR; migrou para **SOFR**.)
- **Leveraged loans** dependem da base de ativos (secured); **high yield/mezz** dependem do caixa.
- **PIK (payment-in-kind):** juros que acumulam no principal em vez de sair em caixa — alivia o caixa no início.

## Níveis de alavancagem (rule of thumb)
- Medidos em múltiplos de EBITDA: **Senior Debt/EBITDA**, **Total Debt/EBITDA**.
- Total debt costuma ficar em ~**4x–6x EBITDA** (varia com mercado, setor e qualidade do crédito). Equity contribution tipicamente **30–50%** do total de financiamento (subiu pós-2008).

## Sources & Uses (tem que balancear)
| Uses (para onde vai o $) | Sources (de onde vem) |
|---|---|
| Compra do equity do alvo (purchase EV) | Revolver (se sacado) |
| Refinanciamento da dívida existente | Term Loans (TLA/TLB) |
| Transaction fees (advisory, legal) | Senior/High Yield Notes |
| Financing fees (OID, underwriting) | Mezzanine |
| Caixa mínimo no balanço | **Sponsor Equity** (o "plug") |
| | Rollover equity do management |

- **Total Sources = Total Uses.** O **equity do sponsor é o plug**: depois de definir quanta dívida o negócio aguenta, o equity cobre o resto.
- **Cash-free, debt-free:** muitos deals assumem que o vendedor entrega sem caixa e sem dívida → ajusta o preço.

## Da estrutura ao retorno
Quanto **menor o equity** (mais dívida), maior o IRR — mas maior o risco. O modelo de LBO testa:
- A empresa **serve a dívida** em todos os anos (covenants de leverage e coverage)?
- Sobra caixa para **cash sweep** (amortização opcional acelera a desalavancagem)?
- O **revolver** cobre anos de aperto?

(A mecânica do debt schedule, juros e circularidade está em `lbo-model-build.md` e na skill financial-modeling, `references/debt-schedule.md`.)
