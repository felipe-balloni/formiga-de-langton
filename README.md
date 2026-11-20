# Formiga de Langton

Simulador interativo e explicação da [formiga de Langton](https://pt.wikipedia.org/wiki/Formiga_de_Langton), um autômato celular com duas regras que, partindo de uma grade vazia, passa cerca de 10 mil passos no caos e depois constrói uma "estrada" periódica para sempre.

## As regras

A cada passo, a formiga olha a cor da célula onde está:

- **apagada** → vira 90° à direita, acende a célula e anda uma casa;
- **acesa** → vira 90° à esquerda, apaga a célula e anda uma casa.

Partindo da grade vazia, a estrada (ciclo de 104 passos que desloca a formiga 2 casas na diagonal) começa por volta do passo 9.975.
Está provado que a trajetória é sempre ilimitada. Que a estrada sempre aparece, não.

## Conteúdo

| Arquivo | O que é |
|---|---|
| `index.html` | Simulador no navegador, sem dependências: rodar/pausar, passo a passo, velocidade, zoom, edição do tabuleiro, regras de várias cores (`LLRR`, `RLR`…) e detecção da estrada. |
| `langton.py` | Versão em Python (NumPy + Matplotlib), também com regras de várias cores. |

## Como rodar

**Navegador:** abra `index.html` direto, ou publique com GitHub Pages (Settings → Pages → Branch `main`, pasta `/ (root)`).

**Python:**

```bash
pip install numpy matplotlib
python langton.py              # regra clássica RL, 11.000 passos
python langton.py LLRR 20000   # outra regra
```

## Referências

- C. G. Langton, *Studying artificial life with cellular automata*, Physica D 22 (1986).
- L. A. Bunimovich e S. E. Troubetzkoy, *Recurrence properties of Lorentz lattice gas cellular automata*, J. Stat. Phys. 67 (1992).
- A. Gajardo, A. Moreira e E. Goles, *Complexity of Langton's ant*, Discrete Applied Mathematics 117 (2002).
