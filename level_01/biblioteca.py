def gera_nome(convite):
  posicao_final = len(convite);
  posicao_inicial = posicao_final - 4
  parte1 = convite[0:4]
  parte2 = convite[posicao_final-4:posicao_final]
  return parte1 + ' ' + parte2 



