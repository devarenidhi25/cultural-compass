import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
from folium.plugins import MarkerCluster

def get_emoji_icon(category):
    if not isinstance(category, str):
        return "📍"
    category = category.lower()
    if "fort" in category:
        return "🏰"
    elif "temple" in category:
        return "🛕"
    elif "museum" in category:
        return "🖼️"
    elif "palace" in category:
        return "👑"
    elif "cave" in category:
        return "🕳️"
    return "📍"

def show_map_explorer(df):
    st.title("🗺️ Explore India's Heritage Sites")

    if df is None or df.empty:
        st.warning("No data available.")
        return

    # Handle if headers are duplicated as data
    if df.iloc[0].astype(str).str.contains("(?i)site|state|category").any():
        df = df.iloc[1:].reset_index(drop=True)

    # Rename and normalize
    df.columns = df.columns.str.lower()
    df = df.rename(columns={
        "site_name": "name",
        "visitors_per_year": "visitors",
        "popularity": "popularity",
        "best_month_to_visit": "best_time",
        "famous_art": "art",
        "latitude": "lat",
        "longitude": "lon",
        "unesco_status": "unesco",
        "description": "description",
        "festival": "activities"
    })

    # Convert types
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")
    df["visitors"] = pd.to_numeric(df["visitors"], errors="coerce")
    df = df.dropna(subset=["lat", "lon"])

    if df.empty:
        st.error("No valid coordinates to display on map.")
        return

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        category = st.selectbox("Category", ["All"] + sorted(df["category"].dropna().unique()))
    with col2:
        state = st.selectbox("State", ["All"] + sorted(df["state"].dropna().unique()))
    with col3:
        min_visitors = st.slider("Min Visitors", 0, int(df["visitors"].max()), 0)

    filtered = df.copy()
    if category != "All":
        filtered = filtered[filtered["category"] == category]
    if state != "All":
        filtered = filtered[filtered["state"] == state]
    filtered = filtered[filtered["visitors"] >= min_visitors]

    st.write(f"📍 {len(filtered)} sites found.")

    if filtered.empty:
        st.info("No matching sites.")
        return

    # Map
    m = folium.Map(location=[22.9734, 78.6569], zoom_start=5)
    marker_cluster = MarkerCluster().add_to(m)

    # Debug marker always visible
    folium.Marker(
        location=[28.6139, 77.2090],
        tooltip="📍 Test Marker: New Delhi",
        popup="🧪 Map is working.",
        icon=folium.Icon(color="red")
    ).add_to(m)

    for _, row in filtered.iterrows():
        popup_info = f"""
        <strong>{get_emoji_icon(row['category'])} {row['name']}</strong><br>
        <b>State:</b> {row['state']}<br>
        <b>Category:</b> {row['category']}<br>
        <b>Visitors:</b> {int(row.get('visitors', 0)):,}<br>
        <b>UNESCO:</b> {row.get('unesco', 'N/A')}<br>
        <b>Best Time:</b> {row.get('best_time', 'N/A')}<br>
        <b>Activities:</b> {row.get('activities', 'N/A')}<br>
        {row.get('description', '')[:150]}...
        """
        folium.Marker(
            location=[row["lat"], row["lon"]],
            tooltip=row["name"],
            popup=folium.Popup(popup_info, max_width=300),
            icon=folium.DivIcon(html=f"""<div style="font-size:24px;">{get_emoji_icon(row["category"])}</div>""")
        ).add_to(marker_cluster)

    folium_static(m, width=1100, height=600)

    # Cards and Table
    st.markdown("### 🏛️ Heritage Site Highlights")
    tab1, tab2 = st.tabs(["🧾 Cards", "📊 Table"])

    with tab1:
        for i in range(0, len(filtered), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(filtered):
                    site = filtered.iloc[i + j]
                    emoji = get_emoji_icon(site.get("category", ""))
                    with cols[j]:
                        st.markdown(f"""
                            <div style="border:1px solid #ccc; padding:10px; border-radius:10px;">
                                <h4>{emoji} {site['name']}</h4>
                                <p><strong>State:</strong> {site['state']}</p>
                                <p><strong>Category:</strong> {site['category']}</p>
                                <p><strong>Visitors:</strong> {int(site.get('visitors', 0)):,}</p>
                                <p><strong>UNESCO:</strong> {site.get('unesco', 'N/A')}</p>
                                <p><strong>Best Time:</strong> {site.get('best_time', 'N/A')}</p>
                                <p>{site.get('description', '')[:100]}...</p>
                            </div>
                        """, unsafe_allow_html=True)

    with tab2:
        required_columns = ["name", "state", "category", "visitors", "popularity", "unesco", "best_time"]
        missing_cols = [col for col in required_columns if col not in filtered.columns]

        if missing_cols:
            st.error(f"❌ Missing columns: {missing_cols}")
        else:
            st.dataframe(filtered[required_columns])

