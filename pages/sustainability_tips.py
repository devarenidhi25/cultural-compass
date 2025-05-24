import streamlit as st

def show_sustainability_tips(sustainability_tips):
    """Display the Sustainability Tips tab content"""
    st.markdown("<h2>Sustainable Tourism Tips</h2>", unsafe_allow_html=True)
    st.markdown("Learn how to travel responsibly and make a positive impact on local communities and the environment.")
    
    # Sustainability overview
    st.markdown("""
    <div class="featured-section">
        <h3 style="color: #1A3A5A; margin-top: 0;">Why Sustainable Tourism Matters in India</h3>
        <p>India's rich cultural heritage and diverse ecosystems face numerous challenges from overtourism, environmental degradation, and cultural commodification. Sustainable tourism practices help preserve these treasures for future generations while ensuring that local communities benefit from tourism.</p>
        <p>By following these guidelines, you can help protect India's cultural and natural heritage while having a more authentic and meaningful travel experience.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filter tips by category
    tip_categories = ['All'] + sorted(list(set(sustainability_tips['category'])))
    selected_tip_category = st.selectbox("Filter by Category", tip_categories)
    
    # Filter by impact level
    impact_levels = ['All', 'High', 'Medium']
    selected_impact = st.selectbox("Filter by Impact Level", impact_levels)
    
    # Apply filters
    if selected_tip_category != 'All':
        tips_filtered = sustainability_tips[sustainability_tips['category'] == selected_tip_category]
    else:
        tips_filtered = sustainability_tips
    
    if selected_impact != 'All':
        tips_filtered = tips_filtered[tips_filtered['impact_level'] == selected_impact]
    
    # Display tips
    if not tips_filtered.empty:
        for i in range(0, len(tips_filtered), 2):
            cols = st.columns(2)
            
            for j in range(2):
                if i + j < len(tips_filtered):
                    tip = tips_filtered.iloc[i+j]
                    
                    with cols[j]:
                        impact_badge = ""
                        if tip['impact_level'] == 'High':
                            impact_badge = '<span class="badge badge-primary">High Impact</span>'
                        else:
                            impact_badge = '<span class="badge badge-light">Medium Impact</span>'
                        
                        st.markdown(f"""
                        <div class="tip-card">
                            <div class="tip-title"><i class="feature-icon">{tip['icon']}</i> {tip['title']} {impact_badge}</div>
                            <p>{tip['description']}</p>
                            <p><strong>Example:</strong> {tip['example']}</p>
                        </div>
                        """, unsafe_allow_html=True)
    else:
        st.info("No tips match your current filters. Please adjust your selection.")
    
    # Community initiatives section
    st.markdown("<h3>Community Tourism Initiatives</h3>", unsafe_allow_html=True)
    
    initiative_col1, initiative_col2, initiative_col3 = st.columns(3)
    
    with initiative_col1:
        st.markdown("""
        <div class="card">
            <h4>Himalayan Homestay Program</h4>
            <p><strong>Location:</strong> Ladakh, Himachal Pradesh, Uttarakhand</p>
            <p>This initiative trains local families to host tourists in their homes, providing authentic cultural experiences while generating income for remote mountain communities.</p>
            <p><strong>Impact:</strong> Over 200 families have increased their income by 30-40% while preserving traditional architecture and lifestyles.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with initiative_col2:
        st.markdown("""
        <div class="card">
            <h4>Kerala Responsible Tourism Mission</h4>
            <p><strong>Location:</strong> Kerala</p>
            <p>A government initiative that connects tourists with local communities through village life experiences, cultural performances, and locally produced handicrafts and cuisine.</p>
            <p><strong>Impact:</strong> Generated over ₹35 crore for local communities and created thousands of jobs, especially for women.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with initiative_col3:
        st.markdown("""
        <div class="card">
            <h4>Spiti Ecosphere</h4>
            <p><strong>Location:</strong> Spiti Valley, Himachal Pradesh</p>
            <p>A social enterprise that combines responsible travel with development initiatives in the remote Spiti Valley, focusing on conservation, clean energy, and cultural preservation.</p>
            <p><strong>Impact:</strong> Installed solar passive houses, greenhouses, and water conservation systems while creating sustainable livelihoods.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Eco-friendly accommodations
    st.markdown("<h3>Eco-Friendly Accommodations</h3>", unsafe_allow_html=True)
    
    eco_cols = st.columns(3)
    
    with eco_cols[0]:
        st.markdown("""
        <div class="card">
            <h4>Dune Eco Village</h4>
            <p><strong>Location:</strong> Puducherry</p>
            <p>Sustainable resort with eco-friendly architecture using recycled materials, organic gardens, and solar power.</p>
            <p><strong>Features:</strong> Rainwater harvesting, waste recycling, organic farm-to-table dining, and natural building materials.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with eco_cols[1]:
        st.markdown("""
        <div class="card">
            <h4>Evolve Back Resorts</h4>
            <p><strong>Location:</strong> Karnataka</p>
            <p>Luxury eco-resorts with zero waste policies, water conservation, and community involvement near Coorg, Kabini, and Hampi.</p>
            <p><strong>Features:</strong> Reverse osmosis water plants, solar heating, organic gardens, and traditional architecture.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with eco_cols[2]:
        st.markdown("""
        <div class="card">
            <h4>CGH Earth Hotels</h4>
            <p><strong>Location:</strong> Kerala</p>
            <p>Eco-sensitive hotels focusing on local community engagement, traditional architecture, and sustainable practices.</p>
            <p><strong>Features:</strong> Zero-waste policies, plastic-free environments, local hiring, and cultural preservation initiatives.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Sustainable travel pledge
    st.markdown("<h3>Take the Sustainable Travel Pledge</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <p>Join thousands of travelers who have committed to exploring India responsibly. The pledge includes:</p>
        <ul>
            <li>Respecting local cultures and traditions</li>
            <li>Minimizing environmental impact</li>
            <li>Supporting local economies</li>
            <li>Preserving heritage sites</li>
            <li>Sharing sustainable practices with other travelers</li>
        </ul>
        <p>By taking this pledge, you'll receive a sustainable travel guide and regular updates on responsible tourism initiatives across India.</p>
    </div>
    """, unsafe_allow_html=True)
    
    pledge_col1, pledge_col2, pledge_col3 = st.columns([1, 2, 1])
    
    with pledge_col2:
        st.button("Take the Pledge", type="primary")
