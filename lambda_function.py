import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-stats')

def lambda_handler(event, context):
    # 1. Get the current 'views' from the item with id '0'
    response = table.get_item(Key={'id': '0'})
    views = response['Item']['views']
    
    # 2. Increment the views
    views = views + 1
    
    # 3. Save the new count back to DynamoDB
    table.put_item(Item={'id': '0', 'views': views})
    
    # 4. Return the updated count to our website

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',  # This is the "Magic" line
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'views': int(views)})
    }

