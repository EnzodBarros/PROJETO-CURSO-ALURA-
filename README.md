Imersão Engenharia de Software: Dev na Era da IA

1. Eu identifico
Variáveis funcionam como "etiquetas" que guardam informações na memória do computador. Neste código, utilizamos 4 variáveis:
Variável	Tipo de dados	O que ela armazena?
operacao	Texto (corda/str)	O caractere correspondente à opção escolhida pelo usuário ('1','2','3' ou '4').
num1	Número decimal (flutuador)	O primeiro número inserido para o cálculo (convertido para ponto flutuante).
num2	Númeroflutuador)	O
resultado	Número decimal (flutuador)	O resultado da operação matemática entre num1enum2.
Dica: Note que a variável operacao armazena texto ('1'), e não número puro (1). É por isso que ela é comparada com aspas simples no código.
2. Como a Aplicação Decide Qual Operação Executar?
A decisão é feita por meio de estruturas de controle de fluxocondicse,Elif,outro):
Primeiro filtro (Validação de entrada):
code
Python
if operacao in ['1', '2', '3', '4']:
Antes de pedir os números, o programa checa: "O que foi digitado está dentro dessa lista de opções válidas?"
Comnão estiver(ex: o nós'9'ou'olá'), ou Python diriaoutrono final e avisa que a opção é invál
Comestiver,
A cascata de decisão:
O Python lê as condições de cima para baixo:
if operacao == '1':Procurar'1', faz uma soma e ignora o restante.
elif operacao == '2': Se não foi a 1ª, mas for '2', faz a subtração e ignora o resto.
elif operacao == '3':S'3', faz a multiplicação.
elif operacao == '4':Procure por "4".'4', vai para o bloco da divisão.
Assim que o Python encontra uma condição verdadeira, ele executa o bloco correspondente e pula todas as outras verificações seguintes.
3. Explicando uma Parte Específica: O Bloco da Divisão
Repare neste trecho dentro da operação 4:
code
Py
elif operacao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nResultado: {num1} / {num2} = {resultado}")
    else:
        print("\nErro: Não é possível dividir por zero!")
Por que isso é necessário? Na matemática e na computação, não existe divisão por zero. Se tentássemos fazer num1 / 0, o Python travaria a execução do programa e exibiria um erro clássico chamado Erro de divisão zero.
Como resolvemos?Nós usamosse dentro de outro se(chamada *condição)condicional aninhada).
O operador !=significa **"diferente"diferente de".
O código"O segundo número é diferente de zero?"
Se for diferente de zero, calcula com segurança. Se for exatamente zero, exibe uma mensagem amigável sem derrubar o programa.
