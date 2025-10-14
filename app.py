import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

# =======================
# 🎨 Custom CSS Styling
# =======================
st.markdown("""
    <style>
        /* Global background */
        .stApp {
            background: linear-gradient(135deg, #e3f2fd, #f3e5f5);
            font-family: 'Poppins', sans-serif;
        }

        /* Title */
        h1 {
            color: #1e88e5;
            text-align: center;
            font-size: 40px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        /* Subtitle */
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #6c757d;
            margin-bottom: 30px;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 2px solid #90caf9;
        }

        /* Prediction box */
        .result-box {
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            background: white;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            margin-top: 20px;
        }

        /* Footer */
        footer {
            text-align: center;
            font-size: 14px;
            color: #757575;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)


# =======================
# 🧠 Load the Model
# =======================
MODEL_PATH = "best_model.pkl"
model = None

try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("❌ Model file 'best_model.pkl' not found! Please upload it in the same directory.")


# =======================
# 🏷️ App Title & Subtitle
# =======================
st.title("📱 Mobile Price Range Prediction App")
st.markdown('<p class="subtitle">Predict the price category of a smartphone using Machine Learning.</p>', unsafe_allow_html=True)


# =======================
# 📖 Sidebar Information
# =======================
st.sidebar.header("About this App")
st.sidebar.write("""
This web app predicts the **price range** of a smartphone  
based on its technical specifications using a trained ML model.
""")
st.sidebar.write("👨‍💻 **Developed by Abhishek**")
st.sidebar.markdown("[🌐 Visit my GitHub](https://github.com/AbhishekShelke)")


# =======================
# 📶 Connectivity Features
# =======================
st.subheader("📶 Connectivity Features")
col1, col2, col3 = st.columns(3)
with col1:
    blue = st.radio("Bluetooth", [1, 0], index=1, horizontal=True)
    dual_sim = st.radio("Dual SIM", [1, 0], index=1, horizontal=True)
with col2:
    four_g = st.radio("4G", [1, 0], index=1, horizontal=True)
    three_g = st.radio("3G", [1, 0], index=1, horizontal=True)
with col3:
    touch_screen = st.radio("Touch Screen", [1, 0], index=1, horizontal=True)
    wifi = st.radio("WiFi", [1, 0], index=1, horizontal=True)


# =======================
# 🧠 Performance Specs
# =======================
st.subheader("🧠 Performance Specs")
col1, col2, col3 = st.columns(3)
with col1:
    clock_speed = st.slider("Clock Speed (GHz)", 0.5, 3.0, 1.8)
with col2:
    ram = st.slider("RAM (MB)", 256, 8000, 4000, step=256)
with col3:
    int_memory = st.slider("Internal Memory (GB)", 2, 128, 32, step=2)

col4, col5, col6 = st.columns(3)
with col4:
    n_cores = st.slider("Number of Cores", 1, 8, 4)
with col5:
    talk_time = st.slider("Talk Time (hrs)", 2, 24, 10)
with col6:
    m_dep = st.slider("Mobile Depth (cm)", 0.1, 1.0, 0.5)


# =======================
# 📷 Camera & Display
# =======================
st.subheader("📷 Camera & Display")
col1, col2, col3 = st.columns(3)
with col1:
    fc = st.slider("Front Camera (MP)", 0, 20, 5)
with col2:
    pc = st.slider("Primary Camera (MP)", 0, 30, 13)
with col3:
    sc_h = st.slider("Screen Height (cm)", 5, 20, 12)

col4, col5, col6 = st.columns(3)
with col4:
    sc_w = st.slider("Screen Width (cm)", 3, 15, 7)
with col5:
    px_height = st.slider("Pixel Height", 0, 2000, 800)
with col6:
    px_width = st.slider("Pixel Width", 0, 2000, 1200)


# =======================
# 🔋 Battery & Build
# =======================
st.subheader("🔋 Battery & Build")
col1, col2 = st.columns(2)
with col1:
    battery_power = st.slider("Battery Power (mAh)", 500, 6000, 3000, step=100)
with col2:
    mobile_wt = st.slider("Mobile Weight (grams)", 80, 250, 150)


# =======================
# 🔮 Prediction Button
# =======================
if st.button("🔍 Predict Price Range"):
    if model is not None:
        try:
            # Create input dataframe
            input_data = pd.DataFrame([[
                battery_power, blue, clock_speed, dual_sim, fc, four_g,
                int_memory, m_dep, mobile_wt, n_cores, pc, px_height,
                px_width, ram, sc_h, sc_w, talk_time, three_g,
                touch_screen, wifi
            ]], columns=[
                'battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
                'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
                'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
                'touch_screen', 'wifi'
            ])

            # Predict
            prediction = model.predict(input_data)[0]

            # Display Result
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            if prediction == 0:
                st.success("🟢 **Low Cost** Smartphone")
            elif prediction == 1:
                st.info("🔵 **Medium Cost** Smartphone")
            elif prediction == 2:
                st.warning("🟠 **High Cost** Smartphone")
            else:
                st.error("🔴 **Very High Cost** Smartphone")
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"⚠️ Error during prediction: {e}")
    else:
        st.error("⚠️ Model not loaded. Please check if 'best_model.pkl' exists.")


# =======================
# 🧾 Footer
# =======================
st.markdown("<footer>© 2025 Abhishek | Machine Learning Project</footer>", unsafe_allow_html=True)
