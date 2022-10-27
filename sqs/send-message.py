#!/usr/bin/python3
import boto3
import botocore
from botocore.exceptions import ClientError
import warnings
warnings.filterwarnings("ignore")


sqs = boto3.client('sqs')
qurl = 'https://queue.amazonaws.com/051801205735/cs4740'

# Send a message to the queue
def send_message(qurl, message):
    try:
        response = sqs.send_message(
            QueueUrl=qurl,
            MessageBody=message
        )
        print(response)
    except ClientError as e:
        print(e)

message = "Howdy cs4740 partners!"
send_message(qurl, message)