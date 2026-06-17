# Exemplo integrado — mini modelo de 3 demonstrações (1 ano)

> Caso mínimo que mostra as ligações DRE ↔ Balanço ↔ DFC e o **balance check fechando**. Números fecham; use como gabarito de linkagem. Valores em $ milhões.

## Ano-base (Year 0)

**DRE Y0:** Receita 1.000 | COGS 600 | GP 400 | SG&A 250 | **EBITDA 150** | D&A 50 | **EBIT 100** | Juros 24 (8% × 300) | Pré-imposto 76 | Imposto 25% = 19 | **Net Income 57**

**Balanço Y0:**
| Ativo | | Passivo + PL | |
|---|---|---|---|
| Caixa | 50 | A/P | 80 |
| A/R | 120 | Dívida | 300 |
| Estoque | 90 | PL | 280 |
| PP&E líq. | 400 | | |
| **Total** | **660** | **Total** | **660** ✓ |

## Premissas (drivers) Year 1
- Receita +10%; COGS 60% de vendas; SG&A 25% de vendas
- D&A 55; Capex 70
- DSO, DIH, DPO mantidos no nível do Y0
- Juros 8% sobre saldo inicial da dívida; cash sweep opcional de 30; sem dividendos

## Passo 1 — DRE Year 1
| | | Cálculo |
|---|---|---|
| Receita | 1.100 | 1.000 × 1,10 |
| COGS | (660) | 60% × 1.100 |
| Gross Profit | 440 | |
| SG&A | (275) | 25% × 1.100 |
| **EBITDA** | **165** | |
| D&A | (55) | premissa |
| **EBIT** | **110** | |
| Juros | (24) | 8% × 300 (saldo inicial) |
| Pré-imposto | 86 | |
| Imposto 25% | (21,5) | |
| **Net Income** | **64,5** | → PL e topo da DFC |

## Passo 2 — Schedules
**Working capital (ratios mantidos):**
- A/R = DSO 43,8d → 132 | Estoque = DIH 54,75d → 99 | A/P = DPO 48,67d → 88
- NWC Y1 = (132+99) − 88 = **143**; NWC Y0 = (120+90) − 80 = **130** → **Δ NWC = +13** (uso de caixa)

**PP&E:** 400 + 70 (capex) − 55 (deprec.) = **415**

**Dívida:** 300 (inicial) − 30 (repag. opcional) = **270** (final)

## Passo 3 — DFC Year 1
| | | |
|---|---|---|
| Net Income | 64,5 | da DRE |
| (+) D&A | 55,0 | não-caixa |
| (−) Δ NWC | (13,0) | do WC schedule |
| **CFO** | **106,5** | |
| (−) Capex | (70,0) | investing |
| **CFI** | **(70,0)** | |
| → Cash available for debt repayment | 36,5 | CFO + CFI |
| (−) Repagamento de dívida | (30,0) | financing |
| **CFF** | **(30,0)** | |
| **Δ Caixa** | **6,5** | CFO+CFI+CFF |
| Caixa final | 56,5 | 50 + 6,5 → balanço |

## Passo 4 — Balanço Year 1 e check
| Ativo | | Passivo + PL | |
|---|---|---|---|
| Caixa | 56,5 | A/P | 88,0 |
| A/R | 132,0 | Dívida | 270,0 |
| Estoque | 99,0 | PL (280 + 64,5) | 344,5 |
| PP&E líq. | 415,0 | | |
| **Total Ativo** | **702,5** | **Total Passivo+PL** | **702,5** |

**Balance check = 702,5 − 702,5 = 0 ✓**

## O que este exemplo prova (as ligações)
- **Net Income (64,5)** apareceu em 3 lugares: fim da DRE, topo da DFC, e no PL (280 → 344,5).
- **D&A (55)** reduziu o PP&E e foi revertido na DFC.
- **Δ caixa da DFC (6,5)** = variação do caixa no balanço (50 → 56,5).
- **Repagamento (30)** saiu da DFC e reduziu a dívida no balanço (300 → 270).
- Mexer em qualquer driver (ex.: capex) propaga pelas 3 demonstrações e o balance check tem que continuar zerado.
