import streamlit as st
from transformers import pipeline
import fitz  # PyMuPDF for PDF handling
import re
import tempfile

# Function to clean extracted text
def clean_text(text):
    # Replace multiple spaces or newlines with a single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Function to extract text from PDF and clean it
def extract_text_from_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    doc = fitz.open(tmp_file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    return clean_text(text)

# Function to chunk large text for context
def chunk_text(text, max_length=1000):
    # Split the text into chunks with a maximum character length
    chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
    return chunks

# Initialize Hugging Face model pipeline
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2", clean_up_tokenization_spaces=True)  # Use GPT-2 for simplicity

model_pipeline = load_model()

# Generate a response
# Generate a response
def get_response(prompt, context):
    combined_prompt = f"Context: {context}\n\nQuestion: {prompt}\nAnswer:"
    response = model_pipeline(
        combined_prompt,
        max_new_tokens=150,  # Ensure concise answers
        num_return_sequences=1
    )
    # Extract only the answer part after the "Answer:" in the generated response
    raw_response = response[0]["generated_text"]
    answer_start = raw_response.find("Answer:") + len("Answer:")
    answer = raw_response[answer_start:].strip()
    return clean_text(answer)


# Streamlit App UI
st.title("Chat with PDF!!!")

# Sidebar for description
st.sidebar.title("Instructions")
st.sidebar.markdown("""
    ### How to Use This Application:
    1. **Upload a PDF File**:  
       Use the file uploader to select and upload the PDF file you wish to analyze. The file should be in `.pdf` format.
    
    2. **Text Extraction**:  
       The application extracts the text from the uploaded PDF using the `PyMuPDF` library (imported as `fitz`).

    3. **Text Chunking**:  
       Large documents are divided into smaller chunks for better processing. Each chunk contains up to 1000 characters.

    4. **Ask Questions**:  
       After the text is processed, type your question about the document.

    5. **Model Response**:  
       The app sends the prompt and the relevant chunk to the model, which generates a response based on the content.

    6. **Receive Insights**:  
       Get detailed insights and answers related to the PDF content.
""")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Extract and clean text from the uploaded PDF
    pdf_text = extract_text_from_pdf(uploaded_file)
    
    # Chunk the extracted text
    text_chunks = chunk_text(pdf_text)
    
    # Display the first chunk as a summary
    st.subheader("PDF Content Summary:")
    st.write(text_chunks[0])  # Display first chunk
    
    # Input for user prompt
    prompt = st.text_area(label="Ask a question based on the PDF content")
    button = st.button("Ok")
    
    if button:
        if prompt:
            # Select relevant chunk based on the question
            relevant_chunk = None
            for chunk in text_chunks:
                if any(keyword.lower() in chunk.lower() for keyword in prompt.split()):
                    relevant_chunk = chunk
                    break

            # If no relevant chunk was found, use the first chunk as a fallback
            if not relevant_chunk:
                relevant_chunk = text_chunks[0]

            # Get response from the model
            response = get_response(prompt, relevant_chunk)
            st.markdown(f"**Answer:** {response}")
