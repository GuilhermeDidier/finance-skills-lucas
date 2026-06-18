# Duration, Convexidade e Risco de Taxa

> Fonte: Securato (cap. 8, Duration — Macaulay 1938, Fisher-Weil 1971) + convenções. A medida de quanto o preço de um título se move quando a taxa muda.

## Duration de Macaulay — o "prazo médio" ponderado pelo VP
```
D_Mac = Σ [ t × VP(CF_t) ] / Preço
```
- É o **prazo médio** dos fluxos, ponderado pelo valor presente de cada um (leva em conta o valor do dinheiro no tempo).
- Para um **zero-cupom**, duration = prazo até o vencimento. Para um título com cupom, duration < prazo (os cupons "puxam" o prazo médio para a frente).
- Em dias úteis (Brasil), expresse em DU e/ou anos (du/252).

## Modified Duration — sensibilidade do preço
```
D_mod = D_Mac / (1 + y/k)          (k = nº de capitalizações por ano)
ΔPreço/Preço ≈ − D_mod × Δy
```
- Mede a **variação percentual do preço** para uma variação de 1 ponto na taxa. Ex.: D_mod = 4 → +1% na taxa ≈ −4% no preço.
- É a aproximação **linear** (de 1ª ordem) — boa para variações pequenas; subestima para grandes (daí a convexidade).

## DV01 / PVBP — sensibilidade em dinheiro
```
DV01 (PVBP) = D_mod × Preço × 0,0001
```
- Variação do preço (em R$) para **1 basis point** (0,01%) de mudança na taxa. Métrica de risco para hedge e limites de tesouraria.
- Some os DV01 das posições para o **DV01 da carteira** (exposição agregada a taxa).

## Convexidade — a correção de 2ª ordem
```
Convexidade = Σ [ t(t+1) × VP(CF_t) ] / [ Preço × (1+y)² ]
ΔPreço/Preço ≈ − D_mod × Δy + ½ × Convexidade × (Δy)²
```
- A relação preço-yield é **curva** (convexa), não reta. A duration sozinha erra; a convexidade corrige.
- **Convexidade é boa para o investidor:** para a mesma duration, mais convexidade = ganha mais quando a taxa cai e perde menos quando sobe. Tem "preço" (yield menor).

## Aplicações
- **Imunização:** casar a **duration dos ativos com a dos passivos** (ou com o horizonte de investimento) neutraliza o risco de taxa de 1ª ordem — o que se perde em preço se ganha em reinvestimento (e vice-versa). Securato detalha a imunização de carteira (cap. 10).
- **Título sintético:** uma carteira de renda fixa pode ser representada por um título sintético equivalente com a mesma duration e VP a mercado.
- **Hedge:** dimensione o hedge (ex.: DI futuro) pelo **DV01 da posição** ÷ DV01 do instrumento de hedge.
- **Barbell vs bullet:** mesma duration, convexidades diferentes (barbell = mais convexo).

## Limites
- Duration/convexidade assumem **deslocamento paralelo** da curva. Mudanças de inclinação/curvatura exigem medidas por vértice (key rate durations).
- Para títulos com opcionalidade (callable), use **effective duration** (recalcula preço com choques de curva, capturando a mudança de fluxos).

## Conectar
Use o preço de `bond-pricing.md`; a curva de `yield-curve-and-credit.md`; e os instrumentos brasileiros (DI futuro para hedge) de `brazilian-instruments.md`.
