"""API応答用のjsonオブジェクトを生成するユーティリティ
"""
import json

def gen_response(code, body):
    """汎用的なレスポンスを生成する

    Args:
        code: httpステータスコード
        body: レスポンスボディ

    Returns:
        jsonレスポンスオブジェクト

    Note:
        ヘッダは付加されない。
    """
    return {
        'statusCode': code,
        'body': json.dumps(body)
    }

def gen_200(result):
    """gen_response(200, {'result': result})
    """
    return gen_response(200, {'result': result})
def gen_400(message = 'Bad request'):
    """gen_response(400, {'message': message})
    """
    return gen_response(400, {'message': message})

def gen_request_event(value):
    """テスト用のリクエストを生成する

    Args:
        value (int): fib関数に渡す値
    Returns:
        aws.lambda.event
    """
    return {
        'path': '/fib',
        'httpMethod': 'GET',
        'queryStringParameters': {'n': f"{value}"}
    }
