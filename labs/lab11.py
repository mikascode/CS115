#************************************************************
# *  Name  : Rashmika Batra 
# * Pledge : I pledge my honor that I have abided by the Stevens Honor System. 
#************************************************************

'''
4-Dice Pig

Adapted from Java to Python by Justin Barish,  11/2018
Modified Nov '19 by Toby Dalton, Nov '20 by Dominick DiMaggio

~ ~ ~

To exercise your looping ability, we're going to be filling in a bunch
of blanks. Joy!

Pig is a game where players take turns rolling dice.
Traditionally, it's only 2, but this is a variant.

The goal is to have their total score reach a certain # of points.
Players take turns earning points by rolling dice.
Each roll adds that sum onto a round score, which my or may not be added
to their total score, dictated as below:

A person's turn lasts until they want to stop rolling or roll some 1s.

If at any point during the player's turn they roll one 1:
their round ends and their round score is added to their total score.

If they roll two 1s:
they lose all points for the round, and their turn is over.

Three 1s:
they lose all of their points in the game, and their turn is over.

If they're unlucky and recieve the 'luck' of four 1s (four-eyed snake ::S):
they immediately lose the game.

Whenever the player decide to stop their turn, their round points are 
added to their total points.

When a player's total points reach 100 (controllable below), they win.
'''
import random

POINTS_TO_WIN = 100
AI_ROUND_TARGET = 20

'''
This lab has 2 parts:

Part 1 (10 pts): Complete the game for two human players.
That is, fill in all of the methods below

Part 2 (2 pts Extra Credit):
Add in an "AI" as the second player, so you will play against the computer.
The AI takes the place of player 2, and will continue rolling until
it reaches its AI_ROUND_TARGET. NOTE: You *will* need to change some of the
function paramaters (I.E. pass in additional values) and other parts of
functions.
'''

#************************************************************
#**   General Game Stuff
#************************************************************

def main():
  '''This is the main function for the pig game'''
  welcome()
  while True:
    # Challenge: Choose whether or not to add AI for each game, and do the rest.
    playGame()
    if not wantsPlayAgain():
      print('Bye!')
      return

# TODO
def playGame():
  '''Play one game of pig
  Alternates between players, and at the end of a player's turn, 
  prints the overall game score for both players'''

  player = 1
  scores = initScores()
  while not gameOver(scores):
    scores=getMove(scores, player)
    print('Current Scores:')
   
    printScore(scores)
    if player==1:
      player=2
    else:
      player=1

def initScores():
  '''initialize the scores to 0'''
  # How you create and work with the scores is up to you!
  return [0,0]

# TODO
def gameOver(scores):
  '''Checks if the game is over
  Game is over when either player's score reaches >= POINTS_TO_WIN.
  [ or 4 ones are rolled :3]
  Prints the win message for the player who won
  If no one won, just returns false'''
  if scores[0]>=POINTS_TO_WIN:
    printWinMessage(1, scores)
    return True
  elif scores[1]>=POINTS_TO_WIN:
    printWinMessage(2, scores)
    return True
  return False

# TODO  
def getMove(scores, player):
  '''Gets a player's move.
  Before every move, prints the current round score and the game score for the player
  Checks if the player wants to continue, and if they do, rolls dice and appropriately changes scores
  '''
  printPlayerMessage(player)
  roundScore = 0
  while True:

    printCurrentPlayerScore(scores, player, roundScore)

    if(not wantsRollAgain(player)):
      if player==1:
        return [scores[0]+roundScore,scores[1]]
      else:
        return [scores[0],roundScore+scores[1]]

    roll = rollDice()
    showRoll(roll)

    count=0
    totalroll=0 
    for x in roll:
      totalroll+=x 
      if x==1:
        count+=1 
      
       
    if count==4:
      
      print("Rolled four 1s... Game over")
      if player==1:
        return [0,POINTS_TO_WIN]
      else:
        return [POINTS_TO_WIN,0]

       
   
    elif count==3:
      print("Rolled three 1s. Score reset!")
      # todo
      if player==1:
        return [0,scores[1]]
      else:
        return [scores[0],0]

    elif count==2 :
      print("Rolled two 1s! Round ended, no score added")
      return scores
    elif count==1:
      print("Rolled one 1! Round ended, score added")
      if player==1:
        return [scores[0]+totalroll,scores[1]]
      else:
        return [scores[0],totalroll+scores[1]]
    else:
      roundScore+=totalroll

def rollDie():
  '''rolls a single die (wow)'''
  return random.randint(1,6)

# TODO
def rollDice():
  '''grabs the roll for four dice'''
  a=rollDie()
  b=rollDie()
  c=rollDie()
  d=rollDie()
  return [a,b,c,d]

#************************************************************  
#**   Useful functions to check if we want to [X] again
#************************************************************

# TODO
def wantsContinue(prompt):
  '''Checks if the response a user gives indicates they want to continue.
  assume the user has to give a Y to mean yes and N to mean no'''
  ans = input(prompt)
  while ans != "N" and ans!="Y":
    ans = input(prompt)
  return ans

# TODO  
def wantsPlayAgain():
  '''Asks a player if they want to play the game again (use wantsContinue()!)'''
  ans=wantsContinue("Would you like to play again? Y for yes, N for no:")
  if ans=="Y":
    return True
  else:
    return False 
    

# TODO
def wantsRollAgain(player):
  '''Asks a player if they want to roll again
  For Part 2, also handle the Computer's decision'''
  ans=wantsContinue("Would you like to play again? Y for yes, N for no:")
  if ans=="Y":
    return True
  else:
    return False 
    


#************************************************************
#**   Functions to Print Things
#************************************************************

def welcome():
  '''Prints the welcome message for the game.
  We might also print the rules for the game and any other
  information that the user might need to know.'''
  print('Welcome to Pig!')

# TODO
def printScore(scores):
  '''prints the current game score for each player'''
  print("Player 1: " + str(scores[0]) + " & Player 2: " + str(scores[1]))

def printWinMessage(winningPlayer, scores):
  print()
  print('***********************Player ' + str(winningPlayer) + ' Won!************************')
  print('***********************Final Score:*************************')
  printScore(scores)

# TODO
def showRoll(roll):
  ''' Prints out the roll'''
  print(roll) 

def printPlayerMessage(player):
  print()
  print('--------------------------------------------------------------')
  print('-------------------Player ' + str(player) + '\'s turn----------------------------')
  print('--------------------------------------------------------------')
  print()

# TODO
def printCurrentPlayerScore(scores, player, roundScore):
  '''Print the score for a specific player. Prints their round score 
  and their overall game score not including their current round score'''
  if player==1:

    print("Player 1 has the round score of " + str(roundScore) + " and an overall score of " + str(scores[0]))
  else:
     print("Player 2 has the round score of " + str(roundScore) + " and an overall score of " + str(scores[1]))
      

if __name__ == '__main__':
  main()
