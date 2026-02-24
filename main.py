import streamlit as st
from spellchecker import SpellChecker

# Initialize the SpellChecker
spell = SpellChecker()

def main():
    # Page configuration
    st.set_page_config(page_title="AI Spell Checker", page_icon="✍️")
    
    st.title("✍️ Spell Checker App")
    st.write("Type your text below to automatically correct spelling errors.")

    # User Input
    user_input = st.text_area("Enter text to check:", placeholder="Enter text here...")

    if user_input:
        words = user_input.split()
        corrected_words = []
        corrections_made = []

        # Process the text
        for word in words:
            # Clean punctuation for a better check
            clean_word = word.strip(".,!?()\"")
            corrected = spell.correction(clean_word)
            
            if corrected and corrected.lower() != clean_word.lower():
                corrections_made.append(f"**{clean_word}** → **{corrected}**")
                # Keep original punctuation if possible
                corrected_words.append(word.replace(clean_word, corrected))
            else:
                corrected_words.append(word)

        # Output Section
        st.subheader("Corrected Text:")
        result = " ".join(corrected_words)
        st.success(result)

        # Show a summary of changes
        if corrections_made:
            with st.expander("See list of corrections"):
                for item in corrections_made:
                    st.write(item)
        else:
            st.info("No spelling errors detected!")

if __name__ == "__main__":
    main()