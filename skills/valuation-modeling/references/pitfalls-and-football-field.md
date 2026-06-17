# Pitfalls de Comps + Football Field (checklist de praticante)

> Fonte: Credit Suisse IB Analyst Handbook (Compco Analysis, checklist de pitfalls; Valuation Matrix). A régua de qualidade que um analista roda antes de entregar.

## Pitfalls mais comuns numa análise de comps (corrija ANTES de entregar)
- **Não incluir todas as classes de ação** (inclusive não-listadas) na market cap.
- **Não normalizar não-recorrentes** (reestruturação, tax holidays) — comps são para going concern; use financials "normalizados".
- **Não anualizar** quando pro-forma para M&A — aquisição feita no meio do ano não consolida 12 meses; anualize p/ múltiplo like-for-like.
- **Não usar market values** para minorities e investments/associates (use FactSet ou sum-of-the-parts de brokers).
- **Não ajustar treasury shares** — não entram na market cap.
- **Share buyback / stock split / mudança de ADR ratio** — ajuste o nº de ações; cheque o ADR ratio.
- **Special dividends** — ajuste no período antes do pagamento.
- **Não revisar os múltiplos na output page** — se um múltiplo está fora da linha, recalcule.
- **Não checar se todas as linhas/colunas entram na média/mediana** — empresas adicionadas depois ficam de fora sem querer.
- **Células "hardcoded"** — perigosas; prefira fórmula que mostre **NM** (not meaningful) para múltiplos negativos/altíssimos. Cheque hardcodes a cada update.
- **Não footnotar premissas / sem audit trail** — toda premissa sourced; checagem independente é parte da finalização.

## "Red lights" — erros básicos que gritam (checagem rápida)
- Preço atual **fora** da faixa 52-week high/low.
- Múltiplos **EV/EBITDA ou P/E não decrescentes** indo para frente (forward deveria ser menor se há crescimento).
- **Margens não melhorando** de forma estável quando deveriam.
- **Enterprise value < equity value** (só faz sentido com caixa líquido > dívida; senão é erro).
- Múltiplos calculados **muito diferentes dos brokers** → assuma que alguém está errado e investigue (alguns brokers usam net debt forward). Diferença = bandeira vermelha → cuidado extra.

## Football Field (Valuation Matrix) — como montar e o erro #1
> "Acertar a **faixa de valor** é provavelmente o pitfall mais comum." Comece sempre pelo football field (floating bars) cruzando todas as metodologias.

**Exemplo real (CS Handbook, € por ação)** — faixas por metodologia e os múltiplos implícitos que cada uma gera:
| Metodologia | Equity value | EV/EBITDA 08E | P/E 08E |
|---|---|---|---|
| Trading range | 1.120–1.320m | 5,5–6,3x | 9,3–11,0x |
| DCF | 1.200–1.360m | 5,8–6,5x | 10,0–11,3x |
| Comparable companies | 1.040–1.300m | 5,2–6,3x | 8,7–10,8x |
| Comparable acquisitions | 1.200–1.400m | 5,8–6,7x | 10,0–11,7x |
| LBO analysis | 1.140–1.320m | 5,6–6,3x | 9,5–11,0x |
| **Selected range** | **1.200–1.300m** | **5,8–6,3x** | **10,0–10,8x** |
| Analyst price targets | 1.200–1.360m | 5,8–6,5x | 10,0–11,3x |

**Leitura:** a *selected range* é mais estreita que a união das metodologias — você usa julgamento pra convergir, não pega o min e o max de tudo. Sempre mostre os **múltiplos implícitos** de cada faixa (cross-check de razoabilidade) e inclua a faixa de LBO (floor) e price targets de analistas como sanity externa.

> 🔗 Conecta com `comparables.md` (cálculo dos múltiplos), `mechanics.md` (treasury shares, minorities, fully diluted) e o Passo 5 do workflow (montar o football field).
