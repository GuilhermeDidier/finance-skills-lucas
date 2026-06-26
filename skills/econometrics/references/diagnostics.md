# Diagnósticos e testes de especificação

> Rodar o modelo é fácil; saber se ele é confiável é o trabalho. Cada problema abaixo tem um teste e uma correção.

## 1. Heterocedasticidade
- **Sintoma:** $Var(u\mid X)$ não constante (comum em dados de seção cruzada, escala variando).
- **Testes:** Breusch-Pagan, White.
- **Consequência:** OLS não-viesado, mas **SE clássico inválido**.
- **Correção:** **erros-padrão robustos (HC)** — na prática, use sempre robusto/cluster e nem teste.

## 2. Autocorrelação (séries temporais / painel)
- **Sintoma:** $Corr(u_t,u_{t-1})\ne 0$.
- **Testes:** Durbin-Watson (clássico, limitado), Breusch-Godfrey (geral), Ljung-Box (resíduos).
- **Correção:** **HAC (Newey-West)**; em painel, cluster por indivíduo; ou modelar a dinâmica (lags).

## 3. Multicolinearidade
- **Sintoma:** regressores muito correlacionados → SE inflados, coeficientes instáveis (mas OLS ainda não-viesado).
- **Diagnóstico:** **VIF** (>10 alerta), correlações altas, sinais "errados".
- **Correção:** não é doença fatal — se a colinearidade não envolve a variável de interesse, ignore. Senão: remover redundância, combinar variáveis, mais dados.

## 4. Especificação funcional
- **RESET (Ramsey):** detecta forma funcional errada (faltam termos não-lineares/interações). H0: especificação ok.
- Considere logs (elasticidades, reduz heterocedasticidade), polinômios, interações.

## 5. Endogeneidade
- **Fontes:** variável omitida, simultaneidade, erro de medida, seleção.
- **Teste (com IV disponível):** **Hausman / Durbin-Wu-Hausman** — H0: regressor exógeno (OLS consistente). Rejeitou → use IV.
- **Sem instrumento**, endogeneidade não se "testa", só se argumenta/contorna pelo desenho.

## 6. Instrumentos (qualidade do IV)
- **Relevância / instrumento fraco:** **F de 1ª fase > 10** (Stock-Yogo); Montiel-Pflueger (effective F) é o padrão moderno; com fraco, use IC de **Anderson-Rubin** (robusto a weak IV).
- **Sobre-identificação:** **Hansen J / Sargan** (H0: todos os instrumentos exógenos). Só testável com mais instrumentos que endógenas — e não prova exogeneidade, só checa consistência mútua.

## 7. Outliers e influência
- **Leverage**, distância de **Cook**, DFBETA. Investigue antes de remover; reporte sensibilidade.
- Robust regression (Huber, quantílica) como checagem.

## 8. Normalidade dos resíduos
- Jarque-Bera, QQ-plot. **Irrelevante em amostra grande** (TCL cuida da inferência). Importa em amostra pequena.

## 9. Estabilidade dos parâmetros
- **Chow test** (quebra em data conhecida); CUSUM, Bai-Perron (quebras desconhecidas, séries temporais).

## Checklist mínimo por estratégia
- **OLS/cross-section:** robusto HC, RESET, VIF se preocupado, suporte/outliers.
- **Painel FE:** cluster por `i`, two-way FE, Hausman (se cogitar RE).
- **IV:** F de 1ª fase, Hausman (endogeneidade), Hansen J (se sobre-identificado), AR se fraco.
- **DiD:** pré-tendências (event study), placebo, escalonamento (Bacon), clustering no nível do tratamento.
- **RDD:** McCrary (densidade), bandwidth ótimo + robustez, continuidade de covariáveis.
- **Séries temporais:** estacionariedade (ADF/KPSS — ver skill **macroeconomics**), autocorrelação (Breusch-Godfrey), HAC.

## Robustez sistemática — specification curve
Em vez de escolher "a" especificação, rode **todas as razoáveis** (combinações de controles, amostras, formas funcionais) e plote a distribuição do coeficiente de interesse (specification curve / multiverse analysis — Simonsohn-Simmons-Nelson). Um efeito robusto sobrevive à maioria; um frágil aparece só em cantos do espaço de especificações. Reporte mediana, dispersão e quantas specs são significativas — antídoto direto a p-hacking.

## Fontes
Wooldridge (testes de especificação) · Cameron-Trivedi (endogeneidade, overdispersion) · Stock-Yogo / Montiel-Pflueger (weak IV) · Andrews-Stock-Sun (2019, weak instruments survey) · Simonsohn-Simmons-Nelson (specification curve).
