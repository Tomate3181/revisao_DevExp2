alunos = []
rodando = True

while rodando:
    print("\nMenu:")
    print("1. Cadastrar aluno")
    print("2. Buscar alunos")
    print("3. Listar todos os alunos")
    print("4. Sair")

    opcao = input("escolha uma das opções: ").strip()
    
    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        idade = input("Digite a idade do aluno: ")
        curso = input("Digite o curso do aluno: ")
        alunos.append({"nome": nome, "idade": idade, "curso": curso})
        print("aluno cadastrado com sucesso")
    elif opcao == "2":
        busca = input("Digite o nome do aluno que deseja buscar: ")
        encontrado = False
        for aluno in alunos:
            if aluno["nome"] == busca:
                print("Aluno encontrado:")
                print("Nome:", aluno["nome"])
                print("Idade:", aluno["idade"])
                print("Curso:", aluno["curso"])
                encontrado = True
                break
        if not encontrado:
            print("Aluno não encontrado.")
            
    elif opcao == "3":
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("Lista de todos os alunos:")
            for aluno in alunos:
                print("Nome:", aluno["nome"], "| Idade:", aluno["idade"], "| Curso:", aluno["curso"])
    elif opcao == "4":
        print("Saindo do programa...")
        rodando = False
    else:
        print("Opção inválida. Tente novamente.")
        