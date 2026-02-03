import json
import boto3

def lambda_handler(event, context):
    location = event['queryStringParameters']['location']
    interest = event['queryStringParameters']['interest']

    events = [
        {"name": "Music Concert", "location": location, "interest": interest},
        {"name": "Tech Meetup", "location": location, "interest": interest}
    ]

    return {
        "statusCode": 200,
        "body": json.dumps(events),
        "headers": {"Content-Type": "application/json"}
    }
