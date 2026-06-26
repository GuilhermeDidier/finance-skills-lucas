# Fontes de dados macro e como tratar

> Onde puxar, com que pacote, e as armadilhas (frequência, dessazonalização, real vs nominal, revisões). Inclui fontes **brasileiras** que faltam nas skills genéricas.

## Tabela de fontes

| Fonte | Cobertura | Pacote Python | Chave? |
|---|---|---|---|
| **FRED** (St. Louis Fed) | US + global macro, séries prontas | `fredapi` / `pandas-datareader` | grátis |
| **World Bank** | desenvolvimento, cross-country | `wbdata` / `wbgapi` | não |
| **IMF** | IFS, WEO, BoP | `pandasdmx` / `imfp` | não |
| **OECD** | países OCDE, indicadores | `pandasdmx` (SDMX) | não |
| **BCB-SGS** 🇧🇷 | Selic, IPCA, câmbio, fiscal, crédito | `python-bcb` | não |
| **BCB Expectativas (Focus)** 🇧🇷 | expectativas de mercado | `python-bcb` (Expectativas) | não |
| **IBGE-SIDRA** 🇧🇷 | PIB, IPCA, PNAD, PMC/PMS/PIM | `sidrapy` | não |
| **IPEADATA** 🇧🇷 | agregador macro/regional BR | `ipeadatapy` | não |
| **Yahoo / investing** | mercado (câmbio, ações, juros) | `yfinance` | não |

## Receita — FRED (US/global)
```python
from fredapi import Fred
fred = Fred(api_key=os.environ["FRED_API_KEY"])  # chave grátis em fred.stlouisfed.org
s = fred.get_series("CPIAUCSL", observation_start="2000-01-01")
```
Séries-chave: `GDPC1` (PIB real), `UNRATE` (desemprego), `CPIAUCSL`/`PCEPI` (preços), `FEDFUNDS`/`DGS10`/`T10Y2Y` (juros/curva), `M2SL` (moeda).

## Receita — Brasil (o diferencial)
```python
# BCB - Sistema Gerenciador de Séries (SGS)
from bcb import sgs
df = sgs.get({"selic": 432, "ipca": 433, "cambio": 1, "igpm": 189},
             start="2010-01-01")
# códigos SGS úteis: 432 Selic meta % a.a. | 433 IPCA % mês | 1 câmbio venda
#                    189 IGP-M | 4189 Selic acumulada | 13521 DBGG % PIB

# BCB - Expectativas (Focus)
from bcb import Expectativas
em = Expectativas().get_endpoint("ExpectativasMercadoAnuais")

# IBGE - SIDRA (PIB, IPCA por grupo, PNAD)
import sidrapy
ipca = sidrapy.get_table(table_code="1737", territorial_level="1",
                         ibge_territorial_code="all", period="last%2012")

# IPEADATA
import ipeadatapy as ip
ip.timeseries("PRECOS12_IPCA12")
```

## Tratamento — as armadilhas
1. **Frequência:** não misture sem alinhar. Agregue (média/soma/fim de período conforme a variável: estoque vs fluxo) — fluxo (PIB) soma; estoque (dívida, câmbio) fim de período.
2. **Dessazonalização:** atividade/emprego têm sazonalidade. Use série **dessazonalizada** (SA) para ciclo, ou aplique X-13-ARIMA-SEATS (`statsmodels.x13`). Não dessazonalize preço de mercado.
3. **Real vs nominal:** deflacione para análise de ciclo/crescimento; nominal para arrecadação/dívida. Use o deflator certo (IPCA p/ consumo, deflator do PIB p/ agregado).
4. **Variação:** preferir **log-diferença** (≈ variação %) para estacionar e interpretar; acumulado 12m para inflação.
5. **Revisões / vintages:** PIB e contas são revisados. Para replicar uma decisão histórica, use **dados de vintage** (ALFRED no FRED) — senão há look-ahead.
6. **Quebras/metodologia:** mudanças de base (ex.: nova PNAD, base do PIB) criam degraus — encadeie séries com cuidado.
7. **Convenções BR:** juros em DU/252; cuidado ao comparar com séries ACT.

## Boas práticas
- API key em **variável de ambiente**, nunca no código.
- **Cache local** (parquet) para não bater a API toda hora; rate-limit em downloads em lote.
- Documente código da série + fonte + data de extração (séries mudam/revisam).
- Função única de carga → DataFrame com índice de data, colunas nomeadas, frequência explícita.

## Catálogo de códigos SGS mais usados (mesa BR)
| Código | Série | Freq. |
|---|---|---|
| 432 | Selic meta (% a.a.) | diária |
| 4189 | Selic acumulada no mês anualizada | mensal |
| 433 | IPCA (% mês) | mensal |
| 13522 | IPCA acumulado 12m | mensal |
| 189 | IGP-M (% mês) | mensal |
| 1 | Câmbio R$/US$ venda | diária |
| 1207 | Reservas internacionais (US$) | mensal |
| 24364 | IBC-Br (índice) | mensal |
| 13521 | DBGG (% PIB) | mensal |
| 4513 | Resultado primário gov. central | mensal |
| 20714 | Crédito total (% PIB) | mensal |

> ⚠️ Séries **diárias** (432, 1, DI) têm **limite de 10 anos por consulta** no SGS — puxe em janelas e concatene (ver `scripts/var-real.py` na própria skill).

## Vintage / real-time data
Para **backtestar previsão** sem look-ahead, use o dado **como era na época** (PIB/contas são revisados):
- **ALFRED** (FRED archival) — `fredapi` aceita `realtime_start`/`realtime_end`.
- BCB e IBGE não expõem vintage facilmente; registre a data de extração e versione os pulls.

## Conexão com o resto do repo
- **SETUP-EXTRAS.md** do repo: `brapi.dev` (MCP) p/ dados de mercado BR (B3/CVM), EODHD/Alpha Vantage p/ global. As skills dão o conhecimento; os extras dão dados de mercado e execução.
- Curva DI / preço de instrumentos → skills **bond-modeling** e **derivatives-modeling**.

## Fontes
Documentação das APIs (FRED, World Bank, BCB-SGS, IBGE-SIDRA, IPEADATA) · `python-bcb`, `sidrapy`, `ipeadatapy`, `fredapi` · QuantEcon (fontes de dados em Python).
