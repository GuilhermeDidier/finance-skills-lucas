# Purchase Accounting, Goodwill e Estrutura do Deal

> Fonte: JP Morgan M&A Reference Manual + Merger Models Guide. Como a contabilidade da aquisição cria goodwill, write-ups e deferred taxes — e por que a estrutura (stock vs asset, taxable vs tax-free) muda tudo.

## Purchase Price Allocation (PPA) e Goodwill
Quando o comprador adquire o alvo, ele aloca o preço pago aos ativos/passivos a **fair value**; o que sobra vira **goodwill**.
```
Goodwill = Equity Purchase Price
         − Book Value do equity do alvo
         + Write-off do goodwill existente do alvo
         + Asset Write-Ups (PP&E e intangíveis a fair value)
         − Deferred Tax Liability criada pelos write-ups
         ± outros ajustes
```
Forma simplificada: **Goodwill = Preço pago − Fair Value dos ativos líquidos identificáveis**.
- **Asset write-ups:** PP&E e intangíveis de vida definida são marcados a fair value (acima do book). Goodwill é o resíduo (vida indefinida, **não amortiza**, sofre impairment test anual).

## O efeito que dói no EPS: nova D&A sobre write-ups
- Write-ups de PP&E e intangíveis criam **depreciação/amortização incremental** → reduz o lucro pro forma → **dilutivo**.
- Por isso write-ups grandes (comuns em alvos com muito intangível) pesam na accretion/dilution.

## Deferred Tax Liability (DTL) — por que aparece
Em deals **sem step-up fiscal** (a maioria dos stock deals), o write-up é só **contábil (book)**, não fiscal (tax). Resultado:
- Para fins **book**, deprecia-se sobre o valor maior (FMV) → menor lucro book.
- Para fins **tax**, deprecia-se sobre a base antiga → o benefício fiscal é menor.
- A diferença temporária cria uma **DTL** (FASB 109 / ASC 740): `DTL = Write-Up × tax rate`. Ela reduz o goodwill criado e reverte ao longo do tempo conforme a D&A incremental é "consumida".

## Stock Deal vs Asset Deal (e step-up)
| | Stock Purchase | Asset Purchase |
|---|---|---|
| O que se compra | As **ações** do alvo (assume ativos + passivos) | Os **ativos** específicos (e passivos selecionados) |
| Base fiscal (step-up) | Geralmente **sem step-up** → cria DTL | **Step-up**: base fiscal sobe a FMV → cria **DTA** (deprecia mais para fins fiscais) |
| Depreciação fiscal | Sobre base antiga | Sobre FMV (maior benefício fiscal) |
| Preferência | Vendedor (geralmente) | Comprador (geralmente — escudo fiscal maior) |
| Passivos ocultos | Comprador herda tudo | Comprador escolhe (deixa passivos pra trás) |

- **Step-up** = aumentar a base fiscal dos ativos para FMV, criando deferred tax asset e maior depreciação dedutível. Sem step-up, ativos revalorizados = FMV só para book; a depreciação book sobe mas a fiscal não.
- **Section 338 (h)(10):** elege tratar um stock deal **como** asset deal para fins fiscais (ganha o step-up mantendo a forma de stock) — comum quando o alvo é subsidiária de outra corporação ou S-corp.

## Taxable vs Tax-Free
- **Taxable:** vendedor paga imposto sobre o ganho agora. Tipicamente quando a consideração é **cash**. Comprador pode obter step-up.
- **Tax-free (reorganization):** vendedor difere o imposto — exige consideração predominantemente em **ações** do comprador (continuidade de interesse). Estruturas: merger estatutário, **forward/reverse triangular merger** (usa subsidiária para isolar passivos e atender requisitos fiscais).
- Forma de consideração (cash vs stock) interage com: tributação do vendedor, accretion/dilution, e quem assume o risco de variação de preço.

## Exemplo de step-up (JPM, simplificado)
PP&E de $180.000, vida 6 anos:
- **Sem step-up:** depreciação fiscal = $180.000/6 = $30.000/ano (base antiga).
- **Com step-up** (revalorizado a, digamos, FMV maior): deprecia sobre o FMV para book **e** tax → maior dedução fiscal, mas pode haver recapture tax pago no step-up.
- Para **book**, PP&E é sempre registrado a FMV (independe do step-up fiscal).

## Conexão
- A nova D&A e a DTL entram no **merger model** (afetam accretion/dilution) — ver `accretion-dilution.md`.
- Minorities/associates e o tratamento de net debt vêm do EV bridge da skill **valuation-modeling** (`references/mechanics.md`).
