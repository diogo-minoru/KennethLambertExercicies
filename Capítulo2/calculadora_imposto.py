"""
    Exercício 1:

    Calculadora para calcular o imposto a pagar
    Neste programa o usuário deve informar a receita bruta anual a qual servirá como base para o cálculo do imposto
    Além da receita bruta anual, também deverá ser informado o número de dependentes
    Por padrão, é realizado um desconto de 10.000 sobre a receita bruta anual antes de realizar o cálculo do imposto
    Para cada dependente, também é descontado um valor de 3.000 sobre a receita bruta anual
    Após os descontos, o imposto de 20% é aplicado sobre o valor

"""

receita_bruta = float(input("Digite a receita bruta anual: "))
dependentes = int(input("Informe o número de dependentes: "))
imposto_a_pagar = 0.2*(receita_bruta - 10000 - (3000 * dependentes))

print(f"Você deve pagar ${'{:.2f}'.format(imposto_a_pagar)}")