# Accretion / Dilution — o coração do merger model

> Fonte: M&A Deals / Merger Models Guide (BIWS) + JP Morgan M&A Reference Manual + Merrill Lynch training. A pergunta central de quase todo merger model: **o deal aumenta (accretive) ou reduz (dilutive) o EPS do comprador?**

## Por que EPS é a métrica
EPS é a **única métrica fácil de calcular que captura o impacto TOTAL** do deal: junta lucro operacional, juros (de dívida nova e caixa usado) e a contagem de ações. EBITDA/NOPAT não servem (são antes de juros e ignoram ações). FCF/share também captura, mas é "sujo" (muitos itens) e sem definição única.
- Empresas **preferem deals accretive** (sobem o EPS). Dilutive não é proibido — comprador costuma aceitar diluição nos primeiros anos se a tese estratégica e o retorno justificarem.

## O atalho conceitual: Weighted Cost of Acquisition vs Yield do Seller
A regra que diz, **sem montar o modelo inteiro**, se o deal é accretive:
```
Yield do Seller = Net Income do Seller / Purchase Equity Value
Weighted Cost of Acquisition = %Cash × custo após-imposto do Caixa
                             + %Debt × custo após-imposto da Dívida
                             + %Stock × custo do Stock (= 1 / P/E do comprador)
```
| Comparação | Resultado |
|---|---|
| Weighted Cost **<** Yield do Seller | **Accretive** |
| Weighted Cost **=** Yield do Seller | Neutro |
| Weighted Cost **>** Yield do Seller | **Dilutive** |

**Custos de cada fonte:**
- **Caixa:** taxa de juros que se deixa de ganhar (foregone interest), após imposto. Próxima do risk-free (baixa) → caixa é o financiamento mais barato.
- **Dívida:** cupom de nova dívida, após imposto (× (1−t)).
- **Stock:** **1 / P/E do comprador** ("the practical version" do cost of equity — foco no EPS, não no WACC). Normalmente o mais caro.

## A regra do deal 100% em ações (P/E rule)
Em deal 100% stock, o custo de aquisição = 1 / P/E do comprador. Então basta comparar P/Es:
| | Resultado |
|---|---|
| **P/E comprador > P/E do Seller (no preço de compra)** | Accretive |
| P/E comprador = P/E do Seller | Neutro |
| **P/E comprador < P/E do Seller (no preço de compra)** | Dilutive |
- Lembre de usar o **P/E do Seller no preço de compra** (já com o prêmio de controle), não o de mercado.
- Para deal 100% cash: se **1/(custo de dívida após imposto) > P/E do Seller** → accretive (Merrill Lynch).

## Os efeitos de aquisição (o que mexe no pro forma)
Ao somar os Pre-Tax Incomes do comprador e do alvo, ajuste por:
- **Dívida nova:** + juros → reduz lucro e EPS.
- **Stock novo:** + ações → reduz EPS.
- **Caixa usado:** − interest income (foregone interest) → reduz lucro e EPS. **É custo de caixa real**, não "custo de oportunidade" — os Pre-Tax Incomes projetados já incluíam aquela receita de juros.
- **Sinergias** (líquidas, após imposto) → aumentam.
- **D&A nova sobre asset write-ups** (purchase accounting) → reduz (ver `purchase-accounting.md`).

## A mecânica passo a passo (pro forma EPS)
1. Some os **Pre-Tax Incomes** projetados de comprador + alvo.
2. Ajuste por: − foregone interest (caixa), − juros (dívida nova), + sinergias, − D&A nova (write-ups).
3. **Combined Net Income** = Combined Pre-Tax Income × (1 − tax rate do **comprador**).
4. **Total Shares** = ações do comprador + **ações emitidas** no deal (= Purchase Equity Value × %Stock / preço do comprador). As ações do **Seller somem** (deixa de existir).
5. **Combined EPS** = Combined Net Income / Total Shares.
6. **Accretion/Dilution %** = Combined EPS / EPS standalone do comprador − 1.

## Pegadinhas (o modelo simples engana)
- **Preço da ação do comprador muda** entre anúncio e fechamento → em deal com ações, a diluição varia. Faça **sensibilidade** sobre o preço do comprador.
- **Tax rate combinado** pode não ser o do comprador (jurisdições diferentes; em prova/entrevista, use o do comprador).
- **Purchase price real** ≠ Purchase Equity Value se houver refinanciamento de dívida, fees e excess cash.

## Como o output é usado na vida real
Screening de alvos, pitch a clientes, e munição em negociação (ex.: "aceitamos mais stock e menos cash se subir o preço 5% — ainda fica accretive pra você"). **Empresas não decidem deals com base no merger model** — é ferramenta de apoio.
