I have a trained machine learning model saved as a pickle file named `best_model.pkl` for **Mobile Price Range Classification**.  
The model predicts the **price range of a mobile phone** based on its specifications.

---

### 📊 Model Input Features
The model takes the following input columns in this exact order:

['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
 'touch_screen', 'wifi']

Descriptions for each:
- **battery_power**: Total energy capacity (mAh)
- **blue**: Has Bluetooth (1 = Yes, 0 = No)
- **clock_speed**: Processor speed (GHz)
- **dual_sim**: Supports dual SIM (1 = Yes, 0 = No)
- **fc**: Front camera megapixels
- **four_g**: Has 4G (1 = Yes, 0 = No)
- **int_memory**: Internal storage (GB)
- **m_dep**: Mobile depth (cm)
- **mobile_wt**: Weight (grams)
- **n_cores**: CPU cores
- **pc**: Primary camera megapixels
- **px_height**: Pixel resolution height
- **px_width**: Pixel resolution width
- **ram**: RAM (MB)
- **sc_h**: Screen height (cm)
- **sc_w**: Screen width (cm)
- **talk_time**: Maximum talk time (hours)
- **three_g**: Has 3G (1 = Yes, 0 = No)
- **touch_screen**: Has touch screen (1 = Yes, 0 = No)
- **wifi**: Has WiFi (1 = Yes, 0 = No)

---

### 🎯 Model Output
The model predicts a price range:
- **0 → Low Cost**
- **1 → Medium Cost**
- **2 → High Cost**
- **3 → Very High Cost**

---

### 🧩 Task for You
Create a **complete Streamlit web app (`app.py`)** that:
1. Loads the `best_model.pkl` file.
2. Provides **intuitive input widgets** for each feature:
   - Use **sliders** for numeric values like `battery_power`, `ram`, `talk_time`, etc.
   - Use **radio buttons** for binary features like `blue`, `dual_sim`, `four_g`, etc.
3. Includes a **“Predict Price Range”** button.
4. When clicked, it should:
   - Prepare the user input as a NumPy array or pandas DataFrame (matching model input format).
   - Predict the price range using the loaded model.
   - Display a **beautiful, color-coded result box**, e.g.:
     - 🟢 “Low Cost” for 0
     - 🔵 “Medium Cost” for 1
     - 🟠 “High Cost” for 2
     - 🔴 “Very High Cost” for 3
5. Include error handling if model file is not found or input is invalid.

---

### 🎨 UI / Design Requirements
Make the Streamlit app look **modern and professional**, with:
- A **clean white or gradient background** (you can use custom CSS or `st.markdown` styling).
- **Title:** “📱 Mobile Price Range Prediction App”
- **Subtitle:** “Predict mobile price category based on technical specifications.”
- **Sidebar:**
  - A short “About this app” section.
  - “Developed by Abhishek” credit.
  - Optionally, a link to my **GitHub profile** (placeholder: `https://github.com/AbhishekShelke`)
- Add a **footer message**: “© 2025 Abhishek | Machine Learning Project”
- Use subtle animations or emojis where suitable.
- Use `st.columns` or `st.expander` to neatly organize inputs into groups like:
  - **Connectivity Features**
  - **Display & Camera**
  - **Performance**
  - **Battery & Build**

---

### ⚙️ Technical Requirements
- Use Python’s `pickle` or `joblib` to load the model.
- Dependencies: `streamlit`, `pandas`, `numpy`, `pickle` (assume they’re preinstalled).
- The app should be runnable with:
