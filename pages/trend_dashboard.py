import streamlit as st
import pandas as pd
import plotly.express as px

def show_trend_dashboard(yearly_trends, monthly_trends, demographics, origin, purpose, spending, enhanced_sites):
    st.markdown("<h2>📊 Heritage Sites Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("Explore trends and statistics from the enhanced Indian heritage dataset.")

    # --- PIE CHART: UNESCO STATUS ---
    st.subheader("UNESCO Status Distribution")
    if 'unesco_status' in enhanced_sites.columns:
        pie_fig = px.pie(
            enhanced_sites,
            names='unesco_status',
            title='UNESCO World Heritage Site Distribution',
            color_discrete_sequence=px.colors.sequential.Plasma
        )
        st.plotly_chart(pie_fig, use_container_width=True)

    # --- BAR CHART: Number of Sites by State ---
    st.subheader("Top States by Number of Heritage Sites")
    if 'state' in enhanced_sites.columns:
        state_counts = enhanced_sites['state'].value_counts().reset_index()
        state_counts.columns = ['State', 'Number of Sites']
        bar_fig = px.bar(
            state_counts,
            x='State',
            y='Number of Sites',
            color='Number of Sites',
            title='Number of Heritage Sites per State',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(bar_fig, use_container_width=True)

    # --- DONUT CHART: Category Distribution ---
    st.subheader("Heritage Sites by Category")
    if 'category' in enhanced_sites.columns:
        donut_fig = px.pie(
            enhanced_sites,
            names='category',
            hole=0.4,
            title='Category of Heritage Sites',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(donut_fig, use_container_width=True)

    # --- HISTOGRAM: Entry Fee ---
    st.subheader("Entry Fee Distribution")
    if 'entry_fee' in enhanced_sites.columns:
        enhanced_sites['entry_fee'] = pd.to_numeric(enhanced_sites['entry_fee'], errors='coerce')
        hist_fig = px.histogram(
            enhanced_sites.dropna(subset=['entry_fee']),
            x='entry_fee',
            nbins=20,
            title='Entry Fee Range Across Sites',
            color_discrete_sequence=['#3a86ff']
        )
        st.plotly_chart(hist_fig, use_container_width=True)

    # --- GEO SCATTER MAP ---
    if 'latitude' in enhanced_sites.columns and 'longitude' in enhanced_sites.columns:
        st.subheader("Map of Heritage Sites")
        geo_fig = px.scatter_geo(
            enhanced_sites,
            lat='latitude',
            lon='longitude',
            hover_name='site_name' if 'site_name' in enhanced_sites.columns else None,
            scope='asia',
            title='Geographic Distribution of Heritage Sites',
            color='state' if 'state' in enhanced_sites.columns else None
        )
        st.plotly_chart(geo_fig, use_container_width=True)

    # --- LINE GRAPH: Visitors vs Year Built ---
    st.subheader("Visitors vs Year Built")
    if 'year_built' in enhanced_sites.columns and 'visitors_per_year' in enhanced_sites.columns:
        line_fig = px.scatter(
            enhanced_sites,
            x='year_built',
            y='visitors_per_year',
            trendline='ols',
            title='Visitors vs Year Built'
        )
        st.plotly_chart(line_fig, use_container_width=True)

    # --- TREEMAP: Visitor Distribution by State and Category ---
    st.subheader("Visitor Distribution by State and Category")
    if 'state' in enhanced_sites.columns and 'category' in enhanced_sites.columns and 'visitors_per_year' in enhanced_sites.columns:
        tree_fig = px.treemap(
            enhanced_sites,
            path=['state', 'category'],
            values='visitors_per_year',
            title='Visitor Distribution by State and Category'
        )
        st.plotly_chart(tree_fig, use_container_width=True)

    # # --- BOX PLOT: Entry Fee by Category ---
    # st.subheader("Entry Fee Variation by Category")
    # if 'entry_fee' in enhanced_sites.columns and 'category' in enhanced_sites.columns:
    #     # Convert entry_fee to numeric and drop NaNs
    #     enhanced_sites['entry_fee'] = pd.to_numeric(enhanced_sites['entry_fee'], errors='coerce')
    #     cleaned_data = enhanced_sites.dropna(subset=['entry_fee', 'category'])

    #     # Show warning or plot
    #     if not cleaned_data.empty:
    #         fee_box_fig = px.box(
    #             cleaned_data,
    #             x='category',
    #             y='entry_fee',
    #             title='Entry Fee by Site Category'
    #         )
    #         st.plotly_chart(fee_box_fig, use_container_width=True)
    #     else:
    #         st.warning("No valid data available for plotting Entry Fee by Category.")

