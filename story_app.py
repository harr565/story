import streamlit as st
import openai

# Configure API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("✨ Kids' Story Generator ✨")
st.write("Create fun, short stories for children!")

# User inputs
theme = st.selectbox("Choose a theme:", ["Animals", "Space", "Friendship", "Adventure", "Magic"])
age_group = st.selectbox("Select age group:", ["3-5 years", "6-8 years", "9-12 years"])
length = st.slider("Story length (words):", 50, 300, 150)

if st.button("Generate Story"):
    prompt = f"Write a short, fun, age-appropriate story for kids aged {age_group}. " \
             f"The theme is {theme}. Keep it under {length} words, with a happy ending."

    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use GPT-4 if available
        prompt=prompt,
        max_tokens=length,
        temperature=0.8
    )

    story = response.choices[0].text.strip()
    st.subheader("Your Story:")
    st.write(story)
