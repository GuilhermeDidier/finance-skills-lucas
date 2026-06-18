# Curva de Juros e Risco de Crédito

> Fonte: Securato + convenções de mercado. A estrutura a termo das taxas e o spread que remunera o risco.

## Estrutura a termo (yield curve)
- Relação entre **taxa** e **prazo**. Formatos: **normal** (sobe com o prazo), **invertida** (cai — sinal de aperto/recessão esperada), **flat**.
- **Spot rate** (taxa à vista): taxa de um zero-cupom para cada vértice. **Forward rate:** taxa futura implícita entre dois vértices:
  ```
  (1 + s_2)^2 = (1 + s_1) × (1 + f_{1,2})   →   f = forward 1→2
  ```
- **Bootstrapping:** extrair as spot rates a partir de preços de títulos (zero-cupom e com cupom), vértice a vértice.
- **Brasil:** a curva prefixada é construída dos **vértices de DI futuro** (B3); a curva de juro real, das **NTN-B**; a inflação implícita = (curva pré) − (curva real) ≈ **breakeven inflation**.

## Por que a curva importa
- Descontar cada fluxo pela **taxa do seu vértice** é mais preciso que uma YTM única.
- A inclinação informa expectativas de juro/inflação e oportunidades (carry, roll-down).
- **Roll-down:** se a curva é positivamente inclinada e estável, um título "rola" para vértices de taxa menor com o tempo → ganho de preço além do carry.

## Risco de crédito e spread
```
Yield do título = taxa livre de risco (curva soberana, mesmo prazo) + credit spread
```
- O **credit spread** remunera risco de **default** e de **liquidez**. Quanto pior o crédito, maior o spread.
- **Z-spread:** spread constante somado a **toda a curva** spot que iguala o VP dos fluxos ao preço (mais correto que spread sobre uma única taxa).
- **Spread duration:** sensibilidade do preço a mudanças no spread (separada da sensibilidade à curva base).

## Ratings e default
- Agências (S&P, Moody's, Fitch): **investment grade** (≥ BBB−/Baa3) vs **high yield/non-investment grade** (< BBB−). Quanto menor o rating, maior o spread exigido.
- Conceitos: **PD** (probability of default), **LGD** (loss given default), **recovery rate** (= 1 − LGD). Perda esperada ≈ PD × LGD.
- No Brasil: rating soberano e corporativo (escala global e nacional); debêntures têm rating próprio.

## Risco de uma carteira de renda fixa
- **Risco de taxa** (curva): medido por duration/DV01 (ver `duration-convexity.md`).
- **Risco de crédito:** spread duration + análise de PD/LGD.
- **Risco de inflação:** relevante em prefixados (NTN-F/LTN); NTN-B protege.
- **Risco de liquidez** e **de reinvestimento** (cupons).

## Conectar
A precificação por curva alimenta `bond-pricing.md`; a sensibilidade, `duration-convexity.md`; os indexadores brasileiros, `brazilian-instruments.md`. Estruturação de crédito/securitização (tranches, waterfalls) → skill **dcm-modeling**.
