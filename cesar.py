texto = "Kjqne fvzjqj vzj ywfsxkjwj t vzj xfgj j fuwjsij t vzj jsxnsf. Htwf Htwfqnsf"

#Função que descobre o valor de deslocamento da Cifra de César
def deslocamento(palavra):
    referencia = "que"
    descobrir_deslocamento = ord(palavra[0]) - ord(referencia[0])
    return descobrir_deslocamento

#Separação do texto e atribuição do deslocamento a variavel shift de uma palavra de 3 caracteres
palavras = texto.split()
palavra_3_caracteres = [palavra for palavra in palavras if len(palavra) == 3]
shift = deslocamento(palavra_3_caracteres[0])


#Crifra de César para descriptografia utilizando o valor recebido de shift
def descriptar (texto, shift):
    texto = texto.lower()
    texto_descriptografado = ""
    for char in texto:
        if char.islower():
            texto_descriptografado += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            texto_descriptografado += char
    return texto_descriptografado

#Mostrando mensagem descriptografada
Mensagem = descriptar(texto,shift)
print(Mensagem)

