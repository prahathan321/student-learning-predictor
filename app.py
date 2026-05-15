import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression

# ---------------- PAGE SETUP ---------------- #

st.set_page_config(
    page_title="Student Learning Predictor",
    page_icon="🎓",
    layout="centered"
)

# Background Style
st.markdown("""
<style>
.stApp {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    color: #333333;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.title("🎓 Student Learning Predictor")
st.write("AI Powered Student Performance Prediction System")

# ---------------- LOGIN ---------------- #

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# ---------------- LOGIN CHECK ---------------- #

if username == "pragal" and password == "2006":

    st.success("Login Successful ✅")

    # ---------------- CSV UPLOAD ---------------- #

    uploaded_file = st.file_uploader(
        "Upload Student CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        # Read CSV
        data = pd.read_csv(uploaded_file)

        # Display Dataset
        st.subheader("📄 Uploaded Dataset")
        st.dataframe(data)

        # ---------------- MACHINE LEARNING ---------------- #

        # Input and Output
        X = data[['StudyHours', 'Attendance', 'Assignment']]
        y = data['Result']

        # Train Model
        model = LogisticRegression()
        model.fit(X, y)

        # ---------------- USER INPUT ---------------- #

        st.subheader("📘 Enter Student Details")

        study = st.slider(
            "Study Hours",
            0,
            12,
            5
        )

        attendance = st.slider(
            "Attendance %",
            0,
            100,
            75
        )

        assignment = st.slider(
            "Assignment Marks",
            0,
            100,
            70
        )

        # ---------------- PREDICTION ---------------- #

        if st.button("Predict Result"):

            # Predict
            result = model.predict([
                [study, attendance, assignment]
            ])

            # Probability
            probability = model.predict_proba([
                [study, attendance, assignment]
            ])

            # Result Display
            st.success(
                f"Predicted Result: {result[0]}"
            )

            # Confidence Score
            st.subheader("📈 Prediction Confidence")

            if result[0] == "Pass":

                st.write(
                    f"{probability[0][1] * 100:.2f}%"
                )

            else:

                st.write(
                    f"{probability[0][0] * 100:.2f}%"
                )

            # Animation
            st.balloons()

        # ---------------- ANALYTICS ---------------- #

        st.subheader("📊 Student Analytics")

        # Line Graph
        fig, ax = plt.subplots()

        ax.plot(
            data['Attendance'],
            label='Attendance'
        )

        ax.plot(
            data['Assignment'],
            label='Assignment'
        )

        ax.legend()

        st.pyplot(fig)

        # ---------------- PIE CHART ---------------- #

        st.subheader("🥧 Pass vs Fail Analysis")

        pass_count = (
            data['Result'] == 'Pass'
        ).sum()

        fail_count = (
            data['Result'] == 'Fail'
        ).sum()

        labels = ['Pass', 'Fail']
        sizes = [pass_count, fail_count]

        fig2, ax2 = plt.subplots()

        ax2.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%'
        )

        st.pyplot(fig2)

else:

    if username != "" or password != "":

        st.error(
            "Invalid Username or Password ❌"
        )
