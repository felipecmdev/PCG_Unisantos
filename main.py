from plot_fumantes import plot_fumantes
from plot_depressivos import plot_depressivos
from plot_fd import plot_fd

# dados para o gráfico de fumantes
dadosf = {
    'X': ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'],
    'Y1': [22.7, 15.7, 19.3, 20.4, 20.3, 20.8, 13.6, 17.5, 17.5, 21.9, 16.4, 23.5, 23.8, 18.8, 15.3, 21.6, 19.0, 24.0, 15.3, 18.0, 16.4, 17.3, 20.2, 19.8, 18.6, 16.9, 18.9],
    'Y2': [16.1, 10.8, 7.9, 6.7, 7.6, 13.7, 8.9, 9.2, 10.8, 10.1, 9.3, 14.1, 13.1, 7.4, 10.4, 14.9, 12.0, 12.5, 10.6, 9.6, 12.3, 7.1, 8.9, 12.5, 11.5, 7.5, 10.6]
}

# dados para o gráfico de depressivos
dadosd = {
    'X': ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'],
    'Y1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.7, 6.6, 0, 0, 4.9, 3.8, 0, 0,3.5, 6.7, 0, 0, 7.0, 4.7, 0, 0],
    'Y2': [7.2, 8.4, 4.8, 3.3, 6.4, 6.7, 9.3, 7.8, 11.3, 5.9, 10.8, 13.5, 15.1, 2.5, 6.6, 17.8, 10.1, 5.8, 8.3, 9.8, 18.9, 8.3, 6.2, 18.4, 11.7, 8.0, 10.3],
}

# dados para o gráfico de fumantes e depressivos
dadosfd = {
    'X': ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'],
    'Y1': [12.1, 19.3, 13.4, 14.5, 13.0, 13.3, 14.6, 15.8, 18.0, 17.1, 13.5, 12.7, 15.2, 13.1, 12.0, 13.5, 18.1, 13.1, 12.7, 14.9, 18.1, 16.0, 14.2, 18.6, 12.8, 14.0, 11.0],
    'Y2': [7.2, 8.4, 4.8, 3.3, 6.4, 6.7, 9.3, 7.8, 11.3, 5.9, 10.8, 13.5, 15.1, 2.5, 6.6, 17.8, 10.1, 5.8, 8.3, 9.8, 18.9, 8.3, 6.2, 18.4, 11.7, 8.0, 10.3],
}

# print e for usados para a criação do cabeçalho
print("")
print("------------------------------------------------------")
print("Trabalho de Felipe, Carvalho Kauan Alves e Lucas Herzog")
print("------------------------------------------------------")
print("A relação entre o tabagismo e a depressão")

for i in range (6):
    print("|")

print("MENU")
print("Escreva: f (fumantes), d (depressivos) fd (para a comparação entre os dois) ou s (para terminar o programa)")
print("")

# while infinito para sempre voltar para a pergunta do que o usuário deseja ver após o if ser chamado, apenas será interrompido 
# caso ele digite 's' para chamar o elif com brake para parar o while
while True: 
 graf = input("O que deseja ver?:")
 print("")

 if (graf == "f"):
    plot_fumantes(dadosf)
    
 elif (graf == "d"):
    plot_depressivos(dadosd)
    print("")
        
 elif (graf == "fd"):
    plot_fd(dadosfd)
    print("")
 elif (graf == "s"):
     print("Obrigado pela atenção!")
     break       
 else:
     print("Opção não definida digite novamente")
     
# com um else feito caso o usuário digite uma opção não listada     
     
     
     
 