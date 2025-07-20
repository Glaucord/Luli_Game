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
print("Welcome to the Lulu Game!")
print("Your mission is to find the Luli Maria.")
choice1 = input('You were walking with Luli to the park, but she smelled something and escaped from you. '
                'She ran around the corner.\nWhen you get there she is gone. '
                'After some running you can choose to go to the "left" street or '
                'the "right" street. Where do you go?').lower()
if choice1 == "left":
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
    choice2 = input('You\'ve found a group of bulldogs who are mad '
                    'because Luli stole their corn cake. \n-Luli loves corn cake- '
                    'Think fast! You see a "dog square" and a "coffe shop". '
                    'To where do you run? ' ).lower()
    if choice2 == "coffe shop":
        choice3 = input('You enter the coffe shopp and they are also worried. It seems like their '
          'corn cake is also missing. \nSuddenly you to the bathroom and here some '
          'noises. You have three doors to choose from. \nThe "left", the "middle" and the "right"'
          ' whitch do you choose?"').lower()
        if choice3 == "left":
            print("You've found her! It looks like she have a whole cake in front of her!")
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
            print("You won the game!")
        elif choice3 == "middle":
            print("It's empty! You've lost the game.")
        elif choice3 == "right":
            print("It have someone! And they're not happy with your intrusion. You've lost the game.")
    else:
        print("Luli is not sociable towards dogs. She prefer humans. You couldn't find her. "
              "You've lost the game.")

else:
    print("You ran to the right street and fell into a hole. Game Over.")
