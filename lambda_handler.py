#This lambda function is triggered on the insert of Dynamodb table 'DynamoKaps'.
#The lambda function in turn, inserts the details of the received record data in to a new Dynamodb table InductionList table.


import json
import logging
import boto3

# Locate the dynamodb table into which we will insert the new value
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('InductionList')

def lambda_handler(event, context):
    # Fetch the new records inserted into dynamodb
    for record in event['Records']:
        NewEMP = {
                'EmpID': record['dynamodb']['NewImage']['EmpID']['S'],
                'EmpName': record['dynamodb']['NewImage']['EmpName']['S']
            }
        print('New REC: ' + record['dynamodb']['NewImage']['EmpID']['S'], record['dynamodb']['NewImage']['EmpName']['S'])
        print('Book: ' + json.dumps(NewEMP, indent=2))
        
		#Let us put the received information from new dynamodb record into new dynamodb table
        table.put_item(
          Item={
              'id':record['dynamodb']['NewImage']['EmpID']['S'], #Make sure the id is defined as String Key
              'Welcome Statement': 'Welcome Mr. ' + record['dynamodb']['NewImage']['EmpName']['S']
            })
            
        print('End of Lambda function')