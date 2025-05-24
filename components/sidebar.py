import streamlit as st
import random

def show_sidebar(data):
    """Display the sidebar with filters and other content"""
    st.markdown("<h3>Explore India</h3>", unsafe_allow_html=True)
    
    # State filter
    all_states = sorted(list(set(data["heritage_sites"]['state']).union(set(data["cultural_events"]['state']))))
    selected_states = st.multiselect("Select States", all_states, default=[])
    
    # Season/Month filter
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
             'July', 'August', 'September', 'October', 'November', 'December']
    selected_months = st.multiselect("Select Months", months, default=[])
    
    # Art form filter
    art_types = sorted(list(set(data["art_forms"]['type'])))
    selected_art_types = st.multiselect("Select Art Forms", art_types, default=[])
    
    # Category filter
    categories = sorted(list(set(data["heritage_sites"]['category'])))
    selected_categories = st.multiselect("Select Categories", categories, default=[])
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Quick links
    st.markdown("<h4>Quick Links</h4>", unsafe_allow_html=True)
    st.markdown("""
    <ul style="list-style-type: none; padding-left: 0;">
        <li>🏛️ <a href="#" style="text-decoration: none;">UNESCO Heritage Sites</a></li>
        <li>🎭 <a href="#" style="text-decoration: none;">Major Festivals</a></li>
        <li>🏞️ <a href="#" style="text-decoration: none;">Natural Wonders</a></li>
        <li>🧠 <a href="#" style="text-decoration: none;">Cultural Insights</a></li>
        <li>🛍️ <a href="#" style="text-decoration: none;">Handicraft Traditions</a></li>
    </ul>
    """, unsafe_allow_html=True)
    
    # Testimonial
    random_testimonial = data["testimonials"].sample(1).iloc[0]
    st.markdown(f"""
    <div class="testimonial">
        <div class="testimonial-content">{random_testimonial['quote']}</div>
        <div class="testimonial-author">{random_testimonial['author']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-size: 0.8rem; color: #666; margin-top: 20px;">
        <p>Cultural Compass helps you discover India's hidden cultural treasures and promotes sustainable tourism.</p>
        <p>Data sourced from tourism boards and cultural organizations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    return {
        "selected_states": selected_states,
        "selected_months": selected_months,
        "selected_art_types": selected_art_types,
        "selected_categories": selected_categories
    }
