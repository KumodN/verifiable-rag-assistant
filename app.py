import streamlit as st
from src.rag_engine import query_rag

st.set_page_config(page_title="Vault-AI | Secure Banking", page_icon="🔒")
st.title("Vault-AI: Commercial Lending System")
st.caption("SECURE TERMINAL | RESTRICTED ACCESS | AUTH: LOCALHOST")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask a question about your document..."):
    
    # User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI Response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing document..."):
            
            response_data = query_rag(prompt)
            answer = response_data["answer"]
            sources = response_data["sources"]

            st.markdown(answer)
            
            if sources:
                with st.expander("View Verified Sources"):
                    for i, doc in enumerate(sources):
                        page_num = doc.metadata.get("page", "Unknown")
                        source_text = doc.page_content.replace("\n", " ")
                        
                        st.markdown(f"**Source {i+1} (Page {page_num})**")
                        st.info(f"...{source_text[:300]}...")
    
    st.session_state.messages.append({"role": "assistant", "content": answer})