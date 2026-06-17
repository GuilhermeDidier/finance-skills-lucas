# Economia do LBO — IRR, MOIC e como o retorno é gerado

> Fonte: Rosenbaum & Pearl, Cap. 4 (Economics of LBOs). As métricas e os mecanismos de retorno.

## IRR — Internal Rate of Return (a métrica primária)
Taxa de desconto que zera o NPV dos fluxos de equity do sponsor (contribuição inicial, dividendos no meio, proceeds no exit). Captura o **valor do tempo** — para um mesmo proceeds, exit mais cedo = IRR maior.
```
−CF0 + CF1/(1+IRR) + CF2/(1+IRR)² + ... + CFn/(1+IRR)ⁿ = 0
```
- **Threshold típico: 15%–20%** em horizonte de ~5 anos (rule of thumb; varia com mercado, risco, tipo de fundo).
- **Drivers do IRR:** performance projetada do alvo, **preço de compra**, **estrutura de financiamento** (tamanho do equity), e **exit multiple e ano**. O sponsor quer minimizar preço e equity, e ter confiança no desempenho futuro e no exit a múltiplo maior.
- Exemplo: contribui $500M no Ano 0, recebe $1.250M no Ano 5 → **IRR ≈ 20%**.

## MOIC / Cash Return / CoC
Múltiplo do caixa investido:
```
MOIC = Total Equity Proceeds / Total Equity Invested
```
- Exemplo: $1.250M / $500M = **2,5x**. Não considera valor do tempo (ao contrário do IRR), mas é cada vez mais usado pelos fundos. Sinônimos: **MOIC** (multiple on invested capital), **CoC** (cash-on-cash).
- **Relação rápida IRR↔MOIC** (sem dividendos no meio): IRR = MOIC^(1/anos) − 1. Ex.: 2,5x em 5 anos → 2,5^0,2 − 1 ≈ **20%**. Regras de bolso: 2x em 5 anos ≈ 15%; 3x em 5 anos ≈ 25%; 2x em 3 anos ≈ 26%.

## Como LBOs geram retorno (os 3 motores)
O equity value cresce por três vias (Rosenbaum, Exhibit 4.6):
1. **Debt paydown (desalavancagem):** o FCF amortiza dívida. Não muda o enterprise value, mas o equity sobe **dólar a dólar** (dívida é claim fixo). Ex.: EV constante em $1bi, dívida cai $500M → equity vai de $300M para $800M.
2. **EBITDA growth:** crescer o EBITDA (orgânico, bolt-on, eficiência) aumenta o EV no mesmo múltiplo → o ganho acrescido vai todo para o equity.
3. **Multiple expansion:** vender a um múltiplo de EBITDA maior que o de entrada (ex.: compra a 8,0x, vende a 9,0x). O mais incerto — não conte com ele no base case; trate como upside.

> Os motores 1 e 2 são equivalentes em retorno quando geram o mesmo Δequity (Rosenbaum mostra ambos chegando a 21,7% IRR / 2,7x). Na prática, um deal combina os três.

## Como a alavancagem amplifica o retorno
Para um EV de saída fixo, **mais dívida (menos equity) = retorno maior** — porque o ganho do equity é dividido por uma base menor.
- Trade-off: mais alavancagem = mais retorno **e mais risco** (caixa apertado para servir juros; risco de default em downturn). Por isso o caixa é stress-tested.
- É a razão de o sponsor maximizar a dívida que o negócio aguenta — limitado pela capacidade de servir a dívida (cash flow) e pelo apetite dos lenders (Debt/EBITDA).

## Bridge de criação de valor (como apresentar)
Decomponha o ganho de equity (entrada → saída) em:
```
Equity no exit = Equity de entrada
              + Crescimento de EV por EBITDA   [(ΔEBITDA) × múltiplo de entrada]
              + Multiple expansion             [(múltiplo saída − entrada) × EBITDA saída]
              + Debt paydown                   [redução da dívida líquida no período]
```
Isso mostra ao IC (investment committee) **de onde vem** o retorno — e se ele depende perigosamente de multiple expansion (otimista) ou de desalavancagem/crescimento (mais sólido).
