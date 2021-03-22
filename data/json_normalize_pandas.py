import re
import json
import pandas as pd
import datetime

     
data = '''{
  "accounts": [
    {
      "_id": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_item": "KdDjmojBERUKx3JkDd9RuxA5EvejA4SENO4AA",
      "_user": "eJXpMzpR65FP4RYno6rzuA7OZjd9n3Hna0RYa",
      "balance": {
        "available": 7205.23,
        "current": 7205.23
      },
      "institution_type": "fake_institution",
      "meta": {
        "name": "Plaid Premier Checking",
        "number": "5204"
      },
      "subtype": "checking",
      "type": "depository"
    }
  ],
  "transactions": [
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "3mg4qV4JZycjewvKEzrLTYMzdr1MmvcO4Z3zX",
      "amount": 240,
      "date": "2018-07-21",
      "name": "Online Transfer from External Sav ...3092",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Account Transfer"
      ],
      "category_id": "21001000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "0AZ0De04KqsreDgVwM1RSRYjyd8yXxSDQ8Zxn",
      "amount": 200,
      "date": "2018-07-21",
      "name": "ATM Withdrawal",
      "meta": {
        "location": {
          "city": "San Francisco",
          "state": "CA"
        }
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Withdrawal",
        "ATM"
      ],
      "category_id": "21012002",
      "score": {
        "location": {
          "city": 1,
          "state": 1
        },
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "eJXpMzpR65FP4RYno6yjhBDxgkM6pXC9RKM9o4",
      "amount": -1042.44,
      "date": "2018-07-16",
      "name": "Company Payroll",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Payroll"
      ],
      "category_id": "21009000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "eJXpMzpR65FP4RYno6yjhBDxgkM6pXC9RKM9o4",
      "amount": -1042.44,
      "date": "2018-07-02",
      "name": "Company Payroll",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Payroll"
      ],
      "category_id": "21009000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "KdDjmojBERUKx3JkDdO5IaRJdZeZKNuK4bnKJ1",
      "amount": 2307.15,
      "date": "2018-06-23",
      "name": "Apple Store",
      "meta": {
        "location": {
          "address": "1 Stockton St",
          "city": "San Francisco",
          "state": "CA"
        }
      },
      "pending": false,
      "type": {
        "primary": "place"
      },
      "category": [
        "Shops",
        "Computers and Electronics"
      ],
      "category_id": "19013000",
      "score": {
        "location": {
          "address": 1,
          "city": 1,
          "state": 1
        },
        "name": 0.2
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "DAE3Yo3wXgskjXV1JqBDIrDBVvjMLDCQ4rMQdR",
      "amount": 3.19,
      "date": "2018-06-21",
      "name": "Gregorys Coffee",
      "meta": {
        "location": {
          "address": "874 Avenue of the Americas",
          "city": "New York",
          "state": "NY"
        }
      },
      "pending": false,
      "type": {
        "primary": "place"
      },
      "category": [
        "Food and Drink",
        "Restaurants",
        "Coffee Shop"
      ],
      "category_id": "13005043",
      "score": {
        "location": {
          "address": 1,
          "city": 1,
          "state": 1
        },
        "name": 0.2
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "eJXpMzpR65FP4RYno6yjhBDxgkM6pXC9RKM9o4",
      "amount": -1042.44,
      "date": "2018-06-15",
      "name": "Company Payroll",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Payroll"
      ],
      "category_id": "21009000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "1vAj1Eja5BIn4R7V6Mp1hBPQgkryZRHryZ0rDY",
      "amount": 80,
      "date": "2018-06-08",
      "name": "ATM Withdrawal",
      "meta": {
        "location": {
          "city": "San Francisco",
          "state": "CA"
        }
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Withdrawal",
        "ATM"
      ],
      "category_id": "21012002",
      "score": {
        "location": {
          "city": 1,
          "state": 1
        },
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "zq7MLAM4N3cjeKvXP9YqtBJXvZeajJCkjQakYv",
      "amount": -240,
      "date": "2018-06-02",
      "name": "Online Transfer from Chk ...1702",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Account Transfer"
      ],
      "category_id": "21001000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "eJXpMzpR65FP4RYno6yjhBDxgkM6pXC9RKM9o4",
      "amount": -1042.44,
      "date": "2018-06-01",
      "name": "Company Payroll",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Payroll"
      ],
      "category_id": "21009000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "96d5AO5gLjC9EowVyn5OCBRjJR9LaOHJnBVJzd",
      "amount": 240,
      "date": "2018-06-01",
      "name": "Online Transfer to Sav ...9606",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Account Transfer"
      ],
      "category_id": "21001000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "VK0EQ5Ea13u9Qwzm6nA8CNaze8gdJoCJvx6JDO",
      "amount": -0.93,
      "date": "2018-05-17",
      "name": "Interest Payment",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "unresolved"
      },
      "category": [
        "Interest"
      ],
      "category_id": "15000000",
      "score": {
        "location": {},
        "name": 0.2
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "eJXpMzpR65FP4RYno6yjhBDxgkM6pXC9RKM9o4",
      "amount": -1042.44,
      "date": "2018-05-15",
      "name": "Company Payroll",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Payroll"
      ],
      "category_id": "21009000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "aJPEm5EVqxF6yk8K5nPeFbDpnPR57wI3xMR3pP",
      "amount": 12.74,
      "date": "2018-05-12",
      "name": "Golden Crepes",
      "meta": {
        "location": {
          "address": "262 W 15th St",
          "city": "New York",
          "coordinates": {
            "lat": 40.740352,
            "lon": -74.001761
          },
          "state": "NY"
        }
      },
      "pending": false,
      "type": {
        "primary": "place"
      },
      "score": {
        "location": {
          "address": 1,
          "city": 1,
          "state": 1
        },
        "name": 0.2
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "moPE4dE1yMHJX5pmRzwrcvpQqPdDnZHEKPREYL",
      "amount": 7.23,
      "date": "2018-05-09",
      "name": "Krankies Coffee",
      "meta": {
        "location": {
          "address": "211 E 3rd St",
          "city": "Winston Salem",
          "state": "NC"
        }
      },
      "pending": false,
      "type": {
        "primary": "place"
      },
      "category": [
        "Food and Drink",
        "Restaurants",
        "Coffee Shop"
      ],
      "category_id": "13005043",
      "score": {
        "location": {
          "address": 1,
          "city": 1,
          "state": 1
        },
        "name": 0.2
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "eJXpMzpR65FP4RYno6yjhBDxgkM6pXC9RKM9o4",
      "amount": -1042.44,
      "date": "2018-05-01",
      "name": "Company Payroll",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Payroll"
      ],
      "category_id": "21009000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "P1xJboJA5Ls31gJrMQEBU5dZD3NmPrH5R6g5jL",
      "amount": 118.23,
      "date": "2018-04-26",
      "name": "Banana Republic",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "digital"
      },
      "category": [
        "Shops",
        "Digital Purchase"
      ],
      "category_id": "19019000",
      "score": {
        "location": {},
        "name": 0.2
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "dRBp95pEwZfMXENvpw3YHY43VNK4LVSP7RkPpA",
      "amount": -800,
      "date": "2018-04-20",
      "name": "Venmo Cashout 18375552",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Third Party",
        "Venmo"
      ],
      "category_id": "21010001",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "moPE4dE1yMHJX5pmRzwrcvpkxdopLxtEKPREYo",
      "amount": 120,
      "date": "2018-04-19",
      "name": "Venmo Payment 16991172",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Third Party",
        "Venmo"
      ],
      "category_id": "21010001",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "eJXpMzpR65FP4RYno6yjhBDxgkM6pXC9RKM9o4",
      "amount": -1042.44,
      "date": "2018-04-17",
      "name": "Company Payroll",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Payroll"
      ],
      "category_id": "21009000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "JmN0JX0q5EcaQJM9ZbOwUYyyp607m4u3PR63Vn",
      "amount": 5.32,
      "date": "2018-04-17",
      "name": "Octane Coffee Bar and Lounge",
      "meta": {
        "location": {
          "address": "1009 Marietta St Nw # B",
          "city": "Atlanta",
          "state": "GA"
        }
      },
      "pending": false,
      "type": {
        "primary": "place"
      },
      "category": [
        "Food and Drink",
        "Restaurants",
        "Coffee Shop"
      ],
      "category_id": "13005043",
      "score": {
        "location": {
          "address": 1,
          "city": 1,
          "state": 1
        },
        "name": 0.2
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "4r0aBVa85Kt3BDPk10a4U5OD3XKjE7Hzxpez6B",
      "amount": 28.57,
      "date": "2018-04-11",
      "name": "Papa Johns Pizza",
      "meta": {
        "location": {
          "address": "2625 David Dr",
          "city": "Metairie",
          "coordinates": {
            "lat": 29.999986,
            "lon": -90.21869
          },
          "state": "LA",
          "zip": "70003"
        }
      },
      "pending": false,
      "type": {
        "primary": "place"
      },
      "category": [
        "Food and Drink",
        "Restaurants",
        "Pizza"
      ],
      "category_id": "13005012",
      "score": {
        "location": {
          "address": 1,
          "city": 1,
          "state": 1,
          "zip": 1
        },
        "name": 0.2
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "eJXpMzpR65FP4RYno6yjhBDxgkM6pXC9RKM9o4",
      "amount": -1042.44,
      "date": "2018-04-03",
      "name": "Company Payroll",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Payroll"
      ],
      "category_id": "21009000",
      "score": {
        "location": {},
        "name": 1
      }
    },
    {
      "_account": "XARE85EJqKsjxLp6XR8ocg8VakrkXpTXmRdOo",
      "_id": "eJXpMzpR65FP4RYno6yjhBDxgkM6pXC9RKM9o3",
      "amount": -1042.44,
      "date": "2018-03-27",
      "name": "Company Payroll",
      "meta": {
        "location": {}
      },
      "pending": false,
      "type": {
        "primary": "special"
      },
      "category": [
        "Transfer",
        "Payroll"
      ],
      "category_id": "21009000",
      "score": {
        "location": {},
        "name": 1
      }
    }
  ],
  "access_token": "test"
}
'''

# deserialize string to object->dict, array->list, etc
obj = json.loads(data)
txns = obj.get('transactions')

# txns_str = json.dumps(txn)
# df = pd.read_json(txns_str)

df = pd.json_normalize(txns)

headers = df.columns
print(headers.to_list())

df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
df['day'] = pd.DatetimeIndex(df['date']).day
df['month_year'] = pd.DatetimeIndex(df['date']).strftime('%Y-%m')

select_cols = ['date', 'amount', 'year', 'month', 'day', 'month_year']

print(df[select_cols])

cond = df['amount'] == -1042.44
print(df.loc[cond][select_cols])

# get all unique values of a column
print(df['type.primary'].unique())

result = df.groupby(['month_year']).sum()
res_cols = ['amount']
print(result[res_cols])        # include month_year columns
#              amount
# month_year         
# 2018-03    -1042.44
# 2018-04    -2612.76
# 2018-05    -2065.84
# 2018-06      305.46
# 2018-07    -1644.88

# json_data = df.to_json(orient='records')
# parsed = json.loads(json_data)
# print(json.dumps(parsed, indent=4))

# if txns is None:
#     print("None transaction")

# for t in txns:
#     if type(t) is dict:
#         print('is dict')
    
#     print(t.get("category"))
