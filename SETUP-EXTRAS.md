# Setup Extras — Potencializando as Skills

As 10 skills dão o **conhecimento**. Para o Claude também **mexer em planilhas** e **puxar dados reais**, vale adicionar estas ferramentas. Ordenadas por impacto. Tudo opcional — as skills funcionam sem isso.

> ⚠️ **Sobre dados:** nenhuma fonte gratuita substitui FactSet/Capital IQ/Bloomberg (o que o banco usa pro número final). Os itens abaixo são ótimos para **drafts, screening, comps rápidos e estudo** — confira o número final na fonte oficial do banco.

---

## 1. 🥇 Excel — construir e ler modelos

### Opção A (recomendada): deixar o Claude usar Python localmente
O Claude Code consegue ler/escrever `.xlsx` rodando Python com `openpyxl`/`pandas` (lê abas, fórmulas e valores; escreve células de volta). Só garanta as libs instaladas:
```bash
python3 -m pip install --upgrade openpyxl pandas numpy numpy-financial yfinance
```
Depois é só pedir: *"abra o modelo X.xlsx, leia a aba DCF e me diga o WACC implícito"* ou *"monte um 3-statement em Excel a partir destas premissas"*.

### Opção B: MCP dedicado de Excel
Se preferir um servidor com ferramentas prontas de formatação/análise:
```bash
# negokaz/excel-mcp-server (via Smithery)
npx -y @smithery/cli install @negokaz/excel-mcp-server --client claude
```
Alternativa: `sbraind/excel-mcp-server` (34 ferramentas). Veja a doc de cada um.

---

## 2. 🥇 Dados do mercado brasileiro — brapi.dev (o mais útil aqui)

Conecta o Claude à **B3, CVM (demonstrações), FIIs, BDRs, ETFs, SELIC e câmbio** — fontes oficiais (CVM, Bacen, IBGE).

```bash
claude mcp add --transport http brapi https://brapi.dev/api/mcp/mcp
```
- Na **primeira vez**, abre o navegador para login na brapi (gratuito). Alternativa: gerar um token no painel da brapi e usar header `Authorization: Bearer SEU_TOKEN`.
- Exemplos depois de instalado: *"qual o ROE e o EV/EBITDA da WEGE3?"*, *"puxe as demonstrações da PETR4 dos últimos 3 anos"*, *"preço e dividendos de ITUB4"*.
- Casa direto com as skills `valuation-modeling`, `bond-modeling` e `financial-modeling` no contexto BR.

---

## 3. 🥈 Dados globais (empresas fora do Brasil)

Escolha **um**, conforme a necessidade:

- **EODHD** — 77 ferramentas, OAuth (sem API key na maioria dos casos), fundamentos + técnico + macro. Boa relação custo/abrangência. → https://eodhd.com/financial-apis/mcp-server-for-financial-data-by-eodhd
- **Alpha Vantage** (MCP oficial) — cobertura ampla; free tier limitado a **25 requisições/dia**. → https://mcp.alphavantage.co/
- **MarketXLS** — o mais completo (1.100+ funções, opções com Greeks); **pago**.
- **Yahoo Finance** (vários MCPs da comunidade) — grátis, mas **instável** (API quebra, lag/buracos nos dados). Use só para lookups rápidos.

Siga a documentação oficial de cada um para o comando exato de instalação.

---

## 4. 🥉 PDFs e OCR (CIMs, earnings, decks)

Para o Claude ler PDFs (filings, releases, apresentações):
```bash
brew install poppler        # extrair texto/renderizar PDF (macOS)
brew install tesseract      # OCR para PDFs escaneados (opcional)
```
Útil com as skills `financial-modeling` (qualidade dos lucros) e `valuation-modeling` (ler release/relatório).

---

## Recomendação enxuta para o Lucas

1. **Python com openpyxl/pandas** (item 1A) — construir/ler modelos.
2. **brapi.dev** (item 2) — dados do mercado brasileiro via CVM/B3.
3. **EODHD** (item 3) — só se cobrir empresas internacionais.

Esse trio + as 10 skills = **conhecimento + dados + execução**.

---

### Como gerenciar os MCPs no Claude Code
```bash
claude mcp list           # ver o que está instalado
claude mcp remove <nome>  # remover
```
A sintaxe pode mudar entre versões do Claude Code — em caso de dúvida, rode `claude mcp --help` ou veja a documentação oficial.
