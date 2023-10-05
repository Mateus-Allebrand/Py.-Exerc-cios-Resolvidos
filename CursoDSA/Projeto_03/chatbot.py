import openai



openai.api_key = "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"

#Função para gerar texto a partir do modelo de linguagem

def gera_texto(texto):

    response = openai.Completion.create(
        
        #refere a uma versão específica do modelo de linguagem GPT-3
        engine = "text-davinci-003",

        #texto inicial da conversa com bot
        prompt = texto,

        #comprimento da resposta gerada pelo modelo
        max_tokens = 150,

        #quantas conclusões gerar para cada prompt
        n = 5,

        #O texto retornado não conterá seguencia de parada
        stop = None,

        #uma medida de aleatoriedade do texto gerado pelo modelo.
        #seu valor de 0 a 1
        #proximo de 1 mais aleatorio, proximo de 0 saida mais identificavel
        temperature = 0.8,

    )

    return response.choices[0].text.strip()


#Função principal
def main():
    print("=-"*30)
    print("BEM VINDO AO CHATBOT".center(30))
    print("\nDigite '\033[33msair\033[m' quando quiser encerrar o chat ")

    # loop
    while True:
        
        #colega mensagem
        usuario_msg = input("\nVocê: ")

        if usuario_msg.lower() == "sair":
            print("=> Chat Finalizado <= ")
            break

        #colocando msg do usuario em uma variavel
        gpt_prompt = f"\nUsuario: {usuario_msg} \nChatBot:"

        #Gera reposta do modelo pela funcção "gera_texto"

        bot_reposta = gera_texto(gpt_prompt)

        print(f"\nChatBot: {bot_reposta}")


if __name__ == "__main__":
    main()