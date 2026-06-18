# Exemplo trabalhado — Black-Scholes, Put-Call Parity e Delta Hedge

> Precifica uma call e uma put europeias, confere a paridade e mostra o delta-hedge. Aritmética verificada.

## Dados
S = 100 | K = 100 (ATM) | T = 1 ano | r = 5% | σ = 20% | sem dividendos.

## 1. d1 e d2
```
d1 = [ln(100/100) + (0,05 + 0,20²/2)·1] / (0,20·√1)
   = [0 + (0,05 + 0,02)] / 0,20 = 0,07 / 0,20 = 0,35
d2 = 0,35 − 0,20·√1 = 0,15
```

## 2. Probabilidades normais (CDF)
```
N(d1) = N(0,35) ≈ 0,6368
N(d2) = N(0,15) ≈ 0,5596
N(−d1) = 0,3632 ;  N(−d2) = 0,4404
e^(−rT) = e^(−0,05) ≈ 0,9512
```

## 3. Preço da Call
```
C = S·N(d1) − K·e^(−rT)·N(d2)
  = 100·0,6368 − 100·0,9512·0,5596
  = 63,68 − 53,23 = R$ 10,45
```

## 4. Preço da Put (direto)
```
P = K·e^(−rT)·N(−d2) − S·N(−d1)
  = 100·0,9512·0,4404 − 100·0,3632
  = 41,89 − 36,32 = R$ 5,57
```

## 5. Conferência — Put-Call Parity
```
C − P = S − K·e^(−rT)
10,45 − 5,57 = 100 − 95,12
4,88 = 4,88  ✅
```
A paridade fecha — call e put são consistentes.

## 6. Delta Hedge
- **Delta da call = N(d1) = 0,6368.** Quem **vende** 1 call sobre 100 ações neutraliza a exposição ao preço **comprando 63,68 ações** (≈ 64).
- À medida que S se move, o delta muda (**gamma**) → o hedge precisa de **rebalanceamento dinâmico**.
- **Theta:** a call perde valor-tempo com o passar dos dias (tudo mais constante); **vega:** se σ subir de 20% para 21%, o prêmio sobe (vega > 0).

## Leituras
- A call ATM custa R$10,45 (≈10% do spot) — quase tudo **valor tempo** (intrínseco = 0 no ATM).
- Subir a **volatilidade** encarece **ambas** (call e put) — por isso straddle é aposta em vol.
- O mesmo arcabouço precifica **opções reais** (adiar/expandir um projeto) e o **equity como call sobre os ativos** (Merton) — ver `black-scholes-greeks.md` e a skill corporate-finance.
- No Brasil, opções sobre ações/Ibovespa são negociadas na **B3**; a IV é lida do preço de mercado (ver `black-scholes-greeks.md`).
