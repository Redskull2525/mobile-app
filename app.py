import streamlit as st
import numpy as np
import pickle

# ------------------------------
# Load the trained model
# ------------------------------
model_path = "best_ml.pkl"  # change if your file has a different name
with open(model_path, "rb") as file:
    model = pickle.load(file)

# ------------------------------
# Streamlit App UI
# ------------------------------
st.title("📱 Mobile Price Range Prediction App")
st.write("Predict the price range (0 = Low, 1 = Medium, 2 = High, 3 = Very High) based on mobile specifications.")

st.sidebar.header("Enter Mobile Specifications")

# Input fields
battery_power = st.sidebar.number_input("Battery Power (mAh)", 500, 5000, 2000)
blue = st.sidebar.selectbox("Bluetooth", [0, 1])
clock_speed = st.sidebar.number_input("Clock Speed (GHz)", 0.1, 3.0, 1.5)
dual_sim = st.sidebar.selectbox("Dual SIM", [0, 1])
fc = st.sidebar.number_input("Front Camera (MP)", 0, 20, 5)
four_g = st.sidebar.selectbox("4G Supported", [0, 1])
int_memory = st.sidebar.number_input("Internal Memory (GB)", 2, 256, 32)
m_dep = st.sidebar.number_input("Mobile Depth (cm)", 0.1, 1.0, 0.5)
mobile_wt = st.sidebar.number_input("Mobile Weight (g)", 50, 300, 150)
n_cores = st.sidebar.slider("Number of Cores", 1, 8, 4)
pc = st.sidebar.number_input("Primary Camera (MP)", 0, 25, 10)
px_height = st.sidebar.number_input("Pixel Height", 0, 2000, 800)
px_width = st.sidebar.number_input("Pixel Width", 0, 2000, 1200)
ram = st.sidebar.number_input("RAM (MB)", 256, 8000, 3000)
sc_h = st.sidebar.number_input("Screen Height (cm)", 5, 20, 10)
sc_w = st.sidebar.number_input("Screen Width (cm)", 0, 20, 5)
talk_time = st.sidebar.number_input("Talk Time (hours)", 2, 20, 10)
three_g = st.sidebar.selectbox("3G Supported", [0, 1])
touch_screen = st.sidebar.selectbox("Touch Screen", [0, 1])
wifi = st.sidebar.selectbox("WiFi Supported", [0, 1])

# Collect inputs into array
features = np.array([[battery_power, blue, clock_speed, dual_sim, fc, four_g,
                      int_memory, m_dep, mobile_wt, n_cores, pc, px_height,
                      px_width, ram, sc_h, sc_w, talk_time, three_g,
                      touch_screen, wifi]])

# ------------------------------
# Prediction
# ------------------------------
if st.button("🔍 Predict Price Range"):
    prediction = model.predict(features)[0]
    st.success(f"Predicted Price Range: **{prediction}**")

    # Optional descriptive message
    ranges = ["Low Cost", "Medium Cost", "High Cost", "Very High Cost"]
    st.info(f"This mobile is predicted to be in the **{ranges[prediction]}** category.")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and Machine Learning")
