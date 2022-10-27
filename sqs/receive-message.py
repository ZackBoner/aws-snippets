#!/usr/bin/python3
import boto3
import botocore
from botocore.exceptions import ClientError
import warnings
warnings.filterwarnings("ignore")


sqs = boto3.client('sqs')
qurl = 'https://queue.amazonaws.com/051801205735/cs4740'


def check_message_count(qurl):
    try:
        response = sqs.get_queue_attributes(
            QueueUrl=qurl,
            AttributeNames=['All']
        )
        # print(response)
        messages = int(response['Attributes']['ApproximateNumberOfMessages'])
        print(messages)
        return messages > 0
    except ClientError as e:
        print(e)

def delete_message(qurl, handle):
    try:
        response = sqs.delete_message(
            QueueUrl=qurl,
            ReceiptHandle=handle
        )
        # print(response)
    except ClientError as e:
        print(e)

# Receive a message from the queue
def receive_message(qurl):
    try:
        if check_message_count(qurl):
            response = sqs.receive_message(
                QueueUrl=qurl,
                MaxNumberOfMessages=1,
            )
        else:
            print("No messages in queue")
            return None
        # print(response)
        BODY = response["Messages"][0]["Body"]
        print(BODY)
        HANDLE = response["Messages"][0]["ReceiptHandle"]
        # print(HANDLE)
        delete_message(qurl, HANDLE)
    except ClientError as e:
        print(e)

receive_message(qurl)