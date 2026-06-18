# Gráficos e Exhibits Clássicos de IB

> Os exhibits recorrentes de um pitchbook e como construí-los. O dado vem das skills profundas; aqui é a forma visual.

## Football Field (o exhibit de valuation)
- **Barras horizontais flutuantes**, uma por metodologia (DCF perpetuidade, DCF exit multiple, trading comps, transaction comps, LBO, 52-week range, analyst targets), mostrando a **faixa** de valor por ação/EV.
- Linha vertical no **preço atual** (e/ou na faixa selecionada). Rótulos de min/max em cada barra.
- Opcional: tabela embaixo com os **múltiplos implícitos** de cada faixa. → skill valuation-modeling (`pitfalls-and-football-field.md`).
- Action title diz a **conclusão** (ex.: "Triangulação aponta valor de R$52–57/ação, ~10% acima do mercado").

## Sources & Uses (M&A/LBO/financing)
- Tabela de duas colunas: **Uses** (compra do equity, refi de dívida, fees) e **Sources** (caixa, dívida nova por tranche, equity/stock). **Totais batem.** → skills mna/lbo/dcm.

## Comps table (trading/transaction)
- Linhas = empresas/transações; colunas = métricas (EV, EV/EBITDA, EV/EBIT, P/E, crescimento, margem). **Mean/median** destacados; outliers marcados (NM). → skill valuation-modeling.

## Accretion/Dilution e sensibilidade
- Tabela do EPS standalone → Combined EPS, com a **% de accretion/dilution**; tabela de **sensibilidade 2-D** (preço × % stock, ou WACC × g). → skills mna/valuation.

## Org chart / estrutura societária
- Caixas hierárquicas (controladora → subsidiárias, % de participação), antes/depois do deal. Mostra fluxo de controle e minorities.

## Process timeline / cronograma
- Linha do tempo horizontal com fases (preparação → 1º round → DD → 2º round → signing → closing) e marcos/datas. → skill mna (deal-process).

## Waterfall chart
- Colunas que somam/subtraem para mostrar uma ponte (ex.: EV → equity value; ou bridge de criação de valor de um LBO). Cores para acréscimo/decréscimo.

## Gráficos de mercado
- **Share price / trading (52-week)**, múltiplos do setor ao longo do tempo, volume de M&A/emissões. Geralmente linha ou coluna, limpos.

## Boas práticas de gráfico
- **Um gráfico, uma mensagem** — escolha o tipo que prova o título.
- **Minimize "chart junk":** sem 3D, sem gradientes pesados, sem grades densas; rótulos diretos > legenda quando possível.
- **Eixos honestos:** comece em zero quando a escala enganaria; rotule unidades.
- **Destaque** a série/ponto que sustenta o argumento (cor de marca vs cinza para o resto).
- **Data labels** nos pontos-chave; fonte no rodapé.
- **think-cell** (add-in) é o padrão de mercado para waterfalls, Gantt e gráficos linkados a Excel (ver `productivity.md`).

## Conectar
Os números → skills valuation/mna/lbo/dcm. Formatação → `formatting-conventions.md`. Construção rápida → `productivity.md`.
