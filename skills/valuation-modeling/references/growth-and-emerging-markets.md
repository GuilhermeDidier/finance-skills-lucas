# Valuar Empresas de Crescimento, Sem-Lucro e em Mercados Emergentes

> Fonte: Damodaran, *The Dark Side of Valuation*. Como valuar o que o DCF/comps tradicionais não dão conta: jovens, alto crescimento, prejuízo, tech/intangível, e empresas em EM (Brasil incluso).

## Por que os métodos padrão falham aqui
- **Lucro/EBITDA negativo** → múltiplos (P/E, EV/EBITDA) não funcionam; crescimento histórico de lucro é sem sentido.
  - Crescimento de lucro com base negativa dá número absurdo: Amazon EBIT −$62M → −$276M daria "+345%". Não use.
- **Sem histórico** → não há série pra extrapolar; betas e comps são frágeis.
- **Intangível pesado** (P&D, marca) → investimento vai pra despesa, deprime lucro e distorce múltiplos (ver `value-drivers.md`).

## O framework do Damodaran (valuation de alto crescimento)
Em vez de partir do lucro, **ancore na receita** e construa o caminho até a maturidade:

### 1. Projetar receita (top-down, decrescente)
- Comece pelo crescimento recente e **reduza ao longo do tempo** (10-fold é fácil para quem fatura $2M, improvável para quem fatura $2bi).
- **Sanity-check de mercado:** projete a receita em dólares 10 anos à frente e compare com o tamanho do mercado e os maiores players. Se implicar **>90–100% de market share**, reveja. (Ex.: Damodaran checa se a receita futura da Amazon não a faria maior que Walmart de forma irreal.)
- Padrão típico: começa muito alto (ex.: 100–400% a.a.) e converge para o **crescimento estável** (~taxa da economia) no ano 10.

### 2. Margem operacional-alvo na maturidade
- Jovens em alto crescimento têm receita baixa e **margem operacional negativa**. Para valerem algo, a receita maior tem que virar **margem positiva** no futuro.
- **Input-chave:** a margem que você espera **na maturidade**. Estime olhando o **negócio de verdade** (concorrentes maduros do setor) — quase nenhuma "pioneira" não tem comparáveis (Amazon ← varejo/catálogo; Yahoo ← jornais com conteúdo+publicidade).
- **Consistência interna:** crescimento agressivo via preço baixo → margens menores. Não projete receita alta E margem alta sem justificar.

### 3. Reinvestimento via Sales-to-Capital Ratio
- Crescimento exige reinvestimento. Em vez de capex/NWC linha a linha (difícil sem histórico), use:
```
Reinvestimento = Δ Receita / (Sales-to-Capital Ratio)
```
- O sales-to-capital vem do setor/peers. Liga crescimento de receita ao capital necessário de forma consistente.

### 4. Caminho até stable growth + custo de capital que evolui
- Modele a transição: à medida que amadurece, **g cai**, **margem sobe**, **beta/WACC convergem** para os de empresa madura.
- No estável, g terminal ≤ crescimento da economia (nominal; ver nota BRL em `dcf.md`).

### 5. Sobrevivência (para os mais arriscados)
- Empresas que queimam caixa podem não sobreviver. Pondere o valor going-concern por uma **probabilidade de falência** quando relevante (valor esperado = p(sobrevive) × valor DCF + p(falha) × valor de liquidação).

## Country Risk Premium (CRP) — mercados emergentes / Brasil
Adicione um prêmio de risco-país ao cost of equity. Método Damodaran (default spread escalado pela volatilidade relativa):
```
CRP = Default Spread soberano × (σ_equity / σ_government bond)

re = rf + βL × ERP(mercado maduro) + λ × CRP
```
- **Default spread:** do rating soberano (ou CDS) sobre o Treasury US. Se não há bond soberano em USD, use o spread de outros países do mesmo rating.
- **σ_equity / σ_bond:** quanto o mercado de ações local é mais volátil que o de títulos local.
- **Exemplo (Índia, Damodaran):** rating Ba2 → default spread ~3,0%; σ_equity 31,82% / σ_bond 14,90% → CRP = 3,0% × (31,82/14,90) = **6,43%**. Somado ao ERP maduro de ~4% → ERP total para a Índia ≈ 10,4%.
- **λ (lambda):** exposição da empresa específica ao risco-país (uma exportadora 100% pode ter λ < 1; uma empresa 100% doméstica, λ ≈ 1). Refina o CRP por empresa em vez de aplicar igual a todas.

### Moeda — a regra que mais gera erro
- **FCF e taxa de desconto na mesma moeda.** BRL nominal com WACC em BRL (rf via NTN-B já embute risco-país e inflação locais); ou USD com WACC em USD + CRP explícito.
- Para converter entre moedas, use o **diferencial de inflação esperada**, não a taxa de câmbio spot.
- Ver também a seção de juro alto/BRL em `dcf.md` (calibração de g) e o CRP em `wacc-capm.md`.
