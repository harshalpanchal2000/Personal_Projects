import textblob
import streamlit as st

def senti(text):
    analysis = textblob.TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"
    
def main():
    st.title("Text Sentiment Analysis Tool")
    user_input = st.text_area("Enter the text you want to analyze:")
    
    if st.button("Analyze Sentiment"):
        sentiment = senti(user_input)
        st.write(f"Sentiment Analysis Result: {sentiment}")

if __name__ == "__main__":
    main()
