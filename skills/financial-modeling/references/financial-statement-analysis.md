# Análise de Demonstrações e Ratios — Fingerprint de Setor

> Fonte: Ivey/HBS, *Identifying Industries: Financial Statement Analysis*. Antes de modelar, é preciso **ler** os financials e entender o modelo de negócio. As demonstrações têm uma "impressão digital" do setor — reconhecê-la valida premissas e detecta anomalias.

## Por que isto importa na modelagem
- Fundamentos são parecidos **dentro** de um setor e variam muito **entre** setores. Usar common-size (% da receita / % do ativo) e ratios revela o modelo de negócio.
- Serve para: sanity-check de premissas (suas margens/DSO/DIH batem com o setor?), benchmarking de comps, e detectar números que "não combinam" com o tipo de negócio.

## As 4 famílias de ratios (e o que revelam)
| Família | Ratios | Revela |
|---|---|---|
| **Liquidez** | Cash ratio, acid test (quick), current ratio | Folga de caixa de curto prazo |
| **Eficiência** | DSO (AR days), inventory turnover, DSI/DIH, asset turnover | Como o capital gira no ciclo operacional |
| **Alavancagem** | Debt/assets, debt/equity, interest coverage | Estrutura de capital e risco financeiro |
| **Rentabilidade** | Gross margin, operating margin, return on sales, ROA, ROE, ROIC | Onde e quanto a empresa lucra |

Use **common-size statements** (balanço como % do ativo; DRE como % da receita) para comparar empresas de tamanhos diferentes.

## Fingerprints de setor (os "tells")
| Setor | Marcas no balanço/DRE | Ratios típicos |
|---|---|---|
| **Software/Tech** | Pouco PP&E, muito caixa/investimentos, **R&D alto**, deferred revenue | **Gross margin altíssimo** (~70–90%), asset turnover baixo |
| **Farmacêutica** | R&D alto, **goodwill/intangíveis altos** (M&A), pouco inventário | Gross margin alto, net margin alto, DSI moderado |
| **Bebidas/Branding** | Goodwill/intangível alto (marca), PP&E moderado | **Gross margin alto** (poder de marca), ROIC alto |
| **Varejo (grocery)** | **Inventário alto, PP&E (lojas)**, pouco AR (paga à vista) | **Margens finíssimas**, **inventory turnover alto**, asset turnover alto |
| **Varejo (livraria/bens duráveis)** | Inventário alto, **DSI alto** (gira devagar) | Margem baixa, turnover baixo |
| **Restaurante (franquia)** | PP&E moderado, inventário baixíssimo (perecível), às vezes **equity negativo** (recompras) | Gross/net margin **altos** no modelo de franquia |
| **Companhia aérea** | **PP&E enorme** (aviões) + capital leases, **alta alavancagem** | Margens baixas/voláteis |
| **Óleo & gás** | **PP&E gigante**, ativo intensivo | Margens cíclicas |
| **Internet retail** | Inventário/PP&E relativamente baixos, **payables altos** (financia-se no fornecedor) | **Net margin baixo**, **asset turnover alto** |
| **Banco** | **"AR" gigantesco** (= empréstimos), **alavancagem altíssima**, payables enormes (depósitos) | AR days absurdo, asset turnover baixíssimo, estrutura totalmente distinta |

### Heurística rápida de identificação
1. **AR days absurdo + alavancagem extrema + asset turnover ~0** → **Banco** (estrutura financeira, não industrial).
2. **PP&E dominando o ativo** → capital-intensivo (aérea, óleo & gás, telecom, utilities).
3. **Inventário alto + margem fina + giro alto** → varejo/grocery; **inventário alto + giro baixo** → bens duráveis/livraria.
4. **Gross margin altíssimo + R&D** → software/pharma; **+ goodwill alto** → pharma (cresce por M&A); **+ caixa/investimentos enormes** → big tech.
5. **Goodwill/intangível alto + margem alta sem R&D** → marca (bebidas/consumo).
6. **Equity negativo + margem alta + dívida alta** → empresa madura que recomprou muitas ações (ex.: restaurante/consumo de marca forte).

## Como usar antes de modelar
1. Rode os common-size + os 4 grupos de ratios da empresa e dos peers.
2. Confirme que o **fingerprint bate** com o negócio declarado — se não bate, investigue (mudança de mix, item não-recorrente, ou shenanigan; ver `quality-of-earnings.md`).
3. Use os ratios do setor como **âncora das premissas** (margens, DSO/DIH/DPO, capex %) em `projection-drivers.md`.
4. Anomalias vs o setor = bandeira para due diligence.
