import pandas as pd

df = pd.read_csv("salarios.csv") # abri com pandas no modo de leitor de csv (para. -> nome arquivo)

print(df) # mandei escrever o conteúdo da variável

df.head() # ativei a possbilidade de filtar pelo cabeçalho
 
print(df["Position Title"].value_counts()) #ele me retorna quantas ocorrencias de cada valor(ex. n° policiais)