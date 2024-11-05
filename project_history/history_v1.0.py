class SearchHistory:

    def __init__(self):
        """
         Inicializa a pilha.
        """
        self.history = [] 

    def search(self, query):
        """
        Adiciona uma nova pesquisa à pilha de histórico.

        Args:
            query (str) -> A string que representa a pesquisa a ser adicionada ao histórico.

        """
        self.history.append(query) 
        print(f'Pesquisa: {query}')

    def undo(self):
        """
        Remove a ultima pesquisa.
        """
        if not self.history:
            print('Nenhuma pesquisa para desfazer.')
        last_search = self.history.pop() # remove o ultimo item da lista
        print(f'Pesquisa desfeita: {last_search}')

    def show_history(self):
        """
        Retorna o historico de pesquisa.
        """
        if not self.history:
            print('Sem historico de pesquisa')
        print('Historico de pesquisa:')
        for i, query in enumerate(reversed(self.history)):
            print(f'{i + 1}: {query}')

# Exemplo de uso
history = SearchHistory()
history.search("Python pilhas") # Adiciona a primeira pesquisa.
history.search("Estruturas de dados") # Adiciona a segunda pesquisa.
history.show_history() # Amostra o histórico de pesquisas.
history.undo() # Remove a ultima pesquisa.
history.show_history() # Amostra o histórico de pesquisas.
