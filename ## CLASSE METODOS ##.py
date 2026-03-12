senha_correta = "1234"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas += 1
        print("Senha incorreta.")

        if tentativas < max_tentativas:
            print("Tente novamente.")

if tentativas == max_tentativas:
    print("Conta bloqueada. Muitas tentativas.")