usuario = "LuhzinhaMinecraft2008"
senha = "Cre3per!"

u_login = input("insira seu nome de usuário: ")
s_login = input("insera sua senha: ")

if u_login == usuario and s_login == senha:
    print("Login concluído com sucesso!")
elif u_login != usuario and s_login == senha:
    print("Usuário incorreto")
elif u_login == usuario and s_login != senha:
    print("Senha incorreta")
else:
    print("Erro! Impossível concluir o login, confira se realmente tem uma conta")