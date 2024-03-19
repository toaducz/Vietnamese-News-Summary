import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import io
import tuoitre
import Vnexpress
import vietnamnet

# Load tokenizer and model outside of the main function

tokenizer1 = AutoTokenizer.from_pretrained("toanduc/vit5-base-vietnews-summarization-sport")
model1 = AutoModelForSeq2SeqLM.from_pretrained("toanduc/vit5-base-vietnews-summarization-sport")

# Use st.cache to cache the results of perform_summarization function
def perform_summarization(sentence):
    inputs = tokenizer1.encode("summarize: " + str(sentence), return_tensors="pt", max_length=4096, truncation=True)
    summary_ids1 = model1.generate(inputs, max_length=512, length_penalty=1.0, num_beams=5 ,early_stopping=True)
    print(summary_ids1)
    summary_text_t5 = tokenizer1.decode(summary_ids1[0], skip_special_tokens=True)
    
    summarized_text = summary_text_t5

    return summarized_text

def main():
    st.title("Dự án CNTT")
    
    # Chọn phương thức nhập liệu từ người dùng
    input_method = st.radio("Chọn Phương Thức Nhập:", ("Nhập Link", "Nhập Tay"))

    if input_method == "Nhập Link":
        # Widget để nhập link
        link_input = st.text_input("Nhập đường link:", "")

        if "https://" in link_input:
            if "https://www.bongda.com.vn/" in link_input:
                text_input = str(tuoitre.crawl_bongda_content(link_input))
                st.write(text_input)
            # if "https://thanhnien.vn/" in link_input:
            #     text_input = str(tuoitre.crawl_tuoitre_content(link_input))
            #     st.write(text_input)
            if "https://vnexpress.net/" in link_input:
                text_input = str(Vnexpress.extract_content(link_input))
                st.write(text_input)
            if "https://vietnamnet.vn/" in link_input:
                text_input = str(vietnamnet.extract_content(link_input))
                st.write(text_input)
        else:
            st.warning("Vui lòng nhập một đường link hợp lệ")
            return
    else:
        # Widget để nhập văn bản
        text_input = st.text_area("Nhập văn bản cần tóm tắt:", "")

    if st.button("Tóm Tắt"):
        # Gọi hàm tóm tắt văn bản ở đây (thay bằng code thực hiện tóm tắt)
        summarized_text = perform_summarization(text_input)

        # Hiển thị kết quả tóm tắt
        st.subheader("Kết Quả Tóm Tắt:")
        st.write(summarized_text)

if __name__ == "__main__":
    main()