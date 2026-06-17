# Exemplo trabalhado — Accretion/Dilution (Company A compra Company B)

> Caso que amarra a regra do Weighted Cost vs Yield com o cálculo do pro forma EPS. Números fecham. Valores em $ milhões, exceto por ação.

## Dados
| | Comprador A | Alvo B |
|---|---|---|
| Net Income | 200 | 50 |
| Ações | 100M | 50M |
| EPS | $2,00 | $1,00 |
| Preço | $40,00 | $20,00 |
| P/E | 20,0x | 20,0x |
| Equity Value | 4.000 | 1.000 |

**Premissas do deal:** prêmio de controle 25%; mix **40% Cash / 30% Debt / 30% Stock**; custo do caixa 3% pré-imposto; custo da dívida nova 6% pré-imposto; tax rate 25%.

## Passo 1 — Purchase Price
```
Purchase Equity Value = 1.000 × (1 + 25%) = $1.250  ($25,00/ação)
Purchase P/E do Seller = 1.250 / 50 = 25,0x
```
Funding: Cash = 40% × 1.250 = **500** | Debt = 30% × 1.250 = **375** | Stock = 30% × 1.250 = **375**

## Passo 2 — Atalho: Weighted Cost vs Yield
```
Custo após-imposto do Caixa = 3% × (1−25%) = 2,25%
Custo após-imposto da Dívida = 6% × (1−25%) = 4,50%
Custo do Stock = 1 / P/E do comprador = 1/20 = 5,00%

Weighted Cost of Acquisition = 40%×2,25% + 30%×4,50% + 30%×5,00%
                             = 0,90% + 1,35% + 1,50% = 3,75%
Yield do Seller = 50 / 1.250 = 4,00%
```
**3,75% < 4,00% → ACCRETIVE.** O comprador "paga" 3,75% para comprar um yield de 4,0%.

## Passo 3 — Confirmar com o pro forma EPS
```
Foregone interest (caixa), após imposto = 500 × 3% × (1−25%) = 11,25
Juros da dívida nova, após imposto       = 375 × 6% × (1−25%) = 16,875

Combined Net Income = 200 + 50 − 11,25 − 16,875 = 221,875
Ações emitidas = 375 / $40 = 9,375M
Total shares = 100 + 9,375 = 109,375M
Combined EPS = 221,875 / 109,375 = $2,029
```
**Accretion = $2,029 / $2,00 − 1 = +1,4%.** ✅ Consistente com o atalho.

## Passo 4 — E se fosse 100% Stock? (P/E rule)
- Custo de aquisição = 1/P/E comprador = 1/20 = 5,0%; Yield do Seller = 4,0% → **5,0% > 4,0% → DILUTIVE**.
- Confirmação: ações emitidas = 1.250/$40 = 31,25M → total 131,25M; Combined NI = 250 (sem efeitos de juros) → EPS = 250/131,25 = **$1,905** → **−4,8%**.
- Regra dos P/Es: comprador 20,0x **<** purchase P/E do Seller 25,0x → dilutivo. ✅ Bate.

## Leitura
O mesmo deal é **accretive** com mix 40/30/30 (alavanca caixa e dívida baratos) e **dilutive** 100% em ações (ações são o financiamento mais caro, ainda mais comprando um alvo a P/E 25x com ações de P/E 20x). Daí a importância do **mix de financiamento** e da **sensibilidade** sobre preço/sinergias. Com sinergias de custo após imposto, mesmo o cenário 100% stock pode virar accretive.
