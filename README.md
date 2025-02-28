Trang web tóm tắt bản tin thể thao chuyển nhượng tiếng việt, dataset được lấy từ ngày 30/12/2023 trở về trước

Link: https://duancntt.streamlit.app/ (Dead)

Chỉ cần nhập link của bài báo thể thao chuyển nhượng tiếng việt vào khung, trang web sẽ trả về bản tóm tắt và cố gắng giữ lại các tiêu chí sau:

-	cầu thủ
-	CLB liên quan, 
-	giá chuyển nhượng, 
-	chi tiết hợp đồng, 
-	lý do chuyển nhượng


(Chỉ mới hỗ trợ bongda.com.vn, https://vnexpress.net, https://vietnamnet.vn/, các trang khác vui lòng nhập nội dung thủ công)

 Streamlit run app.py

 -------------------------------------------------------------------------------------------
 

gcloud builds submit --tag gcr.io/duancntt-415907/streamlit  --project=duancntt-415907

gcloud builds submit --tag gcr.io/duancntt-415907/DuAnCNTT-demo --timeout=2h

gcloud docker -- push gcr.io/duancntt-415907DuAnCNTT-demo



gcloud run deploy --image gcr.io/duancntt-415907/streamlit --platform managed  --project=duancntt-415907 --allow-unauthenticated
