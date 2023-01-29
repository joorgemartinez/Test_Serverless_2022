project_id = server-376217
bucket-name = edem-serverless-bucket2



gcloud builds submit --tag 'gcr.io/server-376217/dataflow/edem:latest' .


gcloud dataflow flex-template build "gs://edem-serverless-bucket2/dataflowtemplate.json" \
  --image "gcr.io/server-376217/dataflow/edem:latest" \
  --sdk-language "PYTHON" 



gcloud dataflow flex-template run "edem-dataflow-job3" \
    --template-file-gcs-location "gs://edem-serverless-bucket2/dataflowtemplate.json" \
    --region "europe-west1"



python edemDeviceData.py \
    --algorithm RS256 \
    --cloud_region europe-west1 \
    --device_id edemDevice \
    --private_key_file rsa_private.pem \
    --project_id server-376217 \
    --registry_id edemRegistry