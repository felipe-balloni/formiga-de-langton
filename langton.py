"""Formiga de Langton (com suporte a regras de várias cores).

Uso:
    python langton.py                 # regra clássica RL, 11.000 passos
    python langton.py LLRR 20000      # outra regra, outro número de passos
"""
import sys

import matplotlib.pyplot as plt
import numpy as np

N = 200
DX, DY = [0, 1, 0, -1], [-1, 0, 1, 0]  # 0=cima 1=dir 2=baixo 3=esq


def simular(regra: str = "RL", passos: int = 11_000, n: int = N) -> np.ndarray:
    regra = regra.upper()
    if len(regra) < 2 or set(regra) - {"L", "R"}:
        raise ValueError("A regra deve ter 2+ letras, só L e R (ex.: RL, LLRR).")

    grid = np.zeros((n, n), dtype=np.uint8)
    x = y = n // 2
    d = 0
    for _ in range(passos):
        c = grid[y, x]
        d = (d + (1 if regra[c] == "R" else -1)) % 4  # vira conforme a cor
        grid[y, x] = (c + 1) % len(regra)             # avança a cor
        x = (x + DX[d]) % n                            # anda (bordas conectadas)
        y = (y + DY[d]) % n
    return grid


if __name__ == "__main__":
    regra = sys.argv[1] if len(sys.argv) > 1 else "RL"
    passos = int(sys.argv[2]) if len(sys.argv) > 2 else 11_000
    grid = simular(regra, passos)
    plt.imshow(grid, cmap="Oranges" if len(regra) == 2 else "turbo", interpolation="nearest")
    plt.title(f"Formiga de Langton — {regra.upper()}, {passos:,} passos".replace(",", "."))
    plt.axis("off")
    plt.show()
