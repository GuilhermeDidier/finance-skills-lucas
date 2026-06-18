# Forwards e Futuros

> Fonte: Securato (contratos a termo/futuro, DI futuro, taxa de câmbio) + convenções. Os derivativos lineares: acordo de comprar/vender um ativo no futuro a um preço fixado hoje.

## Forward vs Futuro
| | Forward | Futuro |
|---|---|---|
| Onde | Balcão (OTC), bilateral | Bolsa (B3), padronizado |
| Risco de contraparte | Sim | Mitigado (câmara/clearing) |
| Liquidação | No vencimento | **Ajuste diário (marcação a mercado)** + margem |
| Customização | Total | Padronizada |
- O **ajuste diário** do futuro (mark-to-market) faz o caixa fluir todo dia (≠ forward, que liquida só no fim) — relevante para custo de carrego e reinvestimento.

## Preço a termo — cost of carry
O preço justo do forward decorre da **não-arbitragem** (comprar à vista e carregar = comprar a termo):
```
F = S × e^((r − q)·T)          (capitalização contínua)
F = S × (1 + r − q)^T          (discreta)
```
- **S** = preço à vista; **r** = taxa livre de risco; **q** = renda do ativo (dividendos/cupom/conveniência); **T** = prazo.
- Commodities: somar **custo de estocagem** (u) e subtrair **convenience yield**: `F = S·e^((r+u−y)T)`.
- **Contango:** F > S (curva de futuros sobe). **Backwardation:** F < S.
- Se o preço de mercado do futuro divergir do F teórico → **arbitragem** (cash-and-carry).

## DI Futuro (B3) — o derivativo de juro mais líquido do Brasil
- Futuro da **taxa média de DI de 1 dia** acumulada até o vencimento. Cotado em **taxa (% a.a., 252)**; PU = 100.000/(1+i)^(du/252).
- Usos: **especular** em juro, **hedgear** posições prefixadas, e **construir a curva** de juros prefixada (vértices). Ver skill **bond-modeling**.
- Hedge de carteira de renda fixa: dimensione pelo **DV01** da posição ÷ DV01 do DI futuro.
- Futuro de **Selic** (lançado 2013) e suas opções complementam o DI.

## Dólar futuro e cupom cambial
- **Dólar futuro (B3):** futuro de taxa de câmbio R$/US$. Preço a termo do câmbio segue a **paridade coberta de juros**:
  ```
  F_câmbio = S_câmbio × (1 + i_BRL) / (1 + i_USD)
  ```
- **Cupom cambial:** a taxa de juro **em dólar** implícita no mercado brasileiro (≈ i_BRL − variação cambial esperada). É o que um investidor em dólar ganha aplicando em reais com hedge cambial. Securato (cap. 10) deriva o cupom cambial a partir dos preços do futuro de dólar e da taxa local. Instrumento: **DDI** (cupom cambial) e **FRA de cupom** na B3.

## Conectar
Opções (não-lineares) → `options.md`; swaps → `swaps.md`; hedge e contexto BR → `hedging-and-brazil.md`. A taxa livre de risco e a curva vêm da skill **bond-modeling**.
