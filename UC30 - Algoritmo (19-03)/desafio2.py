def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    else:
        if saque > 1000:
            saque = saque * 1.02
        return saldo - saque