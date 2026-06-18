# Modelagem dos Ativos — Prepayment, Default e Loss

> Fonte: Allman, *Modeling Structured Finance Cash Flows* (caps. 2–4). O lado dos **ativos**: como projetar o fluxo de caixa do pool (amortização − prepagamento − default + recuperação) que alimenta o waterfall. É o coração da modelagem de securitização — sem isto, o waterfall não tem o que distribuir.

## Os 3 fluxos do pool
```
Caixa do pool no período = Juros + Principal programado + Prepagamentos − Defaults + Recuperações
```
Cada componente é projetado por uma **curva (vetor)** ao longo da vida da operação.

## Amortização do ativo
- **Loan-level vs representative line:** modelar cada empréstimo (preciso, pesado) ou agrupar em "linhas representativas" por características (taxa, prazo, vintage).
- Fixo vs flutuante: a amortização programada segue o cronograma (price/SAC); o saldo cai a cada período.

## Prepayment (pré-pagamento) — o devedor paga antes
- **SMM (Single Monthly Mortality):** % do saldo que pré-paga **no mês**.
- **CPR (Conditional Prepayment Rate):** a versão **anualizada** do SMM (para hipotecas/ativos longos):
  ```
  CPR = 1 − (1 − SMM)^12        (e SMM = 1 − (1 − CPR)^(1/12))
  ```
  ⚠️ CPR é **Conditional** Prepayment Rate — não "Cumulative", e não confundir com **CDR** (default).
- **PSA (Public Securities Association):** curva padrão de hipotecas. **100% PSA** = 0,2% CPR no 1º mês, +0,2%/mês até o 30º mês, e **6% CPR** constante daí em diante. Múltiplos escalam (200% PSA = o dobro).
- **ABS (Absolute Prepayment Speed):** medida para ativos curtos (auto loans); converte-se para SMM: `ABS = 100×SMM / (100 + SMM×(n−1))`, n = períodos desde a originação.
- **Efeito:** prepagamento **encurta a duration/WAL** e devolve principal cedo (risco de reinvestimento; ruim para tranches compradas com ágio).

## Delinquency → Default → Loss → Recovery (a cadeia)
- **Delinquency (inadimplência):** parou de pagar em dia, mas **pode voltar a adimplir**. Analisar delinquency é o ponto de partida da análise de perda (sinaliza tendência de crédito e liquidez).
- **Default:** quando o atraso passa de um limite (ex.: **90 dias**) → classificado como default. Nem todo delinquente vira default.
- **CDR (Conditional Default Rate):** taxa de default anualizada (análoga ao CPR), aplicada ao saldo performing. (MDR = a versão mensal.)
- **Gross loss:** muitas vezes o principal é baixado **na hora** do default.
- **Recovery:** parte é recuperada depois (venda do colateral/repossessão/cobrança), com um **lag** (ex.: 14 meses até a foreclosure + 3 meses para vender).
- **Severity / LGD (loss given default):** fração efetivamente perdida = 1 − recovery rate. **Perda líquida ≈ default × severity**.
- **Loss curve:** perda projetada com **timing** e **severity** (quando e quanto se perde) — calibrada em dados históricos por **vintage** (safra de originação).

## WAL — Weighted Average Life
Vida média do principal: `WAL = Σ [t × principal recebido_t] / principal total`. Encurta com prepayment, alonga com extensão. É a medida de prazo efetivo de uma tranche amortizável (mais relevante que "maturity" final).

## Calibração (como projetar as curvas)
1. Obtenha **dados históricos** (≥3 anos) do ativo: saldo, prepagamento e perdas por período, idealmente por **vintage**.
2. Construa as curvas projetadas (CPR/CDR/severity) por **seasoning** (idade do empréstimo) — perdas e prepagamentos variam com a maturação do pool.
3. **Stress scenarios:** rode múltiplos de PSA, CDR e severity (e timing) para ver se a estrutura aguenta — é o que as agências fazem para dar o rating.

## Conectar
Este fluxo de ativos **entra no topo do waterfall** (`securitization-waterfall.md`): o caixa projetado aqui é o "What You Have" que desce a cascata. Risco de crédito (PD/LGD) e duration → skill **bond-modeling**. No Brasil, o FIDC modela exatamente assim os recebíveis (`brazilian-dcm.md`).
