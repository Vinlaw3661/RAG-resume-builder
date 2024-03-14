import streamlit as st


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role'], avatar= '🧑' if message['role'] == 'user' else '🚀'):
        st.markdown(message['content'])


user_query  = st.chat_input('Ask anything', max_chars= 4000)


if user_query:
    st.session_state.messages.append({'role':'user', 'content':user_query})
    with st.chat_message('user', avatar='🧑'):
        st.markdown(user_query)


    assistant_response = 'Hello'


    if assistant_response:
        st.session_state.messages.append({'role':'assistant', 'content':assistant_response})
        with st.chat_message('assistant', avatar="🚀"):
            st.markdown(assistant_response)



def clear_chat():
    st.session_state.messages = []
    st.markdown('')

clear_button = st.button(
    label="Clear Chat",
    on_click=clear_chat
)





