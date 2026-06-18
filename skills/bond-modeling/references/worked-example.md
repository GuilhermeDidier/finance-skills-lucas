# Exemplo trabalhado — Preço, Duration, DV01 e Convexidade

> Título com cupom anual. Mostra como preço → duration → DV01 → convexidade se encadeiam, e como a previsão de duration+convexidade **bate** com o reapreçamento real. (Exemplo anual para clareza; no Brasil prefixado use DU/252.)

## Dados
Face R$1.000 | cupom **10% a.a.** (R$100/ano) | prazo **3 anos** | YTM **12%**.

## 1. Preço (VP dos fluxos)
| t | Fluxo | Fator (1,12^t) | VP |
|---|---|---|---|
| 1 | 100 | 1,1200 | 89,29 |
| 2 | 100 | 1,2544 | 79,72 |
| 3 | 1.100 | 1,4049 | 782,96 |
| | | **Preço** | **951,96** |
Cupom 10% < yield 12% → negocia com **deságio** (abaixo do par). ✓

## 2. Duration de Macaulay
```
D_Mac = Σ [t × VP(CF_t)] / Preço
      = (1×89,29 + 2×79,72 + 3×782,96) / 951,96
      = 2.597,60 / 951,96 = 2,73 anos
```
(< 3 anos: os cupons puxam o prazo médio para a frente.)

## 3. Modified Duration e DV01
```
D_mod = D_Mac / (1 + y) = 2,73 / 1,12 = 2,44
DV01  = D_mod × Preço × 0,0001 = 2,44 × 951,96 × 0,0001 = R$ 0,232 por título (por 1 bp)
```
Leitura: +1% na taxa ≈ **−2,44%** no preço; cada basis point ≈ **−R$0,23**.

## 4. Convexidade
```
Convexidade = Σ [t(t+1) × VP(CF_t)] / [Preço × (1+y)²]
            = (2×89,29 + 6×79,72 + 12×782,96) / (951,96 × 1,2544)
            = 10.052,4 / 1.194,1 = 8,42
```

## 5. Prever o efeito de +1% na taxa (12% → 13%)
```
Efeito duration   = − D_mod × Δy × Preço = −2,44 × 0,01 × 951,96 = −R$23,20
Efeito convexidade= ½ × Convex × (Δy)² × Preço = 0,5 × 8,42 × 0,0001 × 951,96 = +R$0,40
ΔPreço previsto   ≈ −23,20 + 0,40 = −R$22,80  →  novo preço ≈ R$929,16
```

## 6. Conferência — reapreçar de fato a 13%
| t | Fluxo | 1,13^t | VP |
|---|---|---|---|
| 1 | 100 | 1,1300 | 88,50 |
| 2 | 100 | 1,2769 | 78,32 |
| 3 | 1.100 | 1,4429 | 762,35 |
| | | **Preço a 13%** | **929,17** |

**Previsão R$929,16 vs real R$929,17** — praticamente exato. ✅
- Só com duration: 951,96 − 23,20 = **928,76** (erro de ~R$0,40).
- A **convexidade fecha o gap** — e mostra por que ela é "boa": amortece a perda quando a taxa sobe (e amplifica o ganho quando cai).

## Leitura final
- O risco de taxa do título está **resumido no DV01 (R$0,23/bp)** e na **duration (2,44)**.
- Para **hedgear** uma posição comprada nesse título, venda DI futuro até casar o DV01 (ver `duration-convexity.md` e `brazilian-instruments.md`).
- Se fosse mantido até o vencimento, o retorno realizado seria a YTM de 12% (ignorando reinvestimento); vendendo antes, o resultado é a **marcação a mercado**.
