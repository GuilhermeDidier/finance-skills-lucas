# Qualidade dos Lucros — Detectando Shenanigans

> Fonte: Howard Schilit, *Financial Shenanigans*. Antes de projetar, o histórico precisa ser **limpo e real**. Um modelo construído sobre lucros maquiados projeta ficção. Esta é a etapa de "scrubbing" levada a sério.

## Por que isso importa na modelagem
- Drivers (margens, DSO, crescimento) vêm do histórico. Se o histórico está inflado por truques contábeis, suas premissas herdam a distorção.
- O FCF é mais difícil de manipular que o lucro — **divergência persistente entre net income e cash flow das operações é o maior sinal de alerta**.
- Casos clássicos citados por Schilit: Waste Management, Rite Aid, MicroStrategy, Cendant, Enron — todos detectáveis nos números antes do colapso.

## As 7 categorias de Earnings Manipulation (Schilit)

### Inflar o lucro do período atual
1. **Reconhecer receita cedo demais ou de qualidade questionável** — registrar venda antes da entrega/aceitação; "bill and hold"; reconhecer contratos de longo prazo agressivamente; channel stuffing (empurrar estoque pro canal).
2. **Receita fictícia (bogus revenue)** — vendas sem substância econômica; receita de transações com partes relacionadas; "round-tripping" (vender e recomprar).
3. **Aumentar lucro com ganhos não-recorrentes/one-time** — registrar ganho de venda de ativo como receita operacional; lucro de investimentos como redução de despesa.
4. **Empurrar despesas correntes para período futuro** — capitalizar o que deveria ser despesa (clássico: WorldCom capitalizando custos de linha); depreciar/amortizar devagar demais; não baixar ativos deteriorados.
5. **Não registrar ou reduzir indevidamente passivos** — omitir obrigações; reconhecer receita de pagamentos futuros antecipados; reservas insuficientes (warranties, devoluções).

### Mover lucro entre períodos (gerenciar a tendência)
6. **Empurrar receita corrente para o futuro** — criar reservas ("cookie jar") em anos bons para soltar em anos ruins; reconhecimento conservador artificial para suavizar.
7. **Trazer despesas futuras para o presente como special charge** — "big bath": jogar despesas futuras num grande write-off agora (quando o ano já está ruim) para aliviar anos futuros.

## Red flags práticos (o que olhar)
- **Net income sobe mas cash flow das operações cai** (ou diverge persistentemente) → qualidade baixa.
- **A/R crescendo muito mais rápido que a receita** (DSO subindo) → receita possivelmente empurrada/fictícia.
- **Estoque crescendo mais rápido que vendas** (DIH subindo) → demanda fraca ou problema de obsolescência escondido.
- **Capitalização crescente de custos** (software, custos "de desenvolvimento") → despesa disfarçada de ativo.
- **Margem subindo sem explicação operacional** → revise não-recorrentes e mudanças contábeis.
- **Uso recorrente de "one-time charges"** todo ano → não são one-time.
- **Mudança de política contábil / estimativas** (vida útil, reservas) bem na hora certa.
- **Gap entre lucro contábil (book) e fiscal (tax)** crescente.
- **Receita "outra"/não-operacional** inflando o topo.

## Como aplicar antes de modelar
1. Reconstrua o **histórico ajustado** (Adjusted EBITDA/EBIT/Net Income) removendo não-recorrentes e revertendo agressividade contábil.
2. Reconcilie **net income vs cash flow operacional** ano a ano — explique divergências.
3. Cheque a **tendência de DSO, DIH e capitalização** — se pioram, ajuste as premissas para o nível "real", não o reportado.
4. Só então projete. Documente cada ajuste (rastreabilidade).

> 🔗 Conecta com o scrubbing em `../valuation-modeling/references/mechanics.md` e com a análise de earnings da skill `earnings`.
