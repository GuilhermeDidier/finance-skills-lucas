---
name: dcm-modeling
description: Mercado de dívida (Debt Capital Markets) — instrumentos (IG/HY bonds, leveraged loans, commercial paper, convertibles, mezzanine) e covenants, processo de emissão (rating, pricing/spread, bookbuilding, sindicação, liability management), e securitização/structured finance (SPV, tranches senior/mezz/equity, cash flow waterfall, credit enhancement, triggers), com foco no mercado brasileiro (debêntures, CRI/CRA, FIDC, CVM). Use quando o usuário quiser estruturar/entender uma emissão de dívida, dimensionar covenants, montar um waterfall de securitização, avaliar tranches e credit enhancement, ou navegar o mercado de crédito brasileiro. Gatilhos: "DCM", "emissão de dívida", "debênture", "high yield", "leveraged loan", "covenants", "securitização", "waterfall", "tranche", "ABS/MBS/CLO", "FIDC", "CRI", "CRA", "credit enhancement", "sindicação", "rating".
---

# DCM Modeling (Debt Capital Markets)

Skill para o **mercado primário de dívida e structured finance**: como dívida é emitida, estruturada e securitizada. Analytics de precificação/risco de um título (yield, duration, spread) → skill **bond-modeling**. Esta foca em **estrutura, processo e securitização**.

## Quando usar
- Entender/estruturar uma **emissão de dívida** (bond, loan, debênture): tamanho, prazo, estrutura, covenants.
- Dimensionar **covenants** (maintenance vs incurrence) e entender senioridade/recovery.
- Montar/ler um **cash flow waterfall** de securitização (ABS/MBS/CLO/FIDC).
- Avaliar **tranches** (senior/mezz/equity) e **credit enhancement** (excess spread, OC, subordinação, reserve, triggers).
- Navegar o **processo** (rating, pricing/spread, bookbuilding, sindicação) e **liability management** (refi, tender, dividend recap).
- Mercado **brasileiro:** debêntures (incl. incentivadas), CRI/CRA, FIDC, regras CVM.

**Quando NÃO usar:** precificar/medir risco de um título (YTM, duration, DV01, curva) → skill **bond-modeling**; financiamento de um LBO (tranches do buyout) → skill **lbo-modeling**; derivativos de crédito → skill **derivatives-modeling** (futura).

## Princípios
1. **Spread proporcional ao risco** (rating, senioridade, prazo, mercado).
2. **Senioridade decide tudo** em default: ordem de pagamento e recovery.
3. **Securitização = parsing de risco:** a mesma carteira vira tranches de riscos/ratings diferentes.
4. **Credit enhancement** (excess spread → OC → subordinação → reserve) é o que sustenta o rating da sênior.
5. **Waterfall:** caixa desce por prioridade — "What You Have vs. What You Need".
6. **Covenants** alinham credor e devedor; maintenance (loans) é mais apertado que incurrence (HY).

## Roteiro
1. **Instrumento e estrutura:** que tipo de dívida, garantia, senioridade, covenants — `references/debt-instruments.md`.
2. **Emissão:** rating, pricing (curva + spread), bookbuilding, sindicação — `references/issuance-process.md`.
3. **Securitização (se aplicável):** SPV, tranches, waterfall, credit enhancement, triggers — `references/securitization-waterfall.md`.
4. **Contexto BR:** debênture/CRI/CRA/FIDC, indexador, CVM — `references/brazilian-dcm.md`.

## Formato da saída
1. **Estrutura proposta:** instrumento, prazo, garantia, senioridade, covenants.
2. **Pricing:** referência + spread (justificado por rating/comparáveis).
3. **Securitização:** tranches, waterfall, credit enhancement e o rating implícito da sênior.
4. **Riscos:** crédito, taxa (mismatch/hedge), prepayment, liquidez.
5. **Contexto BR** e premissas explícitas.

## Documentos de apoio
- `references/debt-instruments.md` — espectro de dívida (CP→revolver→TLB→2nd lien→IG/HY→mezz→converts), covenants (maintenance/incurrence), senioridade/recovery.
- `references/issuance-process.md` — papel do DCM, processo (rating→docs→roadshow→bookbuilding→pricing), spread/new-issue concession/OID, sindicação, liability management.
- `references/securitization-waterfall.md` — SPV, asset CF, tranches, priority of payments, credit enhancement (excess spread/OC/subordinação/reserve), triggers, hedges. (Allman)
- `references/brazilian-dcm.md` — debêntures (incentivadas), CRI/CRA, FIDC, notas comerciais, indexadores (CDI/IPCA), CVM 160/476, ANBIMA/B3.
- `references/worked-example.md` — waterfall de uma securitização: cascata, excess spread e como a subordinação protege a sênior no estresse.
