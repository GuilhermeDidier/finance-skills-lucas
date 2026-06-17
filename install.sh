#!/usr/bin/env bash
# Instala (linka) as skills deste repo em ~/.claude/skills/
# Uso:
#   ./install.sh              instala/atualiza os links
#   ./install.sh --uninstall  remove os links criados por este repo
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$REPO_DIR/skills"
SKILLS_DEST="$HOME/.claude/skills"

mkdir -p "$SKILLS_DEST"

uninstall=false
[[ "${1:-}" == "--uninstall" ]] && uninstall=true

for dir in "$SKILLS_SRC"/*/; do
  name="$(basename "$dir")"
  [[ "$name" == _* ]] && continue   # ignora _TEMPLATE e afins
  link="$SKILLS_DEST/$name"

  if $uninstall; then
    if [[ -L "$link" ]]; then rm "$link"; echo "removido: $name"; fi
    continue
  fi

  if [[ -e "$link" && ! -L "$link" ]]; then
    echo "PULANDO $name: já existe um diretório real em $link (não é link)"; continue
  fi
  ln -sfn "${dir%/}" "$link"
  echo "linkado: $name -> $link"
done

echo "ok."
