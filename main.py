import time
from dados import carregar_tarefas, salvar_tarefas

#fazer a interface do terminal
print('-_-_-_-_-_-_-_- Task.Ly -_-_-_-_-_-_-_-')


tarefas = carregar_tarefas() #ligação com o dados.py

#funcoes para cada opção
def op1(tarefas):
    #se a lista de tarefas estiver vazia
    if not tarefas:
        print('Sem tarefas\n')
    else:
        for tarefa in tarefas:
            print(tarefa)

def op2(tarefas):
    #variaveis para a data e a tarefa
    dt = str(input('Digite a data (DD/MM/AAAA): '))
    trf = str(input('Digite a tarefa: '))

    #adiciona a data e a tarefa na lista
    tarefas.append({
        "data": dt,
        "tarefa": trf,
        "concluida": False
    })

    salvar_tarefas(tarefas)
    print("Tarefa adicionada com SUCESSO\u2705 \n")

def escolher_tarefa(tarefas):
    for i, tarefa in enumerate(tarefas):
        print(f'{i + 1} - {tarefa}')
    escolha = int(input("Escolha o numero correspondente à tarefa: ")) - 1
    return escolha

#funcao do menu

def menu():
    while True:
        print('1 - Ver minhas tarefas')
        print('2 - Adicionar tarefa')
        print('3 - Marcar como concluida')
        print('4 - Deletar tarefa')
        print('5 - Encerrar programa\n')

        user_choice = int(input('Selecione o número da opção: '))

        if user_choice == 1:
            op1(tarefas)
        if user_choice == 2:
            op2(tarefas)
        if user_choice == 3:
            if not tarefas:
                print('Você não tem tarefas na agenda\n')
            else:
                indice = escolher_tarefa(tarefas)
                tarefas[indice]['concluída'] = True
                salvar_tarefas(tarefas)

        if user_choice == 4:
            if not tarefas:
                print('Você não tem tarefas na agenda\n')
            else:
                indice = escolher_tarefa(tarefas)
                tarefas.pop(indice)
                salvar_tarefas(tarefas)
                print('removido\n')
        if user_choice == 5:
            palavra = "Programa Encerrado com sucesso, tchau"
            for letra in palavra:
                print(letra, end="", flush=True)
                time.sleep(0.1)
            break

menu()

