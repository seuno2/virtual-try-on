import boto3

def upload_images(s3, bucket_name, object_name, cloth_path, edge_path, person_path, output_path):
    s3.put_object(Bucket=bucket_name, Key=object_name)

    s3.upload_file(cloth_path, bucket_name, object_name + cloth_path.split("/")[-1]) 
    s3.upload_file(edge_path, bucket_name, object_name + edge_path.split("/")[-1])
    s3.upload_file(person_path, bucket_name, object_name + person_path.split("/")[-1])
    s3.upload_file(output_path, bucket_name, object_name + output_path.split("/")[-1])
    