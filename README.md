# Chat with PDF using LLaMA 3.1

## Table of Contents
- [Project Overview.](#project-overview)
- [Task Performed.](#task-performed)
- [Requirements.](#requirements)
- [How to Use It.](#how-to-use-it)
- [Results.](#results)
- [Hugging Face Deployment.](#hugging-face-deployment)

---

## Project Overview:
The **Chat with PDF using LLaMA 3.1** project is a Streamlit application designed to enable users to interact with PDF content. The application offers:
1. PDF upload and content extraction.
2. Summarized sections of the PDF.
3. Question-based interaction with detailed answers using LLaMA 3.1.

This app integrates powerful NLP capabilities, leveraging the Hugging Face Transformers library to enhance user interaction.

---

## Task Performed:

### 1) **Importing Libraries:**
- The necessary libraries for the project were imported, including `streamlit` for creating the web app, `transformers` for the natural language processing model, `PyPDF2` for PDF text extraction, and `openai` for leveraging LLaMA 3.1 for Q&A.
- Libraries for handling user interactions and creating dynamic interfaces were also imported, including `os` and `io`.

### 2) **Building the Streamlit Web Interface:**
- **UI Components:**
  - A file uploader was created to allow users to upload PDF documents for processing.
  - Input fields were designed to take user queries for generating answers based on the PDF content.
  - The output interface was designed to display the results of the text extraction and model-generated responses.

- **User Interaction:**
  - Users can upload PDF files, and the app will read the document content.
  - The app also provides a text area where users can type questions about the PDF content, which is processed by the model to generate detailed answers.

### 3) **PDF Text Extraction:**
- **PDF Processing:**
  - PDFs are processed using the `PyPDF2` library to extract textual content.
  - Each page's text is extracted and concatenated to create a unified text string that can be passed to the model.
  - The text is cleaned to remove any unwanted characters and formatted for easy processing.

### 4) **Text Processing and Summarization:**
- **LLaMA 3.1 Integration:**
  - The extracted text from the PDF is fed into the LLaMA 3.1 model, which performs natural language understanding tasks such as text summarization and question answering.
  - The model is fine-tuned on PDF content to generate concise summaries and relevant answers for user queries.
  - For efficiency, the app ensures that large PDFs are broken down into smaller sections for processing to avoid performance issues.

### 5) **Question Answering Functionality:**
- **User Query Handling:**
  - When a user inputs a question related to the uploaded PDF, the query is passed to the LLaMA 3.1 model, which uses the context from the PDF to provide an accurate response.
  - The model retrieves relevant information from the document and generates context-aware answers, ensuring that users receive precise information based on the PDF's content.

### 6) **Displaying Results:**
- **Output Display:**
  - The app dynamically updates with the generated summary of the PDF after processing, followed by the response to the user query.
  - Results are displayed in a clear, readable format to ensure users can easily interact with the output.

### 7) **Error Handling and UI Feedback:**
- **User-Friendly Design:**
  - The app includes basic error handling for cases where users upload unsupported file types or if the model fails to generate an output.
  - Clear instructions are provided to guide users on how to upload PDFs and input questions.
  
### 8) **Performance Optimization:**
- **Optimizing Speed and Responsiveness:**
  - The PDF text extraction process and model inference were optimized to minimize delays.
  - The app caches frequently used results to improve the overall response time when interacting with the same documents.

### 9) **Hugging Face Deployment:**
- After testing locally, the app was deployed to Hugging Face Spaces, making it publicly accessible.
- The deployment allows anyone to upload PDFs, interact with the model, and receive responses instantly, making it an efficient tool for quick document-based question answering.

### Summary of Task Performed:
The project integrates a PDF document processing pipeline using Streamlit, allowing users to upload PDFs, extract text, and interact with the content via a question-answering system powered by LLaMA 3.1. The process involves building a user-friendly interface, extracting and processing PDF text, and using advanced language models to generate summaries and detailed answers to user queries. The app was then deployed on Hugging Face Spaces, enabling global access to this interactive tool.


---

## Requirements:
To run the project, ensure the following dependencies are installed in your Python environment:

```plaintext
streamlit==1.25.0
transformers==4.35.0
PyPDF2==3.0.1
torch==2.0.1
sentence-transformers==2.2.2
```

## How to Use It
### Upload a PDF File:
Use the file uploader to select and upload the PDF file you wish to analyze. The file should be in .pdf format.

### Text Extraction:
The application extracts the text from the uploaded PDF using the PyMuPDF library (imported as fitz).

### Text Chunking:
Large documents are divided into smaller chunks for better processing. Each chunk contains up to 1000 characters.

### Ask Questions:
After the text is processed, type your question about the document.

### Model Response:
The app sends the prompt and the relevant chunk to the model, which generates a response based on the content.

### Receive Insights:
Get detailed insights and answers related to the PDF content.

## Hugging Face Deployment:
The application is deployed on Hugging Face Spaces, making it accessible to users for seamless interaction. You can access the live demo of the PDF chat application and try it out directly by visiting the link below:

## Results:
The application successfully allows users to extract content from uploaded PDF files, provides concise summaries of the content, and enables detailed question-and-answer interaction. This functionality is powered by the pre-trained LLaMA 3.1 model, ensuring accurate and contextually relevant responses.

### Screenshots:
- **Uploaded PDF Content Summarization:**
  The application processes the uploaded PDF and generates a structured summary of its contents, making it easy for users to understand key points at a glance.
  ![Screenshot 2024-11-21 181931](https://github.com/user-attachments/assets/5b1aa773-adc6-4e97-874d-73ce1a908c49)
  
- **Q&A with Extracted Content:**
  Users can ask specific questions about the PDF's content, and the app provides detailed, context-aware answers based on the extracted text.
  ![Screenshot 2024-11-21 181944](https://github.com/user-attachments/assets/1aa605ae-4249-41af-897e-d065e1428f18)


- [Chat with PDF using LLaMA 3.1 on Hugging Face](https://huggingface.co/spaces/Anuj02003/Chat_with_pdf_using_llama3.1)
  
This deployment allows users to upload PDFs, generate summaries, and interact with the content via a question-answering system powered by the LLaMA 3.1 model. It's designed to be user-friendly and demonstrates the capabilities of the model in a practical setting.


