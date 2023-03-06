import json
import os


def lambda_handler(event, context):
    try:
        print(f'Incoming event: {event}')
        event_body = json.loads(event['body'])
        print(f'Incoming API Gateway Message: {event_body}')
        event_path = event['path']
        print(f'Incoming API Gateway Path: {event_path}')
        event_http_method = event['httpMethod']
        print(f'Incoming API Gateway HTTP Method: {event_http_method}')
    except Exception as e:
        msg = '\nProcessing error. Check Cloudwatch logs.'
        raise Exception(msg)


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    rel_path = '../events/test-agw-event.json'
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as f:
        test_event = json.load(f)
        lambda_handler(test_event, None)