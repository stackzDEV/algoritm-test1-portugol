# Começando a cauculadora
# o objetivo é colocar o maximo de calculos possivel
# (0.2) adicionando subtração
# (0.3) adicionando multiplicação
# (0.4) adicionando divisão e comentando
# (0.5) adicionando raiz quadrada
# (0.6) adicionando porcentagem
# (0.7) corrigindo erros da raiz quadrada
# (0.8) adicionando adição e subtração de porcentagem
# (0.9) adicionando o conversor de moedas

# //variaveis
n1 = int( input("Digite um  número : ") )
n2 = int( input("Digite outro número (caso queira porcentagem digite aqui): "))

# perguntando ao usuário o operador desejado
operators = input('escolha o operador desejado \nADIÇÃO = [+]  \nSUBTRAÇÃO = [-]   \nMULTIPLICAÇÃO = [x] \nDIVISÃO = [/] \nRAIZ QUADRADA = [v] \nPORCENTAGEM = [%] \nADIÇÃO DE PORCENTAGEM = [%+] \nSUBTRAÇÃO DE PORCENTAGEM = [%-] \nCONVERSOR DE DÓLAR = [$] \nCONVERSOR DE EURO = [£] : ')

# operadores validos atualmente
while (operators != "+" and operators != "-" and operators != "x" and operators != "/" and operators != "v" and operators != "%" and operators != "%+" and operators != "%-" and operators != "$" and operators != "£"):

    # tratando com erro de operador invalido , caso ele não selecione um dos operadores a cima ^  
    print ('erro [001] o operador inserido anteriormente era invalido , tente novamente')
    
    # perguntando ao usuário qual o operador desejado novamente
    operators = input('escolha o operador desejado \nADIÇÃO = [+] \nSUBTRAÇÃO = [-] \nMULTIPLICAÇÃO = [x]  \nDIVISÃO = [/] \nRAIZ QUADRADA = [v] \nPORCENTAGEM = [%] \nADIÇÃO DE PORCENTAGEM = [%+] \nSUBTRAÇÃO DE PORCENTAGEM = [%-] \nCONVERSOR DE DÓLAR = [$] \nCONVERSOR DE EURO = [£] : ')

#------------------------------------------------------------------------------
# caso o usuário queira usar o operador [+]
if (operators == '+'):

    result = (n1 + n2)

    # mostrando o resultado
    print ('{} + {} = {}' .format(n1, n2 , result))

#------------------------------------------------------------------------------
# caso o usuário queira usar o operador [+]
elif (operators == '-'):

    if (n1 < n2):

     result = (n2 - n1)

    else:

      result = (n1 - n2)
     
      # mostrando o resultado
      print ('{} - {} = {} ' .format(n1, n2, result))

#------------------------------------------------------------------------------
 # caso o usuário queira usar o operador [x]   
elif (operators == 'x'):
    
      result = (n1 * n2)
      
      # mostrando o resultado
      print('{} x {} = {}' .format(n1 , n2 , result)) 

#------------------------------------------------------------------------------
# caso o usuário queira usar o operador [/]
elif (operators == "/"):

       result = (n1 / n2)
      
       # mostrando o resultado
       print('{} / {} = {}' .format(n1, n2, result )) 

#------------------------------------------------------------------------------
# caso o usuário queira usar o operador [v]
elif (operators == "v"):

    import math

    result = math.sqrt(n1)
 
       #mostrando o resultado
    print('a raiz de {} é {}' .format (n1, result)) 
 
#------------------------------------------------------------------------------
# caso o usuário queira usar o operador [%]      
elif (operators == "%") :
     
    result = ((n1 * n2) /100)   
    
    # mostrando o resultado
    print('{} de {} = {} ' .format(n2, n1, result))

#------------------------------------------------------------------------------
# caso o usuário queira usar o operador [%+]
elif (operators == "%+") :
    
    result = n1 + (n1 * n2/100)
    
    print('o seu valor era de {} e passou a ser {} com um aumento de {}% ' .format(n1, result, n2))

#------------------------------------------------------------------------------
# caso o usuário queira usar o operador [%-]
elif (operators == "%-") :
    
    result =  ((n1 * n2) /100) - n1
  
    print('o seu valor era de {} e passou a ser {} com um desconto de {} ' .format(n1, result , n2))

#------------------------------------------------------------------------------
# caso o usuário queira usar o operador [$]                                          
elif (operators == "$"):

   result = (n1 * 5,46) 
   
   print('o seu valor é {} que em real passou a ser {}'.format(n1, result))
   
#------------------------------------------------------------------------------
# caso o usuário queira usar o operador [£]
elif (operators == "£") :
    
    result = (n1 * 6,33)
    
    print ('o seu valor é {} que em real passou a ser {}'.format(n1, result)) 