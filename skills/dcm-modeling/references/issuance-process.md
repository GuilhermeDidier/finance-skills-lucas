# Mercado Primário — Emissão de Dívida

> Fontes: convenções de DCM + Credit Suisse Handbook. Como uma empresa/governo levanta dívida e como o banco precifica e distribui.

## O papel do DCM
O banco **estrutura, precifica e distribui** a emissão a investidores (não carrega o risco como um fundo). Ganha **underwriting fee / gross spread**. Aconselha sobre: tamanho, prazo (maturity/tenor), estrutura (fixo vs flutuante, secured vs unsecured), e **timing de mercado**.

## O processo (bond/loan)
1. **Mandato e kickoff** — escolha dos bookrunners; due diligence.
2. **Rating** — agências (S&P, Moody's, Fitch) avaliam o crédito → define a faixa de spread. Crítico: IG vs HY muda a base de investidores e o custo.
3. **Documentação** — prospecto/offering memorandum, indenture (covenants, eventos de default), credit agreement (para loans).
4. **Marketing / roadshow** — apresentação a investidores; coleta de interesse (para HY/loans, sindicação).
5. **Bookbuilding e pricing** — coleta de ordens (demanda × spread); define o **spread final** e o cupom.
6. **Allocation, pricing, closing** — alocação aos investidores; liquidação.

## Pricing — como se chega ao cupom/spread
```
Yield da emissão = taxa de referência (curva soberana / SOFR / DI) + new-issue spread
```
- O spread depende de: **rating**, prazo, secured/unsecured, condições de mercado, e a **curva de crédito** dos comparáveis (bonds da mesma empresa/setor/rating já negociados).
- **New-issue concession:** emite-se com um spread um pouco acima do secundário (incentivo ao investidor) — análogo ao IPO discount do ECM.
- **OID (original issue discount):** vender abaixo do par eleva o yield efetivo (comum em leveraged loans).
- Métricas que o investidor olha: **Debt/EBITDA**, **EBITDA/juros (coverage)**, FCF, e a tese de crédito.

## Sindicação (loans)
Para leveraged loans grandes, o banco arranjador **sindica** (distribui partes a outros bancos/institucionais) para pulverizar o risco. **League tables** ranqueiam os bancos por volume.

## Liability management
- **Refinanciamento (refi):** trocar dívida cara/curta por barata/longa.
- **Tender offer / exchange:** recomprar ou trocar bonds existentes.
- **Repricing / amend & extend:** renegociar spread/prazo de loans.
- **Dividend recap:** levantar dívida nova para pagar dividendo ao sponsor (ver skill lbo-modeling).
- **Maturity wall:** concentração de vencimentos → motiva refi antecipado.

## Conectar
Os instrumentos → `debt-instruments.md`. Precificação/risco (yield, duration, spread) → skill **bond-modeling**. Estruturas securitizadas → `securitization-waterfall.md`. Mercado local → `brazilian-dcm.md`.
