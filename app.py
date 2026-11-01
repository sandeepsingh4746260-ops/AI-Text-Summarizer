
# Import Required Libraries

import streamlit as st
from openai import OpenAIError

from utils.groq import GroqSummaryError, generate_summary, get_api_error_message
from utils.pdf_reader import extract_text_from_pdf



# Page Configuration

st.set_page_config(
    page_title="AI Text Summarizer",
    layout="centered"
)



# Application Header

st.title("AI Text Summarizer")

st.markdown("""
### Summarize long text into **3 concise bullet points**
""")

st.divider()



# PDF Upload Section

st.caption(
    "Paste your article, blog, notes, email or any paragraph below."
)

st.subheader("📂 Upload PDF (Optional)")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)





# If user uploads a PDF,

# extract its text and display basic information.

if uploaded_file is not None:

    st.success("✅ PDF Uploaded Successfully")

    pdf_text = extract_text_from_pdf(uploaded_file)

    st.write(f"Characters in PDF : {len(pdf_text)}")

st.markdown("### OR")

# Text Input Section

user_input = st.text_area(
    label="Enter your text",
    placeholder="Paste your text here...",
    height=200
)


# Display character count of typed text

character_count = len(user_input)

st.write(f"Characters : {character_count}")



# Summarize Button

summarize_btn = st.button(
    "Summarize",
    use_container_width=False,
    type="primary"
)



# Summary Output Section

st.subheader("📋 Summary")

summary_box = st.container(border=True)



# Generate Summary

if summarize_btn:

    # Check if user has provided

    # either text or PDF

    if uploaded_file is None and not user_input.strip():

        st.warning("⚠ Please enter text or upload a PDF.")

    else:

        with st.spinner("Generating summary..."):

            # Select input source

            if uploaded_file is not None:

                input_text = pdf_text

            else:

                input_text = user_input

            # Generate AI summary

            try:
                summary = generate_summary(input_text)
            except OpenAIError as error:
                st.error(
                    f"Could not generate summary: {get_api_error_message(error)}"
                )
            except (ValueError, GroqSummaryError) as error:
                st.error(f"Could not generate summary: {error}")
            else:
                summary_box.markdown(summary)



# Information Message

st.info(
    "💡 Tip: Best results are achieved with paragraphs containing at least 100 words."
)