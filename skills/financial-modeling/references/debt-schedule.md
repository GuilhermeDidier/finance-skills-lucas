# Debt Schedule, Juros e Circularidade

> Fonte: Rosenbaum & Pearl, Cap. 5 (Build Debt Schedule). O componente que integra o financiamento às 3 demonstrações e a fonte da circularidade clássica.

## O que o debt schedule faz
Aplica o caixa gerado para fazer repagamentos, calculando os saldos inicial e final de cada tranche de dívida. Ele permite:
- completar a DRE de **EBIT → net income** (via juros);
- completar a seção de **dívida e PL do balanço** (ending balances);
- completar a seção de **financiamento da DFC** (repagamentos/captações).

**Ligações:** repagamentos → financing (DFC); ending debt → balanço; juros → DRE.

## Ordem das tranches (senioridade)
Construa na ordem de segurança/senioridade: **revolver → term loans (TLA, TLB) → bonds (sênior, subordinado)**. Repagamentos opcionais seguem essa cascata (paga o mais sênior/caro primeiro).

## Estrutura de cada tranche
```
Saldo inicial
(−) Repagamento mandatório (amortização contratual, ex.: 1% a.a. do TLB)
(−) Repagamento opcional (cash sweep)
( = ) Saldo final
Juros do ano = taxa × saldo médio (ou inicial)
```
- **Saldo médio** = (inicial + final)/2 → mais preciso, mas **gera circularidade** (juros dependem do final, que depende do repagamento, que depende do caixa...). Saldo inicial evita circularidade ao custo de menos precisão.

## Taxas: fixa vs flutuante
- **Flutuante** (revolver, term loans): taxa = índice base + spread fixo. O índice base era **LIBOR**; desde 2021–2023 migrou para **SOFR** (Secured Overnight Financing Rate). Use a forward curve (Bloomberg).
  - Ex.: revolver a "S+425 bps" com base 1,55% → 5,80%.
- **Fixa** (bonds): cupom fixo sobre o principal.

## Cash Available for Debt Repayment (a cascata)
```
Cash flow das operações
(+/−) Cash flow de investimentos (capex etc.)
( = ) Cash Available for Debt Repayment (levered free cash flow)
(−)   Repagamentos mandatórios (amortização contratual)
( = ) Cash Available for Optional Debt Repayment
(−)   Repagamentos opcionais (cash sweep, na ordem de senioridade)
( = ) Variação de caixa
```
- **Cash sweep:** o excedente após mandatórios é usado para pré-pagar dívida (acelera desalavancagem — motor de retorno em LBO).
- **MinCash:** pode-se manter um caixa mínimo no balanço (input em $), não usado para sweep.
- **Revolver:** se o caixa fica negativo num ano, o revolver é sacado para cobrir (e repago quando sobra caixa). É a "válvula de escape" que evita caixa negativo.

## Circularidade — o loop e como resolver
```
Juros → Net Income → Cash Available for Repayment → Repagamento → Saldo de dívida → Juros (loop)
```
**Soluções:**
1. **Iterative calculation no Excel:** Options → Formulas → Manual → "Enable iterative calculation", máx 100 iterações. (Método Rosenbaum.) Resolve o loop numericamente.
2. **Circuit breaker:** um switch (célula 1/0) que zera os juros temporariamente, quebrando o loop para depurar erros (#REF!/#DIV0 que "travam" a iteração). Volte a ligar depois.
3. **Saldo inicial para juros:** evita a circularidade de raiz (menos preciso, mas robusto). Comum em modelos rápidos.

> ⚠️ Circularidade + um erro de fórmula (#DIV/0!, #REF!) faz o modelo inteiro "explodir" em erros que não somem nem corrigindo a célula. Use o circuit breaker para limpar.

## Outra circularidade comum
Valor por ação ↔ fully diluted shares (TSM): o preço implícito depende das ações diluídas, que dependem do preço (opções in-the-money). Mesma solução: iterative calculation. (Ver `../valuation-modeling/references/mechanics.md`.)
