# Capital Budgeting — Avaliação de Investimentos (NPV, IRR, Real Options)

> Fonte: Strategic Issues in Finance (Shapiro; o capítulo de capital budgeting) + prática. Como decidir se um projeto/investimento cria valor — a régua nível-projeto por trás do "ROIC > WACC".

## A régua de ouro: NPV > 0
Um investimento cria valor para o acionista **apenas se o retorno exceder o retorno exigido** (hurdle rate = custo de capital). Se o retorno só iguala o exigido, o investidor apenas trocou um fluxo de caixa presente por outro de igual valor — **não ficou melhor**.
```
NPV = Σ FCFt / (1 + r)^t − Investimento inicial      (r = hurdle rate / WACC do projeto)
Regra: invista se NPV > 0; entre mutuamente exclusivos, escolha o maior NPV.
```

## De onde vem um NPV positivo (o insight estratégico de Shapiro)
Em **mercado perfeitamente competitivo é impossível** sustentar retorno acima do normal — a concorrência elimina o "economic rent". Portanto:
- **NPV positivo só existe explorando uma imperfeição** = uma **vantagem competitiva sustentável** (ver `strategy-and-power.md` e `../valuation-modeling/references/moat.md`).
- **Papel estratégico da função financeira:** identificar e explicar **a fonte** de cada NPV positivo (atual e projetado). Um NPV positivo sem uma fonte de vantagem identificável é suspeito — provavelmente premissa otimista.
- Finanças é **segundo-ordem**: a criação de valor real vem do produto/mercado (vantagem competitiva), não de engenharia financeira.

## Expectativas já estão no preço (a "expectations treadmill")
- O mercado **já capitaliza** o desempenho superior esperado. As 13 empresas de ROE alto consistente de Shapiro deram retorno **medíocre** aos investidores — porque o ROE alto já estava no preço inicial.
- Implicação: valor para o acionista só cresce ao **superar** as expectativas embutidas no preço; e a gestão deve **gerir as expectativas** para não virarem irrealistas (cujo não-cumprimento é punido rápido).
- Liga com `../valuation-modeling/references/value-drivers.md` (preço = parte atual + parte de valor futuro antecipado).

## Cash flow > lucro contábil
A criação de valor se mede em **fluxo de caixa** descontado, não em profit/EPS/ROE contábil. Reconcilie discrepâncias entre o valuation por earnings e por DCF (ver skill valuation-modeling).

## O toolkit (métricas e armadilhas)
| Métrica | O que é | Regra | Armadilha |
|---|---|---|---|
| **NPV** | VP dos fluxos − investimento | > 0 | A melhor; exige estimar o hurdle rate corretamente |
| **IRR** | taxa que zera o NPV | > hurdle rate | Múltiplas IRRs (fluxos com sinais alternados); assume reinvestimento à própria IRR; ignora escala → use **NPV** para decidir entre projetos |
| **Payback** | tempo p/ recuperar o investimento | < limite | Ignora valor do dinheiro no tempo e fluxos após o payback; só como filtro de liquidez/risco |
| **Discounted payback** | payback com fluxos descontados | < limite | Ainda ignora fluxos após o corte |
| **Profitability Index** | VP dos fluxos / investimento | > 1 | Útil sob racionamento de capital (ranquear por valor por $ investido) |
| **MIRR** | IRR com reinvestimento ao custo de capital | > hurdle | Corrige a premissa de reinvestimento da IRR |

- **NPV é o critério soberano.** IRR é intuitiva mas engana em escala, timing e sinais → quando conflitar com NPV, siga o NPV.
- **Hurdle rate:** WACC do projeto, ajustado ao risco **do projeto** (não o da empresa) — um projeto mais arriscado exige hurdle maior. Cuidado em usar o WACC corporativo para tudo.

## Real Options — o valor da flexibilidade
O DCF/NPV tradicional **subestima** projetos com flexibilidade gerencial, porque assume um caminho fixo. O valor de **poder decidir depois** é uma opção (avaliável por lógica Black-Scholes):
- **Opção de adiar (defer):** esperar por mais informação antes de comprometer capital.
- **Opção de expandir / growth option:** um projeto de NPV baixo pode valer a pena se abrir a porta para um grande follow-on (ex.: P&D, entrar num mercado).
- **Opção de abandonar:** poder sair e recuperar valor residual limita o downside.
- **Opção de contrair/switch:** ajustar escala ou inputs/outputs.
- Inputs análogos a uma call: valor do ativo subjacente (VP dos fluxos), strike (investimento), volatilidade, tempo até decidir, taxa livre de risco. Mais incerteza → **mais** valor de opção (ao contrário do DCF, onde mais risco reduz valor).
- Use quando há **alta incerteza + flexibilidade real** (P&D, recursos naturais, faseamento, startups) — ver também `../valuation-modeling/references/growth-and-emerging-markets.md`.

## Conectar com capital allocation
Capital budgeting é o nível-projeto; **capital allocation** (`capital-allocation.md`) é a carteira de decisões (reinvestir vs M&A vs devolver caixa). A disciplina é a mesma: só comprometer capital onde o retorno ajustado ao risco supera o custo de capital, e a fonte de valor é uma vantagem competitiva real.
