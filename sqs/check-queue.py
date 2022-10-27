#!/usr/bin/python3

import boto3
import warnings
warnings.filterwarnings("ignore")


sqs = boto3.client('sqs')
qurl = 'https://queue.amazonaws.com/051801205735/cs4740'

response = sqs.get_queue_attributes(
    QueueUrl=qurl,
    AttributeNames=['All']
)
# print(response)
messages = response['Attributes']['ApproximateNumberOfMessages']
print(messages)
