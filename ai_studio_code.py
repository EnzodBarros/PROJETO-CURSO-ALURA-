# --- Calculadora Simples em Python ---

print("=== CALCULADORA BÁSICA ===")
print("Escolha a operação desejada:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# 1. Escolha da operação
operacao = input("Digite o número da operação (1/2/3/4): ")

# Verifica se a opção digitada é válida antes de pedir os números
if operacao in ['1', '2', '3', '4']:
    # 2. Entrada dos números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # 3. Decisão e execução do cálculo
    if operacao == '1':
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado}")

    elif operacao == '2':
        resultado = num1 - num2
        print(f"\nResultado: {num1} - {num2} = {resultado}")

    elif operacao == '3':
        resultado = num1 * num2
        print(f"\nResultado: {num1} * {num2} = {resultado}")

    elif operacao == '4':
        # Tratamento especial: não é possível dividir por zero
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nResultado: {num1} / {num2} = {resultado}")
        else:
            print("\nErro: Não é possível dividir por zero!")

else:
    print("\nOpção inválida! Escolha um número entre 1 e 4.")