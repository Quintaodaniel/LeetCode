telefone = [
    [],                     ["a", "b", "c"], ["d", "e", "f"],
    ["g", "h", "i"],        ["j", "k", "l"], ["m", "n", "o"],
    ["p", "q", "r", "s"],   ["t", "u", "v"], ["w", "x", "y", "v"]
]
lista_solucao = []
str_current = ""

def solucao(input:str, size: int):
    global str_current
    for i in range(len(input)):
        if int(input[i]) == 1:
            return -1
        
        elif int(input[i]) <= 9:
            for j in telefone[int(input[i]) -1]:
                str_current += j
                solucao(input[i+1:], size)
                if len(str_current) == size:
                    lista_solucao.append(str_current)
                str_current = str_current[:-1]

        else:
            return -1
        
        
entrada = str(input())

if len(entrada) > 4 or entrada == "":
    print("Erro")

solucao(entrada, len(entrada))

print(lista_solucao)