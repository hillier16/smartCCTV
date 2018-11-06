import boto3

s3 = boto3.client('s3', region_name='ap-northeast-2')
# # S3 bucket create
# s3.create_bucket(Bucket='sound-highlight', CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-2'})

# S3 bucket listing
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List: %s" % buckets)

 # S3 file upload
bucket_name = 'smartcctv'
file_name = '1.py'
s3.upload_file(file_name, bucket_name, file_name)
