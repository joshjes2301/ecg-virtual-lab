import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

st.title("❤️ ECG Virtual Lab")

menu = st.sidebar.selectbox("Select Section", 
                           ["Aim", "Theory", "Experiment", "Quiz", "Feedback"])

if menu == "Aim":
    st.header("🎯 Aim")
    st.write("To calculate heart rate from ECG signal using peak detection.")

elif menu == "Theory":
    st.header("📚 Theory")
    st.write("""
    ECG records electrical activity of the heart.
    Peaks (R-peaks) help calculate heart rate.
    """)

elif menu == "Experiment":
    st.header("🧪 Experiment")
    uploaded_file = st.file_uploader("Upload ECG CSV", type=["csv"])

    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        ecg = data.iloc[:,0]

        fig, ax = plt.subplots()
        ax.plot(ecg)
        st.pyplot(fig)

        peaks, _ = find_peaks(ecg, distance=50)
        ax.plot(peaks, ecg[peaks], "rx")
        st.pyplot(fig)

        bpm = (len(peaks)/len(ecg))*100*60
        st.success(f"Heart Rate: {int(bpm)} BPM")

elif menu == "Quiz":
    st.header("📝 Quiz")
    q = st.radio("ECG measures?",
                 ["Blood pressure","Heart electrical activity","Oxygen"])

    if st.button("Submit"):
        if q == "Heart electrical activity":
            st.success("Correct!")
        else:
            st.error("Wrong")

elif menu == "Feedback":
    st.header("💬 Feedback")
    name = st.text_input("Name")
    fb = st.text_area("Feedback")

    if st.button("Send"):
        st.success("Thank you!")
