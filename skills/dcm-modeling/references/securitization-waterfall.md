# Securitização e o Cash Flow Waterfall

> Fonte: Allman, *Modeling Structured Finance Cash Flows*. Como transformar uma carteira de ativos (recebíveis, empréstimos, hipotecas) em títulos com riscos/ratings diferentes.

## A ideia central
Uma carteira de **ativos** (que geram fluxo de caixa) é vendida a uma **SPV (Special Purpose Vehicle)** isolada (bankruptcy-remote), que emite **títulos (tranches)** lastreados nesses fluxos. Os 3 elementos de um cash flow model (Allman):
1. **Asset cash flow** — os ativos geram juros + principal − **defaults** + **recoveries** (recuperações).
2. **Waterfall (liabilities)** — distribui o caixa por **prioridade de pagamento**.
3. **A estrutura** — tranches, triggers, reserve accounts, hedges.

Tipos: **ABS** (recebíveis/auto/cartão), **MBS/RMBS/CMBS** (hipotecas), **CLO** (leveraged loans), **CDO**.

## A pilha de tranches (parsing de risco)
```
Senior (AAA)     ← paga primeiro, menor taxa, mais protegida
Mezzanine (BBB)  ← intermediária
Equity / First-loss residual ← absorve a 1ª perda, sem rating, maior retorno potencial
```
Cada tranche tem taxa **proporcional ao risco** — a mesma carteira gera papéis de riscos diferentes ("parse risk").

## Priority of Payments (a cascata) — Allman
O caixa disponível desce a cascata; cada nível só recebe se houver caixa após o anterior ("**What You Have vs. What You Need**"):
```
1. Fees (servicing, trustee, administração)
2. Juros da tranche Senior
3. Juros da Mezzanine
4. Principal da Senior (sequencial ou pro-rata)
5. Principal da Mezzanine
6. Reposição de reserve accounts / cura de triggers
7. Excess spread → Equity / residual (first-loss)
```
- **Sequential pay:** principal vai todo para a senior até quitá-la, depois mezz (acelera desalavancagem da senior). **Pro-rata:** divide proporcionalmente.

## Credit Enhancement (o que protege as tranches sêniores)
A mesma carteira aguenta perdas via camadas de proteção (na ordem em que absorvem perda):
1. **Excess spread** — juros dos ativos − (fees + juros das tranches). A 1ª linha de defesa; sobra que cobre perdas.
2. **Overcollateralization (OC)** — ativos > passivos (ex.: $1.000 de ativos lastreando $900 de dívida).
3. **Subordinação** — tranches juniores (mezz/equity) absorvem perda antes da senior.
4. **Reserve account** — caixa segregado para cobrir shortfalls.
- Quanto mais enhancement, **maior o rating** que a senior alcança (agências estressam a estrutura).

## Triggers (proteção dinâmica)
Testes que, se violados, **redirecionam** o caixa para proteger os sêniores:
- **OC/IC triggers** (overcollateralization / interest coverage): se a cobertura cai abaixo do limite, o caixa que iria para equity/mezz é desviado para **amortizar a senior** (deleveraging acelerado).
- Curam-se quando os ratios voltam ao nível.

## Riscos e hedges
- **Mismatch de taxa** ativo-passivo (ativo fixo, passivo flutuante, ou vice-versa) → usar **swaps/caps** (a perna do passivo usa o swap rate).
- **Default e prepayment** dos ativos (prepayment encurta a duration — risco em MBS).
- Modelar **defaults, recoveries e timing** é o coração do modelo (Allman constrói passo a passo no Excel).

## Conectar
Instrumentos e covenants → `debt-instruments.md`. Emissão → `issuance-process.md`. Securitização no Brasil (FIDC/CRI/CRA) → `brazilian-dcm.md`. Risco de crédito (PD/LGD) e duration → skill **bond-modeling**.
