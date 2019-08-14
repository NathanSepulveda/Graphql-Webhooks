# An example to get the remaining rate limit using the Github GraphQL API.

import requests

headers = {"Authorization": "xxxxxxxxx"}


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.monday.com/v2/', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

# THIS IS A GOOD ONE QUERY
query = """
    query 
    {
        boards(ids: 289381959) 
        {
        id 
        name
        columns 
        {
            title
            id
        }
            
        items 
        {
    
            id

            board 
            {
                id
            }
            column_values()
            {
                id
                title
                value
                
            }
            name
            id
        }
        }
    }
"""





result = run_query(query) # Execute the query
print(result)
# print(result)


for column in result["data"]["boards"][0]["columns"]:
    print(column["title"], column["id"])



for item in result['data']["boards"][0]['items']:
    print(item['name'], item['id'])