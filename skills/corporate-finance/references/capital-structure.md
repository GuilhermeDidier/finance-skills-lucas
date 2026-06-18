# Estrutura de Capital — Modigliani-Miller, Trade-off e Pecking Order

> Fonte: Strategic Issues in Finance (papers de Modigliani & Miller) + McKinsey/Koller. Quanto de dívida vs equity uma empresa deve ter — e por que (na teoria) e como (na prática).

## Modigliani-Miller (o ponto de partida teórico)
**Proposição I (sem impostos):** em mercados perfeitos, o **valor da empresa independe da estrutura de capital**. O bolo é o mesmo, não importa como se fatia entre dívida e equity. O valor vem dos ativos/fluxos de caixa, não do financiamento.

**Proposição II:** o **custo do equity sobe linearmente com a alavancagem** (mais dívida → equity mais arriscado → exige retorno maior), de forma que o **WACC permanece constante**. Não há "almoço grátis" em trocar equity caro por dívida barata — o equity remanescente fica mais caro na exata medida.

> Implicação radical (e irrealista): se MM valesse literalmente, a estrutura de capital seria irrelevante. As **imperfeições do mundo real** é que criam uma estrutura ótima.

## Com impostos → o tax shield
Juros são **dedutíveis** → a dívida cria um **tax shield** (escudo fiscal) que adiciona valor:
```
Valor alavancado = Valor desalavancado + PV(tax shield)
PV do tax shield (perpétuo, simplificado) = Dívida × alíquota
```
Isoladamente, isso empurraria a empresa a 100% dívida. Mas...

## Trade-off Theory → estrutura ótima
O benefício do tax shield é compensado pelos **custos de financial distress** (falência, custos de agência, perda de clientes/fornecedores, decisões míopes sob estresse):
```
Valor = Valor desalavancado + PV(tax shield) − PV(custos de financial distress)
```
- A **estrutura ótima** maximiza esse valor (= minimiza o WACC). Conforme se adiciona dívida, o WACC cai (dívida barata pós-imposto) **até** o ponto em que o risco de distress encarece dívida E equity e o WACC volta a subir (ver `../valuation-modeling/references/wacc-capm.md`).
- Empresas com caixa estável e ativos tangíveis (colateral) suportam mais dívida; negócios voláteis/intangíveis, menos.

## Pecking Order Theory (Myers)
Por **assimetria de informação** (gestão sabe mais que o mercado), há uma hierarquia de financiamento:
1. **Lucros retidos** (recurso interno, sem sinal negativo).
2. **Dívida** (sinal moderado).
3. **Equity** por último (emitir ações sinaliza que a gestão acha a ação cara → mercado reage mal).
- Explica por que empresas lucrativas às vezes têm pouca dívida (financiam-se internamente).

## Na prática (o que importa pro banker)
- Alvo de **estrutura-alvo** (não a atual) consistente com a estratégia (ver WACC em valuation).
- Métricas dos lenders: **Debt/EBITDA**, **EBITDA/juros (interest coverage)**, rating de crédito.
- **Capacidade de dívida (debt capacity):** quanto a empresa serve confortavelmente sob estresse — base do dimensionamento em LBO (ver skill lbo-modeling).
- Flexibilidade financeira: manter "pólvora seca" (dry powder) para oportunidades/choques tem valor real (não capturado por MM).
- **Não confundir** redução de WACC com criação de valor: recapitalizar não cria valor por si só (conservation of value) — só muda quem fica com o tax shield e o risco.
