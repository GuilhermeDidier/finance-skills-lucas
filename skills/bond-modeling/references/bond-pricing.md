# Precificação de Títulos

> Fonte: Securato + convenções de mercado. Como achar o preço justo de um título e ler suas medidas de yield.

## O princípio: preço = VP dos fluxos
```
Preço = Σ  Cupom_t / (1 + y)^t  +  Principal / (1 + y)^n
```
- **y** = yield (taxa de desconto / YTM). Subir y → preço cai (**relação inversa preço-yield**).

## Zero-cupom vs com cupom
- **Zero-cupom:** paga só principal + juros no vencimento. `Preço = VF / (1 + y)^n`. Ex.: **LTN, LFT, NTN-B Principal** no Brasil.
- **Com cupom:** paga juros periódicos + principal no fim. Ex.: **NTN-F** (prefixado), **NTN-B** (indexado ao IPCA), com cupom **semestral**.

## Par, ágio (premium) e deságio (discount)
| Relação | Preço | Significado |
|---|---|---|
| Cupom = yield | = par (face) | título "ao par" |
| Cupom > yield | > par (ágio) | paga mais que o mercado exige |
| Cupom < yield | < par (deságio) | paga menos que o mercado exige |
- Com o tempo, o preço **converge ao par** no vencimento ("pull to par").

## Clean price vs dirty price (juros acruados)
```
Dirty price (preço de liquidação) = Clean price + juros acruados
Juros acruados = cupom × (dias decorridos / dias do período)
```
- O **clean price** é o cotado; o **dirty price** é o que se paga de fato (inclui o cupom acumulado desde o último pagamento). No Brasil fala-se em **preço "sujo" (PU)** com os juros corridos.

## Medidas de yield (não confundir)
- **Current yield** = cupom anual / preço. Ignora ganho/perda de capital e timing → medida fraca.
- **Yield-to-maturity (YTM/TIR):** a taxa que iguala preço ao VP de todos os fluxos até o vencimento (a medida principal). Assume reinvestimento dos cupons à própria YTM.
- **Yield-to-call (YTC):** YTM até a data de call (para títulos resgatáveis); use o **yield-to-worst** (o menor entre YTM e YTCs) para conservadorismo.
- **Yield to maturity ≠ cupom** (só são iguais quando o título está ao par).

## PU — Preço Unitário (Brasil)
No mercado brasileiro, títulos públicos são cotados em **PU** (preço unitário, em R$), derivado da taxa negociada:
```
PU (prefixado, DU/252) = VN / (1 + taxa_ano)^(du/252)
```
onde VN = valor nominal (ex.: R$1.000 da LTN) e du = dias úteis até o vencimento. Detalhe por instrumento → `brazilian-instruments.md`.

## Spread
O yield de um título corporativo = **taxa livre de risco (curva soberana) + credit spread**. O spread remunera risco de crédito/liquidez. Ver `yield-curve-and-credit.md`.

## Conectar
Preço calculado aqui alimenta a **sensibilidade** (duration/convexity em `duration-convexity.md`) e a **marcação a mercado** (`brazilian-instruments.md`).
