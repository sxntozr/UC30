programa {
    funcao inicio() {
        real valorCasa, salario, prestacao
        inteiro anos, meses

        escreva("Qual o valor da casa: \n")
        leia(valorCasa)
        escreva("Qual seu salário: \n")
        leia(salario)
        escreva("Em quantos anos você deseja pagar: \n")
        leia(anos)

        meses = anos * 12
        prestacao = valorCasa / meses

        escreva("O valor da prestação dividido em ", meses," fica: " ,prestacao, "\n")

        se(prestacao <- salario * 0.30) {
            escreva("Empréstimo aprovado \n")
        } senao {
            escreva("Empréstimo não aprovado \n")
        }
    }
}