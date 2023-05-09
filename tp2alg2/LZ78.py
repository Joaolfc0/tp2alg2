from trie_tree import Trie

def decompress_aux(compressed, index):
  word = ""
  if compressed[index][0] != 0:
    word = word + decompress_aux(compressed[:compressed[index][0]], compressed[index][0]-1)
    word = word + compressed[index][1] if compressed[index][1] != '' else word
  else:
    word = word + compressed[index][1]

  return word
def decompress(compressed):
    output = ""
    for index, c in compressed:
        if c == '':
            word = ""
            word = word + decompress_aux(compressed[:index ], index - 1)
            output = output + word
        else:
          if index != 0:
            word = ""
            word = word + decompress_aux(compressed[:index ],index - 1)
            word = word + c
            output = output + word
          else:
            output = output + c
            
    return output

def compress(input_str):
  trie = Trie()
  output = []
  idx_inicio = 0
  acabou = 0
  len_input = len(input_str)
  for c in range(len(input_str)):
    idx_palavra = idx_inicio + 1
    if input_str[idx_inicio:idx_palavra] == '':
      break
    while trie.search(input_str[idx_inicio:idx_palavra]) != -1:
      idx_palavra = idx_palavra + 1
      
      if idx_palavra >= len_input+1:
        idx_palavra = idx_palavra -1
        acabou = 1
        break
    if not acabou:
      output.append((trie.search_output(input_str[idx_inicio:idx_palavra])+1, input_str[idx_palavra-1]))
    else:
      output.append((trie.search_output(input_str[idx_inicio:idx_palavra])+1, ''))
      break
    trie.insert(input_str[idx_inicio:idx_palavra])
    idx_inicio = idx_palavra
  return output

def read_from_binary(filename, lista_convertida):
    # Abrir o arquivo em modo de leitura de bytes
    with open(filename, 'rb') as file:
        # Ler todos os bytes do arquivo
        bytes_lidos = file.read()

    # Iterar sobre os bytes lidos em grupos de 5
    for i in range(0, len(bytes_lidos), 5):
        # Obter os dois valores da tupla a partir dos bytes lidos
        valor1 = int.from_bytes(bytes_lidos[i+2:i+5], byteorder='big')
        valor2 = int.from_bytes(bytes_lidos[i:i+2], byteorder='big')
        if valor2 != 0:
          valor2 = chr(int.from_bytes(bytes_lidos[i:i+2], byteorder='big'))
        else:
          valor2 = ''
        
        # Adicionar a tupla convertida à lista de saída
        lista_convertida.append((valor1, valor2))


def write_in_binary(filename,compressed):
  lista_em_bytes = []
  
  for tupla in compressed:
      # Converter o primeiro valor da tupla em um inteiro de 2 bytes
      valor1 = tupla[0].to_bytes(3,byteorder='big')
      
      # Converter o segundo valor da tupla em um valor ASCII de 2 bytes
      valor2 = ord(tupla[1]) if tupla[1]!='' else 0
      valor2 = valor2.to_bytes(2,byteorder='big') 
      
      # Concatenar os valores convertidos em uma única tupla de bytes
      tupla_em_bytes = valor2 + valor1
      
      lista_em_bytes.append(tupla_em_bytes)
  
  saida_em_bytes = b''.join(lista_em_bytes)
  
  with open(filename, 'wb') as file:
      file.write(saida_em_bytes)

      
      
