# Dados em painel

> Painel = mesmas unidades $i$ ao longo de $t$. Ganho central: **controlar heterogeneidade não-observada invariante no tempo** via efeitos fixos. Fontes: Wooldridge (*Cross Section & Panel*, cap. 10–11), Roodman (2009, GMM), Arellano-Bond (1991), Blundell-Bond (1998).

## 1. Por que painel

Modelo: $y_{it}=\beta x_{it}+c_i+u_{it}$, com $c_i$ = efeito individual não-observado (qualidade da gestão, cultura do país, "tipo" da pessoa).

- Se $c_i$ correlaciona com $x_{it}$ → pooled OLS é **viesado** (é OVB com omitida $c_i$).
- Efeitos fixos eliminam $c_i$ **sem observá-lo** — a vantagem central do painel.

## 2. Estimadores

| Estimador | Como | Remove $c_i$? | Identifica de | Quando |
|---|---|---|---|---|
| **Pooled OLS** | ignora painel | não | tudo | raramente válido |
| **Within / FE** | desvio da média do indivíduo | **sim** | variação *intra*-unidade | $c_i$ corr. com $x$ (default) |
| **Between** | médias por indivíduo | não | variação *entre* | raro |
| **Random Effects** | GLS, $c_i$ aleatório | não (assume $c_i\perp x$) | within+between | só se $c_i\perp x$ |
| **First Differences** | $\Delta y=\beta\Delta x+\Delta u$ | sim | variação temporal | T=2 ou erros RW |

### Within transformation (numérico)
$\ddot y_{it}=y_{it}-\bar y_i$. Exemplo: firma com $y=\{10,12,14\}$ → $\bar y=12$ → $\ddot y=\{-2,0,2\}$. Qualquer característica **invariante no tempo** (setor fixo, país, sexo) tem $\ddot x=0$ e **desaparece** — por isso FE não estima coeficiente de variável invariante (e absorve qualquer confundidor invariante).
- **FE vs FD:** com $T=2$ são idênticos. Com $T>2$: FE eficiente se $u$ i.i.d.; FD eficiente se $u$ é random walk. Discrepância grande entre os dois é sinal de má especificação.

**Two-way FE:** soma efeitos de tempo $\lambda_t$ (choques comuns a todos num período). Espinha do DiD.

## 3. FE vs RE — teste de Hausman

- **RE** mais eficiente **se** $c_i\perp x_{it}$ (hipótese forte). Se correlacionar, RE é **viesado**.
- **Hausman:** H0 = RE consistente (diferença FE−RE não-sistemática). Rejeitou → **FE**.
- **Mundlak / Correlated Random Effects:** inclui as médias por indivíduo $\bar x_i$ como regressores — recupera os coeficientes within **e** permite estimar variáveis invariantes no tempo. Versão moderna preferida ao "FE vs RE" binário.
- Na prática aplicada, **FE é o default**; RE é raro fora de contextos específicos.

## 4. Erros-padrão em painel
- **Cluster por indivíduo** (`i`) por padrão — captura autocorrelação serial dentro da unidade (Bertrand-Duflo-Mullainathan mostraram que ignorar isso em DiD subestima SE drasticamente).
- **Two-way clustering** (`i` e `t`) com choques comuns por período.
- **Driscoll-Kraay** p/ dependência espacial/temporal com T grande.

## 5. Painel dinâmico (lagged dependent variable)

$y_{it}=\rho y_{i,t-1}+\beta x_{it}+c_i+u_{it}$

- **Viés de Nickell:** lag da dependente + FE → within **viesado** porque $\bar y_i$ correlaciona com $u$. Viés $\approx -(1+\rho)/(T-1)$ → **sério com T pequeno**, some quando $T\to\infty$.
- **Arellano-Bond (difference GMM):** diferencia (remove $c_i$) e instrumenta $\Delta y_{t-1}$ com **níveis defasados** ($y_{t-2}, y_{t-3},\dots$).
- **Blundell-Bond (system GMM):** acrescenta equações em **nível** instrumentadas por **diferenças defasadas** — muito melhor com séries **persistentes** ($\rho$ perto de 1), onde os instrumentos do diff-GMM são fracos.
- **Diagnósticos GMM (obrigatórios):**
  - **AR(1)** esperado significativo, **AR(2) NÃO** deve rejeitar (Arellano-Bond test de autocorrelação).
  - **Hansen J** (não Sargan, que é frágil a heterocedasticidade): não rejeitar, mas **Hansen J = 1,000 é red flag** de instrumentos demais.
  - **Não prolifere instrumentos** (nº de instrumentos < nº de grupos): use `collapse` e limite os lags. Roodman (2009): "instrument proliferation" enfraquece o Hansen J e enviesa.

## 6. Painéis especiais
- **Desbalanceado:** ok, mas cuide de **atrito/seleção** (por que faltam observações? — se relacionado ao desfecho, viés).
- **Painel macro (N e T grandes):** raízes unitárias em painel (Im-Pesaran-Shin, Levin-Lin-Chu), cointegração em painel (Pedroni, Westerlund), **dependência de cross-section** (CD test de Pesaran) → estimadores **CCE/Mean Group** (Pesaran). Ver também skill **macroeconomics**.

## Armadilhas
- ❌ RE sem Hausman (assume $c_i\perp x$ — quase sempre falso).
- ❌ Esquecer efeitos de **tempo** (two-way) e creditar a $x$ um choque comum.
- ❌ Lag da dependente com FE simples (viés de Nickell) → GMM.
- ❌ System GMM com instrumentos demais (Hansen J → 1,000; use `collapse`).
- ❌ Não clusterizar por indivíduo (subestima SE em DiD — BDM 2004).
- ❌ Interpretar coeficiente de variável invariante no tempo em FE (não existe).

## Fontes
Wooldridge (within/FE/RE/Mundlak) · Bertrand-Duflo-Mullainathan (2004, SE em DiD) · Arellano-Bond, Blundell-Bond · Roodman (2009, `xtabond2`, instrument proliferation) · Pesaran (CCE, CD test).
