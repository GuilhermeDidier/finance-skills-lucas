# Best Practices de Modelagem + Convenções Contábeis

> Como construir um modelo que um sênior consegue auditar, que não quebra, e cujos inputs estão contabilmente corretos. Convenções contábeis baseadas no Credit Suisse IB Analyst Handbook.

## Layout e estrutura
- **Separe inputs de cálculos:** premissas/drivers numa aba (ou bloco) só deles. Nenhum cálculo deve depender de número "chumbado" no meio de uma fórmula.
- **Fluxo lógico:** uma aba/seção por bloco — Premissas → DRE → Balanço → DFC → Schedules (PP&E, WC, Dívida) → Outputs (DCF, sensibilidade).
- **Time series da esquerda pra direita:** histórico | projeção, anos em colunas, separados visualmente (ex.: linha vertical entre A e E).
- **Uma fórmula por linha:** a mesma fórmula copia limpa por todas as colunas do ano (consistência = menos erro).

## Convenção de cores (padrão de Wall Street)
| Cor | Significa |
|---|---|
| **Azul** | Input / hardcode / premissa (o que o usuário digita) |
| **Preto** | Fórmula / cálculo |
| **Verde** | Link de outra aba/planilha |
| **Vermelho** | Alerta / link externo / atenção |

Isso permite a qualquer um (e ao próprio autor, meses depois) saber na hora o que é premissa e o que é cálculo.

## Sinais e formatação
- **Despesas/saídas como negativos** (consistente) ou positivos — escolha uma convenção e mantenha. O comum é a DRE com despesas negativas e somar tudo.
- Sem números chumbados em fórmulas (use referência à célula de premissa).
- Formate números (milhares/milhões), %, casas decimais consistentes. Cabeçalho com unidade ("$ em milhões").

## Error checks (obrigatórios)
- **Balance check:** Ativo − (Passivo + PL) = 0 em todos os anos. Linha visível.
- **Caixa nunca negativo** sem revolver acionado.
- **DFC bate com o caixa do balanço** (Δ caixa da DFC = variação do caixa no balanço).
- **Soma das fontes = soma dos usos** (em transações).
- Crie uma célula-mestre "ERROR CHECK" que agrega todos os checks (TRUE/FALSE).

## Cenários e sensibilidade
- **Toggle de cenário:** uma célula (Base/Bull/Bear) que troca conjuntos de premissas (via CHOOSE/INDEX). Não duplique abas.
- **Tabelas de sensibilidade** (Data Table do Excel) 1-D e 2-D nas variáveis que mais movem o resultado (crescimento, margem, WACC, exit multiple).
- Documente as premissas de cada cenário.

## Higiene geral
- **Não circular sem necessidade:** ative iteration só quando o modelo exige (debt schedule, TSM). Tenha um circuit breaker.
- **Auditabilidade:** evite fórmulas monstro; quebre em linhas intermediárias. Use F2/precedentes para rastrear.
- **Versionamento:** salve versões datadas antes de mudanças grandes.
- **Documente premissas-chave** em comentários/notas.

---

## Convenções contábeis que afetam os inputs (CS Handbook)

### Leases (IFRS 16 / ASC 842, 2019+)
- **Finance leases:** capitalizados — ativo (right-of-use) e passivo (lease liability) no balanço; afetam D&A e juros, **não** o EBITDA "puro".
- **Operating leases (pré-IFRS 16):** ficavam fora do balanço, impactando só o EBITDA via aluguel. Sob IFRS 16, a maioria entrou no balanço.
- Implicação: ao comparar empresas/períodos sob padrões diferentes, padronize (EBITDAR) — ver `../valuation-modeling/references/dcf.md`.

### Pensões (IAS 19)
- Reconheça no balanço a **posição líquida**: valor presente da obrigação de benefício definido (DBO) menos o fair value dos ativos do plano.
- Plano sub-financiado = passivo "debt-like" (entra no net debt / EV bridge).

### Participações em outras empresas
- **Subsidiárias (consolidação integral):** 100% da receita/lucro na DRE; a fatia de terceiros vira **minority/noncontrolling interest** (no PL e subtraída no net income atribuível).
- **Associates/coligadas (equity method):** reconhece só a **fatia** do lucro líquido numa linha única da DRE; a participação é um ativo. Trate como "cash-like" no EV bridge (subtrai).

### Marginal vs effective tax rate
- Para projeção/DCF use a **marginal** (padrão ~25%); a **effective** (a que de fato paga) difere por créditos fiscais, despesas não-dedutíveis, deferred taxes. Use a effective histórica como referência de sanidade.
