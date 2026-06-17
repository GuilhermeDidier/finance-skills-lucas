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

## Camada avançada (banker-grade — Rosenbaum & Pearl, Cap. 3)

### Target capital structure (não a atual, necessariamente)
O WACC é calculado sobre uma **estrutura de capital-alvo** consistente com a estratégia de longo prazo (D/(D+E) e E/(D+E)), **não** automaticamente a atual:
- Examine a estrutura atual e histórica da empresa e a **média/mediana dos comparáveis**.
- Empresa pública já no alvo → use a atual. Privada → use mediana dos comps.
- Escolhido o alvo, assume-se constante por todo o período de projeção.

**Optimal capital structure:** conforme se adiciona dívida (mais barata, pós-imposto), o WACC **cai** até o ponto ótimo; depois disso o risco de inadimplência encarece dívida E equity e o WACC volta a **subir**. Sem dívida, WACC = cost of equity.

### Risk-free rate — convenções de mercado
- Teoria: o instrumento risk-free mais longo (casar com going-concern).
- Prática: maioria usa o **10-year U.S. Treasury** (profundidade/liquidez). **Duff & Phelps** usa yield interpolado de **20 anos**.

### Market risk premium
- Wall Street tipicamente **5%–8%**; Duff & Phelps calcula ~**7%** (série desde 1926, média **aritmética**).
- Muitos bancos têm **política firm-wide** de MRP pra consistência entre projetos. Consulte o sênior/prática da casa.

### Beta — histórico vs preditivo
- Histórico: Bloomberg (`Ticker <Equity> BETA <GO>`), FactSet, Refinitiv. Janela 2–5 anos.
- Retornos passados podem não prever o futuro → muitos preferem **predicted beta** (ex.: **MSCI Barra**, forward-looking, modelo multifator).
- Empresa privada / fora do alvo: desalavanque betas dos comps, tire a **média** (pode ser ponderada por market cap), re-alavanque no D/E-alvo.

### Size Premium (SP) — companhias menores
Evidência empírica: empresas menores são mais arriscadas e o beta não captura tudo (baixo volume → covariância imprecisa). Adicione um prêmio de tamanho ao CAPM:
```
re = rf + βL × (rm − rf) + SP
```
**Duff & Phelps** publica size premia por decis de market cap. Use para mid/small caps.

### Country Risk Premium (CRP) — mercados emergentes (ex.: Brasil)
Para valuation de empresas em EM, adicione um prêmio de risco-país ao cost of equity (método Damodaran):
```
CRP = Default Spread soberano × (σ_equity / σ_government bond)
re  = rf + βL × ERP(mercado maduro) + λ × CRP
```
- **Default spread:** do rating soberano (ou CDS) sobre o Treasury US.
- **σ_equity / σ_bond:** volatilidade relativa do mercado de ações local vs títulos locais.
- **λ (lambda):** exposição da empresa específica ao risco-país (exportadora pura → λ < 1; 100% doméstica → λ ≈ 1). Refina por empresa.
- **Exemplo (Índia):** spread Ba2 ~3,0%; σ_equity 31,82% / σ_bond 14,90% → CRP = 3,0% × 2,135 = **6,43%**; com ERP maduro ~4% → ERP total ≈ 10,4%.
- Alternativa: usar rf local (NTN-B) que já embute risco-país e inflação — **sem somar CRP de novo** (não duplique).
- **Moeda:** FCF em BRL com WACC em BRL (rf via NTN-B), ou FCF em USD com WACC em USD + CRP. **Nunca misture.** Converta moedas por diferencial de inflação, não câmbio spot.
- Detalhe e framework de crescimento/EM → `growth-and-emerging-markets.md`.

### Sensibilizar o WACC
Dado o número de premissas e o impacto enorme na valuation, **sensibilize** os inputs do WACC para produzir um **range**, cruzado com outros inputs (ex.: exit multiple) numa tabela de sensibilidade 2-D.

## Exemplo trabalhado (Black Mountain Beer)
**Cost of equity:** β=1.2, rf=6%, ERP=7.5% → re = 6% + 1.2×7.5% = **15%**.

**WACC:** 8M ações × $12.50 = $100M equity; dívida $150M @ 10%; t=38%.
```
WACC = 10% × (150/250) × (1−0.38) + 15% × (100/250)
     = 3.7% + 6.0% = 9.7%
```

**Desalavancar:** βu = 1.2 / (1 + (1−0.38)×150/100) = 1.2/1.93 = **0.62**.
