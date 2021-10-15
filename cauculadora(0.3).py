# Começando a cauculadora
# (0.2) adicionando subtração
# (0.3) adicionando multiplicação

n1 = int( input("Digite um  número : ") )
n2 = int( input("Digite outro número : "))

operators = input('escolha o operador desejado \nADIÇÃO = [+]  \nSUBTRAÇÃO = [-]   \nMULTIPLICAÇÃO = [x] \n : ')

while (operators != "+" and operators != "-" and operators != "x" ):

    print ('erro [001] o operador inserido anteriormente era invalido , tente novamente')

    operators = input('escolha o operador desejado \nADIÇÃO = [+] \nSUBTRAÇÃO = [-] \nMULTIPLICAÇÃO = [x]')

if (operators == '+'):

    result = (n1 + n2)

    print ('{} + {} = {}' .format(n1, n2 , result))

elif (operators == '-'):

    if (n1 < n2):

        result = (n2 - n1)

    else:


        result = (n1 - n2)

    print ('{} - {} = {} ' .format(n1, n2, result))
    
elif (operators == 'x'):
    
      result = (n1 * n2)
      
      print('{} x {} = {}' .format(n1 , n2 , result)) 