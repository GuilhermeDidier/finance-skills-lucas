---
name: financial-modeling
description: Constrói e audita modelos financeiros de 3 demonstrações (DRE, Balanço, DFC integrados) dirigidos por premissas — projeção de receita/margens, schedules de PP&E, working capital e dívida, juros e circularidade, error checks, cenários e qualidade dos lucros. Use quando o usuário quiser montar/revisar um modelo operacional, projetar demonstrações financeiras, construir schedules (depreciação, working capital, debt), resolver circularidade, fazer o balanço fechar, montar cenários/sensibilidade, ou checar a qualidade do histórico antes de projetar. Gatilhos: "modelo financeiro", "3-statement", "projeção", "DRE/balanço/DFC", "working capital", "debt schedule", "circularidade", "o balanço não fecha", "cenários", "drivers", "premissas".
---

# Financial Modeling

Skill para construir e auditar o **modelo de 3 demonstrações** — a fundação de todo trabalho quantitativo em IB (DCF, LBO, M&A são camadas em cima disto). Princípio que governa tudo: **as três demonstrações são um sistema integrado; se o balanço não fecha, o modelo está errado.**

## Quando usar
- Montar um modelo operacional (3-statement) do zero ou a partir de um template.
- Projetar receita, margens, e construir os schedules (PP&E, working capital, dívida).
- Calcular juros e resolver **circularidade**.
- Fazer o **balanço fechar** (balance check) e rodar error checks.
- Montar **cenários** (base/bull/bear) e tabelas de **sensibilidade**.
- **Limpar o histórico** (qualidade dos lucros) antes de projetar.

**Quando NÃO usar:** valuation/DCF/comps em si → skill valuation-modeling; merger/accretion-dilution → m&a-modeling. (Mas o 3-statement aqui é o que alimenta todas elas.)

## Princípios inegociáveis
1. **Ativo = Passivo + PL, sempre.** Balance check = 0 em todos os anos, ou pare.
2. **Separe inputs de cálculos.** Premissas em azul, fórmulas em preto, links em verde. Zero hardcode dentro de fórmula.
3. **Toda premissa tem justificativa** e é **internamente consistente** (crescer receita exige capex e working capital).
4. **A DFC é a espinha dorsal** — liga DRE e balanço; o caixa final fecha no balanço.
5. **Lixo entra, lixo sai.** Limpe o histórico (scrubbing/qualidade dos lucros) antes de projetar.
6. **Auditável > esperto.** Quebre fórmulas longas; um sênior tem que conseguir rastrear.

## Workflow

### Passo 0 — Limpar o histórico
Antes de projetar, ajuste o histórico por não-recorrentes e cheque a **qualidade dos lucros** (ver `references/quality-of-earnings.md`): net income vs cash flow operacional, tendência de DSO/DIH, capitalização de custos. Projete sobre números **reais**, não reportados.

### Passo 1 — Montar a estrutura
Insira 3+ anos de histórico (DRE, balanço, DFC). Crie a aba de **premissas/drivers**. Ver arquitetura e ligações em `references/three-statement-model.md`.

### Passo 2 — Projetar a DRE até EBIT
Receita (growth ou volume×preço) → COGS/SG&A (% de vendas) → EBITDA → D&A → EBIT. Drivers e regras em `references/projection-drivers.md`.

### Passo 3 — Schedules de apoio
- **PP&E:** final = inicial + capex − depreciação.
- **Working capital:** A/R (DSO), estoque (DIH), A/P (DPO) → Δ NWC.
- **Debt schedule:** saldos, repagamentos (mandatório + cash sweep), juros. Ver `references/debt-schedule.md`.

### Passo 4 — Fechar DRE → DFC → Balanço
EBIT − juros (do debt schedule) → net income. Monte a DFC (CFO + CFI + CFF = Δ caixa). Preencha o balanço (caixa da DFC, schedules, PL = PL inicial + NI − dividendos).

### Passo 5 — Resolver circularidade
Juros ↔ caixa ↔ dívida cria loop. Ative **iterative calculation** no Excel e tenha um **circuit breaker** para depurar. Ver `references/debt-schedule.md`.

### Passo 6 — Checar e estressar
**Balance check = 0.** Caixa não-negativo (senão acione revolver). Δ caixa da DFC = variação do caixa no balanço. Monte cenários e sensibilidade. Ver `references/best-practices.md`.

## Formato da saída
1. **Premissas-chave** declaradas (growth, margens, DSO/DIH/DPO, capex, juros, alíquota).
2. **As 3 demonstrações projetadas** (DRE, Balanço, DFC), ano a ano.
3. **Schedules** (PP&E, working capital, dívida).
4. **Error checks** visíveis (balance check, caixa, conciliação DFC↔balanço).
5. **Cenários/sensibilidade** nas variáveis que mais movem o resultado.
6. **Ressalvas de qualidade** — ajustes feitos no histórico e premissas frágeis.

Sempre mostre o balance check e explique as premissas.

## Documentos de apoio
- `references/three-statement-model.md` — arquitetura, ligações entre as 3 demonstrações, ordem de construção, circularidade.
- `references/projection-drivers.md` — projeção de receita, COGS/SG&A, D&A, capex, NWC (DSO/DIH/DPO, cash conversion cycle).
- `references/debt-schedule.md` — debt schedule, juros (SOFR/fixo), cash sweep, revolver, circularidade e soluções.
- `references/best-practices.md` — layout, convenção de cores, error checks, cenários, e convenções contábeis (IFRS 16 leases, IAS 19 pensões, minorities/associates, tax).
- `references/quality-of-earnings.md` — as 7 categorias de shenanigans (Schilit) e red flags para limpar o histórico.
- `references/worked-example.md` — mini 3-statement de 1 ano com as ligações e o balance check fechando.
