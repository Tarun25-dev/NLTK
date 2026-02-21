import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

st.title("Sentiment Analysis",text_alignment="center")
st.header("Text-Classification")
st.set_page_config(page_title="Text classifier",page_icon="👩‍⚖️")

@st.cache_resource # model trains only once
def train_model():
    data = pd.read_csv("./dataset/sentiment_dataset_1000.csv")
    # remove missing values
    data = data.dropna()
    x = data["text"]
    y = data["label"]
    # convert text to numbers 
    vectorizer = CountVectorizer()
    x_vectorized = vectorizer.fit_transform(x)
    # split dataset 
    x_train,x_test,y_train,y_test = train_test_split(x_vectorized,y,test_size=0.2,random_state=42)
    # train model
    model = MultinomialNB()
    model.fit(x_train,y_train)
    # calculate accuracy
    predictions = model.predict(x_test) # this predicts the 20% dataset that allocated and predicts it label.
    accuracy = accuracy_score(y_test,predictions) # that predictions can used to comapre with original labels in dataset for finding accuracy.
    return model,vectorizer,accuracy
# train once (cached)
model,vectorizer,accuracy = train_model() # we just call the function stored that returns in this three variables
# show accuracy on screen
st.write(f"model accuracy: {round(accuracy*100,2)}%") # round values we taken and we convert from 0 to 1 - 0% to 100% and 2 is for keep 2 decimal places.
# Text input box
user_input = st.text_area("Enter your text here:")
# button
if st.button("Predict"):
    if user_input.strip() != "":
        transformed_text = vectorizer.transform([user_input]) # we pass user input as list
        prediction = model.predict(transformed_text)[0] # why [0] beacuse it predicts a label and retuens in list and only one label is there that too in first element in list so indexx start from 0 we takes as [0]
        if prediction == 1:
            st.success(f"Prediction: 'Positive'")
            st.toast("predicted",duration=1)
        elif prediction == 0:
            st.warning(f"Prediction: 'Negative'")
            st.toast("predicted",duration=1)
    
    