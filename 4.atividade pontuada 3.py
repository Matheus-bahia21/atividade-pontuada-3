import os

os.system ("cls||clear")

def autenticar_usuario():
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    print(f"\nAcesso concedido para a matrícula {matricula}.\n")
    return matricula

def calcular_inss(salario):
    if salario <= 1320.00:
        return salario * 0.075
    elif salario <= 2571.29:
        return salario * 0.09
    elif salario <= 3856.94:
        return salario * 0.12
    elif salario <= 7507.49:
        return salario * 0.14
    else:
        return 1051.05

def calcular_irrf(salario, dependentes=1):
    deducao_dependente = dependentes * 189.59
    base_calculo = salario - deducao_dependente


    if base_calculo <= 2112.00:
        irrf = 0
    elif base_calculo <= 2826.65:
        irrf = base_calculo * 0.075 - deducao_dependente
    elif base_calculo <= 3751.05:
        irrf = base_calculo * 0.15 - deducao_dependente
    elif base_calculo <= 4664.68:
        irrf = base_calculo * 0.225 - deducao_dependente
    else:
        irrf = base_calculo * 0.275 - deducao_dependente

    return irrf

autenticar_usuario()

salario_base = float(input("Digite seu salário base (R$): "))
vt_resposta = input("Deseja receber vale transporte? (s/n): ")
vale_transporte = vt_resposta == 's'  
valor_vr = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): "))

dependentes = int(input("Digite o numero de dependentes: "))
inss = calcular_inss(salario_base)
irrf = calcular_irrf(salario_base, dependentes)
vt = salario_base * 0.06 
vr = valor_vr * 0.20
plano_saude = 150.00 * dependentes

total_descontos = inss + irrf + vt + vr + plano_saude
salario_liquido = salario_base - total_descontos


print("\n --- RESUMO DA FOLHA DE PAGAMENTO ---")
print(f"Salário Base:               R$ {salario_base:,.2f}")
print(f"Desconto INSS:              R$ {inss:,.2f}")
print(f"Desconto IRRF:              R$ {irrf:,.2f}")
print(f"Desconto Vale Transporte:   R$ {vt:,.2f}")
print(f"Desconto Vale Refeição:     R$ {vr:,.2f}")
print(f"Desconto Plano de Saúde:    R$ {plano_saude:,.2f}")
print(f"Total de Descontos:         R$ {total_descontos:,.2f}")
print(f" Salário Líquido:          R$ {salario_liquido:,.2f}")