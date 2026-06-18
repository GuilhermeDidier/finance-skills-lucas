# Renda Fixa Brasileira — Instrumentos e Convenções

> Fonte: Securato, *Cálculo Financeiro das Tesourarias*. O mercado brasileiro tem convenções próprias (DU/252, indexadores) — domínio essencial para o Lucas.

## Taxas de referência
- **Selic:** taxa básica (meta definida pelo Copom). **Selic over** = taxa efetiva diária do overnight (operações lastreadas em títulos públicos, sistema **Selic**).
- **CDI (DI):** taxa dos depósitos interbancários (registrados na **Cetip/B3**). Na prática, **CDI ≈ Selic over** (andam quase coladas). É o **benchmark** da renda fixa privada.
- Convenção: anualizadas em **252 dias úteis**: `(1 + i_ano) = (1 + i_dia)^252`.

## Títulos públicos federais (Tesouro)
| Título | Tipo | Indexador | Cupom | Preço |
|---|---|---|---|---|
| **LTN** (Tesouro Prefixado) | prefixado | — | zero-cupom | VN/(1+i)^(du/252) |
| **NTN-F** (Tesouro Prefixado c/ juros) | prefixado | — | semestral | VP dos cupons + principal |
| **LFT** (Tesouro Selic) | pós-fixado | **Selic** | zero-cupom | VN corrigido pela Selic; baixa volatilidade |
| **NTN-B** (Tesouro IPCA+ c/ juros) | híbrido | **IPCA** | semestral | VN corrigido por IPCA + cupom real |
| **NTN-B Principal** (Tesouro IPCA+) | híbrido | **IPCA** | zero-cupom | VN corrigido por IPCA |

- **Prefixado (LTN/NTN-F):** você trava a taxa nominal; sofre marcação a mercado se a curva mexer.
- **Pós-fixado (LFT):** acompanha a Selic → preço estável (baixa duration de taxa nominal); ideal para caixa.
- **Inflação (NTN-B):** protege o poder de compra (IPCA) + juro real; duration alta nas longas → muito sensível ao juro real.

## Renda fixa privada
- **CDB:** depósito bancário; tipicamente **% do CDI** (ex.: 110% do CDI) ou prefixado/IPCA+. Relação CDB↔CDI é central (Securato cap. 5).
- **LCI/LCA, debêntures, CRI/CRA:** crédito privado; debêntures podem ser % CDI, CDI+spread, ou IPCA+. Carregam **credit spread** (ver `yield-curve-and-credit.md`).

## DI Futuro (B3) — o instrumento de hedge/posição
- Contrato futuro de taxa de juro (DI de 1 dia acumulado) — o mais líquido para **operar e fazer hedge** de taxa prefixada.
- Cotado em **taxa** (% a.a., 252); o PU do contrato = 100.000/(1+i)^(du/252).
- Use o **DV01** da posição ÷ DV01 do DI futuro para dimensionar o hedge (ver `duration-convexity.md`).
- A curva de juros prefixada brasileira é construída a partir dos **vértices de DI futuro** (ver `yield-curve-and-credit.md`).

## Marcação a Mercado (MtM)
- Reprecificar o título pela **taxa de mercado atual** (não a da compra). Prefixados e NTN-B longas oscilam muito: se a curva sobe, o PU cai (marcação negativa) — mesmo sem default.
- Quem **carrega até o vencimento** realiza a taxa contratada; quem vende antes realiza o MtM. Tesouraria/fundos marcam diariamente.
- A volatilidade do MtM é função da **duration** do papel.

## Cupom cambial
Taxa de juro em dólar implícita no mercado brasileiro (cupom cambial = diferencial entre a taxa local e a variação cambial). Securato (cap. 10) deriva a obtenção prática a partir de preços. Relevante para operações dólar-real e hedge cambial.

## Conectar
A matemática (DU/252, juros compostos) está em `fixed-income-math.md`; precificação em `bond-pricing.md`; risco em `duration-convexity.md`. Emissão/estruturação de dívida (mercado primário) → skill **dcm-modeling**.
