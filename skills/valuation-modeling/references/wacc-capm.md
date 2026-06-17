# WACC, CAPM e Beta (referência detalhada)

> Fonte: Merrill Lynch IBD Analyst Training — Valuation Overview (2007).

## WACC — visão geral
Estimativa do retorno exigido por credores e acionistas dado o risco dos fluxos, a indústria e a estrutura de capital.

**Em M&A use o WACC do TARGET, não do adquirente** — é o melhor indicador do retorno exigido para *aquele* investimento (salvo mudança esperada na estrutura de capital).

## Fórmula
```
WACC = rd × (1 − t) × D/(D+E)  +  re × E/(D+E)

E  = market value of equity
D  = market value of debt (só dívida onerosa; NEM toda liability é dívida)
t  = alíquota marginal de imposto
re = cost of equity (via CAPM)
rd = cost of debt (custo atual de mercado da dívida)
```
- Juros são dedutíveis → o custo real da dívida é o **pós-imposto**.
- Use **market values** de D e E (em sala de aula, book de dívida serve).
- Camadas adicionais (conversíveis, preferred) precisam entrar.

## Cost of Debt (rd)
- Observável no mercado: melhor proxy é o **yield-to-maturity** atual dos títulos da empresa.
- Sobe quando D/Capital sobe e EBITDA/juros cai.
- Estimar quando não há bond líquido: (i) YTM de bonds públicos existentes, ou (ii) imputar rating pelos credit stats de comparáveis e referenciar yields de emissões recentes.
- **Toda liability não é dívida.** Inclua short-term debt e current maturities (salvo sazonal/temporário). Calcule líquido de excess cash. Prática comum: um único rd para toda dívida sênior.
- **Conversíveis:** separe em componente dívida + componente warrant/opção e aloque a cada lado.
- **Preferred stock:** classe separada de capital (3ª categoria). Dividendos de preferred **não** são dedutíveis.

## Cost of Equity (re) — CAPM
Equity tem claim residual (subordinado a toda dívida e preferred) → risco e retorno maiores. Não é observável diretamente.

```
re = rf + βL × (rm − rf)
       rf       = risk-free rate
       βL       = beta alavancado
       (rm − rf) = market risk premium (equity risk premium)
```
**Não há P/E na fórmula** — sob CAPM, P/E nada tem a ver com cost of equity.

### Inputs
- **rf (risk-free):** yield do Treasury de 10 anos (alguns usam 30 anos ou T-bills).
- **Market risk premium:** histórico ~7%; muitos hoje usam 3–4%. Muito volátil e é uma das premissas mais importantes do DCF.
- **Small-cap premium:** alguns somam +1–3% para small caps (mais risco/retorno). Equivale a dizer que empresas maiores, ceteris paribus, valem mais.

## Beta
- Mede risco **sistemático** (não diversificável): o quanto os retornos da ação variam com o mercado.
- β = 1.0 → tão arriscada quanto o mercado.
- Use beta **alavancado** no CAPM. Betas de sites (Yahoo, etc.) já são alavancados.
- Use beta da própria empresa, mas **cheque** imputando betas desalavancados de comparáveis e re-alavancando à estrutura-alvo.
- Betas variam muito entre provedores e mercados ilíquidos dão dados ruins → sensibilize.

### Delever / Relever
```
Desalavancar:   βu = βL / (1 + (1 − t) × D/E)
Re-alavancar:   βL = βu × (1 + (1 − t) × D/E)
```
Procedimento p/ empresa privada ou beta suspeito:
1. Pegue betas alavancados de comparáveis.
2. Desalavanque cada um (fórmula acima) e tire a média dos βu.
3. Re-alavanque o βu médio à estrutura-alvo (D/E) da empresa que você valora.
4. Calcule re e WACC.

> ⚠️ **CAPM sob crítica:** Fama-French (2004) mostraram que, no longo prazo, praticamente não há relação entre beta e retorno; CAPM subestima retorno de ações de beta baixo e superestima de beta alto. Use, mas com ceticismo e sensibilidade.

## Exemplo trabalhado (Black Mountain Beer)
**Cost of equity:** β=1.2, rf=6%, ERP=7.5% → re = 6% + 1.2×7.5% = **15%**.

**WACC:** 8M ações × $12.50 = $100M equity; dívida $150M @ 10%; t=38%.
```
WACC = 10% × (150/250) × (1−0.38) + 15% × (100/250)
     = 3.7% + 6.0% = 9.7%
```

**Desalavancar:** βu = 1.2 / (1 + (1−0.38)×150/100) = 1.2/1.93 = **0.62**.
