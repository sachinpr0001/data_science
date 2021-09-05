import pandas as pd
import numpy as np
import requests
import json
file = open('ID.csv')
csvreader = csv.reader(file)
rows = []

for row in csvreader:
        rows.append(row)
rows = rows[1:]
jokes = []
id_array = []
for list_index in rows:
    id = list_index[0]
    id_array.append(id)
    url = "http://api.icndb.com/jokes/{}".format(id)
    response = requests.get(url)
    joke_dict = json.loads(response.content.decode('utf-8'))
    joke = joke_dict["value"]["joke"]
    print(joke)
    jokes.append(joke)
combined = np.vstack((id_array, jokes)).T
df=pd.DataFrame(combined, columns=['ID', 'Jokes']) 
df.to_csv("submission.csv", index=False)