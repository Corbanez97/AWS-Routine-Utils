import json
from orchestrator import Orchestrator
 
def lambda_handler(event, context):
    orchestrator = Orchestrator(event) #Here the event is the routine_config.json
    orchestrator.run_executors()
    return {
        'statusCode': 200,
        'body': json.dumps('Routine Successfully Executed')
    }
