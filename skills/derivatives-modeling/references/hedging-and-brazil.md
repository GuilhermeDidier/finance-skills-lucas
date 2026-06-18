# Hedge na Prática e o Mercado Brasileiro

> Fonte: Securato + convenções B3. Como usar derivativos para gerir risco — e os instrumentos do mercado brasileiro.

## Princípios de hedge
- **Objetivo:** reduzir uma exposição indesejada (taxa, câmbio, commodity, crédito), não especular.
- **Hedge ratio:** quanto do instrumento de hedge por unidade de exposição. Para risco de taxa, dimensione por **DV01** (DV01 da posição ÷ DV01 do hedge). Para opções, por **delta**.
- **Hedge perfeito vs basis risk:** se o instrumento não casa exatamente o ativo (prazo/índice diferente), sobra **basis risk**.
- **Custo do hedge:** futuros/forwards têm custo de carrego; opções custam o prêmio (mas limitam o downside sem cortar o upside).
- **Contabilidade de hedge** (IFRS 9 / CPC 48): hedge accounting evita descasamento de resultado (marca o derivativo junto com o item protegido), se documentado e efetivo.

## Tipos de hedge
- **Risco de taxa de juros:** vender **DI futuro** ou entrar em **swap DI×pré** para travar custo de dívida flutuante. (Carteira de renda fixa → casar DV01.)
- **Risco cambial:** **dólar futuro**, NDF (non-deliverable forward), swap cambial, ou opções de dólar. **Cupom cambial (DDI)** para a perna de juro em dólar.
- **Risco de equity:** vender índice futuro (**Ibovespa futuro**) ou comprar puts (protective put).
- **Risco de commodity:** futuros agro/metais (B3/CME).
- **Risco de crédito:** **CDS**.

## Instrumentos da B3 (mercado brasileiro)
- **DI futuro** — o mais líquido; juro prefixado (curva pré). Futuro de **Selic** + opções.
- **Dólar futuro** e **mini dólar**; **DDI** (cupom cambial); **FRC** (FRA de cupom).
- **Ibovespa futuro** e **mini índice**; **opções sobre ações e sobre Ibovespa**.
- **Swaps de balcão** registrados (DI×pré, DI×dólar, DI×IPCA).
- **NDF** (a termo de moeda, OTC) — muito usado por empresas para hedge cambial.
- Câmara da B3 atua como **contraparte central (CCP)** com margem/garantias → mitiga risco de contraparte.

## Especulação e alavancagem (o outro lado)
Derivativos dão exposição alavancada (paga-se margem, não o notional). Ótimo para hedge; perigoso sem gestão de risco — perdas podem exceder o capital. Tesourarias operam com **limites (VaR, DV01, Greeks)**.

## Real options (a ponte com corporate finance)
A teoria de opções valora a **flexibilidade gerencial** (adiar/expandir/abandonar um projeto) — ver skill **corporate-finance** (`capital-budgeting.md`). A mesma matemática de `black-scholes-greeks.md` se aplica a decisões reais, não só financeiras.

## Conectar
Futuros → `forwards-futures.md`; opções/Greeks → `options.md` e `black-scholes-greeks.md`; swaps → `swaps.md`. Curva/DV01 → skill **bond-modeling**.
