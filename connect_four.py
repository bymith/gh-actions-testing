
from github import Github

def main():
  
  repo = Github(os.environ['GITHUB_TOKEN']).get_repo(os.environ['GITHUB_REPOSITORY'])
  issue = repo.get_issue(number=int(os.environ['ISSUE_NUMBER']))
  readme_text = """
  # Hello!
  ## This is testing :)

  
  """ + issue.title()
  
  with open("README.md", "w") as f:
        f.write(readme_text)

main()
