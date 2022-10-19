# questão 3

# definindo a função
def totalSalario(valorHora, horasTrabalhadas):
    bruto = valorHora*horasTrabalhadas
    ir = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05
    liquido = bruto - ir - inss - sindicato

    return f"\n+ Salário bruto: R$ {bruto}\n- IR: R$ {ir}\n- INSS: R$ {inss}\n- Sindicato: R$ {sindicato}\n= Salário Líquido: R$ {liquido}"

# recebendo inputs
valorHora = float(input("Digite o valor da hora de trabalho: "))
horasTrabalhadas = float(input("Digite a qtde de horas trabalhadas: "))

# chamando a função
print("\nFolha de pagamento: ", (totalSalario(valorHora, horasTrabalhadas)))