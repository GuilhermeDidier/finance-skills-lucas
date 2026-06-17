# Exemplo end-to-end — Valuation completo da "ExemploCo"

> Caso fictício que amarra toda a metodologia (mecânica → DCF → comps → football field). Todos os números fecham; use como gabarito de raciocínio e de checagem. Valores em $ milhões, exceto por ação.

## Dados de entrada
| Item | Valor |
|---|---|
| Preço atual da ação | $50,00 |
| Basic shares | 80,0M |
| Opções in-the-money | 4,0M @ strike médio $40,00 |
| Convertible (in-the-money) | $200,0 @ conversion price $40,00 |
| Dívida "straight" | $800,0 |
| Caixa | $100,0 |
| Minority interest | $50,0 / Preferred: $0 |
| Alíquota marginal | 25% |

## Passo 1 — Fully diluted shares e Enterprise Value

**Opções (TSM):** proceeds = 4,0 × $40 = $160 → recompra = 160/50 = 3,2M → net new = 4,0 − 3,2 = **0,8M**.
**Convert (if-converted):** 200/40 = **5,0M** (e o convert sai do debt, vira equity).
```
Fully diluted shares = 80,0 + 0,8 + 5,0 = 85,8M
Equity Value = 85,8M × $50,00 = $4.290,0
Net Debt = 800 (straight) − 100 (caixa) = $700,0   [convert já reclassificado p/ equity]
Enterprise Value = 4.290 + 700 + 0 (pref) + 50 (minority) = $5.040,0
```

## Passo 1b — LTM (base dos comps)
| | Prior FY 2023 | Current stub (9M24) | Prior stub (9M23) | LTM |
|---|---|---|---|---|
| Revenue | 2.000 | 1.600 | 1.500 | **2.100** |
| EBITDA | 600 | 480 | 440 | **640** |

LTM EBITDA margin = 640/2.100 = **30,5%**.

## Passo 2 — DCF

### UFCF projetado (5 anos)
| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| EBIT | 500,0 | 540,0 | 580,0 | 615,0 | 645,0 |
| − Taxes @25% | (125,0) | (135,0) | (145,0) | (153,8) | (161,3) |
| = NOPAT | 375,0 | 405,0 | 435,0 | 461,3 | 483,8 |
| + D&A | 150,0 | 160,0 | 170,0 | 180,0 | 190,0 |
| − Capex | (170,0) | (180,0) | (190,0) | (200,0) | (210,0) |
| − Δ NWC | (20,0) | (22,0) | (24,0) | (26,0) | (28,0) |
| **= UFCF** | **335,0** | **363,0** | **391,0** | **415,3** | **435,8** |

### WACC
- re = rf 4,0% + βL 1,10 × MRP 5,5% + size premium 1,0% = **11,05%**
- rd pós-imposto = 6,0% × (1 − 0,25) = **4,5%**
- Estrutura-alvo: D/(D+E) = 20%, E/(D+E) = 80%
- WACC = 4,5% × 0,20 + 11,05% × 0,80 = **9,74% ≈ 10,0% (base case; sensibilizar 9,5%–10,5%)**

### Present value (mid-year convention, WACC 10%)
| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Discount factor (t−0,5) | 0,9535 | 0,8668 | 0,7880 | 0,7164 | 0,6512 |
| PV do UFCF | 319,4 | 314,6 | 308,1 | 297,5 | 283,8 |

**Σ PV(UFCF) = $1.523,4**

### Terminal value (os dois métodos)
**A) Perpetuidade (g = 2,5%):**
```
TV(Y5) = 435,8 × 1,025 / (0,10 − 0,025) = 446,6 / 0,075 = 5.955,2
PV(TV) = 5.955,2 × 0,6209 (DF ano 5) = 3.697,8
EV = 1.523,4 + 3.697,8 = 5.221,2
```
**B) Exit multiple (8,0x EV/EBITDA sobre EBITDA Y5 = 645 + 190 = 835):**
```
TV(Y5) = 8,0 × 835 = 6.680,0
PV(TV) = 6.680,0 × 0,6209 = 4.147,8
EV = 1.523,4 + 4.147,8 = 5.671,1
```

### Sanity check 1 — Equivalência terminal value
```
g implícito pelo exit 8,0x = (0,10×6.680 − 435,8)/(435,8 + 6.680) = 3,3%
múltiplo implícito pela perp. 2,5% = 446,6 / (835 × 0,075) = 7,1x
```
Os dois se enquadram (perp. 2,5% ≈ 7,1x; exit 8,0x ≈ 3,3% g). Coerente — exit é só um pouco mais agressivo.

### Sanity check 2 — ROIIC (obrigatório)
Resolvendo da TV de perpetuidade: NOPAT(Y6) = 483,8 × 1,025 = 495,8.
```
5.955,2 = 495,8 × (1 − 0,025/ROIIC) / 0,075  →  ROIIC implícito ≈ 25,2%
```
**⚠️ ROIIC 25% >> WACC 10%.** O modelo assume retorno sobre capital incremental de 25% para sempre. Só é defensável com **moat durável** (ver skill corporate-finance / Measuring the Moat). Sem moat, faça haircut: suba a taxa de reinvestimento ou reduza o FCF terminal.

### Do EV ao valor por ação
| | Perpetuidade | Exit multiple |
|---|---|---|
| Enterprise Value | 5.221,2 | 5.671,1 |
| − Net Debt | (700,0) | (700,0) |
| − Minority Interest | (50,0) | (50,0) |
| = Equity Value | 4.471,2 | 4.921,1 |
| ÷ FD shares (85,8M) | **$52,11** | **$57,36** |

**Faixa DCF: ~$52–57/ação.**

## Passo 3 — Trading Comps
Peers em EV/EBITDA LTM: 7,5x / 8,0x / 8,5x / 9,0x → mediana **8,25x**. Aplicar ao LTM EBITDA $640.
| | Low (7,5x) | Mid (8,25x) | High (9,0x) |
|---|---|---|---|
| Implied EV | 4.800 | 5.280 | 5.760 |
| − Net Debt − Minority (750) | (750) | (750) | (750) |
| = Equity | 4.050 | 4.530 | 5.010 |
| ÷ 85,8M | **$47,20** | **$52,80** | **$58,39** |

**Faixa trading comps: ~$47–58/ação.** (P/E forward dos peers 14–16x dá faixa um pouco mais alta, ~$56–64 — divergência típica; investigar se EBITDA ou EPS está distorcido.)

## Passo 4 — Football Field e conclusão
| Metodologia | Low | High |
|---|---|---|
| **Preço atual** | \$50,00 | \$50,00 |
| DCF (perpetuidade → exit) | \$52,11 | \$57,36 |
| Trading comps (EV/EBITDA) | \$47,20 | \$58,39 |
| Transaction comps | N/A (só em contexto de venda; teria control premium) |

**Conclusão:** faixa de valor convergente em **~$52–57/ação**, com o preço atual ($50) na ponta baixa → **upside modesto (~5–14%)**. Maior alavanca = terminal value (TV é ~71% do EV no DCF). Maior risco = o **ROIIC de 25%** embutido na perpetuidade: se não houver moat que sustente, o valor cai. Sensibilizar WACC (9,5–10,5%) e g/exit antes de cravar.
