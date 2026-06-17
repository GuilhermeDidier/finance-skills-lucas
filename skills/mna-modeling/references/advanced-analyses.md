# Análises Avançadas de M&A — Contribution, Exchange Ratios, Defesas

> Fontes: M&A Deals / Merger Models Guide (Key Rules #5 e #7) + JP Morgan M&A Reference Manual (Seção VI). Complementam o accretion/dilution e o merger model.

## Relative Contribution Analysis
**Ideia:** se o comprador contribui X% das métricas financeiras da combinada, deveria possuir ~X% dela. Se possui menos → pode estar pagando demais; se mais → pagando de menos.
- Some as métricas (Revenue, EBITDA, EBIT, Net Income) de comprador + alvo e calcule a **% de contribuição** de cada um.
- **Combined Pro-Forma Enterprise Value** por métrica = EV atual do comprador / %contribuição do comprador. Ex.: EV comprador $3bi, contribui 75% da receita → pro-forma EV "deveria" ser $3bi / 75% = **$4bi**.
- Para métricas de equity (Net Income): use o Equity Value atual / %contribuição.
- **Implied value do alvo** = Combined Pro-Forma EV − EV atual do comprador → ponte para equity → ÷ ações do alvo = **preço/ação implícito** → ÷ preço do comprador = **exchange ratio implícito**.
- **Output-chave:** gráfico do **offer price vs implied share price** — mostra se o comprador paga demais/de menos.

**Quando é relevante:**
- **Deals 100% stock** (toda mudança de preço afeta a propriedade direta).
- **Mergers of equals (MOE)** (empresas de tamanho similar, quase sempre 100% stock).
- **M&A de empresa privada** (privados ligam menos pra EPS → contribution é a metodologia central).
- **Majority-stock** (≥50% stock).
- ❌ **Não** relevante em 100% cash/debt (vendedor não fica com participação).
- ⚠️ Não inclui sinergias — que podem mudar a conclusão dramaticamente.

## Exchange Ratios e Collars
Em deals com componente de ações, o preço costuma ser fixado por **exchange ratio**, não por % de stock — e o preço da ação do comprador muda entre anúncio e fechamento. Estruturas:

| Estrutura | O que é fixo | O que varia | Quem prefere |
|---|---|---|---|
| **Fixed Exchange Ratio** | nº de ações emitidas | **preço de compra** (e a propriedade do vendedor é fixa) | **Comprador** (limita diluição; certeza de ações). Pode sinalizar falta de confiança nas próprias ações. |
| **Floating Exchange Ratio** | **preço de compra** | nº de ações (e a propriedade varia) | **Vendedor** (se acha que a ação do comprador vai cair: mesmo preço, mais % da combinada) |

- **Fixed 2:1, alvo com 10M ações** → comprador sempre emite 20M; se a ação do comprador vai de $10→$5 ou →$15, o preço varia ($100M a $300M) mas a propriedade do vendedor é fixa (~16,7%).
- **Floating a $220M** → vendedor sempre recebe $220M, mas nº de ações varia com o preço do comprador.

### Collar
Combina fixed e floating dentro de faixas de preço, limitando o risco:
- **Fixed ratio com collar:** propriedade fixa numa faixa; fora dela, trava um preço **máximo/mínimo** (ajusta nº de ações).
- **Floating ratio com collar:** preço fixo numa faixa; fora dela, trava nº de ações **máximo/mínimo**.
- **Útil quando:** alvo é ~10–30% do comprador (nem MOE nem aquisiçãozinha); querem proteção de preço de cash + benefício fiscal de stock; deal cross-border (collar reduz risco de FX); ação do comprador volátil ou as partes discordam da direção do preço.
- **Earn-out:** parte do preço contingente a metas futuras do vendedor — ponte de avaliação quando as partes discordam do valor.

## Como EV e Equity Value mudam no M&A (Key Rule #5)
- **100% cash:** EV do comprador sobe pelo EV do alvo; o caixa vira o negócio do alvo (troca de ativo). Equity value do comprador muda pelo **NPV do deal** (sinergias − prêmio).
- **100% stock:** ações novas aumentam o equity value; o EV combinado ≈ soma dos EVs ± sinergias.
- **Dívida:** aumenta EV e net debt; reduz equity value via juros.
- Regra: foque em **por ação** — a criação de valor real aparece no EPS e no valor por ação, não no tamanho absoluto.

## Takeover Defenses (JP Morgan, Seção VI)
Defesas contra aquisição hostil — relevantes no buy-side hostil e na assessoria de defesa.

### Defesas estruturais (charter/bylaws)
- **Classified (staggered) board** — conselho em 3 classes, só 1/3 eleito por ano → atrasa controle do board.
- **Blank check preferred** — board emite preferred sem aprovação dos acionistas.
- **Limitar ação por written consent** e **supermajority** (2/3, 75%) para aprovar merger.
- **Fair price provision** — exige preço justo aos minoritários (neutraliza two-tier offers).
- **Anti-greenmail** — restringe recompra de ações de um acionista hostil a prêmio.

### Poison Pill (shareholder rights plan) — a defesa mais eficaz
Permite a todos os acionistas **exceto o adquirente hostil** comprar ações com **desconto (~50%)** → dilui massivamente o hostil e encarece a aquisição.
- **Trigger:** adquirente atinge 10–20% das ações (ou 10 dias após tender offer).
- **Flip-in:** ao cruzar o threshold, os rights (menos os do adquirente) viram ações do **alvo** no valor de 2× o exercise price.
- **Flip-over:** numa combinação posterior, viram ações do **adquirente** a 2× o exercise.
- **Exchange:** o board troca cada right por 1 ação do alvo (dilui sem exigir exercício).

### Outras
- **White knight** (comprador amigável alternativo), **Pac-Man** (alvo contra-ataca comprando o adquirente), **crown jewel** (vender o ativo mais cobiçado), **golden parachutes** (indenizações à gestão).
