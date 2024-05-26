import random 

def choose_item(bot=False): 
    if bot: 
        return random.choice(['к', 'н', 'б']) 
    else: 
        choice = input("Камень (к), ножиці (н) бумага (б): ").lower() 
        while choice not in ['к', 'н', 'б']: 
            print("Ваш вибір: к, н або б.") 
            choice = input("Виберіть камінь (к), ножиці (н) або папір (б): ").lower() 
        return choice 

def full_name(item): 
    if item == 'к': 
        return "Камень" 
    elif item == 'н': 
        return "Ножиці" 
    elif item == 'б': 
        return "Бумага" 
    else: 
        return "Помилка" 

def claim_winner(player, bot): 
    if player == 'к': 
        if bot == 'б': 
            return 'bot' 
        elif bot == 'н': 
            return 'player' 
        else: 
            return 'draw'  
    elif player == 'н': 
        if bot == 'б': 
            return 'player' 
        elif bot == 'к': 
            return 'bot' 
        else: 
            return 'draw' 
    elif player == 'б': 
        if bot == 'к': 
            return 'player' 
        elif bot == 'н': 
            return 'bot' 
        else: 
            return 'draw' 

    else: 
        return None 

def play_game(): 
    print("Камень. Ножниці. Бумага'") 
    player_choice = choose_item(bot=False) 
    bot_choice = choose_item(bot=True) 

    print("Гравець вибрав:", full_name(player_choice)) 
    print("Комп'ютер вибрав:", full_name(bot_choice)) 

    winner = claim_winner(player_choice, bot_choice) 
    if winner == 'player': 
        print("you win!") 
    elif winner == 'bot': 
        print("you lose") 
    else: 
        print("draw") 

play_game()