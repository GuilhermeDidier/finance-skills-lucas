# IPO e Capital Markets (ECM / DCM)

> Fontes: Credit Suisse Handbook (IPO application) + Rosenbaum (Part Four: IPOs). Como empresas levantam capital — a função de capital markets.

## ECM — Equity Capital Markets
Emissão de **ações**. Produtos: **IPO** (abertura de capital), **follow-on** (oferta subsequente), **block trade**, **rights issue**, **convertibles**.

### O processo de IPO
1. **Seleção dos underwriters** (bookrunners) e mandato; due diligence.
2. **Drafting do prospecto** (registration statement — S-1 nos EUA / prospecto na CVM); contas auditadas.
3. **Valuation** (comps de trading, DCF) → faixa de preço de oferta. Nota: comps são primários em IPO (DCF confirma).
4. **Roadshow** — gestão apresenta a investidores institucionais.
5. **Bookbuilding** — os bancos coletam ordens (demanda × preço) e montam o "book".
6. **Pricing** — preço final definido na noite anterior à estreia, com base na demanda. Deixa-se um **IPO discount** (ações precificadas um pouco abaixo do fair value para garantir performance no 1º dia).
7. **Alocação e estreia** (trading).

### Mecânica que o banker precisa saber
- **Primary vs secondary:** **primário** = ações **novas** → dinheiro entra na empresa (dilui, financia crescimento/dívida). **Secundário** = venda de ações **existentes** por acionistas atuais → **não** afeta a empresa nem seus financials.
- **Circularidade dos proceeds (P/E):** os proceeds primários reduzem dívida/geram juros → mudam o net income → mudam a valuation por P/E → mudam os proceeds. Resolver com iteração (ver skill financial-modeling).
- **% da empresa vendida** = montante levantado / equity value pós-money.
- **Greenshoe (over-allotment):** opção de vender ~15% a mais se a demanda for forte (estabiliza o preço).
- **Lock-up:** insiders proibidos de vender por ~90–180 dias pós-IPO.
- **Underwriting fee / gross spread:** a comissão dos bancos (% dos proceeds).

### Pro-forma de IPO
Calcule o **net income pro-forma** considerando o uso dos proceeds (pagar dívida → menos juros; ou caixa → mais interest income), com o efeito fiscal. Compare os múltiplos pós-oferta com os comps.

## DCM — Debt Capital Markets (visão geral)
Emissão de **dívida**: **investment-grade bonds**, **high yield bonds**, **leveraged loans**, **commercial paper**. O banco estrutura, precifica (spread sobre o benchmark/SOFR) e distribui a investidores.
- Pricing depende do **rating de crédito**, maturidade, covenants e condições de mercado.
- 🔗 Detalhe de estruturação, precificação e modelagem de dívida → skill **dcm-modeling** / **bond-modeling** (quando criadas). Tranches e leveraged finance em LBO → skill **lbo-modeling**.

## Restructuring (visão geral)
Para empresas em distress: renegociar/trocar dívida (exchange offers), Chapter 11 (EUA) / recuperação judicial (Brasil), debt-for-equity swaps. Sell-side (assessora o devedor) ou buy-side (assessora os credores). Valuation distressed e waterfall de prioridade de credores são centrais.
