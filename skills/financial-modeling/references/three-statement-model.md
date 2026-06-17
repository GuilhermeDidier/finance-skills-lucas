# O Modelo de 3 Demonstrações (3-Statement Model)

> A fundação de quase todo trabalho de modelagem em IB: DRE, Balanço e DFC **integrados** e dirigidos por premissas. Tudo (DCF, LBO, M&A) é construído por cima disso.

## Arquitetura: as 3 demonstrações ligadas
```
        DRE (Income Statement)              Balanço (Balance Sheet)
   Receita → ... → EBIT → Net Income  ┐    Ativo = Passivo + PL
                                       │
                  Net Income ──────────┼──→ Lucros retidos (PL)
                                       │
        DFC (Cash Flow Statement)      │
   Net Income + D&A ± ΔNWC − Capex ────┘
   ± Financiamento = Δ Caixa ──────────────→ Caixa (Balanço)
```
**A DFC é a espinha dorsal:** parte do net income (DRE), reverte não-caixa e capta variações de balanço, e o caixa final fecha no balanço. Se as três não se conversam, o modelo está errado.

## Regra de ouro: o balanço TEM que fechar
`Ativo = Passivo + Patrimônio Líquido`, em **todos** os anos. Monte uma linha de **balance check** (Ativo − Passivo − PL = 0). Se não bate, há erro de ligação — não prossiga.

## As ligações que não podem faltar
| Item | Sai de | Entra em |
|---|---|---|
| Net Income | DRE | PL (lucros retidos) + topo da DFC |
| D&A | DRE / schedule | add-back na DFC; reduz PP&E no balanço |
| Capex | schedule | uso de caixa (investing) na DFC; aumenta PP&E |
| Δ NWC | schedule de WC | uso/fonte de caixa (operating) na DFC |
| Depreciação acumulada | PP&E schedule | reduz PP&E líquido no balanço |
| Dívida (ending balance) | debt schedule | passivo no balanço |
| Juros | debt schedule | DRE (acima do net income) |
| Repagamentos/captações | debt schedule | financing na DFC |
| Caixa final | DFC | ativo no balanço |
| Dividendos/recompras | premissa | financing na DFC; reduz PL |

## Ordem de construção (passo a passo)
1. **Histórico:** insira 3+ anos de DRE, balanço e DFC reportados (limpos — ver `quality-of-earnings.md`).
2. **Premissas/drivers:** numa aba separada (crescimento de receita, margens, DSO/DIH/DPO, capex %, alíquota, juros, dividendos).
3. **DRE até EBIT:** receita → COGS → SG&A → EBITDA → D&A → EBIT (ver `projection-drivers.md`).
4. **Schedules de apoio:**
   - **PP&E schedule:** PP&E final = PP&E inicial + capex − depreciação.
   - **Working capital schedule:** A/R, estoque, A/P via ratios; calcula ΔNWC.
   - **Debt schedule:** saldos, juros, repagamentos (ver `debt-schedule.md`).
5. **Fechar a DRE:** EBIT − juros (do debt schedule) ± outros → pré-imposto → impostos → **net income**.
6. **Montar a DFC:** operating (NI + D&A ± ΔNWC) + investing (−capex) + financing (dívida/dividendos) = **Δ caixa**.
7. **Fechar o balanço:** ativos (caixa da DFC, A/R, estoque, PP&E do schedule), passivos (A/P, dívida do schedule), PL (PL inicial + NI − dividendos).
8. **Balance check** = 0. Rode os error checks.
9. **Cenários e sensibilidade** (ver `best-practices.md`).

## Circularidade — por que aparece e como resolver
Juros dependem do saldo de dívida → que depende do caixa disponível para amortizar → que depende do net income → que depende dos juros. **Loop circular.** Soluções:
- Ativar **iterative calculation** no Excel (Options → Formulas → Enable iterative calculation, máx 100 iterações). É o método do Rosenbaum.
- Ou usar um **circuit breaker** (switch que zera os juros pra quebrar o loop quando precisa depurar).
- Detalhe em `debt-schedule.md`.

## Os 3 modos de "checar" o modelo
1. **Balance check** = 0 sempre.
2. **Sinais econômicos fazem sentido?** Margens estáveis/plausíveis, caixa não fica negativo (senão precisa de revolver), dívida amortiza coerente.
3. **Sanity vs histórico e peers** — drivers projetados não podem destoar do passado sem justificativa.
