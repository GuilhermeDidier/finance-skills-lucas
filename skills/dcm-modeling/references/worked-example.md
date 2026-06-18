# Exemplo trabalhado — Waterfall de uma Securitização

> Mostra a cascata de pagamentos, o excess spread e como a subordinação protege a tranche sênior em um cenário de perdas. Valores ilustrativos.

## A estrutura
Carteira de recebíveis de **R$1.000** (yield 10% a.a.), securitizada numa SPV que emite:
| Tranche | Valor | % | Rating | Taxa |
|---|---|---|---|---|
| **Sênior** | 800 | 80% | AAA | 5% |
| **Mezzanine** | 150 | 15% | BBB | 9% |
| **Equity (residual)** | 50 | 5% | — | residual |

**Credit enhancement da sênior:** subordinação = mezz + equity = **R$200 (20%)** + excess spread + (eventual reserve account).

## Cenário-base (1 ano, sem perdas)
Caixa de juros gerado pelos ativos = 1.000 × 10% = **R$100**. Desce a cascata:
```
1. Fees (servicing/trustee)            (5,0)
2. Juros Sênior   (800 × 5%)          (40,0)
3. Juros Mezzanine (150 × 9%)         (13,5)
   = Excess spread → Equity/residual   41,5
```
**Excess spread = 100 − 5 − 40 − 13,5 = R$41,5** → vai para o equity (e/ou reserve account). É a **1ª linha de defesa** (absorve perda antes de qualquer tranche).

## Cenário de estresse (perda de R$30 nos ativos)
Juros disponíveis caem para **R$70** (defaults reduziram a geração):
```
1. Fees                                (5,0)
2. Juros Sênior                       (40,0)
3. Juros Mezzanine                    (13,5)
   = Excess spread restante            11,5
```
- **Sênior e Mezzanine recebem 100% dos juros** — intactas.
- O **equity absorve a perda** (excess spread caiu de 41,5 → 11,5). A subordinação funcionou: a perda bateu primeiro no first-loss.
- Só depois de **esgotar todo o excess spread + reserve account + a tranche equity inteira** é que a **mezzanine** começaria a sofrer; e só depois dela, a **sênior**. Por isso a sênior é AAA.

## Trigger em ação (proteção dinâmica)
Se a cobertura (OC/IC) cair abaixo do limite, o **trigger desvia** o caixa que iria ao equity para **amortizar a sênior** antecipadamente — desalavancando a estrutura e protegendo o topo. Cura-se quando os ratios voltam ao nível.

## Leituras
- A mesma carteira (yield 10%) gerou um papel **AAA a 5%** e outro **BBB a 9%** — "parsing" de risco via subordinação + excess spread.
- O **equity** tem o maior retorno potencial (fica com todo o excess spread) e o maior risco (first-loss).
- Modelar isso de verdade (Allman) exige projetar **defaults, recoveries e timing** período a período e rodar a cascata em cada um — ver `securitization-waterfall.md`.
- No Brasil, essa lógica é o **FIDC** (cotas sênior e subordinada) — ver `brazilian-dcm.md`.
