def main():
  readme_text = """
  # Hello!
  ## This is testing :)
  """
  with open("README.md", "w") as f:
        f.write(readme_text)

main()
