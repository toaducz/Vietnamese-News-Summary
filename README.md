gcloud builds submit --tag gcr.io/duancntt-415907/streamlit  --project=duancntt-415907

gcloud builds submit --tag gcr.io/duancntt-415907/DuAnCNTT-demo --timeout=2h

gcloud docker -- push gcr.io/duancntt-415907DuAnCNTT-demo



gcloud run deploy --image gcr.io/duancntt-415907/streamlit --platform managed  --project=duancntt-415907 --allow-unauthenticated