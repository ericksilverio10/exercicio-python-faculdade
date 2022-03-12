'''
Escreva um programa que leia palavras, até que a palavra “fim” (com qualquer grafia) seja digitada.
As palavras menores que 4 caracteres ou maiores do que 15 caracteres devem ser rejeitadas.
Para as palavras aceitas troque as vogais : a,e,i,o ,u respectivamente por @,&,!,#,%, mostrando a palavra depois das trocas.
Conte as palavras iniciadas por vogal.
No final mostre: o total de palavras lidas, o total de palavras não rejeitadas e o total de palavras que iniciaram por vogal
'''
cont=1
contlidas=1
contvogal=0
vogais = ['A','E','I','O','U']
while True:
    palavra=input('Digite uma palavra com 4 a 15 caracteres ou FIM para encerrar: ')
    palavra=palavra.upper()
    if palavra[0] in vogais:
        contvogal += 1
    if palavra=="FIM":
        print('quantidade de palavras lidas: ',cont-1)
        print('quantidade de palavras não rejeitadas: ',contlidas-1)
        print('quantidade de palavras iniciadas por vogal: ',contvogal)
        break
    else:
        cont=cont+1
        if len(palavra)>4 and len(palavra)<15:
            contlidas=contlidas+1
            palavra = palavra.replace('A','@')
            palavra = palavra.replace('E','&')
            palavra = palavra.replace('I','!')
            palavra = palavra.replace('O','#')
            palavra = palavra.replace('U','%')
            print('Trocando as vogais da palavra por simbolo: ',palavra)
        else:
            print('Palavra rejeitada! a palavra deve ter entre 4 a 15 letras!')
