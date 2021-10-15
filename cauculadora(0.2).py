# Começando a cauculadora
# (0.2) adicionando subtração

n1 = int( input("Digite um  número : ") )
n2 = int( input("Digite outro número : "))

operators = input('escolha o operador desejado \nADIÇÃO = [+] \nSUBTRAÇÃO = [-]')

while (operators != "+" and operators != "-" ):

    print ('erro [001] o operador inserido anteriormente era invalido , tente novamente')

    operators = input('escolha o operador desejado \nADIÇÃO = [+] \nSUBTRAÇÃO = [-]')

if (operators == '+'):

    result = (n1 + n2)

    print ('{} + {} é igual a {}' .format(n1, n2 , result))

elif (operators == '-'):

    if (n1 < n2):

        result = (n2 - n1)

    else:


        result = (n1 - n2)

    print ('{} - {} é igual a {} ' .format(n1, n2, result))