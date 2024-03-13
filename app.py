import streamlit as st


resume = None
cover_letter = None
writing_style = None

st.title("Howdy! :wave: Let's get you that internship you've been losing sleep over asap :briefcase: ...")

with st.sidebar:
    st.subheader("Cover letter generator")
    with st.form(key='my_form',border=False):
        page = st.text_input(
            label='Provide link to internship details page',
            max_chars= 70
        )

        style = st.selectbox(
            'What style do you want the essay in?',
            ('Formal', 'Conversational','Confident','Storytelling', 'Inspirational','Custom'),
            key='cover letter style'
            )

        if style == 'Custom':
            style_document = st.file_uploader(
                label='Please upload style guide:', 
                accept_multiple_files=True
                )


        user_address = st.text_area(

            label="Enter your address",
            max_chars=50
        )

        company_address = st.text_area(
            label='Enter the recepient address',
            max_chars=50
        )

        button = st.form_submit_button(label='Generate Cover Letter')



st.subheader("Resume")

resume = st.file_uploader(label="Let me in on some of the cool stuff you've done")


st.subheader("Cover Letter")


has_cover_letter = st.selectbox(
    'Do you have a cover letter',
    ('No','Yes'),
    placeholder=" "
)

if has_cover_letter == 'Yes':
    cover_letter = st.file_uploader(label='Please upload your cover letter')
else:
    cover_letter = False

st.subheader("Writing Style")


writing_style = st.selectbox(
        'What style do you want your essays, cover letter and resume in?',
        ('Formal', 'Conversational','Confident','Storytelling', 'Inspirational','Custom')
        )

if writing_style == 'Custom':
    essay_style_document = st.file_uploader(
        label='Please upload a sample PDF of the writing style:', 
        accept_multiple_files=True,
        key='essay style'
        )



respond_button = None
essay_response = None


st.subheader('Anything else I should know about you?')

configuration_status = st.selectbox(
    label="Don't be shy. I don't bite :hatching_chick: ... I think  :japanese_goblin:",
    options= ('All good','I left something out')
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





    


