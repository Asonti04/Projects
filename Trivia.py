#trivia game containing 3 modes each containing 3 questions
#The following game was created by ASONTI GINN
#Date 6/2/2023
print('''
    *   *   *   *   *   *   *   *   *
            WELCOME TO TRIVIA
    *   *   *   *   *   *   *   *   *
''')
print('                 TOPICS')
print('''
*   *   *   *   *   *   *   *   *   *   *
 POP CULTURE | VIDEO GAMES | FOOD CHAINS
*   *   *   *   *   *   *   *   *   *   *
''')

while True:
    topic = input('         Type \'exit\' to leave\n      SELECT A TOPIC: ')
    
    if topic == 'POP CULTURE':
        print('You selected POP CULTURE, lets being with something easy.\n *    *    *   * Use the numbers 1, 2, & 3 to answer *    *    *   *\nQuestion 1. What song had the most streams on youtube for the year 2022?')
        pcq1 = int(input('1. Encanto- We don\'t talk about bruno, 2. Future- Wait for U, 3. Karol G- Provenza '))
        if pcq1 != 1:
            print('Sorry that is incorrect, the answer was 1. Encanto- We don\'t talk about bruno. You lose!')
            
        else:
            print('''
            *   *   *   *   *   * 
                   CORRECT!
            *   *   *   *   *   * 
            ''')
            print('Question 2. What was considered the most popular luxury brand of 2022?')
            pcq2 = int(input('1. Louis Vutton, 2. Versace, 3. Gucci '))   
            if pcq2 != 3:
                print('Sorry that is incorrect, the answer was 3. Gucci. You got 1 answer correct.')
            else:
                print('''
            *   *   *   *   *   * 
                CORRECT AGAIN!
            *   *   *   *   *   *   
            ''')
                print('Final Question. What football team won the 2023 Superbowl?')
                pcq3 = int(input('1. Chiefs , 2. Eagles , 3. Rams '))
                if pcq3 != 1:
                    print('Sorry that is incorrect, the answer was 1. Chiefs . You got 2 correct answers, SO CLOSE')
                else:
                    print('''
            *   *   *   *   *   *   
                  YOU WIN!!
            *   *   *   *   *   *   
                    ''')
                    print('           Try another game\n                OR')
                    
   
    elif topic == 'VIDEO GAMES':
        print('Okay gamer get ready for your first question!\n*    *    *   * Use the numbers 1, 2, & 3 to answer *    *    *   *\nQuestion 1. What Gaming system had the most sales as of 2022?') 
        pcq1 = int(input('1. Playstation, 2. Nintendo Switch, 3. XBOX '))
        if pcq1 != 1:
            print('Sorry that is incorrect, the answer was 1. Playstation. Better Luck next time!')
            
        else:
            print('''
            *   *   *   *   *   * 
                   CORRECT!
            *   *   *   *   *   * 
            ''')
            print('Question 2. What was the most purchased video game as of 2022?')
            pcq2 = int(input('1. Madden NFL 2023, 2. Call of Duty: Modern Warfare II, 3. God of War Ragnarok '))   
            if pcq2 != 2:
                print('Sorry that is incorrect, the answer was 2. Call of Duty: Modern Warfare II. You got 1 answer correct.')
            else:
                print('''
            *   *   *   *   *   * 
                CORRECT AGAIN!
            *   *   *   *   *   *   
            ''')
                print('Final Question. What year was the very first playstation released?')
                pcq3 = int(input('1. 1996  , 2. 1990 , 3. 1994 '))
                if pcq3 != 3:
                    print('Sorry that is incorrect, the answer was 3. 1994. You got 2 correct answers, SO CLOSE')
                else:
                    print('''
            *   *   *   *   *   *   
                  YOU WIN!!
            *   *   *   *   *   *   
                    ''')
                    print('           Try another game\n                OR')

     
    elif topic == 'FOOD CHAINS':
        print('           Lets talk food!\n*    *    *   * Use the numbers 1, 2, & 3 to answer *    *    *   *\nQuestion 1. What Fast Food company sold the most burgers as of 2023?')
        pcq1 = int(input('1. Wendys, 2. Mcdonalds, 3. Burger King '))
        if pcq1 != 2:
            print('Sorry that is incorrect, the answer was 2. Wendys. Maybe you should try again!')
            
        else:
            print('''
            *   *   *   *   *   * 
                   CORRECT!
            *   *   *   *   *   * 
            ''')
            print('Question 2. What company\'s slogan is: Better Ingredients, Better Pizza?')
            pcq2 = int(input('1. Domino\'s, 2. Pizza Hut, 3. Papa Johns '))   
            if pcq2 != 3:
                print('Sorry that is incorrect, the answer was 3. Papa Johns. You got 1 answer correct.')
            else:
                print('''
            *   *   *   *   *   * 
                CORRECT AGAIN!
            *   *   *   *   *   *   
            ''')
                print('Final Question. Which of the following fast food logos DOES NOT contain the color red?')
                pcq3 = int(input('1. Panda Express, 2. Subway, 3. Popeyes '))
                if pcq3 != 2:
                    print('Sorry that is incorrect, the answer was 2. Subway. You got 2 correct answers, SO CLOSE')
                else:
                    print('''
            *   *   *   *   *   *   
                  YOU WIN!!
            *   *   *   *   *   *   
                    ''')
                    print('           Try another game\n                OR')
        
    elif topic == 'exit':
        print('''
        *   *   *   *   *   *   *
           Thanks for playing!
        *   *   *   *   *   *   *
        ''')
        break
    
    else:
        print('Invalid entry, please try POP CULTURE, VIDEO GAMES, or FOOD CHAINS')