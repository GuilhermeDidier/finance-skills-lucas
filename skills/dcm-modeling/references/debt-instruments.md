# Instrumentos de Dívida e Covenants

> Fontes: Allman + convenções de mercado + Rosenbaum (leveraged finance). Os produtos do mercado de dívida e o que os diferencia. Analytics de precificação/risco (yield, duration) → skill **bond-modeling**.

## O espectro de dívida (do mais seguro/barato ao mais arriscado/caro)
| Instrumento | Garantia | Investidor | Taxa | Característica |
|---|---|---|---|---|
| **Commercial Paper** | unsecured, curtíssimo prazo | money markets | baixa | financiamento de curto prazo (working capital) |
| **Revolving Credit Facility** | senior secured | bancos | flutuante | linha rotativa |
| **Term Loan A / B** | senior secured (1st lien) | bancos (A) / institucionais (B) | flutuante (SOFR+) | TLB = amortização mínima, bullet |
| **Second Lien** | secured subordinada | institucionais | maior | entre senior e HY |
| **Investment-Grade Bonds** | unsecured | institucionais | cupom fixo, spread baixo | rating ≥ BBB− |
| **High-Yield Bonds** | unsecured/subordinada | HY funds | cupom alto | rating < BBB−; covenants de incurrence |
| **Mezzanine** | subordinada | mezz funds | alto + PIK + warrants | híbrido dívida-equity |
| **Convertibles** | sênior/subordinada | conversíveis | cupom baixo | opção de conversão em equity |

- **Leveraged loans** (TLB) e **high yield** são o "leveraged finance" — financiam LBOs e empresas alavancadas (ver skill **lbo-modeling**).
- **Floating** (loans): SOFR + spread (antes LIBOR). **Fixed** (bonds): cupom. **PIK:** juros capitalizam no principal (alívio de caixa).

## Covenants (proteções do credor)
- **Maintenance covenants:** testados **periodicamente** (ex.: Debt/EBITDA ≤ X, EBITDA/juros ≥ Y todo trimestre). Típicos de **leveraged loans**. Quebrar = evento de default → renegociação.
- **Incurrence covenants:** testados **só quando a empresa age** (ex.: emitir mais dívida, pagar dividendo). Típicos de **high yield bonds**. Mais frouxos ("cov-lite" quando há poucos).
- **Negative covenants:** restrições (limite de dívida, de dividendos, de venda de ativos, de liens — negative pledge).
- **Change-of-control:** em aquisição, o credor pode exigir repagamento (put a 101) — relevante em M&A (ver skill mna-modeling).

## Senioridade e recuperação
- Em default, paga-se na ordem de **prioridade/senioridade** (secured 1st lien → 2nd lien → senior unsecured → subordinada → equity). Quanto mais sênior + garantido, maior o **recovery rate**.
- O **spread** exigido reflete PD × LGD (ver bond-modeling, `yield-curve-and-credit.md`).

## Conectar
Precificação e risco de taxa desses papéis → skill **bond-modeling**. Tranches estruturadas (ABS/MBS/CLO) → `securitization-waterfall.md`. Mercado primário (emissão) → `issuance-process.md`.
