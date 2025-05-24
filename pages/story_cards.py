import streamlit as st


def show_story_cards(art_forms):
    # Select the first art form as the featured art (or use any other logic you prefer)
    featured_art = art_forms.iloc[0] if not art_forms.empty else None
    if featured_art is not None:
        img_path = f"images/{featured_art['name'].lower()}.jpg"  # or .png depending on your images
    else:
        img_path = "kathakali-classical-artform.webp"  # Placeholder image if no art form is available
        
    st.markdown(f"""
    <div class="featured-section">
        <div class="featured-title">Featured Art Form: {featured_art['name']}</div>
        <div style="display: flex; gap: 20px; align-items: center;">
            <div style="flex: 1;">
                <img src="{img_path}" style="width: 100%; border-radius: 15px; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);">
            </div>
            <div style="flex: 2;">
                <h3 style="color: #1A3A5A; margin-top: 0;">{featured_art['name']} - {featured_art['region']}</h3>
                <p><strong>Type:</strong> {featured_art['type']}</p>
                <p><strong>Description:</strong> {featured_art['description']}</p>
                <p><strong>History:</strong> {featured_art['history']}</p>
                <p><strong>Cultural Significance:</strong> {featured_art['significance']}</p>
                <div style="margin-top: 15px;">
                    <span class="badge badge-primary">{featured_art['type']}</span>
                    <span class="badge badge-secondary">{featured_art['region']}</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Art form filters
    art_filter_col1, art_filter_col2, art_filter_col3 = st.columns(3)
    
    with art_filter_col1:
        art_type_filter = st.selectbox("Filter by Type", ['All'] + sorted(list(set(art_forms['type']))))
    
    with art_filter_col2:
        art_region_filter = st.selectbox("Filter by Region", ['All'] + sorted(list(set(art_forms['region']))))
    
    with art_filter_col3:
        art_sort = st.selectbox("Sort by", ['Name', 'Region', 'Type'])
    
    # Apply filters
    if art_type_filter != 'All':
        art_forms_display = art_forms[art_forms['type'] == art_type_filter]
    else:
        art_forms_display = art_forms
    
    if art_region_filter != 'All':
        art_forms_display = art_forms_display[art_forms_display['region'] == art_region_filter]
    
    # Apply sorting
    if art_sort == 'Name':
        art_forms_display = art_forms_display.sort_values('name')
    elif art_sort == 'Region':
        art_forms_display = art_forms_display.sort_values('region')
    else:
        art_forms_display = art_forms_display.sort_values('type')
    
    if not art_forms_display.empty:
        # Create rows of 3 cards each
        for i in range(0, len(art_forms_display), 3):
            cols = st.columns(3)
            
            for j in range(3):
                if i + j < len(art_forms_display):
                    art = art_forms_display.iloc[i+j]
                    
                    with cols[j]:
                        # Create a placeholder image URL
                        img_url = f"/placeholder.svg?height=200&width=400&text={art['name']}"
                        
                        st.markdown(f"""
                        <div class="story-card">
                            <img src="{img_url}" alt="{art['name']}">
                            <div class="story-content">
                                <div class="story-title">{art['name']}</div>
                                <div class="story-region">{art['region']} | {art['type']}</div>
                                <div class="story-desc">{art['description']}</div>
                                <div style="margin-top: 10px;">
                                    <span class="badge badge-primary">{art['type']}</span>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
    else:
        st.info("No art forms match your current filters. Please adjust your selection.")
    
    # Art and culture insights
    st.markdown("<h3>Art & Culture Insights</h3>", unsafe_allow_html=True)
    
    art_col1, art_col2, art_col3 = st.columns(3)
    
    with art_col1:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🎭</div>
            <div class="feature-title">Classical Traditions</div>
            <div class="feature-text">
                India's classical arts follow ancient traditions codified in texts like Natya Shastra. These art forms have been preserved through guru-shishya (teacher-student) lineages for centuries, maintaining their authenticity while evolving subtly.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with art_col2:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🏺</div>
            <div class="feature-title">Folk Expressions</div>
            <div class="feature-text">
                Folk arts represent the cultural expressions of communities, often tied to seasonal cycles, harvests, and local deities. These art forms use locally available materials and tell stories relevant to community life and values.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with art_col3:
        st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">🧵</div>
            <div class="feature-title">Textile Heritage</div>
            <div class="feature-text">
                India's textile traditions represent one of the oldest continuous crafts in the world. Each region has distinctive styles, techniques, and motifs that reflect local cultural influences, trade history, and environmental factors.
            </div>
        </div>
        """, unsafe_allow_html=True)
