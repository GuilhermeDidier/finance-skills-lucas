# DCM Brasileiro — Instrumentos e Mercado Local

> Convenções do mercado de dívida brasileiro (CVM/B3/ANBIMA). Diferenças importantes para o Lucas. Analytics (yield, duration, indexadores DU/252) → skill **bond-modeling**.

## Instrumentos de crédito privado
- **Debêntures:** o principal título de dívida corporativa. Remuneração típica: **% do CDI**, **CDI + spread**, ou **IPCA + spread** (ou prefixada). Podem ser simples ou conversíveis; com garantia (real/flutuante) ou quirografária/subordinada.
  - **Debêntures incentivadas (Lei 12.431):** para infraestrutura, com **isenção de IR** para pessoa física → demanda forte, spread menor.
- **Notas Comerciais (commercial paper):** dívida de curto prazo.
- **CRI / CRA** (Certificados de Recebíveis Imobiliários / do Agronegócio): securitização lastreada em recebíveis imobiliários/agro; **isentos de IR** para PF → muito demandados.
- **FIDC** (Fundo de Investimento em Direitos Creditórios): veículo de **securitização** brasileiro — compra recebíveis e emite cotas **sênior** e **subordinada** (a lógica de tranches/waterfall de `securitization-waterfall.md` aplica diretamente).
- **Letras Financeiras (LF):** dívida de bancos, prazo mínimo, pode ser subordinada (capital regulatório).

## Indexadores (a remuneração)
- **% do CDI** ou **CDI + spread** (pós-fixado) — o mais comum em crédito privado.
- **IPCA + spread** (inflação + juro real) — comum em prazos longos/infra.
- **Prefixado** — trava a taxa nominal.
- Day count **DU/252** (ver skill bond-modeling).

## Regulação e distribuição (CVM)
- Ofertas reguladas pela **CVM** (atualmente **Resolução CVM 160**, que unificou as antigas Instruções 400 — oferta pública ampla — e 476 — esforços restritos a investidores profissionais/qualificados). A 476/regime restrito é a via rápida e mais usada para debêntures.
- **ANBIMA:** autorregulação e selo; **B3:** registro/negociação. **Agências de rating** locais (escala nacional `.br`) e globais.
- Investidores: fundos de crédito, DTVMs, bancos, e cada vez mais o varejo (via fundos e plataformas).

## Particularidades vs mercado externo
- Mercado **majoritariamente pós-fixado (CDI)** — diferente do mercado americano (predominantemente prefixado/cupom fixo).
- Curva de juros local construída de **DI futuro** (pré) e **NTN-B** (real) — ver skill bond-modeling.
- Benefícios fiscais (incentivadas, CRI/CRA) distorcem a demanda e comprimem spreads desses papéis.
- **Tesouro Direto** dá acesso do varejo aos títulos públicos.

## Conectar
Estrutura de FIDC/CRI/CRA segue o waterfall de `securitization-waterfall.md`. Precificação/risco → skill **bond-modeling** (`brazilian-instruments.md`). Processo de emissão → `issuance-process.md`.
