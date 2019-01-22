####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Isaiah&Nethanial' # Only 10 chars displayed.
strategy_name = 'B Until C'
strategy_description = 'Betrays unless enemy colludes in last 10 turns, then colludes
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history) >= 10:
        for result in their_history[-10:]:
            if result == 'c':
                return 'c'
    else:
        return 'b'
