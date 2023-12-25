from bs4 import BeautifulSoup
import requests
import json
from emailer import email

def getHomework() -> str:

    with open('..\config\config.json') as config:
        config = json.load(config)

    soup = BeautifulSoup(requests.get(config['website']).text, features="html.parser")

    mostRecentHomework = soup.h2.text
    homework = ''

    if not mostRecentHomework == config['lastHomework']:
        config['lastHomework'] = mostRecentHomework
        # Update json file to latest HW
        with open('..\config\config.json', 'w') as file:
            file.write(json.dumps(config, indent=4))
        homework += mostRecentHomework
        homework += '\n https://novillo-cs.github.io/apcsa/contents/homework'
    
    return homework

homework = getHomework()
if not homework == '':
    email(homework)

