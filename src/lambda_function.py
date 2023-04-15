"""AWS lambdaのエントリーポイント
"""

import json
from fibonacci import fib
from restutils import *

def lambda_handler(event, context):
    """AWS lambdaのエントリーポイント
   """
    path = event['path']
    method = event['httpMethod']
    params = event['queryStringParameters']

    if path == '/fib' and method == 'GET':
        return handler_fib(event, context, params)

def handler_fib(event, context, params):
    """AWS lambdaとfib関数とのグルーコード
   """
    try:
        n = int(params["n"])
        result = fib(n)
        return gen_200(result)
    except ValueError:
        return gen_400(f'n must be an integer more than 0 but got {params["n"]}.')
    except BaseException as e:
        print(e)
        return gen_400()
        
