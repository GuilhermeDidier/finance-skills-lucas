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
| _(em construção)_ | | |

## Como criar uma nova skill

1. Copie `skills/_TEMPLATE/` para `skills/<nome-da-skill>/`.
2. Edite o `SKILL.md` (frontmatter `name`/`description` + procedimento).
3. Jogue os documentos de apoio em `references/`.
4. Rode `./install.sh` de novo (cria o link da nova skill).
5. Adicione a linha na tabela acima.
