# Opções — Conceitos e Payoffs

> Fonte: Strategic Issues in Finance (Black & Scholes, 1973) + convenções. O derivativo não-linear: o **direito** (não a obrigação) de comprar/vender.

## Definições
- **Call:** direito de **comprar** o ativo ao strike K até/na data de exercício.
- **Put:** direito de **vender** o ativo ao strike K.
- **Europeia:** exercício só no vencimento. **Americana:** a qualquer momento até o vencimento.
- O comprador (long) paga um **prêmio**; o vendedor (short/lançador) recebe o prêmio e assume a obrigação.

## Payoffs no vencimento
```
Long Call:  máx(S − K, 0) − prêmio
Long Put:   máx(K − S, 0) − prêmio
Short Call: −máx(S − K, 0) + prêmio   (perda potencial ilimitada)
Short Put:  −máx(K − S, 0) + prêmio
```
- Uma opção só é exercida se "vale a pena": call se **S > K**; put se **S < K**; senão, expira sem valor (lapse).

## Moneyness e os 2 componentes do prêmio
- **ITM** (in-the-money): call com S>K / put com S<K. **ATM:** S≈K. **OTM:** sem valor intrínseco.
```
Prêmio = Valor Intrínseco + Valor Tempo
Valor intrínseco = máx(S−K,0) [call]  ou  máx(K−S,0) [put]
Valor tempo = prêmio − valor intrínseco   (decai até zero no vencimento — theta)
```

## Os value drivers (o que move o prêmio)
Black & Scholes resumem que o valor de uma opção depende de:
1. **Preço do ativo (S)** vs **strike (K)** — quão dentro/fora do dinheiro.
2. **Tempo até o vencimento (T)** — mais tempo = mais valor (mais chance de cruzar o strike).
3. **Volatilidade (σ)** — **o driver-chave**: mais volatilidade = mais valor (o downside é limitado ao prêmio, o upside não).
4. **Taxa livre de risco (r)** — compara-se o **VP do strike** (descontado a r) com S.
5. **Dividendos/renda (q)** — reduzem o valor da call (o detentor não recebe os dividendos; o preço do ativo cai ex-dividendo).
> A vantagem real da opção é **adiar a decisão** até ver o preço se mover — por isso T e σ são tão importantes (liga com **real options** em corporate-finance).

## Put-Call Parity (a relação de não-arbitragem)
```
C − P = S − K·e^(−rT)        (europeias, sem dividendos)
```
- Permite derivar o preço de uma put a partir da call (e vice-versa), montar posições sintéticas (ex.: ação sintética = long call + short put), e detectar arbitragem se a paridade não vale.

## Estratégias comuns (combinações)
- **Covered call** (ações + short call): gera renda, limita upside.
- **Protective put** (ações + long put): seguro contra queda.
- **Spreads** (bull/bear): comprar e vender strikes diferentes (limita custo e payoff).
- **Straddle/strangle** (call + put): aposta em **volatilidade** (movimento grande, direção indiferente).
- **Collar:** protective put + covered call (caixa quase zero) — análogo ao collar de M&A.

## Opções embutidas
Muitos instrumentos têm opcionalidade: bonds **callable/putable**, **conversíveis** (skill valuation-modeling/mna), prepayment em hipotecas (skill dcm), e **equity como call sobre os ativos** da empresa (modelo de Merton — ver `black-scholes-greeks.md`).

## Conectar
Precificação (Black-Scholes, binomial) e sensibilidades (Greeks) → `black-scholes-greeks.md`. Hedge → `hedging-and-brazil.md`.
