from os import system, name


# Funçao para limpar tela após cada execução
def limpa_tela():

    #windowns
    if name == 'nt': #'nt' é o nome interno do windowns
        _ = system('cls') #comando para limpar tela no windowns 
        #Obs. _= é pq a função system retona algo. Estou jogando esse retorno para o (_)
    #Mac ou linux
    else:
        _= system('clear')  #comando para limpar tela no Mac ou linux



    


def status(num):
    board =  [
    """        _________
        ||======\033[33m|\033[m
        ||      \033[33m|\033[m
        ||      
        ||
        ||
        ||
      __||_________
    """,
    """        _________
        ||======\033[33m|\033[m
        ||      \033[33m|\033[m
        ||      \033[30mO\033[m
        ||
        ||
        ||
      __||_________
    """,
    """        _________
        ||======\033[33m|\033[m
        ||      \033[33m|\033[m
        ||      \033[30mO\033[m
        ||      \033[30m|\033[m 
        ||
        ||
      __||_________
    """,
    """        _________
        ||======\033[33m|\033[m
        ||      \033[33m|\033[m
        ||      \033[30mO\033[m
        ||     \033[30m/|\033[m 
        ||
        ||
      __||_________
    """,
     """        _________
        ||======\033[33m|\033[m
        ||      \033[33m|\033[m
        ||      \033[30mO\033[m
        ||     \033[30m/|\\\033[m 
        ||
        ||
      __||_________
    """,
      """        _________
        ||======\033[33m|\033[m
        ||      \033[33m|\033[m
        ||      \033[30mO\033[m
        ||     \033[30m/|\\\033[m 
        ||     \033[30m/\033[m
        ||
      __||_________
    """,
       """        _________
        ||======\033[33m|\033[m
        ||      \033[33m|\033[m
        ||      \033[30mO\033[m
        ||     \033[30m/|\\\033[m 
        ||     \033[30m/ \\\033[m
        ||
      __||_________
    """,
]
    return (f"{board[num]}")
