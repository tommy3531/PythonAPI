import requests

# https://api.propublica.org/congress/v1/members/senate/RI/api-key=FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji/current.json
# https://api.propublica.org/congress/v1/members/senate/MO/api-key=FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji/current.json

def getSentatorByState(state):
    return 'https://api.propublica.org/congress/v1/members/senate/' + state +'/api-key=FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji/current.json'

def listSentatorByState(state):

    url = "https://api.propublica.org/congress/v1/members/senate/" +state+"/api-key=FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji/current.json"

    headers = {
        'x-api-key': "FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji",
        'cache-control': "no-cache",
        'postman-token': "84558452-50c3-23a9-85f7-e1db4c66735f"
    }

    response = requests.request("GET", url, headers=headers)
    return response.json()
    # if resp.status_code != 200:
    #     print('Something went wrong'.format(resp.status_code))
    # else:
    #     # print("This is the json")
    #     return resp.json()

