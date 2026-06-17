# Drivers de Projeção (DRE e Working Capital)

> Fonte: Rosenbaum & Pearl, Cap. 3 (Project Free Cash Flow). Como projetar cada linha com premissas defensáveis.

## Princípio: toda premissa precisa de justificativa
Cada taxa de crescimento e margem tem que se sustentar em: ganho/perda de market share, tendências de end market, mix de produto, pricing, aquisições, ciclo do setor. E precisam ser **internamente consistentes** — crescimento maior de receita exige mais capex e working capital.

## Receita (top line)
- **Público:** ancore nas estimativas de consensus/research para os 2–3 primeiros anos; nos anos finais, decline em direção a um crescimento estável.
- **Privado:** use tendências históricas + research dos peers.
- Métodos: crescimento % a.a., ou **volume × preço** (preferível quando há dados de unidades/preço).
- **Sanity de mercado:** cheque o tamanho de receita implícito vs o mercado endereçável (não pode implicar market share absurdo).

## COGS e SG&A → margens
- Dirija por **% de vendas** (gross margin e SG&A/sales), com base em histórico e research.
- Anos finais: geralmente **margem constante** no nível do último ano de consensus, salvo tendência justificável (operating leverage, mix, pricing).
- COGS por unidade (volume × custo unitário) quando aplicável.
- Alternativa enxuta: modelar só EBITDA/EBIT (sem detalhe de COGS/SG&A) — mas aí o NWC tem que ser dirigido por % de vendas (falta detalhe de COGS pra estoque/A/P).

## EBIT → FCF (a ponte)
```
        EBIT
  (−)   Impostos (alíquota marginal; padrão 25%, referência = effective tax rate histórico)
  ( = ) EBIAT / NOPAT
  (+)   D&A
  (−)   Capex
  (−)   Aumento (+ se redução) em NWC
  ( = ) Unlevered Free Cash Flow
```

## D&A — depreciação e amortização
- **Depreciação:** não-caixa; aproxima a redução do valor do PP&E ao longo da vida útil. Straight-line = valor uniforme (ativo de $100M, vida 10 anos → $10M/ano).
- Dois métodos de projeção:
  - **Quick-and-dirty:** % de vendas ou % de capex (histórico). Suficiente na maioria.
  - **PP&E schedule (mais correto):** vida média do PP&E atual + período de depreciação do capex novo. Raramente muda muito o resultado.
- **Amortização:** reduz intangíveis de vida definida (patentes, licenças, customer lists). Goodwill (vida indefinida) **não** amortiza — fica no balanço e sofre impairment test anual.
- **Regra de steady state:** assuma capex ≈ depreciação no último ano da projeção, pra manter a base de PP&E estável na perpetuidade (senão o valuation fica distorcido por base crescente/decrescente).

## Capex
- É **gasto capitalizado** (vai pro balanço, vira despesa via depreciação), e **saída de caixa** no ano da compra → subtrai no FCF.
- Histórico (cash flow statement, seção investing; MD&A) é bom proxy. Ajuste por estratégia: modo expansão (capex alto) vs colheita (capex baixo).
- Sem guidance: % de vendas em linha com histórico (top line growth exige base de ativos maior).

## Net Working Capital (NWC)
```
NWC = (A/R + Estoque + Despesas antecipadas/outros AC)
      − (A/P + Contas a pagar acumuladas + outros PC)
```
- Usa **ativos circulantes não-caixa** menos **passivos circulantes não-onerosos** (exclui caixa e dívida de curto prazo).
- **Δ NWC** é fonte/uso de caixa: aumento de NWC = **uso** de caixa (empresa em crescimento prende caixa em estoque/A/R); aumento de A/P = **fonte** de caixa.
- Δ NWC = NWC(n) − NWC(n−1). Aumento → subtrai no FCF; redução → soma.

### Projetar os componentes por ratios (recomendado)
| Componente | Ratio | Fórmula |
|---|---|---|
| Accounts Receivable | **DSO** (days sales outstanding) | A/R / Sales × 365 |
| Inventory | **DIH** (days inventory held) | Inventory / COGS × 365 |
| Accounts Payable | **DPO** (days payable outstanding) | A/P / COGS × 365 |
- DSO baixo = recebe rápido (bom). DIH baixo = gira estoque rápido (bom). DPO alto = segura pagamento (fonte de caixa).
- Projete A/R = DSO/365 × Sales; Estoque = DIH/365 × COGS; A/P = DPO/365 × COGS.
- Ratios: nível do último ano ou média de 3 anos; ajuste por guidance/tendência. Sem info detalhada → NWC como % de vendas (quick-and-dirty).
- **Cash Conversion Cycle** = DSO + DIH − DPO (dias que o caixa fica preso no ciclo operacional).
