import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == '/users':
            if payload == None:
                # for testing
                # return (self.database)
                return json.dumps(self.database)
            else:
                names = json.loads(payload)['users']
                names.sort()
                list_output = list(
                    filter(lambda user: user['name'] in names, self.database['users']))
                return json.dumps({"users": list_output})

    def post(self, url, payload=None):
        if url == '/add':
            name = json.loads(payload)['user']
            item_added = {"name": name, "owes": {},
                          "owed_by": {}, "balance": 0.0}
            self.database['users'].append(item_added)
            return json.dumps(item_added)
        if url == '/iou':
            iou = json.loads(payload)
            lender = iou['lender']
            borrower = iou['borrower']
            amount = iou['amount']
            # now look for lender and borrower and edit their entries
            # for this I will loop over all the elements
            for i in range(len(self.database['users'])):
                # Editing the lender
                if self.database['users'][i]['name'] == lender:
                    # checking if lender is already owed by the borrower
                    if borrower in self.database['users'][i]['owed_by'].keys():
                        self.database['users'][i]['owed_by'][borrower] += amount
                    # checking if lender owes borrower any money
                    elif borrower in self.database['users'][i]['owes'].keys():
                        # checking if lender owes borrower more than the current amount
                        if amount < self.database['users'][i]['owes'][borrower]:
                            self.database['users'][i]['owes'][borrower] -= amount
                        # checking if the current loan is equal to prior loans
                        elif amount == self.database['users'][i]['owes'][borrower]:
                            self.database['users'][i]['owes'].pop(borrower)
                        # checking if the current loan is greater than prior loans
                        else:
                            self.database['users'][i]['owed_by'][borrower] = amount - \
                                self.database['users'][i]['owes'][borrower]
                            self.database['users'][i]['owes'].pop(borrower)
                    # new loan between lender and borrower
                    else:
                        self.database['users'][i]['owed_by'][borrower] = amount
                    self.database['users'][i]['balance'] += amount
                # editing the borrower
                if self.database['users'][i]['name'] == borrower:
                    if lender in self.database['users'][i]['owes'].keys():
                        self.database['users'][i]['owes'][lender] += amount
                    elif lender in self.database['users'][i]['owed_by'].keys():
                        if amount < self.database['users'][i]['owed_by'][lender]:
                            self.database['users'][i]['owed_by'][lender] -= amount
                        elif amount == self.database['users'][i]['owed_by'][lender]:
                            self.database['users'][i]['owed_by'].pop(lender)
                        else:
                            self.database['users'][i]['owes'][lender] = amount - \
                                self.database['users'][i]['owed_by'][lender]
                            self.database['users'][i]['owed_by'].pop(lender)
                    else:
                        self.database['users'][i]['owes'][lender] = amount
                    self.database['users'][i]['balance'] -= amount
            iou_status = self.get(
                "/users", json.dumps({"users": [lender, borrower]}))
            return iou_status


# Testing
database = {
    "users": [
        {"name": "Adam", "owes": {}, "owed_by": {
            "Bob": 3.0}, "balance": 3.0},
        {"name": "Bob", "owes": {"Adam": 3.0},
         "owed_by": {}, "balance": -3.0},
    ]
}
# api = RestAPI(database)
# payload = json.dumps({"users": ["Bob", "Adam"]})
# response = api.get("/users", payload)
# print(response)
# print((api.get("/users")['users'][0]['owed_by']['Bob']))

# # # Useful links:
# # # <https://www.programiz.com/python-programming/json>
# # # has a conversion table for python data types --> json types
# # # <https://www.programiz.com/python-programming/json>
# # # has the reverse tables
# # # NOTE: Always remember to use `loads()` and `dumps()`, instead of `load()` and `dump()`
# # # In order to use one method in another you call it by using `self.method_name`. From StackOverflow: <https://stackoverflow.com/questions/25825693/calling-one-method-from-another-within-same-class-in-python>
