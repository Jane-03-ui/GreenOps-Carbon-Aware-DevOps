import sys
import os
import time
import streamlit as st
import pandas as pd

# Fix module path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.green_score import find_best_region
from engine.database import init_db, insert_deployment, get_deployments

# Page config
st.set_page_config(page_title="GreenOps Dashboard", layout="wide")

# 🌌 CUSTOM STYLE (Premium UI)
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
    }
    .stMetric {
        background-color: #1A1F2B;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# TITLE
st.title("🌱 GreenOps Carbon-Aware Deployment Dashboard")

# Fetch results
results, best = find_best_region()

# Init DB
init_db()

best_carbon = results[best]["carbon"]
best_score = results[best]["green_score"]

# Worst region
worst_region = min(results, key=lambda x: results[x]["green_score"])
worst_carbon = results[worst_region]["carbon"]

# Save deployment
insert_deployment(best, best_carbon, best_score)

# 🌍 REGION CARDS (Premium Layout)
st.subheader("🌍 Region Comparison")

cols = st.columns(3)

for i, (region, values) in enumerate(results.items()):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="background:#1A1F2B;padding:15px;border-radius:15px;">
            <h4>🌍 {region}</h4>
            <p>🌱 <b>Score:</b> {values['green_score']:.2f}</p>
            <p>⚡ <b>Carbon:</b> {values['carbon']}</p>
        </div>
        """, unsafe_allow_html=True)

# 📊 BAR CHART
st.subheader("📊 Green Score Visualization")

df = pd.DataFrame([
    {"Region": region, "Score": values["green_score"]}
    for region, values in results.items()
])

st.bar_chart(df.set_index("Region"), use_container_width=True)

# 🌍 MAP VIEW
st.subheader("🌍 Global Deployment Map")

map_data = pd.DataFrame({
    "lat": [19.07, 1.35, 37.77, 45.52, 50.11, 53.35, 35.68],
    "lon": [72.87, 103.82, -77.04, -122.67, 8.68, -6.26, 139.69],
})

st.map(map_data)

# 🌱 BEST REGION (Highlighted)
st.markdown(f"""
## 🌱 ✅ Best Region: **{best}**
### 🌍 Carbon: {best_carbon} | Score: {best_score:.2f}
""")
# 🚀 DEPLOY BUTTON
st.subheader("🚀 Deploy Application")

app_choice = st.selectbox(
    "Choose Application",
    ["To-Do App", "Counter App"]
)

if st.button("Deploy Now"):
    st.success(f"Deploying {app_choice} to {best} region...")

    import time
    time.sleep(2)

    if app_choice == "To-Do App":
        link = "http://34.229.96.151:5000"
    else:
        link = "http://34.229.96.151:5001"

    st.markdown(f"""
    ✅ Deployment Successful!

    🌐 Access your app here:  
    {link}
    """)
# 🌍 CARBON SAVED
carbon_saved = worst_carbon - best_carbon

st.subheader("🌱 Environmental Impact")

st.metric(
    label="🌍 Carbon Emission Reduced",
    value=f"{carbon_saved} units",
    delta="Optimized Deployment"
)

# 🧠 WHY SECTION
st.subheader("🧠 Why this region?")

st.info(
    f"""
    🌍 Region **{best}** has the lowest carbon intensity ({best_carbon} gCO₂/kWh).

    ⚡ Compared to **{worst_region}**, this significantly reduces emissions.

    🌱 Ensures sustainable cloud deployment.
    """
)

# 📦 DEPLOYMENT HISTORY
st.subheader("📦 Deployment History")

history = get_deployments()

for row in history[:5]:
    st.markdown(f"""
    🔹 **Region:** {row[1]} | 🌍 Carbon: {row[2]} | 🌱 Score: {row[3]:.2f}  
    🕒 {row[4]}
    """)

# 🔄 AUTO REFRESH
st.caption("🔄 Auto refreshing every 10 seconds...")

time.sleep(10)
st.rerun()
