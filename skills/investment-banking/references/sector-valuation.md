# Valuation por Setor — Onde as Regras Mudam

> Fonte: 400 Questions IB Interview Guide (2025), seções de coverage groups. As metodologias padrão (comps, precedentes, DCF) **não** se aplicam igual em todo setor. Saber as diferenças é o que separa um banker genérico de um de cobertura. Detalhe de valuation geral → skill valuation-modeling.

## FIG — Bancos e Seguradoras (o grupo mais técnico)
**Bancos comerciais** ganham pelo **spread de juros** (emprestam, captam via depósitos/dívida). Diferenças radicais:
- **Balance Sheet first:** o balanço dirige a performance; projeta-se o balanço primeiro.
- **Só Equity Value:** não dá para separar operação de financiamento → **Enterprise Value não se aplica**. Use Equity Value e múltiplos de equity.
- **DDM em vez de DCF:** "free cash flow" não significa nada (capex/ΔNWC não são reinvestimento) → use **Dividend Discount Model**, **cost of equity** (não WACC), dividendos como proxy de FCF.
- **Múltiplos:** **P/BV, P/TBV, P/E** (não EV/EBITDA). Forte correlação **ROE ↔ P/BV**:
  ```
  P/BV  = (ROE − g) / (Cost of Equity − g)
  P/TBV = (ROTCE − g) / (Cost of Equity − g)
  ```
  Banco possivelmente mal precificado: ROE igual aos pares mas P/BV bem diferente.
- **Regulatory Capital:** buffer (Tangible Common Equity ajustado) contra perdas inesperadas; restringe crescimento. Perdas esperadas vão em **Allowance for Loan Losses** (banco) / **Claims Reserve** (seguro).
- **Seguradoras:** parecidas, mas projeção parte dos **prêmios** (DRE), não do balanço; Statutory Accounting; **Embedded Value** para vida; capital via RBC Ratio.
- **Asset managers / broker-dealers / fintech:** operam como empresas normais (fees/transações) → EV/EBITDA e DCF unlevered funcionam.

## REITs — Real Estate Investment Trusts
- Distribuem **90%+ do lucro** como dividendos → **pouco/zero imposto corporativo**; 75%+ da receita e dos ativos em real estate.
- **Múltiplos próprios:** **FFO** (Funds from Operations) e **AFFO**, **P/FFO** e **P/AFFO** (EV/EBITDA ainda válido). FFO ≈ net income + D&A imobiliária − ganhos de venda (a depreciação imobiliária distorce o lucro contábil).
- **NAV Model** (central p/ REITs US, que registram a custo histórico − depreciação):
  1. Projete o **NOI** forward 12 meses → divida por um **Cap Rate** → Market Value dos ativos imobiliários.
  2. Some outros ativos a fair value; marque os passivos (dívida) a mercado e subtraia → **NAV** → ÷ ações = **NAV/ação** vs preço.
- **US vs IFRS:** IFRS marca propriedades a fair value todo ano (NAV fácil); US deprecia a custo histórico (NAV exige cálculo).
- Às vezes usa-se **Levered DCF** (dívida/serviço previsíveis).

## Oil & Gas
Verticais: **E&P/upstream**, **midstream** (storage/transport), **downstream** (refino), oilfield services, integradas.
- **E&P (o mais diferente):** preços fora do controle, ativos que **depletam**, altamente cíclico.
  - **NAV Model** = DCF no nível do **ativo (poço)**, **sem terminal value**, descontado ao **10% padrão da indústria**. Modela declínio de produção (IP rate → declina até o EUR), cenários de commodity (high/mid/low), D&C costs, LOE, royalties/working interest.
  - Múltiplos: **EV/EBITDAX** (X = exploration expense), **EV/Proved Reserves**, **EV/Daily Production**.
  - **Reserve Life Ratio** = Proved Reserves / produção anual; **Production Replacement Ratio**. Cuidado: empresa que infla NAV contando reservas Probable/Possible (não só Proved).
- **Midstream:** muitas são **MLPs** (pass-through, sem imposto corporativo; distribuem quase todo o cash flow; emitem dívida/equity constantemente) → múltiplos de **yield** e **DDM** em vez de DCF.

## Power & Utilities
- **Regulated utilities:** retorno permitido sobre a **rate base** (ativos regulados) — crescimento previsível, dividendos altos. Valua-se por **P/E, dividend yield, e EV/EBITDA**, com foco no **rate base growth** e no **allowed ROE** do regulador.
- **Independent power / renewables:** mais como project finance (fluxos contratados via PPAs); DCF por projeto/ativo.

## Tech / SaaS (normal companies, mas com KPIs próprios)
- Empresas de software de alto crescimento: foco em **receita recorrente (ARR/MRR)**, **EV/Revenue** e **EV/ARR** (lucro/EBITDA muitas vezes negativo no início), **Rule of 40** (crescimento % + margem FCF % ≥ 40), **net revenue retention**, **CAC/LTV**, **magic number**.
- Valuation por crescimento/intangível → skill valuation-modeling (`growth-and-emerging-markets.md`); intangíveis distorcem múltiplos (`comparables.md`).

## Regra geral para reconhecer
Pergunte: a empresa ganha dinheiro pelo **balanço** (banco/seguro → Equity Value, DDM, P/BV) ou pela **operação** (normal → EV, DCF, EV/EBITDA)? Os ativos **depletam** (E&P → NAV sem TV) ou são **regulados** (utility → rate base)? É **pass-through** (REIT/MLP → FFO/yield/distribuições)?
