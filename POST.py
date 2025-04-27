import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Extract AppName and Status from the request body
    body = json.loads(event.get('body', '{}'))
    print(body)
    app_name = body.get('AppName')
    status = body.get('Status')

    # Validation: Check if both AppName and Status are provided
    if not app_name or not status:
        return {
            'statusCode': 400,
            "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"},
            'body': json.dumps({'error': 'Both AppName and Status are required'})
        }

    # Specify the DynamoDB table name
    table_name = 'appliance'
    table = dynamodb.Table(table_name)

    try:
        # Check if the item with the given AppName exists
        response = table.get_item(
            Key={'AppName': app_name}
        )

        if 'Item' in response:
            # If the item exists, return it
            return {
                'statusCode': 200,
                "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"},
                'body': json.dumps({'message': 'Item already exists', 'item': response['Item']})
            }
        else:
            # If the item does not exist, create it
            table.put_item(
                Item={
                    'AppName': app_name,
                    'Status': status
                }
            )
            return {
                'statusCode': 201,
                 "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"},
                'body': json.dumps({'message': 'New item created successfully'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"},
            'body': json.dumps({'error': str(e)})
        }
