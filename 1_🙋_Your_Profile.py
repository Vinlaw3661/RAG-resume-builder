import streamlit as st


resume = None
cover_letter = None
writing_style = None
internship_link = None
has_cover_letter = None
cover_letter = None
respond_button = None
essay_response = None


st.title("Howdy! :wave: Let's get you that internship you've been losing sleep over...")

st.subheader("Internship :necktie:")
internship_link = st.text_input('Enter link to the internship details page')

st.subheader("Resume :medal:")
resume = st.file_uploader(label="Let me in on some of the cool stuff you've done")


st.subheader("Cover Letter :bookmark_tabs:")
has_cover_letter = st.selectbox(
    'Bragged about yourself already?',
    (None,'Yes','No'),
    placeholder=" "
)

if has_cover_letter == 'Yes':
    cover_letter = st.file_uploader(label='Please upload your cover letter')
else:
    cover_letter = False


st.subheader("Writing Style :pencil2:")
writing_style = st.selectbox(
        'What style do you want your essays, cover letter and resume in?',
        (None,'Unamused 😒 (not recommended)','Formal 🧑‍💼', 'Conversational 💬','Confident 😤','Storytelling 📖', 'Inspirational 🤩','Custom 🔨')
        )

if writing_style == 'Custom 🔨':
    essay_style_document = st.file_uploader(
        label='Please upload a sample PDF of the writing style:', 
        accept_multiple_files=True,
        key='essay style'
        )



st.subheader('Anything else I should know about you? 🪞')
configuration_status = st.selectbox(
    label="Don't be shy. I don't bite :hatching_chick:",
    options= (None,'We all good','I left something out')
)

if configuration_status == 'I left something out':

    st.write('What else would you like to share?')

    addional_info_text = st.text_area(
        'Tell me more about yourself',
        placeholder='Hopefully something interesting')
    
    st.write(
        '###### Orr.....'
        )

    addional_info_docs = st.file_uploader('Upload more files for context',accept_multiple_files=True)

    if addional_info_text or addional_info_docs:

        proceed_button= st.button(
            label="Let's proceed :rocket:"
        )
else:
    if configuration_status:
        proceed_button= st.button(
            label="Let's proceed :rocket:"
        )





    


