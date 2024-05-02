import os
from github import Github

repo = Github(os.environ['GITHUB_TOKEN']).get_repo(os.environ['GITHUB_REPOSITORY'])
issue = repo.get_issue(number=int(os.environ['ISSUE_NUMBER']))
# board is 7x6 I *think*
# took me way to long to realize \n is counted as a character
board = [ 
  [[],[],[],[],[],[],[]],
  [[],[],[],[],[],[],[]],
  [[],[],[],[],[],[],[]],
  [[],[],[],[],[],[],[]],
  [[],[],[],[],[],[],[]],
  [[],[],[],[],[],[],[]],
  [[],[],[],[],[],[],[]],
  [[],[],[],[],[],[],[]]
]
isRed = False

def read_board():
  boardLines = []
  
  with open("README.md", "r") as f:
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
  |   |   | - | - | - | - | - |
  |   |   | - | - | - | - | - |
  |   |   | - | - | - | - | - |
  |   |   | - | - | - | - | - |
  |   |   | - | - | - | - | - |
  
  """
  for row in board:
    readme_text += row
  
  with open("README.md", "w") as f:
        f.write(readme_text)
  
  issue.edit(state='closed') # we done :)

main()
