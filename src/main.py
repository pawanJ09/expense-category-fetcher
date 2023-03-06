import json
import os


def lambda_handler(event, context):
    try:
        event_body = json.loads(event['body'])
        print(f'Incoming API Gateway Message: {event_body}')
        event_path = json.loads(event['path'])
        event_http_method = json.loads(event['httpMethod'])
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