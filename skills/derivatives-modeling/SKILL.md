---
name: derivatives-modeling
description: Derivativos — forwards e futuros (cost of carry, DI futuro, dólar futuro, cupom cambial), opções (payoffs, put-call parity, Black-Scholes, binomial, Greeks, volatilidade implícita), swaps (IRS, currency, CDS, swap DI×pré/dólar), e hedge na prática, com foco no mercado brasileiro (B3). Use quando o usuário quiser precificar um derivativo, calcular Black-Scholes/Greeks, montar um hedge (taxa/câmbio/equity), entender futuros/opções/swaps, ou navegar os instrumentos da B3. Gatilhos: "derivativo", "futuro", "forward", "opção", "call", "put", "Black-Scholes", "Greeks", "delta", "vega", "volatilidade", "swap", "hedge", "DI futuro", "dólar futuro", "cupom cambial", "put-call parity", "CDS".
---

# Derivatives Modeling

Skill para **precificar e usar derivativos** — instrumentos cujo valor deriva de um ativo subjacente. Dois grandes grupos: **lineares** (forwards/futuros/swaps, valor ∝ ao subjacente) e **não-lineares** (opções, com convexidade/Greeks). Forte ênfase em **hedge** e no mercado **brasileiro (B3)**.

## Quando usar
- **Precificar** forward/futuro (cost of carry), opção (Black-Scholes/binomial), ou swap.
- Calcular **Greeks** (delta/gamma/vega/theta/rho) e **volatilidade implícita**.
- Montar/dimensionar um **hedge** (taxa via DI futuro/swap; câmbio via dólar futuro/NDF; equity via put/índice).
- Entender **put-call parity**, estratégias de opções (spreads, straddle, collar).
- Navegar instrumentos da **B3** (DI futuro, dólar futuro, cupom cambial, opções, swaps de balcão).
- Conectar com **real options** (corporate-finance) e **equity como opção/Merton** (crédito).

**Quando NÃO usar:** precificação/risco de títulos à vista (YTM/duration) → skill **bond-modeling**; estruturação de dívida/securitização → skill **dcm-modeling**; real options em capital budgeting → skill **corporate-finance**.

## Princípios
1. **Não-arbitragem precifica os lineares:** F = S × cost of carry; desvios = arbitragem.
2. **Volatilidade é o coração das opções** — mais σ = mais prêmio (downside limitado ao prêmio).
3. **Opção = direito, não obrigação** — só se exerce se vale a pena (S vs K).
4. **Greeks medem o risco** — delta (preço), gamma (convexidade), vega (vol), theta (tempo).
5. **Hedge dimensiona por sensibilidade:** DV01 (taxa) ou delta (opções); cuidado com basis risk.
6. **Derivativo é alavancado** — ótimo para hedge, perigoso sem limites de risco.

## Roteiro
1. **Linear ou não-linear?** Forward/futuro/swap → `references/forwards-futures.md` / `references/swaps.md`. Opção → `references/options.md`.
2. **Precifique:** cost of carry (lineares); Black-Scholes/binomial (opções) — `references/black-scholes-greeks.md`.
3. **Meça o risco:** Greeks (opções) ou DV01 (taxa).
4. **Hedge:** dimensione por delta/DV01; escolha o instrumento da B3 — `references/hedging-and-brazil.md`.

## Formato da saída
1. **Preço** do derivativo e as premissas (S, K, T, r, σ; ou curva/cost of carry).
2. **Sensibilidades:** Greeks (opções) ou DV01/delta (lineares) e o que significam.
3. **Hedge sugerido:** instrumento, quantidade (hedge ratio) e basis risk.
4. **Contexto BR:** instrumento B3 aplicável; cupom cambial se houver câmbio.
5. **Premissas e limitações** explícitas (BS assume σ/r constantes, etc.).

## Documentos de apoio
- `references/forwards-futures.md` — forward vs futuro, cost of carry, contango/backwardation, DI futuro, dólar futuro e cupom cambial. (Securato)
- `references/options.md` — calls/puts, payoffs, moneyness, valor intrínseco/tempo, value drivers, put-call parity, estratégias. (Black & Scholes)
- `references/black-scholes-greeks.md` — fórmula de Black-Scholes, binomial (CRR), volatilidade implícita/smile, os Greeks, delta-hedge, equity como opção (Merton).
- `references/swaps.md` — IRS, currency swap, swap brasileiro (DI×pré/dólar/IPCA), basis, total return, CDS; valoração e DV01.
- `references/hedging-and-brazil.md` — princípios de hedge (hedge ratio, basis risk, hedge accounting), tipos de hedge e instrumentos da B3.
- `references/worked-example.md` — call/put ATM por Black-Scholes, put-call parity conferida e delta-hedge.

> 🔗 Curva/DV01 → skill bond-modeling. Real options → corporate-finance. Conversíveis → valuation/mna. Cupom cambial/risco-país → bond/valuation.
