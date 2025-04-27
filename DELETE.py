import json
import boto3
from botocore.exceptions import ClientError

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'appliance'  # Replace with your DynamoDB table name
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Extract the AppName from the path parameters
    try:
        AppName = event['pathParameters']['AppName']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'AppName is required in the path parameters'})
        }

    try:
        # Check if the item exists
        response = table.get_item(
            Key={
                'AppName': AppName  # Replace 'AppName' with your partition key name
            }
        )
        print("GetItem response:", response)

        # If item is not found, return a 404 error
        if 'Item' not in response:
            return {
                'statusCode': 404,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "DELETE, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type",
                },
                'body': json.dumps({'message': 'Item not found'})
            }

        # If the item exists, proceed to delete it
        delete_response = table.delete_item(
            Key={
                'AppName': AppName
            }
        )
        print("DeleteItem response:", delete_response)

        return {
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            'body': json.dumps({'message': 'Item deleted successfully'})
        }

    except ClientError as e:
        # Handle DynamoDB client errors
        print("DynamoDB ClientError:", e.response['Error']['Message'])
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            'body': json.dumps({'error': e.response['Error']['Message']})
        }
    except Exception as e:
        # Catch any other exceptions and print them
        print("Exception:", str(e))
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            'body': json.dumps({'error': 'Internal server error: ' + str(e)})
        }
