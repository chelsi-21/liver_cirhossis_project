import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Liver Cirrhosis Predictor", layout="centered")

model = pickle.load(open('model.pkl', 'rb'))

st.markdown("""
<style>
.stApp {
    background-color: #f5f9ff;
    color: black;
}
h1 {
    text-align: center;
    color: #0b7285;
}
.stButton>button {
    background-color: #20c997;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
[data-testid="stSidebar"] {
    background-color: #e7f5ff;
    color: black;
}
</style>
""", unsafe_allow_html=True)

st.title("🩺 Liver Cirrhosis Prediction App")

st.markdown("### 👋 Welcome!")
st.write("Enter patient details to predict liver health risk.")

st.markdown("---")

st.sidebar.title("📘 Parameter Info")

st.sidebar.markdown("""
**Bilirubin:** High level may indicate liver damage.  
**Albumin:** Low level indicates poor liver function.  
**Platelets:** Low count may indicate liver disease.
""")

st.subheader("🧾 Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age *", min_value=0, value=0)
    bilirubin = st.slider("Bilirubin Level", 0.0, 10.0, 1.0)

with col2:
    albumin = st.slider("Albumin Level", 1.0, 5.5, 4.0)
    platelets = st.slider("Platelet Count", 50, 500, 250)

st.markdown("---")

if st.button("🔍 Predict"):

    if age == 0:
        st.toast("⚠️ Please enter your age before prediction", icon="⚠️")

    else:
        input_data = np.array([[age, bilirubin, albumin, platelets]])
        prediction = model.predict(input_data)

        st.subheader("📊 Result")

        if prediction[0] == 0:
            st.error("⚠️ High Risk of Liver Cirrhosis")

            st.markdown("### 🩺 Health Tips:")
            st.write("1. Eat fresh fruits and vegetables 🥦")
            st.write("2. Drink warm lemon water 🍋")
            st.write("3. Avoid oily food 🍔")
            st.write("4. Include turmeric & garlic 🧄")
            st.write("5. Sleep properly 😴")

        else:
            st.success("✅ Low Risk of Liver Cirrhosis")

st.markdown("---")
