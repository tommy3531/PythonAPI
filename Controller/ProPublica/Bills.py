import requests


def getBillDetails():
    jsonOfBillDetails = billDetails('115', 'hr2810')
    return jsonOfBillDetails


def billDetails(congress, bill_id):
    """ Congress 105-115 """
    specificBillURL = 'https://api.propublica.org/congress/v1'
    url = specificBillURL + "/" + congress + "/bills/" + bill_id + ".json"
    headers = {
        'x-api-key': 'FuMVFXTU3fJHtKTHC9v480ZXmampcvt6J0vzYBji'
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        print('Something went wrong'.format(response.status_code))
    else:
        return response.json()
