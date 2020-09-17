import boto3
s3 = boto3.client('s3')
s3.download_file(
  'data-lake-for-analytics', 
  'external_summary_tables/push_turn_off_training_records/features/turned_off_features_v1.snappy.parquet', 
  'dataset/turned_off_features_v1.snappy.parquet'
)