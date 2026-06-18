---
name: bond-modeling
description: Analytics de renda fixa — precificação de títulos (preço-yield, zero-cupom e com cupom, clean/dirty, par/ágio/deságio), medidas de yield (YTM/TIR, current yield, yield-to-worst), risco de taxa (Macaulay/modified duration, DV01, convexidade, imunização), curva de juros (spot/forward, bootstrapping) e crédito (spread, rating, PD/LGD), com foco no mercado brasileiro (LTN, NTN-B, NTN-F, LFT, CDI/Selic, DI futuro, DU/252, marcação a mercado). Use quando o usuário quiser precificar um título, calcular YTM/duration/DV01/convexidade, montar/ler uma curva de juros, avaliar risco de taxa ou crédito, hedgear renda fixa, ou entender instrumentos brasileiros. Gatilhos: "renda fixa", "título", "bond", "precificar", "YTM", "TIR", "duration", "DV01", "convexidade", "curva de juros", "yield", "spread de crédito", "LTN/NTN-B/NTN-F/LFT", "CDI", "Selic", "DI futuro", "marcação a mercado", "imunização".
---

# Bond Modeling (Renda Fixa — Analytics)

Skill para **precificar e medir o risco** de instrumentos de renda fixa. O fio condutor: preço = VP dos fluxos descontados pela taxa/curva; e o risco de taxa se resume em **duration, DV01 e convexidade**. Forte ênfase no **mercado brasileiro** (DU/252, indexadores). Emissão/estruturação de dívida (mercado primário) → skill **dcm-modeling**.

## Quando usar
- **Precificar** um título (zero-cupom ou com cupom) e calcular o **PU**.
- Calcular **YTM/TIR**, current yield, yield-to-worst.
- Medir **risco de taxa**: Macaulay/modified duration, **DV01**, convexidade.
- Montar/ler a **curva de juros** (spot/forward, bootstrapping, breakeven inflation).
- Avaliar **risco de crédito** (spread, Z-spread, rating, PD/LGD).
- **Hedge** de renda fixa (dimensionar por DV01, DI futuro) e **imunização**.
- Entender **instrumentos brasileiros** (LTN/NTN-B/NTN-F/LFT, CDI/Selic, marcação a mercado).

**Quando NÃO usar:** emissão/sindicação/estruturação (securitização, tranches, waterfalls) → skill **dcm-modeling**; derivativos de taxa/opções → skill **derivatives-modeling** (futura).

## Princípios
1. **Preço = VP dos fluxos.** Suba a taxa, o preço cai (relação inversa).
2. **Convenção importa:** Brasil = **DU/252**; confirme sempre o day count.
3. **Risco de taxa = duration/DV01** (1ª ordem) **+ convexidade** (2ª ordem).
4. **Yield ≠ cupom** (só são iguais ao par); use **YTM/TIR** como medida principal.
5. **Carregar até o vencimento** realiza a taxa contratada; **vender antes** realiza a marcação a mercado.
6. **Crédito = soberano + spread**; separe risco de taxa de risco de crédito.

## Roteiro
1. **Defina os fluxos** e a **convenção** (DU/252? ACT/360?) — ver `references/fixed-income-math.md`.
2. **Precifique** (VP dos fluxos / PU); identifique par/ágio/deságio; calcule YTM — `references/bond-pricing.md`.
3. **Meça o risco de taxa:** duration, modified duration, DV01, convexidade — `references/duration-convexity.md`.
4. **Use a curva** (descontar por vértice, forwards, spread de crédito) — `references/yield-curve-and-credit.md`.
5. **Contexto brasileiro:** indexador, marcação a mercado, hedge com DI futuro — `references/brazilian-instruments.md`.

## Formato da saída
1. **Preço/PU** e classificação (par/ágio/deságio) com a YTM.
2. **Medidas de risco:** duration, DV01, convexidade — e o que significam (sensibilidade a 1bp / 1%).
3. **Cenários:** efeito de variações de taxa (duration + convexidade) e/ou de spread.
4. **Contexto BR:** indexador, day count, marcação a mercado, hedge sugerido.
5. **Premissas** explícitas (curva, convenção, reinvestimento).

## Documentos de apoio
- `references/fixed-income-math.md` — TVM, juros compostos, equivalência de taxas, DU/252, TIR/YTM, desconto.
- `references/bond-pricing.md` — preço-yield, zero-cupom vs cupom, par/ágio/deságio, clean/dirty, medidas de yield, PU.
- `references/duration-convexity.md` — Macaulay/modified duration, DV01/PVBP, convexidade, imunização, hedge.
- `references/yield-curve-and-credit.md` — estrutura a termo, spot/forward, bootstrapping, credit spread/Z-spread, rating, PD/LGD.
- `references/brazilian-instruments.md` — LTN/LFT/NTN-B/NTN-F, CDI/Selic, CDB, DI futuro, DU/252, marcação a mercado, cupom cambial.
- `references/worked-example.md` — título 3 anos: preço, duration, DV01, convexidade e a previsão batendo no reapreçamento.
