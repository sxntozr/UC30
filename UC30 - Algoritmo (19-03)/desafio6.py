def lancar_foguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Combustível insuficiente"
    elif clima != "bom":
        return "Clima desfavorável"
    elif sistema_ok == False:
        return "Falha no sistema"
    else:
        return "Lançamento autorizado"