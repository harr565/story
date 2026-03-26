import streamlit as st
import openai

# Configure your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("✨ Kids Story Generator ✨")
st.write("Create fun, short stories for children!")

# User inputs
character = st.text_input("Main character (e.g., dragon, princess, robot):")
setting = st.text_input("Story setting (e.g., forest, space, castle):")
moral = st.text_input("Moral of the story (optional):")

if st.button("Generate Story"):
    if character and setting:
        prompt = f"Write a short, fun, and age-appropriate story for kids. \
The main character is a {character}, the setting is {setting}. \
Make it engaging, simple, and end with a positive message. \
Moral: {moral if moral else 'Friendship and kindness'}."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.8
        )

        story = response.choices[0].message["content"]
        st.subheader("Your Story:")
        st.write(story)
    else:
        st.warning("Please enter both a character and a setting.")
