# Frameworks de análise macro

> Cada indicador só faz sentido **contra uma referência** (consenso, meta, potencial, histórico) e dentro de um modelo de como a economia se move. Fontes cruzadas: Blanchard (*Macroeconomics*), Mankiw (*Macroeconomics*), Carlin-Soskice (*Macroeconomics: Institutions, Instability...* — modelo 3-equações), Romer (*Advanced Macro*), relatórios de BC (RPM/Inflation Reports).

## 1. Contas nacionais — o mapa
- **PIB pela despesa:** $Y = C + I + G + (X - M)$. Saiba qual componente puxa.
- **Nominal vs real:** real = nominal deflacionado. Ciclo → use **real**; arrecadação/dívida → **nominal**.
- **Hiato do produto** = (PIB efetivo − potencial)/potencial. Positivo → pressão inflacionária; negativo → ociosidade. Estimado por filtro (HP, mas cuidado com viés de fim de amostra) ou função de produção.
- **Identidade poupança-investimento:** $S - I = X - M$. Déficit em conta corrente = poupança externa. Conecta fiscal, externo e investimento (déficits "gêmeos").

## 2. Demanda × Oferta agregada (AD-AS)
- **Choque de demanda:** produto e inflação na **mesma** direção (ex.: estímulo fiscal → ambos sobem).
- **Choque de oferta:** direções **opostas** (choque de petróleo → inflação sobe, produto cai = **estagflação**).
- Diagnosticar a natureza do choque **define a resposta de política** (BC acomoda choque de oferta ruim ou não?).

## 3. IS-LM / IS-MP e Mundell-Fleming (curto prazo, preços rígidos)
- **IS:** equilíbrio de bens (juro ↑ → investimento ↓ → Y ↓).
- **LM → MP:** na versão moderna (Romer/Carlin-Soskice) o BC fixa a **taxa de juros** por uma regra, não a oferta de moeda → curva **MP** horizontal no juro escolhido.
- **Mundell-Fleming (economia aberta):** IS-LM + mobilidade de capital e câmbio. Resultado central — **trilema/trindade impossível**: não dá para ter ao mesmo tempo (1) câmbio fixo, (2) livre mobilidade de capital e (3) política monetária autônoma. Escolha 2 das 3.
  - Câmbio **flutuante** + capital móvel → política **monetária** é potente, **fiscal** é fraca (crowding-out via câmbio).
  - Câmbio **fixo** + capital móvel → política **fiscal** é potente, **monetária** impotente (juro amarrado ao externo).
  - Brasil hoje: flutuante + capital razoavelmente móvel → monetária autônoma (mas condicionada pelo prêmio de risco).

## 4. Curva de Phillips
$$\pi_t = \pi^e_t + \kappa\,(hiato_t) + \text{choque de oferta}_t$$
- **Expectativas ($\pi^e$) são o termo central** — se desancoram, a inflação sobe sem aquecimento. Por isso o BC obceca com expectativas (Focus).
- **NAIRU / desemprego de equilíbrio:** abaixo dele, inflação acelera.
- **Versão novo-keynesiana (NKPC):** $\pi_t = \beta E_t\pi_{t+1} + \kappa\,(hiato)$ — inflação é *forward-looking* (depende da expectativa futura), o que dá poder ao **forward guidance**. Versão híbrida adiciona inércia ($\pi_{t-1}$), relevante no Brasil (indexação).

## 5. Modelo novo-keynesiano de 3 equações (a síntese moderna)
O arcabouço que os BCs usam mentalmente (Carlin-Soskice / Woodford simplificado):
1. **IS dinâmica:** hiato depende do hiato esperado e do **juro real** vs neutro: $\,hiato_t = E_t hiato_{t+1} - \sigma(i_t - E_t\pi_{t+1} - r^*)$.
2. **Curva de Phillips (NKPC):** $\pi_t = \beta E_t\pi_{t+1} + \kappa\,hiato_t$.
3. **Regra do BC (Taylor):** o BC escolhe $i_t$ para minimizar perda em (inflação−meta) e hiato.
→ Determina conjuntamente juro, hiato e inflação. É a "história" por trás de toda IRF de choque monetário.

## 6. Política monetária — regra de Taylor
$$i_t = r^* + \pi_t + \phi_\pi(\pi_t - \pi^*) + \phi_y\,hiato_t$$
- $r^*$ = juro neutro real; $\pi^*$ = meta. **Princípio de Taylor:** $\phi_\pi>1$ (subir o juro **mais** que a inflação para o juro *real* apertar de fato — senão a inflação foge).
- É a **função de reação** do BC: leia cada decisão como resposta a (inflação−meta) e hiato, condicionada a expectativas.
- **Transmissão:** juro → crédito / câmbio / expectativas / preço de ativos → demanda → inflação, com defasagem de **~6–18 meses** ("lags longos e variáveis" — Friedman). Por isso o BC age sobre a **inflação projetada**, não a corrente.
- **Limite inferior (ZLB/ELB):** com juro perto de zero, BC recorre a **QE**, forward guidance, juro negativo (não é o caso BR, mas é o canal de DM).

## 7. Crescimento de longo prazo — Solow (e além)
- $Y = A\,K^\alpha L^{1-\alpha}$. Capital tem retornos decrescentes → no longo prazo, crescimento per capita vem da **produtividade (PTF/A)**.
- **Convergência condicional**; poupança eleva o **nível** de estado estacionário, não a taxa de crescimento de longo prazo.
- **Decomposição do crescimento** (growth accounting): $\hat Y = \hat A + \alpha\hat K + (1-\alpha)\hat L$ — separa contribuição de capital, trabalho e PTF (o "resíduo de Solow").
- **Endógeno** (Romer, Lucas): P&D, capital humano e externalidades sustentam crescimento. Lente para separar **ciclo** (hiato, política) de **tendência** (produtividade, demografia, reformas).

## 8. Setor externo e câmbio
- **Balanço de pagamentos:** conta corrente + conta financeira ≈ 0. Déficit em CC financiado por entrada de capital.
- **Paridade descoberta de juros (UIP):** $i - i^* \approx E[\Delta s] + \text{prêmio de risco}$. Base para ler câmbio vs juro — mas **falha empiricamente** (forward premium puzzle / carry trade): juro alto não deprecia na velocidade prevista no curto prazo.
- **PPP** (paridade de poder de compra): âncora de **longo prazo** do câmbio real; no curto prazo desvia muito.
- **Pass-through cambial** → inflação (forte em emergentes; ver `brazilian-macro.md`).

## Como ler um indicador (receita)
1. **Veio acima/abaixo do consenso?** (a **surpresa** move mercado, não o nível).
2. **Onde está vs meta / potencial / histórico?**
3. **Choque de oferta ou de demanda?** (define a reação do BC).
4. **O que muda na função de reação** (Taylor/Copom) e na **curva de juros**?
5. **Sinal vs ruído:** dado volátil? olhe **núcleos / médias móveis / dessazonalizado / tendência**.

## Armadilhas
- ❌ Ler nível sem referência (consenso/meta/potencial).
- ❌ Confundir choque de oferta com de demanda → resposta de política errada.
- ❌ Usar Taylor com $\phi_\pi<1$ (inflação indeterminada/explosiva).
- ❌ Tratar hiato/PTF como observáveis precisos (são estimados, revisados, com viés de fim de amostra).
- ❌ Esperar que UIP "limpa" preveja câmbio de curto prazo.

## Fontes
Blanchard, Mankiw (intro/intermediário) · Carlin-Soskice, Romer (modelo 3-equações, NK, Solow) · Woodford (*Interest and Prices*, NK) · Taylor (1993), Clarida-Galí-Gertler (regra/NKPC) · Obstfeld-Rogoff (economia aberta, Mundell-Fleming) · relatórios de BC (RPM, Inflation Reports).
