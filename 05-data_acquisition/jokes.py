import csv
import requests
import json
import pandas as pd
file = open('ID.csv')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
        rows.append(row)
rows = rows[1:]
jokes = []

for list_index in rows:
    id = list_index[0]
    url = "http://api.icndb.com/jokes/{}".format(id)
    response = requests.get(url)
    joke_dict = json.loads(response.content.decode('utf-8'))
    joke = joke_dict["value"]["joke"]
    print(joke)
    jokes.append(joke)
# print(jokes)

csv = pd.DataFrame(jokes)[['ID','joke']]
csv.to_csv("submission.csv",index=False)

# df=pd.DataFrame(jokes, columns=['ID', 'Jokes']) 
# print(df.head())




# with open('output.csv','w') as result_file:
#     wr = csv.writer(result_file)
#     wr.writerows([jokes])

print("csv created successfully")