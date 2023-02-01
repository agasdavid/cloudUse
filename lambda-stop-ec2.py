import boto3

def lambda_handler(event, context):
    # Connect to the EC2 service
    ec2 = boto3.client('ec2')
    
    # Get the list of instances to be stopped/started
    instances = ['instance-id-1', 'instance-id-2']
    
    # Stop or start the instances
    if event['action'] == 'stop':
        ec2.stop_instances(InstanceIds=instances)
        print(f"Stopped instances: {instances}")
    else:
        ec2.start_instances(InstanceIds=instances)
        print(f"Started instances: {instances}")
        
    return {
        'statusCode': 200,
        'body': 'Success'
    }