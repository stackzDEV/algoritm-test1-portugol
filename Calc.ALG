Algoritmo "CALCULADORA  2000"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 08/09/2021
Var
// Se��o de Declara��es das vari�veis 
  a,b   : caractere
  num,num2 : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
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