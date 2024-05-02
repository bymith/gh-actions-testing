import os
from github import Github

repo = Github(os.environ['GITHUB_TOKEN']).get_repo(os.environ['GITHUB_REPOSITORY'])
issue = repo.get_issue(number=int(os.environ['ISSUE_NUMBER']))
# board is 7x6 I *think*
# took me way to long to realize \n is counted as a character
board = [ 
  [[],[],[],[],[],[]],
  [[],[],[],[],[],[]],
  [[],[],[],[],[],[]],
  [[],[],[],[],[],[]],
  [[],[],[],[],[],[]],
  [[],[],[],[],[],[]],
  [[],[],[],[],[],[]],
  [[],[],[],[],[],[]]
]
isRed = False

def read_board():
  boardLines = []
  
  with open("boardstate.board", "r") as f:
    boardLines = f.readlines()

  if "0" in boardLines[0]:
    isRed = True
  
  boardLines.pop(0)
  
  y=0
  
  print(len(boardLines))
  for line in boardLines:
    x=0
    print(len(line))
    for character in line:
      print(x)
      print(y)
      print("-")
      board[x][y] = character # he he wrong side im dumb
      x+=1
    y+=1

def main():

  read_board()
  
  readme_text = """
  # Hello!
  ## you can play connect 4 below!

  | [1] | [2] | [3] | [4] | [5] | [6] | [7] |
  | - | - | - | - | - | - | - |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  
  """ % (board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0],board[6][0],
        board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1],board[6][1],
        board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2],board[6][2],
        board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3],board[6][3],
        board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4],board[6][4],
        board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5],board[6][5])
  for row in board:
    print(row)
  
  with open("README.md", "w") as f:
        f.write(readme_text)
  
  issue.edit(state='closed') # we done :)

main()
