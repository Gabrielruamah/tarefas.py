tarefas = []

while True:
    tarefa = input("Digite uma tarefa (ou 'sair'): ")

    if tarefa == "sair":
        break

    tarefas.append(tarefa)

print("Suas tarefas:")
for t in tarefas:
    print("-", t)
