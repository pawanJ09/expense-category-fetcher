import json


def lambda_handler(event, context):
    try:
        event_body = json.loads(event['Records'][0]['body'])
        print(f'Incoming API Gateway Message: {event_body}')
        event_path = json.loads(event['Records'][0]['path'])
        event_http_method = json.loads(event['Records'][0]['httpMethod'])
    except Exception as e:
        msg = '\nProcessing error. Check Cloudwatch logs.'
        raise Exception(msg)


if __name__ == '__main__':
    lambda_handler(None, None)