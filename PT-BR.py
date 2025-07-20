print(r'''           ____,'`-, 
      _,--'   ,/::.; 
   ,-'       ,/::,' `---.___        ___,_ 
   |       ,:';:/        ;'"`;"`--./ ,-^.;--. 
   |:     ,:';,'         '         `.   ;`   `-. 
    \:.,:::/;/ -:.                   `  | `     `-. 
     \:::,'//__.;  ,;  ,  ,  :.`-.   :. |  ;       :. 
      \,',';/O)^. :'  ;  :   '__` `  :::`.       .:' ) 
      |,'  |\__,: ;      ;  '/O)`.   :::`;       ' ,' 
           |`--''            \__,' , ::::(       ,' 
           `    ,            `--' ,: :::,'\   ,-' 
            | ,;         ,    ,::'  ,:::   |,' 
            |,:        .(          ,:::|   ` 
            ::'_   _   ::         ,::/:| 
           ,',' `-' \   `.      ,:::/,:| 
          | : _  _   |   '     ,::,' ::: 
          | \ O`'O  ,',   ,    :,'   ;:: 
           \ `-'`--',:' ,' , ,,'      :: 
            ``:.:.__   ',-','        ::' 
    -hrr-      `--.__, ,::.         ::' 
                   |:  ::::.       ::' 
                   |:  ::::::    ,::' ''')
print("Bem-vindo ao Jogo da Lulu!")
print("Sua missão é encontrar a Luli Maria.")
choice1 = input('Você estava passeando com a Luli no parque, mas ela sentiu um cheiro e fugiu de você. '
                'Ela dobrou a esquina.\nQuando você chega lá, ela sumiu. '
                'Depois de correr um pouco, você pode escolher ir pela rua da "esquerda" ou '
                'pela rua da "direita". Para onde você vai? ').lower()
if choice1 == "esquerda":
    print('''         ,--._______,-. 
       ,','  ,    .  ,_`-. 
      / /  ,' , _` ``. |  )       `-.. 
     (,';'""`/ '"`-._ ` \/ ______    \\ 
       : ,o.-`- ,o.  )\` -'      `---.)) 
       : , d8b ^-.   '|   `.      `    `. 
       |/ __:_     `. |  ,  `       `    \ 
       | ( ,-.`-.    ;'  ;   `       :    ; 
       | |  ,   `.      /     ;      :    \ 
       ;-'`:::._,`.__),'             :     ; 
      / ,  `-   `--                  ;     | 
     /  \                   `       ,      | 
    (    `     :              :    ,\      | 
     \   `.    :     :        :  ,'  \    : 
      \    `|-- `     \ ,'    ,-'     :-.-'; 
      :     |`--.______;     |        :    : 
       :    /           |    |         |   \ 
       |    ;           ;    ;        /     ; 
     _/--' |   -hrr-   :`-- /         \_:_:_| 
   ,',','  |           |___ \ 
   `^._,--'           / , , .) 
                      `-._,-' ''')
    choice2 = input('Você encontrou um grupo de buldogues que estão bravos '
                    'porque a Luli roubou o bolo de milho deles. \n-A Luli ama bolo de milho- '
                    'Pense rápido! Você vê uma "praça de cachorros" e uma "cafeteria". '
                    'Para onde você corre? ' ).lower()
    if choice2 == "cafeteria":
        choice3 = input('Você entra na cafeteria e eles também estão preocupados. Parece que o '
          'bolo de milho deles também sumiu. \nDe repente, você vai em direção ao banheiro e ouve alguns '
          'barulhos. Você tem três portas para escolher. \nA da "esquerda", a do "meio" e a da "direita".'
          ' Qual você escolhe? ').lower()
        if choice3 == "esquerda":
            print("Você a encontrou! Parece que ela tem um bolo inteiro na frente dela!")
            print('''           ____,'`-, 
               _,--'   ,/::.; 
            ,-'       ,/::,' `---.___        ___,_ 
            |       ,:';:/        ;'"`;"`--./ ,-^.;--. 
            |:     ,:';,'         '         `.   ;`   `-. 
             \:.,:::/;/ -:.                   `  | `     `-. 
              \:::,'//__.;  ,;  ,  ,  :.`-.   :. |  ;       :. 
               \,',';/O)^. :'  ;  :   '__` `  :::`.       .:' ) 
               |,'  |\__,: ;      ;  '/O)`.   :::`;       ' ,' 
                    |`--''            \__,' , ::::(       ,' 
                    `    ,            `--' ,: :::,'\   ,-' 
                     | ,;         ,    ,::'  ,:::   |,' 
                     |,:        .(          ,:::|   ` 
                     ::'_   _   ::         ,::/:| 
                    ,',' `-' \   `.      ,:::/,:| 
                   | : _  _   |   '     ,::,' ::: 
                   | \ O`'O  ,',   ,    :,'   ;:: 
                    \ `-'`--',:' ,' , ,,'      :: 
                     ``:.:.__   ',-','        ::' 
             -hrr-      `--.__, ,::.         ::' 
                            |:  ::::.       ::' 
                            |:  ::::::    ,::' ''')
            print("Você ganhou o jogo!")
        elif choice3 == "meio":
            print("Está vazio! Você perdeu o jogo.")
        elif choice3 == "direita":
            print("Tem alguém! E a pessoa não está feliz com a sua invasão. Você perdeu o jogo.")
    else:
        print("A Luli não é sociável com outros cachorros. Ela prefere humanos. Você não conseguiu encontrá-la. "
              "Você perdeu o jogo.")

else:
    print("Você correu para a rua da direita e caiu em um buraco. Fim de Jogo.")
