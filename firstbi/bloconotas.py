# """
# (1) 1.  Desp op - Variavel = [Desp. Operacionais] - [Desp. Variavel]

#     (4)  1.1  Desp. Operacionais = SUM(F_ARGO_Relatorio_ContasAPagarPorPeriodo[Valor Desp Op.])

#     (5) 1.2  Desp. Variavel = CALCULATE(SUM(F_ARGO_Relatorio_ContasAPagarPorPeriodo[Valor Desp Op.]), F_ARGO_Relatorio_ContasAPagarPorPeriodo[contaFinanceira] in {
#         "1.7.10 /  DESPE /  ENERGIA ELÉTRICA",
#         "1.1 |  /  DESPESAS COM PESSOAL",
#         "1.1.21 /  DESPE /  SALARIOS TOTAL",
#         "1.3 |  /  DESPESAS COM MANUTENÇÃO E CONSERVAÇÃO",
#         "1.7.10 /  DESPE /  ENERGIA ELÉTRICA",
#         "USO E CONSUMO"})


# """

#(2) 2. Desp op Variavel (Hora) = [Folha Hora] + [Variavel hora]

    # (13) 2.1 Folha Hora = [Folha dia] / 24

        # (11) 2.1.1 Folha dia = [Pagamentos Folha Rateio]/30

            # (19) 2.1.1.1 Pagamentos Folha Rateio = CALCULATE(SUM(F_FolhaPagamento[cp_eve_val_p]), F_FolhaPagamento[cp_competencia] = MAX(F_FolhaPagamento[cp_competencia]), FILTER(F_FolhaPagamento,DISTINCTCOUNT(F_FolhaPagamento[cp_nome_car]) > 1), F_FolhaPagamento[cp_nome_car] in { "ATENDENTE",
            #                 "ATENDENTE DE LOJA",
            #                 "ATENDENTE.",
            #                 "AUX LIMPEZA",
            #                 "AUXILIAR DE COZINHA",
            #                 "AUXILIAR DE LIMPEZA",
            #                 "CAIXA",
            #                 "COZINHEIRO (A)",
            #                 "OPERADOR DE CAIXA"})



    #(26) 2.2 Variavel hora = [Variavel Dia]/24

        # (24) 2.2.1 Variavel Dia = [Desp. Variavel] / [Dias despe]

        #     2.2.1.1  [Desp. Variavel] => já tenho calculado (5)

            # 2.2.1.2  (9) Dias despe = DISTINCTCOUNT(F_ARGO_Relatorio_ContasAPagarPorPeriodo[emissao])



#    (3) 3. Desp op Variavel Dia proporcional hora = [Variavel dia proporcional Hora]

       # (25) 3.1 Variavel dia proporcional Hora = [Variavel hora] * [Numero horas]

          #  3.1.1 [Variavel hora] já tenho (26)

            # 3.1.2 Numero horas = DISTINCTCOUNT(F_ARGO_Relatorio_VendasPorDataDeEmissao_Cliente[porHora])



# (7) 7. Despesa por hora = [Despesa por Dia]/ CALCULATE([Numero horas],
#          ALLSELECTED(F_ARGO_Relatorio_VendasPorDataDeEmissao_Cliente[porHora]))


#         7.1 Despesa por Dia = [Desp op - Variavel] / [Dias despe]




# (8) Dias = DISTINCTCOUNT(D_Calendario[Data])


#  (10)  Dias Receita = DISTINCTCOUNT(F_ARGO_Relatorio_VendasPorDataDeEmissao_Cliente[dataEmissao])

# """
# Num Colaboradores = CALCULATE(DISTINCTCOUNT(F_FolhaPagamento[cp_cpf]),
#      F_FolhaPagamento[cp_competencia] = MAX(F_FolhaPagamento[cp_competencia]))

# """


# """Pagamento Funcioanrio = CALCULATE([Desp. Operacionais],
#    F_ARGO_Relatorio_ContasAPagarPorPeriodo[fornecedor] in
#    {"3167 - FOLHA DE PAGAMENTO", "3213 - INSS", "3529 - FGTS"})"""

# """
#     (17) Pagamento Funcionario Hora = [Pagamento Funcioanrio] / 30 / 24

# """

# """
# Receita = SUM(F_ARGO_Relatorio_VendasPorDataDeEmissao_Cliente[valorTotal])
# """


# """Receita por Dia = [Receita] / [Dias Receita]"""

# """Resultado = [Receita por Dia] - [Despesa por Dia] - [Variavel dia proporcional Hora]"""

#"""Valor Comprado Mercadoria = CALCULATE(SUM(F_ARGO_Relatorio_VendasDiaADia[totalCusto]),
   #   F_ARGO_Relatorio_VendasDiaADia[tipo]<>"COMBUSTÍVEIS")"""

#"""Folha dia proporcional Hora = [Folha Hora] * [Numero horas]"""

# """Pagamentos Folha = CALCULATE(SUM(F_FolhaPagamento[cp_eve_val_p]), 
#    F_FolhaPagamento[cp_competencia] = MAX(F_FolhaPagamento[cp_competencia]))"""