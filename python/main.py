import streamlit as st
import pandas as pd
import plotly.express as px
import json

#Website Logo
st.image("2.png", width=200)  # Display the logo

#Navigation Menu
st.sidebar.title("Navigation")
goal = st.sidebar.selectbox("Fitness Goal", ["Lose Weight", "Gain Muscle", "Maintain Weight"])
menu = st.sidebar.selectbox("Select Page", ["Home", "Online Nutritionist Appointment", "Tips"])

#Personal Details Form
st.sidebar.title("Personal Details")
name = st.sidebar.text_input("Enter Your Name")
age = st.sidebar.number_input("Age", min_value=15, max_value=80, value=25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
activity = st.sidebar.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active"])

# Save User Data
DATA_FILE = "user_data.json"

def load_data():
    """Load user data from a JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    """Save user data to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

user_data = load_data()

if st.sidebar.button("Save Details"):
    user_data.update({
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "activity": activity,
        "goal": goal
})
    save_data(user_data)
    st.sidebar.success("Details Saved!")

#Home Page
if menu == "Home":
    st.title(f" Fauji Fit Nation - Welcome {name}!")

    # BMI Calculator
    st.subheader("Body Mass Index (BMI) Calculator")
    bmi = weight / ((height / 100) ** 2)
    st.metric(label="Your BMI", value=f"{bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight - Consider gaining weight!")
    elif 18.5 <= bmi < 25:
        st.success("Healthy weight - Keep it up!")
    elif 25 <= bmi < 30:
        st.warning("Overweight - Consider losing weight!")
    else:
        st.error("Obese - Focus on weight loss!")

    # Weight Tracking
    st.subheader(" Weight Tracking")
    if "weight_log" not in user_data:
        user_data["weight_log"] = []

    new_weight = st.number_input("Enter today's weight (kg)", min_value=30, max_value=200, value=weight)
    if st.button("Log Weight"):
        user_data["weight_log"].append({"weight": new_weight, "day": len(user_data["weight_log"]) + 1})
        save_data(user_data)
        st.success("Weight logged!")

    if user_data["weight_log"]:
        df = pd.DataFrame(user_data["weight_log"])
        fig = px.line(df, x="day", y="weight", title="Weight Progress")
        st.plotly_chart(fig, use_container_width=True)

# Diet Plan
    st.subheader("🍽 Diet Plan Based on BMI")
    if bmi < 18.5:
        st.write("🔹 Weight Gain Diet: Increase calorie intake with high-protein and carb-rich foods.")
        st.write("Suggested Dietitian: [Abraham The Pharmacist](https://www.youtube.com/@AbrahamThePharmacist)")
        st.write("[Ramadan Weight Gain Diet Plan](https://youtu.be/NH84Di_sCuA?si=f4KlfL1WQ3-IjIDz)")
        st.write("[Full Day Eating for Weight Gain](https://youtu.be/zpJLoBUzinM?si=3OKha1LxVVEONPZI)")
    elif bmi >= 25:
        st.write("🔹 Weight Loss Diet: Reduce calorie intake, eat more protein, fiber, and healthy fats.")
        st.write("Suggested Dietitian: [Dr. Ayesha Nasir](https://www.youtube.com/@AyeshaNasir)")
        st.write("[Ramzan Diet Plan](https://youtu.be/9wohNfJLwwI?si=_QCGR7_FGTXAZHLy)")
        st.write("[OMAD Diet Plan](https://youtu.be/LV9fkrozn24?si=jGgGuIEYKQ0CBHH0)")
    else:
        st.write("🔹 Maintain Weight: Eat balanced meals with moderate calories.")

# Exercise Plan
    st.subheader("🏃 Exercise Plan")
    st.write("Create your own exercise plan for Home or Gym based on your fitness goal.")
    st.write("[Home Workout](https://youtu.be/UIPvIYsjfpo?si=FhG3DwQyrG84LIuj)")
    st.write("[Full Body Gym Workout](https://youtu.be/eTxO5ZMxcsc?si=2Cdnvj-5UbHpSfil)")

# Calorie Calculator
    st.subheader("🔥 Calorie Calculator")
    activity_multipliers = {"Sedentary": 1.2, "Light": 1.375, "Moderate": 1.55, "Active": 1.725}
    bmr = 10 * weight + 6.25 * height - 5 * age + (5 if gender == "Male" else -161)
    daily_calories = bmr * activity_multipliers[activity]
    st.write(f"💡 Calories needed per day: {daily_calories:.0f} kcal")
# Motivation
    st.subheader("💡 Motivation")
    if goal == "Lose Weight":
        st.info("Remember: 1 kg weight loss = 7700 calorie deficit!")
    elif goal == "Gain Muscle":
        st.info("Keep pushing! Muscle growth takes consistency and effort.")
    else:
        st.info("Stay active and keep a balanced diet for long-term fitness.")

# Contact Us (Toggle Button)
    st.write("Developed by Usman Ali & G. Muhammad")

# Initialize session state for contact visibility
    if "show_contacts" not in st.session_state:
        st.session_state.show_contacts = False

# Toggle contact visibility on button click
    if st.button("Contact Us"):
        st.session_state.show_contacts = not st.session_state.show_contacts
# Display contacts
    if st.session_state.show_contacts:
        st.write("📞 Usman Ali: +923363894558")
        st.write("📞 G. Muhammad: +923133483167")
        st.write("📧 Usman Ali: usmanalipirzada1122@gmail.com")
        st.write("📧 G. Muhammad: ghulammuhammadmirani9@gmail.com")

#Online Nutritionist Appointment page
elif menu == "Online Nutritionist Appointment":
    st.subheader("👨‍⚕ Book an Online Nutritionist Appointment")
    st.write("Find the best nutritionists in Pakistan for an online consultation:")
    st.markdown("- [InstaCare - Online Nutritionists](https://instacare.pk/appointments/nutritionist)")
    st.markdown("- [Oladoc - Book a Nutritionist](https://oladoc.com/pakistan/lahore/nutritionist)")
    st.markdown("- [Sehat Kahani - Online Dietitian Consultation](https://sehatkahani.com)")
    st.markdown("- [Marham - Find & Book Nutritionists](https://www.marham.pk/doctors/nutritionist)")
    st.markdown("- [Dawaai - Online Nutritionist Consultation](https://dawaai.pk/healthcare-services/online-consultation/nutritionist)")

#Tips Page
elif menu == "Tips":
    st.subheader("💡 Fitness Tips")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Weight Gain Tips"):
            st.write("1. Eat more calories than you burn.")
            st.write("2. Consume protein-rich foods like chicken, fish, and eggs.")
            st.write("3. Strength train regularly with progressive overload.")
            st.write("4. Drink high-calorie smoothies and shakes.")
            st.write("5. Eat every 3-4 hours to maintain a surplus.")
            st.write("6. Incorporate healthy fats like nuts and olive oil.")
            st.write("7. Get enough sleep for muscle recovery.")
            st.write("8. Avoid excessive cardio, focus on resistance training.")
            st.write("9. Stay hydrated but don't drink too much before meals.")
            st.write("10. Track your progress and adjust accordingly.")
    with col2:
        if st.button("Weight Loss Tips"):
            st.write("1. Eat in a calorie deficit to lose weight.")
            st.write("2. Increase protein intake to preserve muscle.")
            st.write("3. Perform strength training to boost metabolism.")
            st.write("4. Incorporate HIIT workouts for fat burning.")
            st.write("5. Drink plenty of water and stay hydrated.")
            st.write("6. Reduce sugar and processed food intake.")
            st.write("7. Get at least 7-9 hours of quality sleep.")
            st.write("8. Practice mindful eating and portion control.")
            st.write("9. Stay active throughout the day, take the stairs.")
            st.write("10. Track your meals and progress for accountability.")