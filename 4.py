import os
os.system("clear || cls ")

def calcular_inss(salario):
    if salario <= 1320.00:
        inss = salario * 0.075
    elif salario <= 2571.29:
        inss = salario * 0.09
    elif salario <= 3856.94:
        inss = salario * 0.12
    elif salario <= 7507.49:
        inss = salario * 0.14
    else:
        inss = 1051.05  # Teto do INSS
    return min(inss, 1051.05)

def calcular_irrf(salario, dependentes):
    deducao_dependente = 189.59 * dependentes
    base_irrf = salario - deducao_dependente
    if base_irrf <= 2112.00:
        irrf = 0
    elif base_irrf <= 2826.65:
        irrf = base_irrf * 0.075
    elif base_irrf <= 3544.00:
        irrf = base_irrf * 0.15
    elif base_irrf <= 4256.00:
        irrf = base_irrf * 0.225
    else:
        irrf = base_irrf * 0.275
    return irrf

def main():
    print("Sistema de Folha de Pagamento\n")
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")

    # Dados do funcionário
    salario_base = float(input("Informe seu salário base (R$): "))
    vale_transporte_opcao = input("Deseja receber vale transporte? (s/n): ").strip().lower()
    valor_vale_refeicao = float(input("Informe o valor do vale refeição fornecido pela empresa (R$): "))

    # Considerando 1 dependente
    dependentes = 1

    # Cálculos
    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, dependentes)
    vale_transporte = salario_base * 0.06 if vale_transporte_opcao == 's' else 0
    vale_refeicao = valor_vale_refeicao * 0.20
    plano_saude = 150.00 * dependentes

    descontos_totais = inss + irrf + vale_transporte + vale_refeicao + plano_saude
    salario_liquido = salario_base - descontos_totais

    # Exibição dos resultados
    print("\n--- Demonstrativo de Pagamento ---")
    print(f"Matrícula: {matricula}")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {vale_transporte:.2f}")
    print(f"Desconto Vale Refeição: R$ {vale_refeicao:.2f}")
    print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
    print(f"Total de Descontos: R$ {descontos_totais:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()
