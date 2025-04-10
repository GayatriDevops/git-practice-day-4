import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')  # Change region if needed

    try:
        response = ec2.run_instances(
            ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID
            InstanceType='t2.micro'
            KeyName='aws-key',  # Replace with your EC2 key pair name
            MinCount=1,
            MaxCount=1,
            SecurityGroupIds=['sg-0123456789abcdef0'],  # Replace with your security group ID
            SubnetId='subnet-0123456789abcdef0',  # Replace with your subnet ID
            
