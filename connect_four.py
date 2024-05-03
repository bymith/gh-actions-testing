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
    for character in line:
      board[x][y] = character # he he wrong side im dumb
      if character == "0":
        board[x][y] = "."
      x+=1
    y+=1
  print(board)
  print("^^^^ read board")

def fall(colNum):
  if not board[colNum][0] == ".":
    issue.create_comment("bruh that column is filled...")
    issue.create_comment(str(board))
    return

  y = 0
  for rowItem in board[colNum]:
    if not rowItem == "." or y == len(board[colNum])-1:
      if isRed:
        board[colNum-1][y] = "x"
      else:
        board[colNum-1][y] = "o"
      break
    y+=1
    

def main():

  if not issue.title.startswith("dropTile|"):
    issue.create_comment("Grrrr you didn't get the format right >:(")
    issue.edit(state='closed')
  
  read_board()

  turn = "blue"

  if isRed:
    turn = "red"

  fall(int(issue.title.split("|")[1]))
  
  readme_text = """
  # Hello!
  ## you can play connect 4 below!

  It is **%s's** turn. (o is blue, x is red, and a . is nothing (github will just collapse the row if I don't have something there))
  
  | [1](%s) | [2](%s) | [3](%s) | [4](%s) | [5](%s) | [6](%s) | [7](%s) |
  | - | - | - | - | - | - | - |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  | %s | %s | %s | %s | %s | %s | %s |
  
  """ % (turn,
        "https://github.com/bymith/gh-actions-testing/issues/new?title=dropTile%7C1&body=Hit+sumbit+new+issue+or+just+press+enter.+Then+just+wait+like+30+seconds+for+it+to+update+%3A%29",
        "https://github.com/bymith/gh-actions-testing/issues/new?title=dropTile%7C2&body=Hit+sumbit+new+issue+or+just+press+enter.+Then+just+wait+like+30+seconds+for+it+to+update+%3A%29",
        "https://github.com/bymith/gh-actions-testing/issues/new?title=dropTile%7C3&body=Hit+sumbit+new+issue+or+just+press+enter.+Then+just+wait+like+30+seconds+for+it+to+update+%3A%29",
        "https://github.com/bymith/gh-actions-testing/issues/new?title=dropTile%7C4&body=Hit+sumbit+new+issue+or+just+press+enter.+Then+just+wait+like+30+seconds+for+it+to+update+%3A%29",
        "https://github.com/bymith/gh-actions-testing/issues/new?title=dropTile%7C5&body=Hit+sumbit+new+issue+or+just+press+enter.+Then+just+wait+like+30+seconds+for+it+to+update+%3A%29",
        "https://github.com/bymith/gh-actions-testing/issues/new?title=dropTile%7C6&body=Hit+sumbit+new+issue+or+just+press+enter.+Then+just+wait+like+30+seconds+for+it+to+update+%3A%29",
        "https://github.com/bymith/gh-actions-testing/issues/new?title=dropTile%7C7&body=Hit+sumbit+new+issue+or+just+press+enter.+Then+just+wait+like+30+seconds+for+it+to+update+%3A%29",
        board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0],board[6][0],
        board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1],board[6][1],
        board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2],board[6][2],
        board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3],board[6][3],
        board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4],board[6][4],
        board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5],board[6][5])
  for row in board:
    print(row)
  
  with open("README.md", "w") as f:
    f.write(readme_text)

  with open("boardstate.board", "w") as f:
    theString = "0\n"
    if isRed:
      theString = "1\n"

    theString += "%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s" % (
        board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0],board[6][0],
        board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1],board[6][1],
        board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2],board[6][2],
        board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3],board[6][3],
        board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4],board[6][4],
        board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5],board[6][5])
    print(board)
    print(theString)
    f.write(theString)
  
  issue.edit(state='closed') # we done :)

main()
