import streamlit as st
import uuid
from api_client import APIClient

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Knowledge Assistant")

#st.write("Welcome to your AI assistant!")

client = APIClient()

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

for chat_message in st.session_state.messages:
    with st.chat_message(chat_message["role"]):
        st.write(chat_message["content"])

prompt = st.chat_input("Ask something")


if prompt:

    # Save and display user message immediately
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)
    try: 
        # Show assistant placeholder
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = client.chat(
                    session_id=st.session_state.session_id,
                    message=prompt
                )

                st.write(response["response"])

        # Save assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response["response"]
        })
    except Exception as e:
        st.error(f"Error: {e}")    
    st.rerun()
#st.write(response["response"])

with st.sidebar:
    st.header("Settings")

    st.header("Knowledge Base")
    uploaded_file = st.file_uploader("Upload a document",type=["pdf", "docx", "txt"])
    if uploaded_file is not None:
        with st.spinner("Uploading document..."):
            result = client.upload_document(uploaded_file)
        st.success(result["message"])

        st.text_area(
            "Extracted Text",
            result["text"],
            height=300
        )
        
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()
