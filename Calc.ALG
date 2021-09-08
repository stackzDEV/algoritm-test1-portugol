Algoritmo "CALCULADORA  2000"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 08/09/2021
Var
// Seção de Declarações das variáveis 
  a,b   : caractere
  num,num2 : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreva ("0:")
   leia (num)
   escreva ("0:")
   leia(num2)
   escreval ("[operador =]")
   escreval ("[+]")
   escreval ("[-]")
   escreval ("[*]")
   escreval ("[/]")
   leia(a)
   escolha a
     caso "+"
      escreval("=",num+num2)
     caso "-"
      escreval("=",num-num2)
     caso "*"
      escreval("=",num*num2)
     caso "/"
      escreval("=",num/num2)
     outrocaso
      escreval("erro:001 , apenas operadores comuns permitidos")

   fimescolha

Fimalgoritmo