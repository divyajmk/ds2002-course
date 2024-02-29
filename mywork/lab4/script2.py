#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3


import boto3
import requests 
import urllib.request

# Prompt User for Input 
url = input("Enter your URL: ")

# File to save the URL
# Used a gif file like it said in the instructions
filename = 'downloaded_file.gif'
# Documentation used: https://docs.python.org/3/howto/urllib2.html
urllib.request.urlretrieve(url, filename)

bucket = 'ds2002-yaq7fm'
filepath = 'projects/downloaded_file.gif'

# Create Client 
s3 = boto3.client('s3', region_name="us-east-1")

# Upload File to S3
# Documentation: https://www.pythonforbeginners.com/files/with-statement-in-python
with open(filename, 'rb') as f:
# Use ACL parameter to make the URL public 
# Use ContentType parameter to prevent the image from being downloaded when link is clicked
# (I was having that issue)
         s3.put_object(
                Body = f,
                Bucket = bucket,
                Key = filepath,
                ACL = 'public-read',
                ContentType = 'image/gif')

# Create URL
# Variables as stated in the lab description 
bucket_name = bucket
object_name = filepath
expires_in = 604800


presigned_url = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': object_name},
                ExpiresIn=expires_in)

print(presigned_url)

# Output of URL
# This link works in the learner lab, but it does not work now.
# This issue has been acknowledged
#https://ds2002-yaq7fm.s3.amazonaws.com/projects/downloaded_file.gif?AWSAccessKeyId=ASIAU6GDY6IJRTIQAZWF&Signature=2cx7XM20UuFaLKdMcEsQzwfW4Aw%3D&x-amz-security-token=FwoGZXIvYXdzEAsaDIIzhVnY%2FYfEqytvCSLEAVsl8iWl9yr6QgsbT3EH%2FqOZRg9FeeZfKNExNp7KkmFMfzxHS7O44t%2F1unSJ%2FNzmr6UcpXcquKYVTDn1dQEoD10PproDKO5S2Rsli8A7%2Brqwn2E90XHIPV3rMTnI%2BPR7lYIMBIoOnrmZOUpK3AYMAg%2FkZBSnX4pOSJhqN5X5eRfO1TGNRpgzEPleeUg3foVHriJMuyIHX0JuLjkm695PT%2B1tWRIC1%2Fzvi%2BKPm2tSeyUnSgIDE3Nuo7h933O%2Big89MSYjDfEow5T6rgYyLfPLRFMvwEV4tPGpWkqWfG2zKMcS30Ka%2BV%2F%2BPk4mScJWiKuHBI%2BAgKzwC%2BgwsA%3D%3D&Expires=1709688261

