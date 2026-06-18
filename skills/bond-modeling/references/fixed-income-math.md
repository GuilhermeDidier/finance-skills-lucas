# Matemática Financeira de Renda Fixa

> Fonte: Securato, *Cálculo Financeiro das Tesourarias* + convenções de mercado. A base de cálculo por trás de qualquer título.

## Valor do dinheiro no tempo
```
VF = VP × (1 + i)^n              (juros compostos)
VP = VF / (1 + i)^n
```
- **Juros simples** (J = VP×i×n): usado em prazos curtos/descontos comerciais (duplicatas).
- **Juros compostos:** padrão em renda fixa — juros sobre juros.

## Taxas: equivalência e conversão
- **Taxa efetiva** vs **nominal**: a efetiva considera a capitalização real.
- **Equivalência composta** (a regra de ouro): para converter entre períodos, use potência, não proporção:
  ```
  (1 + i_ano) = (1 + i_mês)^12 = (1 + i_dia)^(dias no ano)
  ```
- **Taxa over / overnight:** no Brasil, a Selic/CDI são taxas over (diárias), anualizadas por **252 dias úteis**.

## Day count (contagem de dias) — atenção, muda o preço
- **Brasil: DU/252** (dias **úteis** / 252) é a convenção dominante para títulos públicos prefixados (LTN, NTN-F) e DI. **Distintivo do mercado brasileiro.**
  ```
  fator de desconto = (1 + i_ano)^(du/252)
  ```
- Outras convenções (mais comuns lá fora): **ACT/360, ACT/365, 30/360**. Sempre confirme a convenção do papel — usar a errada erra o preço.

## TIR — Taxa Interna de Retorno (= YTM)
A TIR é a taxa que **zera o NPV** de um fluxo (preço = VP dos fluxos):
```
Preço = Σ  CF_t / (1 + TIR)^t  →  resolver para TIR
```
- Em renda fixa, a TIR de um título mantido até o vencimento é o seu **yield-to-maturity (YTM)**.
- **TIRM (TIR modificada):** corrige a premissa de reinvestimento dos fluxos à própria TIR (reinveste a uma taxa de financiamento/aplicação realista). Útil quando os fluxos intermediários não rendem a TIR.
- Calcule com a função `TIR`/`IRR` (Excel) ou Newton-Raphson; entenda a intuição (desconto que iguala preço aos fluxos).

## Valor presente de um fluxo de caixa
```
VP = Σ  F_j / (1 + i_j)^(d_j)
```
- Cada fluxo F_j tem seu prazo d_j e pode ter sua própria taxa i_j (quando se usa a **curva** em vez de uma taxa única — ver `yield-curve-and-credit.md`).
- Descontar pela curva (cada vértice com sua taxa) é mais correto que uma TIR única, mas a TIR única é o "resumo" do título.

## Desconto (mercado de recebíveis)
- **Desconto simples (comercial):** D = F × δ × n; VP = F − D. Usado em duplicatas/notas.
- A **taxa efetiva** embutida num desconto simples é maior que δ (porque δ incide sobre o valor de face, não sobre o VP). Securato deriva: `i = δ / (1 − δ×n)`.

## Conectar
Estes blocos alimentam tudo: precificação (`bond-pricing.md`), sensibilidade (`duration-convexity.md`) e os instrumentos brasileiros (`brazilian-instruments.md`).
