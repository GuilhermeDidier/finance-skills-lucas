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
Enterprise Value = Equity Value − Cash + Debt + Preferred + Noncontrolling Interest (+ outros)
```
**O que SIGNIFICAM (não a fórmula):**
- **Equity Value** = valor de **tudo** que a empresa tem (Net Assets = Total Assets − Total Liabilities), mas só para os **acionistas** (common).
- **Enterprise Value** = valor das **operações core** do negócio (Net Operating Assets), para **TODOS os investidores** (equity, dívida, preferred, etc.).
- **Analogia da casa:** comprou por $500K com $100K de entrada → EV = $500K (preço total), Equity = $100K (entrada). Mudar a entrada para $250K muda o Equity, **não** o EV → EV é "capital structure-neutral".

**Por que precisa dos dois:** uma metodologia produz Equity Value, outra produz EV — você tem que transitar entre eles. EV é neutro a estrutura de capital; Equity Value importa porque a maioria das valuations é da ótica do acionista.

**Current vs Implied:** *Current* usa preço/share count/balanço atuais. *Implied* usa uma metodologia (ex.: DCF) para estimar o que **deveria** valer. (Casa: list price $500K = Current EV; sua estimativa $450K = Implied EV.)

**Basic vs Diluted Equity Value:** Basic = shares × preço. Diluted inclui dilutivos (opções/warrants via **TSM**, converts via **if-converted**) → Diluted Shares × preço. Use o **diluted** (mede melhor o valor para os acionistas). Mecânica → skill valuation-modeling (`mechanics.md`).

**Da Equity para o EV (resposta técnica):** subtraia **non-operating assets** (caixa, investimentos, equity investments/associates, assets held for sale, NOLs) e some linhas de **outros grupos de investidores** (dívida, preferred, pensão sub-financiada, **noncontrolling interest**, às vezes leases).
- **Por que subtrair equity investments e somar NCI?** Equity investments (<50% em outra empresa) são **não-core** → subtrai (como caixa). NCI (a fatia que a controladora **não** detém numa subsidiária >50% consolidada) é **outro grupo de investidores** → soma.
- Regra de coerência: EV no topo → métrica **pré-juros** (Sales/EBITDA/EBIT); Equity Value → **pós-juros** (Net Income/EPS).
- **Por que EV não muda ao emitir dívida?** Caixa +X e dívida +X se cancelam. Equity value também não muda na emissão.

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
- **Por que valuar empresa pública** (já tem market cap)? Porque o mercado **pode estar errado** — você checa se a visão dele bate com a sua (casa de $500K que você acha que vale $450K).

**Prós e contras das 3 principais:**
| Metodologia | Prós | Contras |
|---|---|---|
| **Public comps** | dados de mercado reais, rápido, sem premissas de longo prazo | comps nem sempre existem; ruim p/ voláteis/ilíquidas; pode subavaliar potencial de LP |
| **Precedent transactions** | preços reais pagos; reflete tendências da indústria | dados incompletos; deal terms/condições distorcem; comps raros |
| **DCF** | "mais correto" na teoria; menos sujeito a oscilações de mercado; reflete fatores específicos | muito dependente de premissas de longo prazo; disputa sobre cost of equity/WACC |

- **Qual dá o maior valor?** É pegadinha — depende. Resposta segura: **DCF é o mais variável** (depende das premissas); **transaction comps tendem a ser > trading comps** pelo **control premium**.
- **Asset intensity importa:** entre duas empresas de mesmo EBITDA/crescimento, a **menos intensiva em capital** (menor capex/NWC → mais FCF) vale mais — ex.: healthcare/software > industrials.
- DCF é primário em M&A (comps confirmam); comps são primários em IPO.
- **Valuation muda por setor** (banco → DDM/P-BV; REIT → FFO/NAV; E&P → NAV/reserves) → ver `sector-valuation.md`.
- Detalhe completo → skill **valuation-modeling**.

## 5. DCF (resumo)
UFCF (EBIT×(1−t) + D&A − capex − ΔNWC) descontado ao **WACC** → enterprise value; − dívida líquida → equity. **Terminal value** (perpetuidade ou exit multiple) domina o valor → cuidado. Detalhe → **valuation-modeling**.

## 6. Merger Model — accretion/dilution (resumo)
Soma os Pre-Tax Incomes, ajusta por juros (dívida), foregone interest (caixa), sinergias e nova D&A; Combined NI ÷ total shares = Combined EPS. **Accretive** se Combined EPS > EPS standalone. Atalho: **Weighted Cost of Acquisition vs Yield do Seller**; em 100% stock, compare os **P/Es**. Detalhe → skill **mna-modeling**.

## 7. LBO Model (resumo)
Sponsor compra com muita dívida; paga a dívida com o FCF; sai em 3–7 anos. Retorno (**IRR/MOIC**) vem de **debt paydown + EBITDA growth + multiple expansion**. Mais alavancagem = mais retorno e risco. Detalhe → skill **lbo-modeling**.

## 8. Brain teasers / curveballs
Costumam testar raciocínio (ex.: estimar tamanho de mercado, "quantos X cabem em Y", lógica de probabilidade). O avaliador quer **estrutura de pensamento**, não o número exato — declare premissas e mostre o caminho.
