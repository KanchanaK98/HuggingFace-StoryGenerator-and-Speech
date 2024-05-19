import streamlit as st
from app import imgtotext,textToStory,storyToSpeech
def main():
    st.set_page_config(page_title="Story Maker")
    st.header("Let's make a story...")
    uploaded_file = st.file_uploader("Choose an Image",type="jpg")

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name,"wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file,caption="Uploaded Image",use_column_width=True)
        with st.spinner('Processing...'):
            makeText = imgtotext(uploaded_file.name)
            story = textToStory(makeText)
            storyToSpeech(story)

        with st.expander("Text"):
            st.write(makeText)
        with st.expander("Story"):
            st.write(story)
        st.audio("audio.flac")




if __name__ == '__main__':
    main()