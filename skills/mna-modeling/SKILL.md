---
name: mna-modeling
description: Modela fusões e aquisições — merger model, análise de accretion/dilution de EPS, purchase price e mix cash/debt/stock, purchase accounting (goodwill, write-ups, DTL), sinergias, e estrutura/processo do deal (sell-side, buy-side, taxable vs tax-free). Use quando o usuário quiser avaliar uma aquisição, montar um merger model, checar se um deal é accretive ou dilutive, definir o financiamento (cash/debt/stock), calcular goodwill e nova D&A, valorar sinergias, ou entender estrutura/processo de M&A. Gatilhos: "M&A", "merger", "aquisição", "accretion", "dilution", "merger model", "accretive", "dilutive", "goodwill", "sinergias", "purchase accounting", "exchange ratio", "collar", "contribution analysis", "poison pill", "takeover defense", "white knight", "sources and uses", "premium de controle".
---

# M&A Modeling

Skill para modelar fusões e aquisições no padrão de banco de investimento. A pergunta central: **o deal cria valor — e é accretive ou dilutive ao EPS do comprador?** Constrói-se em cima do 3-statement (skill financial-modeling) e do valuation (skill valuation-modeling).

## Quando usar
- Montar ou revisar um **merger model** (comprador + alvo combinados).
- Determinar se um deal é **accretive/dilutive** e por quê.
- Definir **purchase price** (prêmio/múltiplo) e o **mix cash/debt/stock**.
- Calcular **goodwill, asset write-ups, DTL e nova D&A** (purchase accounting).
- Valorar **sinergias** (revenue e cost) e achar o preço máximo defensável.
- Entender **estrutura/processo** (sell-side/buy-side, taxable vs tax-free, stock vs asset).

**Quando NÃO usar:** valuation standalone (DCF/comps) → valuation-modeling; LBO detalhado (sponsor) → usa esta + a lógica de LBO (floor). O 3-statement de cada empresa → financial-modeling.

## Princípios inegociáveis
1. **EPS é a métrica.** Accretion/dilution = Combined EPS vs EPS standalone do comprador.
2. **Sinergia é o motor.** O prêmio de controle só se justifica se sinergias + valor standalone > preço pago.
3. **O mix de financiamento decide.** Caixa (mais barato) → dívida → ações (mais caro). Ações de comprador "caro" comprando alvo "caro" → dilutivo.
4. **Foregone interest é custo real**, não custo de oportunidade.
5. **Sensibilize sempre** — preço da ação do comprador, nível de sinergia, prêmio.
6. **Disciplina com sinergias** — superestimar revenue synergies e subestimar custos de integração é o erro clássico.

## Workflow
Siga o build de 8 passos (`references/merger-model.md`):

### Passo 1 — Atalho de triagem (antes do modelo)
Cheque rápido com **Weighted Cost of Acquisition vs Yield do Seller** (ou a P/E rule para 100% stock) se o deal tende a accretive/dilutive. Ver `references/accretion-dilution.md`.

### Passo 2 — Purchase price e financiamento
Prêmio de controle (público, ~20–40%, confirmado por valuation) ou múltiplo (privado). Mix cash/debt/stock pela ordem de custo, respeitando caixa mínimo e Debt/EBITDA razoável. Monte **Sources & Uses**.

### Passo 3 — Purchase accounting
Calcule **goodwill** (preço − fair value dos ativos líquidos), **asset write-ups**, **DTL**, e a **nova D&A** incremental. Ver `references/purchase-accounting.md`.

### Passo 4 — Sinergias
Revenue (ceticismo) e cost (mais confiáveis), com phase-in, após imposto, menos custos de integração. Ver `references/synergies.md`.

### Passo 5 — Combinar e calcular accretion/dilution
Some os Pre-Tax Incomes, ajuste por juros (dívida nova), foregone interest (caixa), sinergias e nova D&A → Combined Net Income × (1 − tax do comprador) ÷ total shares = **Combined EPS** → accretion/dilution %.

### Passo 6 — Cash flow, desalavancagem e sensibilidade
Projete o caixa combinado, repagamento de dívida, Debt/EBITDA e EBITDA/juros. Monte tabelas de sensibilidade (preço, sinergia, % stock).

## Formato da saída
1. **Veredito:** accretive ou dilutive, em quanto (%), e o driver principal.
2. **Purchase price & Sources/Uses:** preço, prêmio, mix de financiamento.
3. **Accretion/dilution bridge:** dos EPS standalone ao Combined EPS, item a item.
4. **Purchase accounting:** goodwill, write-ups, DTL, nova D&A.
5. **Sinergias:** breakeven (sinergia mínima p/ neutralidade) e sensibilidade.
6. **Estrutura/risco:** forma de consideração, taxable/tax-free, riscos do deal.

Sempre mostre as premissas e sensibilize preço/sinergias.

## Documentos de apoio
- `references/merger-model.md` — build de 8 passos, purchase price, mix cash/debt/stock, Sources & Uses.
- `references/accretion-dilution.md` — Weighted Cost vs Yield, P/E rule (100% stock), efeitos de aquisição, pro forma EPS.
- `references/purchase-accounting.md` — goodwill, write-ups, DTL, nova D&A; stock vs asset, step-up, Section 338, taxable vs tax-free.
- `references/synergies.md` — revenue vs cost synergies, valoração, phase-in, custos de integração, disciplina.
- `references/deal-process-structure.md` — strategic vs financial buyer, sell-side/buy-side, etapas (NDA→LOI→DD→SPA→closing), estruturas legais, alocação de risco.
- `references/advanced-analyses.md` — contribution analysis, exchange ratios e collars (fixed/floating), como EV/equity mudam no M&A, e takeover defenses (poison pill flip-in/flip-over, staggered board, white knight).
- `references/worked-example.md` — caso A compra B com accretion/dilution calculado (atalho + pro forma EPS) e a variante 100% stock.
