apresentadores = {'PINHEIRO': 'Bom Dia Nação',
                  'ARAUJO': 'Bom Dia Nação',
                  'BONNER': 'Jornal Brasileiro',
                  'VASCONCELOS': 'Jornal Brasileiro'}

sobrenome = str(input("Digite o sobrenome do apresentador: ")).upper

if apresentadores[sobrenome]:
    print(f"O apresentador apresenta o programa {apresentadores[sobrenome]}.")
else:
    print("Apresentador(a) Desconhecido(a)!")
    
    
