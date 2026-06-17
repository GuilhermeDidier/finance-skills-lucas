# Exemplo trabalhado — LBO da "AlvoCo" (IRR, MOIC e value bridge)

> Caso que fecha a conta de entrada → exit, com IRR/MOIC e o bridge de criação de valor. Valores em $ milhões.

## Entrada (Year 0)
| | |
|---|---|
| EBITDA de entrada | 200 |
| Múltiplo de entrada | 8,0x |
| **Enterprise Value de compra** | **1.600** |
| Dívida (5,0x EBITDA) | 1.000 |
| **Equity do sponsor (plug)** | **600** |

Sources & Uses (cash-free, debt-free, fees ignorados p/ clareza): Dívida 1.000 + Equity 600 = **1.600** = compra do EV. ✓

## Premissas do hold (5 anos)
- EBITDA cresce de 200 → **280** (≈7% a.a., via crescimento orgânico + eficiência)
- FCF cumulativo amortiza dívida: 1.000 → **600** (repaga 400 no período)
- Múltiplo de saída = **8,0x** (igual à entrada — conservador, sem multiple expansion)

## Saída (Year 5)
```
EV de saída = 8,0x × 280 = 2.240
Dívida líquida no exit = 600
Equity de saída = 2.240 − 600 = 1.640
```

## Retornos
```
MOIC = 1.640 / 600 = 2,73x
IRR  = 2,73^(1/5) − 1 ≈ 22,3%
```
Acima do threshold de 20% → **deal atrativo** mesmo sem multiple expansion.

## Value creation bridge (de onde vem o retorno)
```
Equity de entrada                                          600
(+) Crescimento de EV via EBITDA: (280−200) × 8,0x       +640
(+) Multiple expansion: (8,0−8,0) × 280                    +0
(+) Debt paydown: 1.000 − 600                            +400
( = ) Equity de saída                                    1.640
```
Conferência: ΔEquity = 640 + 0 + 400 = 1.040; 600 + 1.040 = **1.640** ✓.
**Leitura:** o retorno vem de **crescimento de EBITDA (640)** e **desalavancagem (400)** — fontes sólidas. Zero dependência de multiple expansion → tese robusta (o múltiplo maior no exit seria upside).

## Sensibilidade do IRR ao múltiplo de saída (EBITDA exit = 280, dívida 600)
| Múltiplo saída | EV saída | Equity saída | MOIC | IRR |
|---|---|---|---|---|
| 7,0x | 1.960 | 1.360 | 2,27x | ~17,8% |
| **8,0x (base)** | **2.240** | **1.640** | **2,73x** | **~22,3%** |
| 9,0x | 2.520 | 1.920 | 3,20x | ~26,2% |

## O floor de valuation (uso no football field)
Invertendo: para um IRR-alvo de **20%** em 5 anos (MOIC ≈ 2,49x), o equity de saída precisaria render 600 × 2,49 = 1.494. Com EV de saída 2.240 e dívida 600 (equity 1.640 > 1.494), há folga → o sponsor poderia **pagar mais na entrada** (menos equity/mais preço) e ainda bater 20%. Esse preço-máximo é o **floor** que entra na valuation-modeling e o lance do financial buyer na mna-modeling.
