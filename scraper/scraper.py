import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.advocatekhoj.com/library/bareacts/index.php"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

acts_table_container = soup.find(id="content_container")
acts_table = acts_table_container.select_one("table:nth-of-type(1)")

rows = acts_table.findAll('tr')
rows = rows[464:]
for i, row in enumerate(rows):
    a = row.find('a').get('href')
    act_meta = a.split('/index.php?Title=')
    act_blob = act_meta[0]
    act_title = act_meta[1]
    print(act_blob, act_title)
    curr_dict = {"name": act_title}
    for i in range(1,600):
        print(f"At {act_blob}-Section-{i}-{act_title}")
        ACT_URL = f"https://www.advocatekhoj.com/library/bareacts/{act_blob}/{i}.php"
        act_page = requests.get(ACT_URL)
        if act_page.status_code != 200:
            print("Got a NON-200")
            print(act_page.status_code)
            print(act_page.reason)
            break
        else:
            p_soup = BeautifulSoup(act_page.content, "html.parser")
            # check if page is a 404
            if p_soup.findAll(text="UH OH! You're lost."):
                print(f"Hit a 404 for {act_blob}-Section-{i}-{act_title}")
                break
            else:
                c_container = p_soup.find(id="maincontainer")
                paras = c_container.findAll('p')
                final_str = str()
                for p in paras:
                    final_str += p.get_text()
                
                curr_dict[i] = final_str
    
    with open(f'api/data/{act_blob}.json', 'w') as fp:
        json.dump(curr_dict, fp)
