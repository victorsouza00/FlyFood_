matriz = [["D", 0 , "B" , 0 , 0 ],
          [0 , 0 , 0 , 0 , 0 ],
          ["E", 0 , 0 ,  0 , 0 ],
          [0 , 0 , 0 , 0 , 0 ],
          [0 , 0 ,  0 ,  0 , 0 ]]


def PontosCounter(array):
    ArrayValores = []
    Pontos = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] != 0:
                nome = array[i][j]
                Pontos.append(nome)
                coordenadas = (i, j)
                ArrayValores.append(coordenadas)
    return ArrayValores

# print(PontosCounter(matriz))


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def permute(a, l, r, result):
    if l == r:
        result.append(a[:])
    else:
        for i in range(l, r + 1):
            swap(a, l, i)
            permute(a, l + 1, r, result)
            swap(a, l, i)
result = []
n = len(PontosCounter(matriz))
permute(PontosCounter(matriz), 0, n - 1, result)


def list(arr,perm):
  linhas = len(arr)
  colunas = len(arr[0])
  solucao = []
  A=(linhas - 1, 0)#Começo
  B=(0, colunas - 1)#Fim
  menor = 9999999999999999999999
  for caminho in perm:
    print(caminho)
    x = abs(caminho[0][0] - A[0]) + abs(caminho[0][1] - A[1])
    y = 0
    for j in range(len(caminho)-1):
       y += abs(caminho[j+1][0] - caminho[j][0]) + abs(caminho[j+1][1] - caminho[j][1])

    z = y + x + abs(caminho[-1][0] - B[0]) + abs(caminho[-1][1] - B[1])

    if z < menor:
      menor = z
      solucao = caminho

  return menor,solucao


print(list(matriz,result))
