# import json
# import boto3

# # Initialize DynamoDB resource
# dynamodb = boto3.resource('dynamodb')

# def lambda_handler(event, context):
#     # Extract AppName and Status from the request body
#     body = json.loads(event.get('body', '{}'))
#     app_name = body.get('AppName')
#     status = body.get('Status')
#     print('AppName',app_name,'Status',status)

#     # Validation: Check if both AppName and Status are provided
#     if not app_name or not status:
#         return {
#             'statusCode': 400,
#             'body': json.dumps({'error': 'Both AppName and Status are required'})
#         }

#     # Specify the DynamoDB table name
#     table_name = 'appliance'
#     table = dynamodb.Table(table_name)
#     print("passed")


#     try:
#         # Check if the item with the given AppName exists
#         response = table.get_item(
#             Key={'AppName': app_name}
#         )

#         if 'Item' not in response:
#             return {
#                 'statusCode': 404,
#                 'body': json.dumps({'error': 'Item with AppName not found'})
#             }

#         # Update the Status attribute
#         table.update_item(
#             Key={'AppName': app_name},
#             UpdateExpression='SET #st = :status',
#             ExpressionAttributeNames={'#st': 'Status'},
#             ExpressionAttributeValues={':status': status}
#         )

#         return {
#             'statusCode': 200,
#             'body': json.dumps({'message': 'Status updated successfully'})
#         }

#     except Exception as e:
#         return {
#             'statusCode': 500,
#             'body': json.dumps({'error': str(e)})
#         }


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
                "Access-Control-Allow-Headers": "Content-Type",
            },
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

        if 'Item' not in response:
            return {
                'statusCode': 404,
                "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",},
                'body': json.dumps({'error': 'Item with AppName not found'})
            }

        # Update the Status attribute
        table.update_item(
            Key={'AppName': app_name},
            UpdateExpression='SET #st = :status',
            ExpressionAttributeNames={'#st': 'Status'},
            ExpressionAttributeValues={':status': status}
        )

        return {
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            'body': json.dumps({'message': 'Status updated successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            'body': json.dumps({'error': str(e)})
        }
