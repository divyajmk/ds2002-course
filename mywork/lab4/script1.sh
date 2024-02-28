#!/bin/bash 


# Fetch the image and Output to a new File
curl https://www.civitatis.com/f/brasil/rio-de-janeiro/tour-privado-rio-janeiro-589x392.jpg > brazil.jpg

# Upload file to bucket
aws s3 cp brazil.jpg s3://ds2002-yaq7fm/

# Create an expiring URL 
URL=$(aws s3 presign --expires-in 604800 s3://ds2002-yaq7fm/brazil.jpg)

# Output URL
echo $URL

# This is the URl that expires in 7 days (a week from 2/27/24)
https://ds2002-yaq7fm.s3.us-east-1.amazonaws.com/brazil.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAU6GDY6IJRTIQAZWF%2F20240228%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240228T012342Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEAsaDIIzhVnY%2FYfEqytvCSLEAVsl8iWl9yr6QgsbT3EH%2FqOZRg9FeeZfKNExNp7KkmFMfzxHS7O44t%2F1unSJ%2FNzmr6UcpXcquKYVTDn1dQEoD10PproDKO5S2Rsli8A7%2Brqwn2E90XHIPV3rMTnI%2BPR7lYIMBIoOnrmZOUpK3AYMAg%2FkZBSnX4pOSJhqN5X5eRfO1TGNRpgzEPleeUg3foVHriJMuyIHX0JuLjkm695PT%2B1tWRIC1%2Fzvi%2BKPm2tSeyUnSgIDE3Nuo7h933O%2Big89MSYjDfEow5T6rgYyLfPLRFMvwEV4tPGpWkqWfG2zKMcS30Ka%2BV%2F%2BPk4mScJWiKuHBI%2BAgKzwC%2BgwsA%3D%3D&X-Amz-Signature=d8e66b309555df839f5fa53d19b027e1a2b613e226af48137997b0f7377c603e

