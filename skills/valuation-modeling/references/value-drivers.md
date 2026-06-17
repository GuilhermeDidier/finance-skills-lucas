# Value Drivers — criação de valor, economic profit e o que os múltiplos escondem

> Fontes: McKinsey/Koller, *Valuation: Measuring and Managing the Value of Companies*; Mauboussin (Morgan Stanley/Counterpoint Global), *What Multiples Miss*. É a camada conceitual que conecta DCF, ROIC e múltiplos — o "porquê" por trás dos números.

## O princípio central (McKinsey)
**Uma empresa cria valor quando o ROIC > custo de capital (WACC).**
- Se ROIC ≤ WACC, **crescimento não cria valor** (pode até destruir).
- O objetivo é a combinação de **crescimento + ROIC** que maximiza o valor presente dos fluxos.
- Crescer com ROIC alto cria muito valor; crescer com ROIC baixo consome caixa sem recompensa (caso "Logan's Stores": cresce lucro investindo pesado, mas ROIC cai e o cash flow encolhe).

## A trindade: Growth, ROIC e Cash Flow
As três variáveis estão amarradas matematicamente — descreva a empresa por **duas** (geralmente growth e ROIC, comparáveis no tempo e vs peers):
```
Growth          = ROIC × Investment Rate
Investment Rate = Growth / ROIC
Cash Flow       = NOPAT × (1 − Growth/ROIC)
```
**Exemplo (Value Inc. vs Volume Inc.):** ambas crescem 5% e geram NOPAT $100.
- Value Inc.: ROIC 20% → reinveste só 25% → cash flow $75.
- Volume Inc.: ROIC 10% → reinveste 50% → cash flow $50.
Mesmo crescimento, **valor muito diferente** — quem tem ROIC alto reinveste menos para o mesmo g e sobra mais caixa.

## A Value Driver Formula (o DCF de crescimento constante)
Com g e ROIC constantes, o DCF colapsa em:
```
            NOPAT_{t=1} × (1 − g/ROIC)
Value  =   ─────────────────────────────
                   WACC − g
```
- Mostra explicitamente que valor é função de **g, ROIC e WACC**.
- 🔗 **É a mesma relação do ROIIC** em `dcf.md`: o termo `(1 − g/ROIC)` é a parcela do NOPAT que vira caixa livre. Se ROIC = WACC, o g some da equação (não cria valor). Use esta fórmula para sanity-check do terminal value: ela revela o ROIC implícito embutido na sua perpetuidade.
- Na prática, raramente se usa sozinha (assume g e ROIC constantes pra sempre), mas é o melhor lembrete do que dirige valor.

## Economic Profit (EVA) — valor sem precisar projetar caixa
```
Economic Profit = Invested Capital × (ROIC − WACC)
Value = Invested Capital inicial + PV(Economic Profit projetado)
```
- Mede, **ano a ano**, se a empresa cobre o custo do capital. EP > 0 → cria valor; EP = 0 → ROIC = WACC.
- **Exemplo:** $500 de capital a ROIC 20% e WACC 10% → EP = $500 × (20%−10%) = $50/ano. Já $1.000 a ROIC 10% → EP = $0 (não cria valor apesar de "lucrar").
- Vantagem: dá uma leitura de criação de valor **por período** que o DCF agregado esconde. Equivalente ao DCF (descontado, o EP dá o mesmo valor).

## Conservation of Value
**Só cria valor o que aumenta os fluxos de caixa** (via maior ROIC ou crescimento lucrativo). Não criam valor por si só: recompras, mudanças de estrutura de capital sem efeito em caixa, troca de método contábil, engenharia financeira. Desconfie de "criação de valor" que não passa por ROIC ou crescimento.

## Múltiplos são atalho de DCF (Mauboussin — *What Multiples Miss*)
- Um múltiplo (P/E, EV/EBITDA) é **taquigrafia** de um DCF: por trás dele estão **ROIC, crescimento e custo de capital**. Quem usa múltiplo sem entender esses drivers está terceirizando o julgamento pro mercado.
- **Múltiplos altos frequentemente precedem retornos abaixo da média** no longo prazo (reversão à média) — mas podem refletir, racionalmente, expectativa de criação de valor. Não é regra mecânica.
- **Combine P/E e EV/EBITDA:** quando divergem para empresas parecidas, a diferença geralmente está na **alavancagem** (P/E é pós-financiamento/alavancado; EV/EBITDA é desalavancado) ou em itens não-operacionais. Investigue a divergência — é informação.
- **Intangíveis distorcem múltiplos:** firmas que investem pesado em P&D/marca (tech, farma) gastam o investimento via despesa, deprimindo lucro reportado e inflando o múltiplo. Ajustar por investimento em intangível muda muito a leitura.
  - *Ex. Microsoft FY2023:* net income $72,4bi → ajustado por intangível **$83,0bi (+14,7%)**; EBITDA $102,4 → $109,7bi; **P/E 34,9 → 30,5x**; **EV/EBITDA 24,2 → 16,9x**. Diferenças materiais.

## Como usar isto no valuation (lente prática)
1. Antes do DCF, calcule **ROIC histórico vs WACC** — a empresa cria ou destrói valor hoje?
2. Decomponha o forecast em **crescimento × ROIC** (não só "receita sobe X%"). Cheque a consistência (reinvestimento = g/ROIC).
3. No terminal value, use a value driver formula para ver o **ROIC implícito** — se for muito acima do WACC pra sempre, exige moat (ver skill corporate-finance / Measuring the Moat).
4. Ao usar múltiplos, lembre que está embutindo premissas de ROIC/g/WACC dos peers — explicite-as.
