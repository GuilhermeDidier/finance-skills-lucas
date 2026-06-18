# Black-Scholes, Binomial e os Greeks

> Fonte: Strategic Issues in Finance (Black & Scholes 1973; binomial = Cox-Ross-Rubinstein 1979) + convenções. Como precificar uma opção e medir suas sensibilidades.

## A fórmula de Black-Scholes (call europeia, sem dividendos)
```
C = S·N(d1) − K·e^(−rT)·N(d2)
P = K·e^(−rT)·N(−d2) − S·N(−d1)

d1 = [ ln(S/K) + (r + σ²/2)·T ] / (σ·√T)
d2 = d1 − σ·√T
```
- **N(·)** = função de distribuição normal padrão acumulada (CDF). **N(d2)** ≈ probabilidade (risk-neutral) de a call terminar ITM.
- **Com dividendos contínuos (q):** troque S por S·e^(−qT) e ajuste d1 com (r − q).
- **Premissas (e limitações):** σ e r constantes, sem custos/impostos, log-normalidade dos retornos, exercício europeu, mercado contínuo. O mundo real viola várias → daí o **vol smile/skew**.

## Modelo Binomial (discreto, mais geral)
- A cada passo o preço sobe (×u) ou desce (×d); valora-se a opção por **indução reversa** (backward induction) com a **probabilidade risk-neutral**:
  ```
  p = (e^(rΔt) − d) / (u − d)
  Valor = e^(−rΔt) · [ p·V_up + (1−p)·V_down ]
  ```
- Black-Scholes é o **caso limite** do binomial quando o nº de passos → ∞. O binomial é melhor para **opções americanas** e com dividendos (testa exercício antecipado a cada nó).

## Volatilidade — o input que não se observa
- **Histórica:** desvio-padrão dos retornos passados (anualizado).
- **Implícita (IV):** a σ que faz a fórmula bater no **preço de mercado** da opção. É a "visão do mercado" sobre a vol futura.
- **Vol smile/skew:** a IV varia por strike (não é constante como BS assume) — puts OTM costumam ter IV maior (medo de crash). É o sinal de que BS é uma aproximação.

## Os Greeks — sensibilidades do prêmio
| Greek | Mede | ∂ de quê |
|---|---|---|
| **Delta (Δ)** | sensibilidade ao **preço do ativo** | ∂V/∂S — para a call, = N(d1) (0→1) |
| **Gamma (Γ)** | variação do delta | ∂²V/∂S² — maior perto do ATM |
| **Vega (ν)** | sensibilidade à **volatilidade** | ∂V/∂σ |
| **Theta (Θ)** | decaimento pelo **tempo** | ∂V/∂t — em geral negativo p/ quem compra |
| **Rho (ρ)** | sensibilidade à **taxa de juro** | ∂V/∂r |

- **Delta-hedging:** neutralizar a exposição ao preço — para um short de 1 call, compre **Δ** ações. Como Δ muda (gamma), rebalanceia-se dinamicamente.
- **Delta-gamma hedge:** neutraliza 1ª e 2ª ordens. Carteiras de opções são geridas por **livro de Greeks**.

## Equity como opção (modelo de Merton)
Black & Scholes notaram: o **equity de uma empresa alavancada é uma call sobre os ativos**, com strike = principal da dívida.
- Acionistas exercem (pagam a dívida) se os ativos valerem mais que a dívida; senão, "abandonam" (limited liability) → default.
- Usado em **risco de crédito** (distance-to-default, KMV/Merton): a dívida é como vender uma put sobre os ativos. Liga com `../dcm-modeling` e `../bond-modeling` (PD).

## Conectar
Conceitos de opção → `options.md`. Aplicação em hedge → `hedging-and-brazil.md`. Real options em projetos → skill **corporate-finance** (`capital-budgeting.md`).
