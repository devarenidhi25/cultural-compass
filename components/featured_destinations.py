import streamlit as st


def show_featured_destinations(featured_destinations):
    """Display the featured destinations section"""
    st.markdown("<h2>Featured Destinations</h2>", unsafe_allow_html=True)
    st.markdown("Discover these hidden gems of India's cultural landscape", unsafe_allow_html=True)

    featured_cols = st.columns(3)

    for i, (_, destination) in enumerate(featured_destinations.iterrows()):
        with featured_cols[i]:
            # Create a placeholder image URL
            img_url = f"/placeholder.svg?height=200&width=400&text={destination['name']}"

            st.markdown(f"""
            <div class="story-card">
                <img src="{img_url}" alt="{destination['name']}">
                <div class="story-content">
                    <div class="story-title">{destination['name']}</div>
                    <div class="story-region">{destination['state']} | Best time: {destination['best_time']}</div>
                    <div class="story-desc">{destination['description']}</div>
                    <p style="margin-top: 10px; font-weight: 500;">Why visit: {destination['why_visit']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
