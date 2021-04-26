from string import Template

import boto3
from botocore.exceptions import ClientError
from backend.settings import API

SENDER = "courses@edu.skillslab.center"
AWS_REGION = "us-east-2"
CHARSET = "UTF-8"

client = boto3.client('ses',
                      region_name=AWS_REGION,
                      aws_access_key_id='AKIAJQKRNB3M3PRFVHQA',
                      aws_secret_access_key='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')

def send_email(email, course):
    with open('static/uploads/emails/body.html') as file:
        lines = file.read()
    text = Template(lines)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': text.substitute(title=course.title,
                                                date=course.date_started,
                                                body=course.email_text,
                                                api=API + '/static/uploads/emails')
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': course.title,
                },
            },
            Source=SENDER,

        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
