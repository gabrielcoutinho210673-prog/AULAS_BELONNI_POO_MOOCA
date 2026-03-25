senha_correta = "Senhacorreta"
usuario_correto = "teste"
max_tentativas = 3
tentativas = 0

while tentativas < max_tentativas:
    usuario = input("Digite o usuario:\n")
    senha = input("Digite a senha:\n")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login feito com sucesso!")

    elif tentativas == max_tentativas:
        print("Conta suspensa")

    else:
        tentativas += 1
        print("Usuário ou senha incorretos!")

        