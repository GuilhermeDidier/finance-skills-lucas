# Construindo o Merger Model (build de 8 passos)

> Fonte: M&A Deals / Merger Models Guide. O processo completo de montar o modelo de combinação comprador + alvo.

## Os 8 passos
1. **Projetar as demonstrações** de comprador e alvo — no mínimo as DREs projetadas e DFCs simplificadas. Modelo 3-statement completo ajuda, mas não é obrigatório (cash flow is king; ver skill financial-modeling).
2. **Estimar Purchase Price e financiamento** — prêmio sobre o preço (público) ou múltiplo (privado); mix Cash/Debt/Stock (ver abaixo).
3. **Sources & Uses + Purchase Price Allocation** — quanto o comprador "realmente paga" e os efeitos (nova D&A sobre write-ups, goodwill). Ver `purchase-accounting.md`.
4. **Combinar os Balanços** (opcional) — avalia a estrutura de capital pro forma (Debt/Equity/Cash razoáveis?).
5. **Calcular Sinergias** (opcional) — receita (cross/up-sell, expansão geográfica) e custo (consolidação de pessoal/instalações). Ver `synergies.md`.
6. **Combinar as DREs e calcular Accretion/Dilution** — somar Pre-Tax Incomes, ajustar por sinergias, D&A de write-ups e efeitos de Cash/Debt/Stock → Combined EPS. Ver `accretion-dilution.md`.
7. **Cash flow, repagamento de dívida e ratios** — projetar o caixa combinado, desalavancagem, Debt/EBITDA e EBITDA/juros (viabilidade).
8. **Sensibilidade** — accretion/dilution sob diferentes preços de compra, níveis de sinergia e preço da ação do comprador.

## Purchase Price e o mix Cash / Debt / Stock
- **Público:** Purchase Equity Value = preço atual × (1 + prêmio de controle) × ações. Confirme com DCF/comps/precedentes que o preço é razoável e que o prêmio está na faixa de deals comparáveis (tipicamente ~20–40%).
- **Privado:** múltiplo de EBITDA/receita.
- **Por que Equity Value (não Enterprise Value):** o piso é pagar 100% das ações do Seller. O comprador raramente "repaga" a dívida do alvo — refinancia/substitui. Itens como pensão e minority não mudam o funding. (Com ajustes de fees e excess cash, o "preço real" fica perto do Purchase Equity Value.)

**Ordem do funding (do mais barato ao mais caro):**
1. **Caixa** do comprador (mais barato) — use o máximo possível, respeitando um caixa mínimo.
2. **Dívida** nova — até um Debt/EBITDA combinado razoável (peers em 4–5x, p.ex.). EBITDA do alvo aumenta a capacidade.
3. **Stock** — sem limite técnico, mas: ninguém quer ceder controle, e empresas frequentemente emitem ações só até onde o deal continua accretive.

## Sources & Uses
Toda transação tem que **balancear fontes = usos**:
| Uses (para onde vai o $) | Sources (de onde vem) |
|---|---|
| Purchase Equity Value do alvo | Caixa do comprador |
| Refinanciamento da dívida do alvo | Nova dívida emitida |
| Transaction fees (advisory, legal) | Novas ações (stock) |
| Financing fees | (Caixa do alvo, se usado) |

## Tax rate e ações
- Combined Net Income = Combined Pre-Tax Income × (1 − tax rate do **comprador**) — padrão (alvo vira subsidiária). Na vida real pode diferir (jurisdições).
- Ações emitidas = Purchase Equity Value × %Stock / preço do comprador. As **ações do Seller somem**.

## Conexão com outras skills
- O 3-statement de cada empresa vem da skill **financial-modeling**.
- A confirmação do preço (DCF/comps) vem da **valuation-modeling**.
- Comprador **financial sponsor** (PE) → o teto que ele paga é dado pela análise de **LBO** (define o "floor" de valuation) → ver skill **lbo-modeling**.
