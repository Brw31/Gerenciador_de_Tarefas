# Importação das bibliotecas necessárias.
import easygui
import tarefa

# Laço de repetição da interação com o usuário.
while (True):

    # Itens a serem exibidos no menu.
    itens = ['Adicionar Tarefa', 'Alterar Tarefa', 'Listar Tarefas', 'Deletar Tarefa', 'Concluir Tarefa', 'Salvar Tarefas', 'Sair']

    # Solicita a escolha do usuário.
    escolha = easygui.buttonbox('Escolha uma opção:', choices=itens)

    # Verifica qual foi a escolha do usuário e chama a função.
    if (escolha == 'Adicionar Tarefa'):

        # Solicita as informações do usuário.
        titulo = easygui.enterbox('Digite o título da tarefa:')
        prazo = easygui.enterbox('Digite o prazo da tarefa (DD/MM/AA)')

        # Chama a função que adicionar a tarefa a lista.
        resultado = tarefa.adicionar_tarefa(titulo, prazo)
        easygui.msgbox(resultado)

        # Apresenta a tarefa adicionada.
        easygui.codebox('Listagem de Tarefas', 'Gerencimento de Tarefas', tarefa.listar_tarefas())

    elif (escolha == 'Alterar Tarefa'):

        # Solicita as informações do usuário.
        indice = int(easygui.enterbox('Digite o código da tarefa:'))
        novo_titulo = easygui.enterbox('Digite o novo título da tarefa:')
        novo_prazo = easygui.enterbox('Digite o novo prazo da tarefa (DD/MM/AA):')

        # Chama a função que altera a tarefa a lista.
        resultado = tarefa.alterar_tarefa(indice, novo_titulo, novo_prazo)
        easygui.msgbox(resultado)

        # Apresenta a tarefa alterada.
        easygui.codebox('Listagem de Tarefas', 'Gerencimento de Tarefas', tarefa.listar_tarefas())

    elif (escolha == 'Listar Tarefas'):

        # Apresenta todas as tarefas cadastradas.
        easygui.codebox('Listagem de Tarefas', 'Gerencimento de Tarefas', tarefa.listar_tarefas())

    elif (escolha == 'Deletar Tarefa'):

        # Solicita as informações do usuário.
        indice = int(easygui.enterbox('Digite o código da tarefa:'))

        # Chama a função que deleta a tarefa.
        resultado = tarefa.deletar_tarefa(indice)
        easygui.msgbox(resultado)

    elif (escolha == 'Concluir Tarefa'):

        # Solicita as informações para o usuário.
        indice = int(easygui.enterbox('Digite o código da tarefa:'))

        # Chama a função que troca o status da tarefa pra concliuda.
        resultado = tarefa.concluirTarefa(indice)
        easygui.msgbox(resultado)

         # Apresenta a tarefa alterada.
        easygui.codebox('Listagem de Tarefas', 'Gerencimento de Tarefas', tarefa.listar_tarefas())

    elif (escolha == 'Salvar Tarefas'):

        #chama a função que irá salvar as tarefas
        resultado = tarefa.salvarTarefas()
        easygui.msgbox(resultado)

    #Fim do if
    elif (escolha == 'Sair'):
        break