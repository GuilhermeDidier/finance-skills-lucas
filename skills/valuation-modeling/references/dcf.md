# DCF — Discounted Cash Flow (referência detalhada)

> Fonte: Merrill Lynch IBD Analyst Training — Valuation Overview (2007). Destilado para uso prático.

## O que é
Valor de um negócio = valor presente líquido dos fluxos de caixa projetados. Inclui (1) os FCFs do período explícito de forecast e (2) um **terminal value** ao fim do período. Descontados a uma taxa compatível com o risco.

DCF é **forward-looking** — o valor vem do futuro projetado, não do passado.

### Regra de bolso de uso
- **M&A → DCF é a técnica primária**, comps confirmam.
- **IPO → comps são primários**, DCF confirma.

## Três técnicas equivalentes (mesmas premissas → mesmo valor)
| Técnica | Fluxos de caixa | Taxa de desconto | Quando usar |
|---|---|---|---|
| **WACC (a padrão)** | Unleveraged FCF (antes de financiamento) | WACC | Maioria dos casos. Assume estrutura de capital constante. Leva a **enterprise value**. |
| **APV (Adjusted Present Value)** | Operating CF + tax shields valorados separadamente | Custo de equity desalavancado p/ operação; custo pré-imposto da dívida p/ tax shield | Quando a estrutura de capital varia muito no período. Leva a EV. |
| **Flows to Equity (FTE)** | FCF após financiamento (flows to equity) | Cost of equity (CAPM, beta alavancado) | Serviços financeiros (difícil separar juros operacionais de financeiros). Leva direto a **equity value**. |

**Padrão = WACC-based.** O resto desta referência foca nele.

## O processo (5 passos)
1. **Projeções** — projetar resultados operacionais e FCF, tipicamente 5 ou 10 anos.
2. **Discount rate** — usar WACC (ver `wacc-capm.md`).
3. **Terminal value** — estimar valor ao fim do forecast (exit multiple e/ou perpetuidade). **Costuma ser a maior parte do valor — cuidado redobrado aqui.**
4. **Present value** — descontar e gerar um *range* de valores variando taxas e premissas.
5. **Ajustes** — somar/subtrair ativos e passivos não capturados no FCF (excess cash, investimentos, real estate ocioso, minority interest, etc.).

## Unleveraged Free Cash Flow (UFCF) — a ponte
Deriva-se do forecast mesmo que ele inclua dívida: exclui-se receita/despesa de juros e tax-effect no EBIT. O valor do tax shield já entra via custo da dívida pós-imposto no WACC.

```
        EBIT
  (–)   Taxes (à alíquota marginal)      ← NÃO é a mesma da DRE; exclui o tax shield dos juros
  ( = ) Tax-Effected EBIT  (= NOPAT = EBIAT = Net income + juros após impostos)
  (+)   Depreciação & amortização
  (±)   Aumento (redução) de deferred tax liabilities
  (∓)   Aumento (redução) de working capital ajustado
  (–)   Capex
  ( = ) Unleveraged Free Cash Flow
```
- **Working capital ajustado** = ativo circulante − passivo circulante, **excluindo** excess cash do ativo e short-term debt/current maturities do passivo.
- Use **cash taxes** (olhe o deferred no cash flow statement).

## Terminal Value — dois métodos

### A) Exit Multiple Method (o mais usado)
- Assume venda do negócio no ano N.
- TV = múltiplo de **EV/EBITDA** ou **EV/EBIT** (múltiplos de EV, nunca P/E — coerência com EV).
- Múltiplo derivado dos trading comps, **com desconto** sobre os níveis atuais (crescimento desacelera). Tipicamente **15–20% de desconto**; nunca acima do múltiplo atual da empresa.
- Recomendação: basear no múltiplo **trailing** (não forward), porque você aplica o múltiplo ao último ano do forecast (olhando para trás).
- Cuidado com indústrias cíclicas → use média móvel.

### B) Perpetuity Growth Method (o mais teórico)
```
Terminal Value(ano N) = FCF_N × (1 + g) / (r − g)
```
- g = crescimento perpétuo do **FCF** (não de vendas/lucro); r = WACC.
- **Lembrar de descontar** esse TV do ano N para o presente.
- **Nominal vs real:** DREs são nominais. g de 3% ≈ crescimento real zero (inflação US ~3%). Tudo bem g baixo/negativo real — só explique.
- **Limites de g:** evite g acima do crescimento dos últimos anos do forecast. >6% nominal (crescimento de longo prazo da economia) é geralmente insustentável.
- **R−g é decisivo:** se r=10% e g=5%, o múltiplo implícito de FCF é 20x. Juros baixos → TVs enormes.

### Equivalência entre os dois (sanity check obrigatório)
```
g implícito (a partir do exit multiple) = [(WACC × TV_n) − FCF_n] / [FCF_n + TV_n]
múltiplo implícito (a partir do g)      = [FCF_n × (1 + g)] / [EBITDA_n × (WACC − g)]
```
Use TV, FCF e EBITDA do ano terminal, **não descontados**. Cheque se o g implícito pelo seu exit multiple é razoável (e vice-versa).

### Problemas clássicos do terminal value
- **The cliff:** empresa cresce 15% no forecast e cai pra 6% de repente só pra resolver o modelo → irreal. Solução: estender o forecast pra g descer gradualmente.
- **Capex vs depreciação:** devem ficar ~equilibrados na perpetuidade. Se g>3% nominal, capex deve exceder depreciação em ~10–20%.
- **Taxes:** alíquota de caixa baixa (deferred alto) não dura pra sempre — suba pra marginal na perpetuidade.
- **Forecast curto demais:** 5 anos costuma ser pouco. O *competitive advantage period* (período em que ROIC incremental > WACC) é estimado em **12–15 anos** para o mercado como um todo.

## ROIIC — o check que separa amador de profissional
g só **cria valor** se **ROIIC > WACC**. Se ROIIC = WACC, g pode ser qualquer coisa que não muda o TV.
```
Quando ROIIC = WACC:   FCF_{N+1}/(WACC − g) = NOPAT_{N+1}×(1 − g/ROIIC)/(WACC − g) = NOPAT/WACC
```
Check cru de ROIIC: `Δ NOPAT (ano a ano) / Δ investimento`, onde Δ investimento = Δ working capital + capex − depreciação.
Se o ROIIC implícito do seu modelo estiver muito acima do WACC (ex.: 27% vs 8%), **as premissas estão furadas** — reveja antes de entregar.
> Ref.: Mauboussin, "Common Errors in DCF Models".

## Present Value
```
PV = Σ  UFCF_t / (1 + r)^t
```
**Mid-year convention** (assume caixa no meio do período, mais realista; gera valor um pouco maior):
```
PV = Σ  UFCF_t / (1 + r)^(t − 0.5)
```

## Ajustes finais (do EV ao equity value e por ação)
- **Excess cash** → soma ao EV (líquida contra dívida). Exclua interest income do EBITDA (senão dupla contagem).
- **Investimentos / unconsolidated subsidiaries** → some (valor de mercado ou book). Exclua earnings/dividendos deles do EBITDA.
- **Minority interest** → subtraia.
- **Real estate ocioso / ativos redundantes** → some.
- **Operações deficitárias** → avalie separado (incluir no DCF dá valor negativo implícito).
- **Operating leases** (relevante p/ varejo): capitalize (≈ 8× a despesa anual de aluguel) e trate como dívida; some o aluguel ao EBITDA → EBITDAR.

```
Equity Value = Enterprise Value − Net Debt (+ ajustes acima)
Valor por ação = Equity Value / diluted shares outstanding
```

## Sensibilidade (sempre)
Monte tabelas sensibilizando as variáveis que realmente movem o valor: **vendas, margens, WACC, e o múltiplo terminal / g de perpetuidade**. DCF é altamente sensível a TV e custo de capital.

## Limitações honestas (diga ao cliente)
- DCF tradicional **subestima** quando há *real options* (postergar/abandonar/mudar estratégia têm valor).
- Resultado é altamente sensível a WACC e TV.
- Range amplo de forecasts é possível → triangule sempre com comps.
