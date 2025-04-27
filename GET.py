import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Extract appliance name from query parameters
    AppName =  event['pathParameters']['AppName']
    print(AppName)

    if not AppName:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',  # CORS header
                'Access-Control-Allow-Methods': 'GET'
            },
            'body': json.dumps({'error': 'Appliance name is required'})
        }

    # Specify the DynamoDB table name
    table = dynamodb.Table('appliance')

    try:
        # Fetch the item from DynamoDB
        response = table.get_item(
            Key={
                'AppName': AppName
            }
        )
        # print(response)
        item = response.get('Item', None)
        print(item)
        
        if item != None:
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',  # CORS header
                    'Access-Control-Allow-Methods': 'GET'
                },
                'body': json.dumps(item)
            }
        else:
            print(response)
            return {
                'statusCode': 404,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',  # CORS header
                    'Access-Control-Allow-Methods': 'GET'
                },
                'body': json.dumps({'error': 'Item not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',  # CORS header
                'Access-Control-Allow-Methods': 'GET'
            },
            'body': json.dumps({'error': str(e)})
        }
