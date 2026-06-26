---
name: macroeconomics
description: Macroeconomia aplicada para mercado/banking — frameworks de análise (oferta/demanda agregada, IS-LM, Solow, Phillips, regra de Taylor, política monetária e fiscal, contas nacionais e balanço de pagamentos), séries temporais macro (estacionariedade, ARIMA, VAR/SVAR, cointegração/VECM, funções de resposta a impulso, previsão e nowcasting) e dados macro (FRED, World Bank, IMF, e fontes brasileiras BCB/SGS, IBGE/SIDRA, IPEADATA), com forte contexto do mercado brasileiro (Copom/Selic, IPCA, câmbio, fiscal, curva DI). Use quando o usuário quiser interpretar/projetar indicadores macro, montar um modelo de série temporal (VAR, ARIMA, cointegração), prever inflação/juros/PIB/câmbio, ler um ciclo econômico, entender política monetária/fiscal, ou puxar e tratar dados macro. Gatilhos: "macroeconomia", "macro", "PIB", "inflação", "IPCA", "Selic", "Copom", "juros", "câmbio", "política monetária", "política fiscal", "regra de Taylor", "Phillips", "IS-LM", "ciclo econômico", "VAR", "SVAR", "cointegração", "VECM", "ARIMA", "estacionariedade", "previsão", "nowcasting", "FRED", "BCB", "SGS", "IBGE", "IPEADATA".
---

# Macroeconomics (Macroeconomia Aplicada)

Skill para **interpretar, modelar e projetar a economia agregada** com olhar de mercado/banking. Dois fios condutores: (1) um **framework** para ler cada indicador dentro do ciclo e da função de reação do Banco Central; (2) **séries temporais macro** feitas com honestidade (estacionariedade primeiro, fora-da-amostra depois). Forte ênfase no **Brasil** (Copom/Selic, IPCA, câmbio, fiscal, curva DI). A econometria de identificação causal (DiD/IV/painel) → skill **econometrics**.

## Quando usar
- **Interpretar** um indicador macro (PIB, IPCA, emprego, hiato, câmbio) dentro do ciclo e da reação do BC.
- **Projetar/prever** uma variável macro: inflação, Selic/juros, PIB, câmbio — com modelo de série temporal.
- Montar um **modelo de séries temporais**: ARIMA, **VAR/SVAR**, **cointegração/VECM**, IRFs, decomposição de variância.
- Fazer **nowcasting** com indicadores antecedentes / dados de alta frequência.
- Entender **política monetária e fiscal** (regra de Taylor, dominância fiscal, sustentabilidade da dívida).
- **Puxar e tratar dados macro** (FRED/World Bank/IMF e BCB-SGS/IBGE-SIDRA/IPEADATA).

**Quando NÃO usar:** identificação de efeito causal micro (DiD/IV/RDD/painel) → skill **econometrics**; precificação de títulos/curva de juros como instrumento → skill **bond-modeling**; câmbio/juros como derivativo (DI futuro, cupom cambial, swaps) → **derivatives-modeling**.

## Princípios
1. **Todo indicador é lido contra uma referência:** expectativa (consenso), meta (do BC), potencial (hiato) ou o próprio histórico. Número solto não diz nada.
2. **O BC reage a expectativas e hiato**, não ao dado corrente isolado — pense pela **função de reação** (Taylor/Copom).
3. **Estacionariedade primeiro.** Regressão de séries não-estacionárias gera correlação espúria; ou diferencie, ou modele a **cointegração** (VECM).
4. **Previsão honesta = fora-da-amostra.** Ajuste in-sample não vale nada; valide com janela rolante e compare contra benchmark ingênuo (random walk).
5. **Identificação em VAR exige estrutura** (ordenamento de Cholesky, restrições de sinal): a IRF depende das suposições, não só dos dados.
6. **Contexto BR muda a leitura:** indexação, DU/252, histórico inflacionário, prêmio de risco fiscal/cambial e dominância fiscal alteram a transmissão.

## Roteiro
1. **Enquadre a pergunta**: interpretar um dado, prever uma variável, ou estimar relações dinâmicas? — ver `references/macro-frameworks.md`.
2. **Pegue os dados** na fonte certa e trate (frequência, dessazonalização, real vs nominal) — `references/data-sources.md`.
3. **Teste estacionariedade** (ADF/KPSS) e decida o tratamento (diferenciar vs cointegrar) — `references/macro-timeseries.md`.
4. **Modele**: ARIMA (univariado), VAR/SVAR (dinâmica multivariada), VECM (com cointegração); gere IRFs/forecast — `references/macro-timeseries.md`.
5. **Contexto BR**: leia o resultado pela ótica Copom/fiscal/câmbio — `references/brazilian-macro.md`.
6. **Valide fora-da-amostra** e contra benchmark; explicite incerteza (bandas).

## Formato da saída
1. **Leitura do indicador/cenário** contra a referência (consenso/meta/potencial) e o que muda na função de reação do BC.
2. **Modelo** usado (especificação, ordem, defasagens, identificação) e por quê.
3. **Resultado**: projeção com **banda de incerteza**, IRFs ou relação de longo prazo (cointegração) — interpretados economicamente.
4. **Validação**: desempenho fora-da-amostra vs benchmark ingênuo.
5. **Contexto BR**: implicação para Selic/curva DI/câmbio/fiscal.
6. **Código** reprodutível (R/Python) + fonte dos dados e premissas.

## Documentos de apoio
- `references/macro-frameworks.md` — oferta/demanda agregada, IS-LM, Solow, curva de Phillips, regra de Taylor, contas nacionais, balanço de pagamentos, ciclo econômico e como ler cada indicador.
- `references/macro-timeseries.md` — estacionariedade (ADF/KPSS), ARIMA/SARIMA, VAR/SVAR (Cholesky, restrições de sinal, IRF, FEVD), cointegração/VECM (Engle-Granger, Johansen), previsão e validação out-of-sample. **Fecha a lacuna de séries temporais macro.**
- `references/brazilian-macro.md` — BCB/Copom/Selic/ata, sistema de metas de inflação, IPCA e núcleos, câmbio e intervenção, fiscal (dívida/PIB, regra fiscal), curva DI e expectativas Focus, dominância fiscal.
- `references/data-sources.md` — FRED (`fredapi`), World Bank (`wbdata`), IMF/OECD, e BR: BCB-SGS (`python-bcb`), IBGE-SIDRA (`sidrapy`), IPEADATA; séries-chave, frequência, dessazonalização e armadilhas (vintages/revisões).
- `references/worked-example.md` — um VAR Selic×IPCA×câmbio (ou previsão de IPCA com SARIMA) com testes, IRF e validação fora-da-amostra fechando ponta a ponta.
