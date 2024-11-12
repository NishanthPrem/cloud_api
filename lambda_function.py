import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-api-db')

def lambda_handler(event, context):
    try:
        # Query DynamoDB table with the key "id" set to "resume"
        response = table.get_item(Key={'id': 'resume'})
        
        # Check if the item exists in the response
        if 'Item' in response:
            item = response['Item']
            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps("Item not found")
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error retrieving data: {str(e)}")
        }
