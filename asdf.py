from bs4 import BeautifulSoup as bs
from classes.EnemyAttributes import EnemyAttributes

def main():
  with open('./views/wight.html') as file:
    soup = bs(file, 'html.parser')

  name = soup.find(id='name')
  level = soup.find(id='level')
  alignment = soup.find(id='alignment')
  size = soup.find(id='size')
  enemyType = soup.find(id='enemyType')
  additionalTag = soup.find(id='additionalTagWrapper')

  print(name)
  print(level)
  print(alignment)
  print(size)
  print(enemyType)
  print(additionalTag.contents)

  test = EnemyAttributes(

  )

main()