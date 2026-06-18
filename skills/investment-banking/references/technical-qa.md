# Technical Quick-Reference (Accounting, EV/Equity, Valuation, Deals)

> Fontes: M&I 400 / 400 Questions (estrutura) + perguntas_respostas_IB (efeitos FCFF/EV) + conhecimento canônico. A base técnica que todo banker tem na ponta da língua. As mecânicas profundas vivem nas outras skills; aqui é o resumo conectado e o Q&A.

## 1. As 3 demonstrações ligadas (a pergunta mais clássica)
**"A depreciação aumenta $10. O que acontece nas 3 demonstrações?"** (tax 25%)
- **DRE:** EBIT −$10 → lucro pré-imposto −$10 → **net income −$7,5** (−$10 × (1−25%)).
- **DFC:** começa em NI −$7,5; soma de volta a depreciação **+$10** (não-caixa) → **CFO +$2,5** → caixa +$2,5.
- **Balanço:** caixa **+$2,5** e PP&E **−$10** → ativos **−$7,5**; lucros retidos **−$7,5** (PL) → passa o balance check. ✅
> Variações pedem: aumento de capex, write-down, accrual, compra de estoque, emissão de dívida. O método é sempre o mesmo: DRE → DFC → Balanço, e o balanço **tem** que fechar (ver skill financial-modeling).

## 2. Enterprise Value vs Equity Value
```
Enterprise Value = Equity Value + Total Debt + Preferred + Minority Interest − Cash
```
- **Equity value:** valor para os acionistas. **EV:** valor de todo o capital (operação), independente da estrutura de capital.
- Múltiplo com **EV** no topo → métrica **pré-juros** embaixo (Sales/EBITDA/EBIT). **Equity value** → **pós-juros** (Net Income/EPS).
- **Por que EV não muda ao emitir dívida?** Caixa +X e dívida +X se cancelam (EV = Equity + dívida líquida). Equity value também não muda na emissão.
- (Mecânica de fully diluted shares / TSM → skill valuation-modeling, `mechanics.md`.)

## 3. Efeitos no FCFF / EV / Equity (Q&A — estilo perguntas_respostas_IB)
| Evento | FCFF | EV | Equity Value |
|---|---|---|---|
| AR (contas a receber) **+10** | ↓ (↑NWC, uso de caixa) | ↓ | ↓ (via DCF) |
| AP (fornecedores) **+10** (atrasa pagamento) | ↑ (↓NWC, libera caixa) | ↑ | ↑ |
| Depreciação **+20** | ↑ (add-back não-caixa) | ↑ | ↑ (no DCF; contábil imediato: neutro) |
| Capex **+15** | ↓ (uso de caixa) | ↓ | ↓ |
| Emissão de dívida **+50** | — (caixa +50, dívida +50) | — (EV inalterado) | — (no momento) |
| Impairment **+30** (não-caixa) | — | — | — (DCF inalterado) |
| Venda de ativo acima do book | ↑ (gera caixa) | ↑ | ↑ |
| Antecipar pagamento a fornecedor | ↓ (↑NWC) | ↑ (↓caixa → ↑dívida líq.) | — |
> Regra mental: o que mexe em **caixa operacional** mexe no FCFF (e no EV via DCF). O que é **não-caixa** (impairment, depreciação no instante contábil) não muda o DCF. Cuidado: o que muda **dívida líquida** muda o EV mesmo sem mudar FCFF.

## 4. Valuation — as metodologias (resumo)
- **Trading comps, transaction comps, DCF, LBO** (floor), sum-of-the-parts. Triangule num **football field**.
- **Qual dá o maior valor?** Em geral: **transaction comps** (incluem control premium) e **DCF** (se premissas otimistas) tendem a ser mais altos; **trading comps** e **LBO** (floor) mais baixos. Mas depende do caso.
- DCF é primário em M&A (comps confirmam); comps são primários em IPO.
- Detalhe completo → skill **valuation-modeling**.

## 5. DCF (resumo)
UFCF (EBIT×(1−t) + D&A − capex − ΔNWC) descontado ao **WACC** → enterprise value; − dívida líquida → equity. **Terminal value** (perpetuidade ou exit multiple) domina o valor → cuidado. Detalhe → **valuation-modeling**.

## 6. Merger Model — accretion/dilution (resumo)
Soma os Pre-Tax Incomes, ajusta por juros (dívida), foregone interest (caixa), sinergias e nova D&A; Combined NI ÷ total shares = Combined EPS. **Accretive** se Combined EPS > EPS standalone. Atalho: **Weighted Cost of Acquisition vs Yield do Seller**; em 100% stock, compare os **P/Es**. Detalhe → skill **mna-modeling**.

## 7. LBO Model (resumo)
Sponsor compra com muita dívida; paga a dívida com o FCF; sai em 3–7 anos. Retorno (**IRR/MOIC**) vem de **debt paydown + EBITDA growth + multiple expansion**. Mais alavancagem = mais retorno e risco. Detalhe → skill **lbo-modeling**.

## 8. Brain teasers / curveballs
Costumam testar raciocínio (ex.: estimar tamanho de mercado, "quantos X cabem em Y", lógica de probabilidade). O avaliador quer **estrutura de pensamento**, não o número exato — declare premissas e mostre o caminho.
