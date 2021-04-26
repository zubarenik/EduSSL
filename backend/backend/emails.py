from string import Template

import boto3
from botocore.exceptions import ClientError
from backend.settings import API

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
