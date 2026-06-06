_contador_grid = 0

def aplicar_malha(container, linhas, colunas, pesos_linhas=None, pesos_colunas=None):
    global _contador_grid

    if not hasattr(container, "_grid_id"):
        _contador_grid += 1
        container._grid_id = _contador_grid

    grupo_lin = f"lin_{container._grid_id}"
    grupo_col = f"col_{container._grid_id}"

    pesos_l = (pesos_linhas or [])
    pesos_c = (pesos_colunas or [])

    if pesos_linhas is not None and len(pesos_l) != linhas:
        print(f"\n[AVISO] pesos_linhas diferente de linhas ({len(pesos_l)} != {linhas}). Ajustando automaticamente.")

    if pesos_colunas is not None and len(pesos_c) != colunas:
        print(f"\n[AVISO] pesos_colunas diferente de colunas ({len(pesos_c)} != {colunas}). Ajustando automaticamente.")

    pesos_l = (pesos_l + [1] * linhas)[:linhas]
    pesos_c = (pesos_c + [1] * colunas)[:colunas]

    for linha, peso in zip(range(linhas), pesos_l):
        container.rowconfigure(linha, weight=peso, uniform=grupo_lin)

    for coluna, peso in zip(range(colunas), pesos_c):
        container.columnconfigure(coluna, weight=peso, uniform=grupo_col)
