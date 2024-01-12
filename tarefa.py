# Lista que irá agrupar todas as tarefas.
tarefas = []

# Função que adiciona tarefas a lista.
def adicionar_tarefa(titulo, prazo):

    # Verifica se os campos estão preenchidos adequadamente.
    if (titulo != '' and prazo != ''):

        # Adiciona a nova tarefa a lista.
        tarefa = {'Título': titulo, 'Prazo': prazo, 'Status': 'Pendente'}
        tarefas.append(tarefa)

        # Retorna uma mensagem de sucesso.
        return('Tarefa adicionada com sucesso!!!')
    else:

        # Retorna uma mensagem de erro.
        return('Por favor, preencha todos os campos...')
    
# Função que altera uma tarefa criada na lista.
def alterar_tarefa(indice, novo_titulo, novo_prazo):

    # Verifica se o índice existe.
    if (indice > 0 and indice <= len(tarefas)):

        # Atualiza as informações da tarefa.
        tarefas[indice - 1]['Título'] = novo_titulo
        tarefas[indice - 1]['Prazo'] = novo_prazo

        # Retorna uma mensagem de sucesso.
        return('Tarefa alterada com sucesso!!!')
    else:

        # Retorna uma mensagem de erro.
        return('Não foi possível alterar a tarefa informada...')

# Função que retorna todas as tarefas criadas na lista.
def listar_tarefas():

    # String que retorna as tarefas cadastradas.
    listagem = ''

    # Monta a listagem das tarefas usando laço de repetição.
    for indice, tarefa in enumerate(tarefas, start=1):

        # Monta a string com todas as tarefas da lista.
        listagem += f"{indice} - Título da Tarefa: {tarefa['Título']} - Prazo: {tarefa['Prazo']} - Status: {tarefa['Status']}\n"

    # Retorna a string com a listagem de tarefas.
    return(listagem)

# Função que remove uma tarefa da lista.
def deletar_tarefa(indice):

    # Verifica se o índice existe.
    if (indice > 0 and indice <= len(tarefas)):

        # Remove a tarefa da lista.
        removida = tarefas.pop(indice - 1)

        # Retorna uma mensagem de sucesso para o usuário.
        return(f'Tarefa removida com sucesso: {removida}!!!')
    else:

        # Retorna uma mensagem de erro.
        return('Não foi possível remover a tarefa da lista...')
    
#função que muda o status para concluido de uma tarefa
def concluirTarefa(indice):

    # Verifica se é existente
    if (indice > 0 and indice <= len(tarefas)):

        # Atualiza o status da tarefa.
        tarefas[indice - 1]['Status'] = 'Concluída'

        #retorna mensagem para o usuário
        return('Tarefa concluída com sucesso!!!')
    
    else:

        # Retorna uma mensagem de erro.
        return('Não foi possível concluir a tarefa...')
    
#função que salva as tarefas em um arquivo de texto
def salvarTarefas():

    # Abre para alterar o arquivo
    database = open('Tarefas.txt', 'a')

    # Monta a listagem das tarefas.
    listagem = ''
    for indice, tarefa in enumerate(tarefas, start=1):

        # Monta a string com todas as tarefas da lista.
        listagem += f"Título da Tarefa: {tarefa['Título']} - Prazo: {tarefa['Prazo']} - Status: {tarefa['Status']}\n"
    
    #adiciona a lista de tarefas no arquivo
    database.write(listagem)
    
    #fecha o arquivo
    database.close()

    # Alerta para o usuário que foi atualizado
    return ('Banco de dados atualizado.')