# ☀️ SunlightSavings - Intelligent Solar Panel Optimization

Harnessing the power of the sun should be as intuitive as glancing at a map, but with precision tailored to your unique housing setup. **SunlightSavings** is a sophisticated yet user-friendly tool that empowers users to make data-driven decisions about maximizing solar energy production and financial savings.

---

## 🌟 Inspiration

Many solar optimizers today offer **cookie-cutter recommendations**, failing to maximize energy savings or optimize designs for unique housing setups. **SunlightSavings** dares to rethink **simplicity and depth** in renewable energy solutions.

Designed for **property owners in North Carolina**, SunlightSavings provides more than a **generic layout of sun-kissed rooftops**—it serves as a **personalized advisor**, analyzing **solar incidence with precision** while accommodating a range of **solar panel models** that most competitor optimizers overlook.

With its **blend of user-oriented features and robust performance metrics**, this optimizer not only identifies **solar efficiency opportunities** but also **guides users step-by-step** toward achieving them.

---

## 🛠️ What It Does

**SunlightSavings** is a powerful web-based solar optimization tool that:
- **Pinpoints the sunniest areas of any building** using precise sunlight mapping and **advanced roof detection**.
- **Optimizes panel placement** for maximum energy production, factoring in **roof type, solar incidence, and shading**.
- **Supports multiple commercial solar panel models** to ensure tailored recommendations based on real efficiency differences.
- **Conducts a detailed cost-benefit analysis**, projecting:
  - **Energy output**
  - **Installation costs**
  - **Long-term savings**
  - **Tax incentives and credits**
- Uses the proprietary **Kumar-Mendoza Equation** to calculate **Net Present Value (NPV)**, factoring in:
  - Energy production
  - Initial implementation costs
  - Depreciation values
  - NC energy rates

With SunlightSavings, users can **maximize their savings, reduce their carbon footprint, and make informed solar investments**.

---

## 🏗️ How We Built It

**Frontend:**
- **React.js** for a **smooth and interactive** user experience.
- **Google Maps API** for rooftop visualization and user-friendly navigation.

**Backend:**
- **Flask** for efficient data processing and API handling.
- **Google Solar API** to retrieve **solar incidence, elevation data, and map layers**.
- **NumPy & GeoTIFF encoders** to process and generate **precise heatmaps**.
- **Google Geocoding API** to convert user-provided addresses into geographic coordinates.

**Financial & Solar Calculations:**
- **Python’s scientific computing libraries** for:
  - **Solar efficiency modeling**
  - **Cost-benefit analysis**
  - **Custom NPV equation (Kumar-Mendoza Equation)**

---

## 🔥 Challenges We Faced

### 🚧 **1. Finding Accurate Solar Incidence Data**
- Most APIs **lacked the accuracy** required for our analysis.
- The **Google Solar API** provided a strong foundation, but **limited documentation** meant extensive **experimentation** and **debugging**.

### 🗺️ **2. Layering Map Data with High Precision**
- Needed to **align and merge multiple geographic datasets**.
- Used **GeoTIFF encoders** with **NumPy** to generate accurate **solar radiation heatmaps**.

### 📊 **3. Developing the Kumar-Mendoza Equation for Solar NPV**
- Balancing **solar panel efficiency, cost projections, and energy output** required extensive financial modeling.
- The final equation provides **users with actionable, data-driven insights**.

### 🔗 **4. Integrating the Web App with the Backend**
- Handling **GeoTIFF requests** required **efficient workflows** and **asynchronous processing**.

---

## 🏆 Accomplishments We're Proud Of

✅ **A fully functional, user-friendly solar optimizer.**  
✅ **Successfully integrating the Google Solar API** despite limited documentation.  
✅ **Developing the Kumar-Mendoza Equation**, a sophisticated **custom NPV model** for real-world solar investments.  
✅ **Bridging complex geographic and financial calculations** into an **intuitive, interactive interface**.  
✅ **Collaborating as a team for the first time** and solving **technical challenges in under 24 hours**!

---

## 📚 What We Learned

🔹 **API Integration Best Practices:**  
  - Working with a **new API** requires **trial, error, and persistence**.  
🔹 **Efficient Data Processing for Geographic Analysis:**  
  - Merging multiple **GeoTIFF layers** using **NumPy**.  
🔹 **Building a Scalable Financial Model:**  
  - Crafting the **Kumar-Mendoza Equation** for **solar ROI analysis**.  
🔹 **Asynchronous Workflows in Web Development:**  
  - Handling **time-sensitive API requests** and ensuring **fast, smooth UX**.  
🔹 **The Power of Teamwork Under Pressure:**  
  - **Collaboration, adaptability, and problem-solving** led to **a finished product in record time!** 🚀

---

## 🚀 What's Next for SunlightSavings

🔜 **Expanding Nationwide**  
- **Adapting our models** for **state-specific incentives, energy rates, and carbon offsets**.  

🔜 **Localized Financial and Regulatory Data**  
- Integrating **tax credits, rebate programs, and net metering policies** **state-by-state**.  

🔜 **Incorporating More Solar Panel Models**  
- Providing **deeper customization** for panel selection.  
---

## 🛠️ Built With

- **React.js**
- **Flask**
- **Google Maps API**
- **Google Solar API**
- **Google Geocoding API**
- **NumPy**
- **GeoTIFF Encoders**
- **Python (Pandas, NumPy, SciPy)**
- **Financial Modeling (Kumar-Mendoza Equation)**

---

🙌 **Proudly built at HackDuke 2025!** 🚀

---

## 📜 License
**MIT License** – Free to use, modify, and improve!  

---

### **🌞 SunlightSavings: Smart, Data-Driven Solar Planning!**
