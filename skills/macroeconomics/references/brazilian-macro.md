# Macro brasileira — leitura de mercado

> Contexto que muda a interpretação: regime de metas, indexação, histórico inflacionário, prêmio de risco fiscal/cambial e dominância fiscal.

## 1. Política monetária — BCB e Copom
- **Selic** = taxa básica (meta definida pelo **Copom**, ~8 reuniões/ano). Selic *meta* (decisão) vs Selic *efetiva* (over, no mercado de reservas).
- **Regime de metas de inflação** (desde 1999): meta definida pelo CMN para o **IPCA** (cheio), com banda de tolerância (±1,5 p.p.). Meta contínua a partir de 2025.
- **Ata do Copom** e **Relatório de Política Monetária (RPM)** (ex-RTI): leem o balanço de riscos e o juro neutro. Comunicação (forward guidance, balanço de riscos "assimétrico") move a curva tanto quanto a decisão.
- **Função de reação:** Copom responde a **expectativas (Focus)** e **hiato**, condicionado ao risco fiscal e cambial. Em estresse fiscal, o juro precisa subir mais para o mesmo aperto.

## 2. Inflação — IPCA e núcleos
- **IPCA** (IBGE) = índice oficial da meta. **IPCA-15** = prévia. **IGP-M** (FGV) = mais sensível a atacado/câmbio (usado em aluguéis, tarifas).
- **Núcleos** (médias aparadas, EX0-EX3, dupla ponderação) e classificação **livres × administrados**, **serviços × bens × alimentos**: serviços/núcleos medem a inflação **subjacente/inercial** que o BC consegue afetar; administrados e alimentos são mais choque de oferta.
- **Inércia e indexação:** salários, aluguéis e contratos indexados → choques se propagam (memória inflacionária). Por isso ancorar expectativas é vital.
- **Pass-through cambial:** depreciação do real → inflação de bens comercializáveis (elevado em emergente).

## 3. Câmbio (BRL)
- Regime de **câmbio flutuante** com intervenções do BC (swaps cambiais, leilões, linhas) — o swap cambial é a principal ferramenta (hedge sem gastar reserva à vista).
- Drivers: diferencial de juros (carry), risco fiscal/político (prêmio), commodities/termos de troca, dólar global (DXY), fluxo comercial e financeiro.
- **UIP frequentemente "falha"** (carry trade): juro alto não deprecia na velocidade prevista — prêmio de risco e fluxo dominam no curto prazo.

## 4. Fiscal — o risco que condiciona tudo
- **Dívida:** DBGG (Dívida Bruta do Governo Geral) e DLSP (líquida) em % do PIB. Resultado **primário** (antes de juros) vs **nominal** (depois).
- **Dinâmica (r−g):** com juro real alto, estabilizar a dívida exige primário positivo relevante. Acompanhe expectativa de primário e trajetória DBGG/PIB.
- **Arcabouço fiscal** (regra vigente desde 2023, substituiu o teto de gastos): bandas de despesa atreladas à receita, metas de primário. Credibilidade da regra → prêmio de risco.
- **Dominância fiscal (risco):** se o mercado duvida da solvência, subir Selic pode **depreciar** o câmbio e elevar inflação (juro perde tração) e piorar a dívida — o BC fica "preso". Leitura central para o Brasil.

## 5. Atividade e emprego
- **PIB trimestral** (IBGE, ótica da despesa e da oferta); **IBC-Br** (BCB) = proxy mensal de atividade ("PIB do BC").
- **Emprego:** PNAD Contínua (desemprego, força de trabalho, renda) e **CAGED** (emprego formal mensal). Informalidade alta → leitura cuidadosa.
- **Confiança/PMI** (FGV, S&P Global) como antecedentes.

## 6. Curva de juros e expectativas
- **Curva DI (B3)** = expectativa de Selic + prêmios; principal termômetro de mercado da política monetária (ver skills **bond-modeling** e **derivatives-modeling** para o instrumento).
- **Boletim Focus** (BCB, semanal): mediana das expectativas de mercado para IPCA, Selic, PIB, câmbio. **Insumo direto da função de reação** — desancoragem do Focus é gatilho de aperto.
- **Convenção DU/252** (dias úteis) em juros BR — atenção ao comparar com séries internacionais (ACT/360 etc.).

## 7. Calendário e fontes que movem mercado
- IPCA/IPCA-15 (IBGE), Copom (decisão + ata), RPM trimestral, Focus (segundas), PIB (IBGE), dados fiscais (Tesouro/BCB), PNAD/CAGED, balança comercial (MDIC), fluxo cambial (BCB).
- **FOMC/CPI dos EUA e DXY** afetam diretamente câmbio e curva BR (canal externo).

## Armadilhas de leitura BR
- ❌ Ler Selic sem o risco fiscal (transmissão muda sob estresse).
- ❌ Olhar IPCA cheio e ignorar núcleos/serviços (a parte que o BC controla).
- ❌ Esquecer indexação/inércia ao projetar desinflação.
- ❌ Aplicar UIP "limpa" ao real (prêmio de risco domina).
- ❌ Comparar juros BR (DU/252) com global sem ajustar convenção.

## Glossário de siglas
| Sigla | Significado |
|---|---|
| **CMN** | Conselho Monetário Nacional — define a meta de inflação |
| **Copom** | Comitê de Política Monetária do BCB — decide a Selic |
| **RPM** | Relatório de Política Monetária (ex-RTI) — projeções e balanço de riscos, trimestral |
| **Focus** | Boletim de expectativas de mercado (BCB), semanal |
| **IBC-Br** | Índice de Atividade Econômica do BC — proxy mensal do PIB |
| **DBGG / DLSP** | Dívida Bruta do Governo Geral / Dívida Líquida do Setor Público (% PIB) |
| **PNAD-C** | Pesquisa Nacional por Amostra de Domicílios Contínua (IBGE) — desemprego/renda |
| **CAGED** | Cadastro Geral de Empregados e Desempregados — emprego formal mensal |
| **DI / CDI** | Depósito Interfinanceiro / sua taxa — referência de juros de mercado |
| **PTAX** | Taxa de câmbio de referência do BCB |

## Como ler uma ata do Copom (checklist)
A ata (terça após a decisão) move a curva tanto quanto a decisão. Procure:
1. **Balanço de riscos** — simétrico ou **assimétrico** (viés altista = mais propenso a subir). É o sinal mais importante.
2. **Forward guidance** — sinaliza o próximo passo? ("magnitude semelhante", "encerrar o ciclo", "manter por período prolongado").
3. **Avaliação do hiato e do mercado de trabalho** — aquecido/folgado.
4. **Expectativas (Focus)** — ancoradas na meta ou desancorando? gatilho de aperto.
5. **Riscos fiscais e externos** — menção a prêmio de risco, câmbio, juro global (Fed).
6. **Dissidências** — votos divergentes sinalizam inflexão à frente.

## Episódios-caso (para calibrar leitura)
- **2015–16:** recessão profunda + crise fiscal/política → inflação de dois dígitos com atividade caindo (choque de oferta de administrados + câmbio + desancoragem). Selic a 14,25%.
- **2020–21:** Selic a 2% (mínimo histórico) na pandemia → reabertura + choque global de commodities/energia + câmbio → inflação dispara → **ciclo de aperto agressivo** (2021–22) levando a Selic a 13,75%.
- **Choques cambiais recorrentes:** episódios de estresse fiscal em que **juro alto coincide com depreciação** — o "puzzle" do `worked-example.md`, coerente com prêmio de risco/dominância fiscal.

## Fontes
RPM e atas do Copom (BCB) · Boletim Focus · Securato (instrumentos/convenções BR) · FMI Article IV Brasil · notas técnicas do BCB (núcleos de inflação, juro neutro) · Tesouro Nacional (relatórios fiscais).
