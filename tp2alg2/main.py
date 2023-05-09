
import sys
import os.path
import LZ78


def main():
  # Obtem os argumentos da linha de comando
  if len(sys.argv) < 3:
    return
  opcao = sys.argv[1]
  arquivo_entrada = sys.argv[2]
  arquivo_saida = None
  if len(sys.argv) > 3:
    if sys.argv[3] == "[-o":
      if len(sys.argv) < 5:
        return
      arquivo_saida = sys.argv[4]
      arquivo_saida = arquivo_saida[:-1]

  # Cria o nome do arquivo de saída se não foi especificado
  if arquivo_saida is None:
    if opcao == "-c":
      arquivo_saida = os.path.splitext(arquivo_entrada)[0] + ".z78"
    elif opcao == "-x":
      arquivo_saida = os.path.splitext(arquivo_entrada)[0] + ".txt"

  # Realiza a compressão ou descompressão
  if opcao == "-c":
    with open(arquivo_entrada, "r") as arquivo:
      entrada = arquivo.read()
      str_entrada = str(entrada)
      saida = LZ78.compress(str_entrada)
      LZ78.write_in_binary(arquivo_saida, saida)
  if opcao == "-x":
    descomprimido = []
    LZ78.read_from_binary(arquivo_entrada,descomprimido)
    saida = LZ78.decompress(descomprimido)
    with open(arquivo_saida,"w") as file:
      print(saida,file=file)


if __name__ == "__main__":
  main()
