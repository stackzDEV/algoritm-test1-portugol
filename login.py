print('o usuario eh "Usuario" e a senha eh "0000" ')
login = 'Usuario'
senha = '0000'

entra_login = input ('Digite seu nome de usuario')
entra_senha = input ('Digite sua senha')

if entra_login == login and entra_senha == senha:
    print ('[sistema conectado com sucesso]')
else :
    print ('[senha ou usuario incorretos tente novamente]')
