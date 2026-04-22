alunos = []

while True:
    print("\n1- Inserir\n2- Listar\n0- Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome: ")
        idade = input("Idade: ")
        curso = input("Curso: ")
        alunos.append({'nome': nome, 'idade': idade, 'curso': curso})
    
    elif opcao == '2':
        for aluno in alunos:
            print(f"nome: {aluno['nome']}")
            print(f"idade: {aluno['idade']}")
            print(f"curso: {aluno['curso']}")
            print("-" * 15)
    
    elif opcao == '0':
        break