import streamlit as st
import random

st.title("✨ Kids Story Generator (Offline) ✨")
st.write("Create fun, short stories for children without an API key!")

# Inputs
character = st.text_input("Main character (e.g., dragon, princess, robot):")
setting = st.text_input("Story setting (e.g., forest, space, castle):")
moral = st.text_input("Moral of the story (optional):")

# Story templates
templates = [
    "Once upon a time, there was a {character} who lived in a {setting}. One day, they discovered a magical secret that changed everything. In the end, they learned that {moral}.",
    "In a faraway {setting}, a brave {character} set out on an adventure. Along the way, they met new friends and faced challenges. Finally, they realized that {moral}.",
    "A cheerful {character} loved exploring the {setting}. After a surprising adventure, they discovered the importance of {moral}.",
]

# Button
if st.button("Generate Story"):
    if character and setting:
        chosen_template = random.choice(templates)
        story = chosen_template.format(
            character=character,
            setting=setting,
            moral=moral if moral else "kindness and friendship"
        )

        st.subheader("Your Story:")
        st.write(story)
    else:
        st.warning("Please enter both a character and a setting.")
