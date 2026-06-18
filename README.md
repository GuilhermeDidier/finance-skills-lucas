# finance-skills-lucas

Skills personalizadas do Claude Code para o **Lucas** — fluxos do dia a dia no mercado financeiro.

Cada skill é uma pasta em `skills/` com um `SKILL.md` (instruções + gatilho) e, quando preciso,
uma subpasta `references/` com os documentos de apoio (carregados só quando a skill precisa).

## Instalação

```bash
git clone https://github.com/GuilhermeDidier/finance-skills-lucas.git
cd finance-skills-lucas
./install.sh
```

O `install.sh` cria links simbólicos de cada skill em `~/.claude/skills/`.
Para atualizar depois: `git pull` (os links já apontam para o repo).

Para desinstalar: `./install.sh --uninstall`.

## Skills disponíveis

> Tabela preenchida conforme as skills forem criadas.

| Skill | O que faz | Quando usar |
|-------|-----------|-------------|
| `valuation-modeling` | Valuation completo (DCF, trading/transaction comps, sum-of-the-parts) e triangulação em football field | "quanto vale", DCF, WACC, múltiplos, terminal value, valor por ação |
| `financial-modeling` | Modelo de 3 demonstrações integrado (DRE/Balanço/DFC), schedules, circularidade, cenários e qualidade dos lucros | "modelo financeiro", "3-statement", projeção, working capital, debt schedule, "o balanço não fecha" |
| `mna-modeling` | Merger model, accretion/dilution, purchase accounting (goodwill/write-ups/DTL), sinergias e estrutura de deal | "M&A", merger, accretion, dilution, goodwill, sinergias, mix cash/debt/stock |
| `lbo-modeling` | Leveraged buyout: financiamento por tranches, debt schedule, IRR/MOIC, 3 motores de retorno, preço-máximo (floor) | "LBO", buyout, private equity, sponsor, IRR, MOIC, alavancagem |
| `corporate-finance` | Estrutura de capital (MM), capital allocation, payout (dividendos/buybacks), criação de valor e vantagem competitiva (7 Powers) | estrutura de capital, capital allocation, dividendos, buyback, ROIC, 7 powers, Modigliani-Miller |
| `investment-banking` | Guarda-chuva: divisões/grupos, IPO e capital markets, technicals canônicos, prep de entrevista; roteia para as skills profundas | "investment banking", IPO, ECM/DCM, pitchbook, entrevista, technicals, "o que faz um banqueiro" |

## Como criar uma nova skill

1. Copie `skills/_TEMPLATE/` para `skills/<nome-da-skill>/`.
2. Edite o `SKILL.md` (frontmatter `name`/`description` + procedimento).
3. Jogue os documentos de apoio em `references/`.
4. Rode `./install.sh` de novo (cria o link da nova skill).
5. Adicione a linha na tabela acima.
