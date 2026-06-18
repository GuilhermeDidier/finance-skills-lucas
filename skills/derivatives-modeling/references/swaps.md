# Swaps

> Fonte: Securato + convenções. Troca de fluxos de caixa entre duas partes — o derivativo de balcão mais usado por tesourarias para gerir risco de taxa e câmbio.

## Interest Rate Swap (IRS) — o mais comum
Troca de **juro fixo por flutuante** (ou vice-versa) sobre um **notional** (que não troca de mãos).
- Ex.: a empresa tem dívida flutuante (CDI) e teme alta de juros → entra num swap **recebendo CDI, pagando pré** → fixa o custo.
- **Valor de um IRS** = diferença entre dois "bonds": `V = VP(perna recebida) − VP(perna paga)`. No início, V ≈ 0 (a taxa fixa é a **swap rate** que zera o valor). Depois, V oscila com a curva.
- Equivale a uma **carteira de FRAs** (forward rate agreements).
- **Swap rate:** a taxa fixa que iguala o VP das duas pernas no início — derivada da curva de juros (ver skill bond-modeling).

## Currency Swap
Troca de fluxos (e geralmente o **principal**) em **moedas diferentes**. Usado para captar/aplicar em moeda estrangeira com hedge. Há troca de principal no início e no fim (ao contrário do IRS).

## O "swap" no Brasil (registrado na B3/Cetip)
- Contrato de balcão registrado, geralmente **DI × pré**, **DI × dólar (cupom cambial)**, **DI × IPCA**, etc. Liquidação por diferença no vencimento.
- Muito usado por empresas para **hedge de dívida** (ex.: trocar exposição a CDI por pré, ou dívida em dólar por CDI).
- A perna de câmbio usa o **cupom cambial** (ver `forwards-futures.md`).

## Outros swaps
- **Basis swap:** troca dois índices flutuantes (ex.: CDI × IPCA).
- **Total return swap:** troca o retorno total de um ativo por um juro — sintetiza exposição sem deter o ativo.
- **Credit Default Swap (CDS):** "seguro" contra default de um emissor — o comprador paga um prêmio periódico e recebe se houver evento de crédito. Precifica risco de crédito (PD/LGD; ver bond-modeling). O **CDS soberano** é referência do risco-país (liga com country risk premium da skill valuation-modeling).

## Valoração e risco
- Marca-se a mercado descontando cada perna pela **curva** apropriada.
- Risco de taxa medido por **DV01** (some ao DV01 da carteira). Risco de contraparte (mitigado por colateral/CSA e clearing).

## Conectar
Curva e DV01 → skill **bond-modeling**. Cupom cambial e DI futuro → `forwards-futures.md`. Hedge prático → `hedging-and-brazil.md`.
