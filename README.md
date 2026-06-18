# finance-skills-lucas

**Skills de Claude Code para Investment Banking & Mercado Financeiro — feitas sob medida para o Lucas.**

Um conjunto de **10 skills** que dão ao Claude Code conhecimento profundo, em nível de banco, para te ajudar no dia a dia: valuation, modelagem, M&A, LBO, corporate finance, renda fixa, derivativos e pitchbooks. Cada skill foi destilada de fontes de referência do mercado (Rosenbaum, McKinsey, Damodaran, Mauboussin, JP Morgan, Credit Suisse, Securato, entre outras) e adaptada ao **contexto brasileiro** onde faz sentido (DU/252, CDI/Selic, NTN-B, debêntures, cupom cambial).

---

## 🚀 Instalação

```bash
git clone https://github.com/GuilhermeDidier/finance-skills-lucas.git
cd finance-skills-lucas
./install.sh
```

O `install.sh` cria links das skills em `~/.claude/skills/`. Pronto — abra o Claude Code e elas já estão ativas.

- **Atualizar:** `git pull` (os links já apontam para o repo, atualiza sozinho).
- **Desinstalar:** `./install.sh --uninstall`.

---

## 💡 Como usar

As skills **disparam sozinhas** quando você fala do assunto. Não precisa decorar comando — é só pedir naturalmente:

> *"Faça um DCF da TechBR com EBITDA de 700M..."* → dispara `valuation-modeling`
> *"Esse deal é accretive ou dilutive se eu pagar 25% de prêmio?"* → dispara `mna-modeling`
> *"Qual o IRR de um buyout a 8x com 5x de dívida?"* → dispara `lbo-modeling`
> *"Precifica uma NTN-B e me dá a duration"* → dispara `bond-modeling`
> *"Monta o football field desse pitch"* → dispara `powerpoint-for-ib`

Cada skill tem um `SKILL.md` (o cérebro: quando agir + o passo a passo) e arquivos em `references/` (o conhecimento denso: fórmulas, exemplos resolvidos). O Claude carrega as referências só quando precisa.

---

## 📚 As 10 skills

### 🎯 Avaliação & Modelagem
| Skill | O que faz | Fontes |
|-------|-----------|--------|
| **valuation-modeling** | Valuation completo: DCF, trading/transaction comps, football field, value drivers (ROIC×crescimento), moat, country risk premium, valuation de crescimento/EM | Merrill Lynch, Rosenbaum, McKinsey, Damodaran, Mauboussin, Credit Suisse |
| **financial-modeling** | Modelo de 3 demonstrações integrado, schedules (PP&E/WC/dívida), circularidade, cenários, qualidade dos lucros, análise de ratios/fingerprint de setor | Rosenbaum, Credit Suisse, Financial Shenanigans, HBS |
| **corporate-finance** | Estrutura de capital (Modigliani-Miller), capital allocation, payout, capital budgeting (NPV/IRR/real options), criação de valor e vantagem competitiva (7 Powers) | McKinsey, Strategic Issues, 7 Powers, Competition Demystified, Innovator's Dilemma |

### 🤝 Transações
| Skill | O que faz | Fontes |
|-------|-----------|--------|
| **mna-modeling** | Merger model, accretion/dilution, purchase accounting (goodwill/write-ups/DTL), sinergias, contribution analysis, exchange ratios, takeover defenses | JP Morgan M&A, Merger Models Guide, Sherman, Rosenbaum |
| **lbo-modeling** | Leveraged buyout: estrutura de financiamento, debt schedule, IRR/MOIC, os 3 motores de retorno, preço-máximo (floor de valuation) | Rosenbaum (cap. 4–5) |

### 💰 Renda Fixa & Derivativos
| Skill | O que faz | Fontes |
|-------|-----------|--------|
| **bond-modeling** | Precificação, YTM, duration/DV01/convexidade, curva de juros, crédito — com instrumentos BR (LTN/LFT/NTN-B/NTN-F, CDI/Selic, DI futuro, marcação a mercado, taxa over) | Securato |
| **dcm-modeling** | Mercado de dívida: instrumentos e covenants, emissão (rating/pricing/sindicação), securitização (asset modeling, tranches, waterfall, credit enhancement), DCM BR (debênture/CRI/CRA/FIDC) | Allman |
| **derivatives-modeling** | Forwards/futuros (cost of carry, DI/dólar/cupom cambial), opções (Black-Scholes, Greeks, put-call parity), swaps (IRS/CDS), hedge — foco B3 | Strategic Issues (Black-Scholes), Securato |

### 🏦 Guarda-chuva & Comunicação
| Skill | O que faz | Fontes |
|-------|-----------|--------|
| **investment-banking** | Visão geral (divisões/grupos), IPO e capital markets, technicals canônicos (3-statement, EV vs equity), valuation por setor (FIG/REIT/oil&gas), mental math, prep de entrevista — e **roteia** para as skills profundas | 400 Questions, M&I 400, Credit Suisse |
| **powerpoint-for-ib** | Pitchbooks no padrão de banco: estrutura, action titles, formatação (banker blue), exhibits (football field/sources & uses/etc.), think-cell e quality check | Craft de IB |

---

## 🔗 As skills conversam entre si

Elas foram desenhadas como um sistema, não peças soltas — e apontam umas para as outras:

- **valuation** usa o 3-statement de **financial-modeling** e o floor de **lbo-modeling**; compartilha value drivers e moat com **corporate-finance**.
- **mna** se apoia em valuation (preço), financial-modeling (3-statement) e lbo (comprador financeiro).
- **bond ↔ dcm ↔ derivatives** se cruzam (analytics ↔ estrutura ↔ hedge); todas com contexto brasileiro.
- **investment-banking** é a porta de entrada: para perguntas amplas, ela explica e encaminha para a skill certa.
- **powerpoint-for-ib** comunica visualmente os números que as outras produzem.

---

## 🗂️ Estrutura do repositório

```
finance-skills-lucas/
├── README.md            ← este guia
├── install.sh           ← instala/atualiza/remove as skills
├── skills/
│   ├── valuation-modeling/
│   │   ├── SKILL.md          ← quando agir + workflow
│   │   └── references/       ← fórmulas, exemplos resolvidos
│   ├── financial-modeling/
│   └── ... (10 skills)
└── _TEMPLATE/           ← modelo para criar novas skills
```

Cada skill traz pelo menos um **worked-example** com a aritmética fechando (DCF, accretion/dilution, IRR de LBO, preço+duration de um título, Black-Scholes, waterfall) — para você ver a metodologia aplicada de ponta a ponta.

---

## ➕ Criar uma nova skill

1. Copie `skills/_TEMPLATE/` para `skills/<nome-da-skill>/`.
2. Edite o `SKILL.md` (frontmatter `name`/`description` com gatilhos claros + o procedimento).
3. Coloque o material de apoio em `references/`.
4. Rode `./install.sh` de novo.
5. Adicione a linha na tabela acima.

---

*Feito com cuidado para o Lucas. Bom uso! 🚀*
