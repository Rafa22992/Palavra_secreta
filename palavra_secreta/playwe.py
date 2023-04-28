from random import shuffle

bordas = '_' * 35

titulo = 'Jogo Da Palavra Secreta'

print(bordas)
print(f'{titulo.upper():=^35}')
print(bordas)

base_palavras = []

nova_palavra = ''
nova_letra = ''

numero_tentativas = 0
cont_lista = 0
contagem_palavras = 0
cont_nivel_jogo = 0
numero_palavras = 0

while True:

    while cont_nivel_jogo < 1:

        print(bordas)
        print('Escolha o nível do jogo:')
        print('=' * 15)
        print('1- Fácil')
        print('2- Médio')
        print('3- Difícil')
        print('=' * 15)
        print(bordas)

        escolha_nivel_jogo = input('[1] [2] [3]: ')
        print(bordas)

        try:
            if escolha_nivel_jogo.isalpha():
                print('Digite [1] [2] OU [3]')
                continue

            int_nivel_jogo = int(escolha_nivel_jogo)

            if int_nivel_jogo == 1:
                numero_palavras = 2
                contagem_palavras = numero_palavras

            if int_nivel_jogo == 2:
                numero_palavras = 4
                contagem_palavras = numero_palavras
            
            if int_nivel_jogo == 3:
                numero_palavras = 6
                contagem_palavras = numero_palavras

            if int_nivel_jogo > 3 or int_nivel_jogo < 1:
                print('Digite [1] [2] OU [3]')
                continue

            cont_nivel_jogo += 1

        except:
            print('Digite [1] [2] OU [3]')

    # ---------------------- usuario escolhe as palavras e são embaralhadas
    while cont_lista < numero_palavras:

        escolher_palavras = input(f'Digite {contagem_palavras} palavras: ').lower()
        print(bordas)

        if not escolher_palavras.isalpha():
            print('Digite apenas palavras!!!')
            print(bordas)
            continue

        base_palavras.append(escolher_palavras)

        shuffle(base_palavras)

        palavra_secreta = base_palavras[0]

        contagem_palavras -= 1
        cont_lista += 1

#---------------------------------início do jogo
    letra_usuario = input('Digite uma letra: ').lower()
    print(bordas)

    if not letra_usuario.isalpha():
        print('Você só poderá digitar letras')
        print(bordas)
        continue
    
    tentativas_lim = len(letra_usuario)

    if tentativas_lim > 1:
        print('Você só pode digitar uma letra!!!')
        print(bordas)
        continue

    if letra_usuario in palavra_secreta:
        print(f'Obaaaa!!!(a letra {letra_usuario.upper()} esta na palavra secreta!!!)')
        nova_letra += letra_usuario

    else:
        print(f'Ahhh!!!(a letra {letra_usuario.upper()} não esta na palavra secreta!!!)')
        print(bordas)

    palavra_certa = ''
    for letra in palavra_secreta:
        
        if letra in nova_letra:
            palavra_certa += letra

        else:
            palavra_certa += '*'

    borda_palavra = '=' * 35
    print(palavra_certa)
    print(borda_palavra)

    numero_tentativas += 1

    if palavra_certa == palavra_secreta:
        print(f'PARÁBENS VOCÊ COMPLETOU A PALAVRA SECRETA')
        print(bordas)
        print(f'A palavra secreta era {palavra_secreta.upper()}')
        print(bordas)
        
        print(f'Número de tentativas {numero_tentativas} x')
        print(bordas)

        sair = input('Deseja sair? ').startswith('s')
        print(bordas)

        if sair:
            break

        else:
            cont_nivel_jogo = 0
            contagem_palavras = numero_palavras
            base_palavras = []