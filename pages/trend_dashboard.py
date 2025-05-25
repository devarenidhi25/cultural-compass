import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def show_trend_dashboard(yearly_trends, monthly_trends, demographics, origin, purpose, spending):
    """Display the Trend Dashboard tab content"""
    st.markdown("<h2>Tourism Trends & Insights</h2>", unsafe_allow_html=True)
    st.markdown("Explore data-driven insights about tourism patterns across India.")
    
    # Overview metrics
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    
    with metrics_col1:
        total_visitors = yearly_trends[yearly_trends['Year'] == 2022]['Visitors'].sum()
        st.metric(label="Total Visitors (2022)", value=f"{total_visitors:,.0f}")
    
    with metrics_col2:
        growth_rate = ((yearly_trends[yearly_trends['Year'] == 2022]['Visitors'].sum() / 
                       yearly_trends[yearly_trends['Year'] == 2021]['Visitors'].sum()) - 1) * 100
        st.metric(label="YoY Growth", value=f"{growth_rate:.1f}%", delta=f"{growth_rate:.1f}%")
    
    with metrics_col3:
        top_state = yearly_trends[yearly_trends['Year'] == 2022].groupby('State')['Visitors'].sum().idxmax()
        st.metric(label="Top Destination", value=top_state)
    
    with metrics_col4:
        intl_visitors = total_visitors * (origin['Percentage'][origin['Origin'] == 'International'].values[0] / 100)
        st.metric(label="International Visitors", value=f"{intl_visitors:,.0f}")
    
    # Create dashboard layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3>Yearly Tourism Trends</h3>", unsafe_allow_html=True)
        
        # Filter for top 5 states by visitors in 2022
        top_states = yearly_trends[yearly_trends['Year'] == 2022].sort_values('Visitors', ascending=False)['State'].unique()[:5]
        yearly_top5 = yearly_trends[yearly_trends['State'].isin(top_states)]
        
        # Create line chart
        fig = px.line(
            yearly_top5, 
            x='Year', 
            y='Visitors', 
            color='State',
            title='Tourism Trends (2018-2022)',
            labels={'Visitors': 'Number of Visitors', 'Year': 'Year'},
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        
        fig.update_layout(
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode="x unified",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial, sans-serif", size=12, color="#333333")
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("<h3>Visitor Demographics</h3>", unsafe_allow_html=True)
        
        # Create pie chart for demographics
        fig = px.pie(
            demographics, 
            values='Percentage', 
            names='Age_Group',
            title='Visitor Age Distribution',
            color_discrete_sequence=px.colors.sequential.Teal,
            hole=0.4
        )
        
        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=40, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
            annotations=[dict(text='Age Groups', x=0.5, y=0.5, font_size=15, showarrow=False)],
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial, sans-serif", size=12, color="#333333")
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("<h3>Seasonal Tourism Patterns</h3>", unsafe_allow_html=True)
        
        # Create a selector for states
        selected_trend_state = st.selectbox(
            "Select State for Seasonal Analysis",
            sorted(monthly_trends['State'].unique())
        )
        
        # Filter data for selected state
        state_monthly = monthly_trends[monthly_trends['State'] == selected_trend_state]
        
        # Create bar chart
        fig = px.bar(
            state_monthly, 
            x='Month', 
            y='Visitors',
            title=f'Monthly Visitors to {selected_trend_state} (2022)',
            labels={'Visitors': 'Number of Visitors', 'Month': 'Month'},
            color_discrete_sequence=['#218380']
        )
        
        # Add month names
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        fig.update_xaxes(tickvals=list(range(1, 13)), ticktext=month_names)
        
        fig.update_layout(
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial, sans-serif", size=12, color="#333333")
        )
        
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("<h3>Purpose of Visit</h3>", unsafe_allow_html=True)
        
        # Create donut chart for purpose of visit
        fig = px.pie(
            purpose, 
            values='Percentage', 
            names='Purpose',
            title='Why Tourists Visit India',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        
        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=40, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
            annotations=[dict(text='Purpose', x=0.5, y=0.5, font_size=15, showarrow=False)],
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial, sans-serif", size=12, color="#333333")
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Additional insights section
    st.markdown("<h3>Tourism Insights</h3>", unsafe_allow_html=True)
    
    insight_col1, insight_col2, insight_col3 = st.columns(3)
    
    with insight_col1:
        # Domestic vs International
        fig = px.pie(
            origin, 
            values='Percentage', 
            names='Origin',
            title='Visitor Origin',
            color_discrete_sequence=['#FF9933', '#1A3A5A']
        )
        
        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial, sans-serif", size=12, color="#333333")
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with insight_col2:
        # Spending patterns
        fig = px.bar(
            spending,
            x='Category',
            y='Percentage',
            title='Tourist Spending Patterns',
            color_discrete_sequence=['#218380']
        )
        
        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial, sans-serif", size=12, color="#333333"),
            xaxis={'categoryorder':'total descending'}
        )
        
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        
        st.plotly_chart(fig, use_container_width=True)
    
    with insight_col3:
        # COVID impact
        covid_impact = yearly_trends.groupby('Year')['Visitors'].sum().reset_index()
        
        fig = px.line(
            covid_impact,
            x='Year',
            y='Visitors',
            title='COVID-19 Impact on Tourism',
            markers=True,
            color_discrete_sequence=['#1A3A5A']
        )
        
        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial, sans-serif", size=12, color="#333333")
        )
        
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
        
        # Add annotation for COVID dip
        fig.add_annotation(
            x=2020,
            y=covid_impact[covid_impact['Year'] == 2020]['Visitors'].values[0],
            text="COVID-19 Impact",
            showarrow=True,
            arrowhead=1,
            ax=0,
            ay=-40
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Create a heatmap of visitors by state
    st.markdown("<h3>Tourism Heatmap by State</h3>", unsafe_allow_html=True)
    
    # Aggregate data by state for 2022
    state_data = yearly_trends[yearly_trends['Year'] == 2022].groupby('State')['Visitors'].sum().reset_index()
    
    # Create choropleth map
    fig = px.choropleth(
        state_data,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Visitors',
        color_continuous_scale='Teal',
        range_color=(0, state_data['Visitors'].max()),
        hover_data=['Visitors'],
        labels={'Visitors': 'Number of Visitors'}
    )
    
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        height=600,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Arial, sans-serif", size=12, color="#333333")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tourism trends analysis
    st.markdown("<h3>Tourism Trend Analysis</h3>", unsafe_allow_html=True)
    
    trend_col1, trend_col2 = st.columns(2)
    
    with trend_col1:
        st.markdown("""
        <div class="card">
            <h4>Key Insights</h4>
            <ul>
                <li><strong>Post-COVID Recovery:</strong> Tourism is steadily recovering but has not yet reached pre-pandemic levels</li>
                <li><strong>Domestic Tourism Boom:</strong> Domestic tourism has grown faster than international tourism post-pandemic</li>
                <li><strong>Emerging Destinations:</strong> States like Gujarat and Odisha are seeing significant growth in visitor numbers</li>
                <li><strong>Experiential Tourism:</strong> There's a growing trend toward experiential and cultural tourism over traditional sightseeing</li>
                <li><strong>Digital Influence:</strong> Social media is increasingly influencing travel decisions and destination choices</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with trend_col2:
        st.markdown("""
        <div class="card">
            <h4>Future Projections</h4>
            <ul>
                <li><strong>Full Recovery by 2024:</strong> Tourism expected to reach pre-pandemic levels by 2024</li>
                <li><strong>Sustainable Tourism Growth:</strong> Eco-friendly and sustainable tourism options projected to grow by 25%</li>
                <li><strong>Cultural Tourism Expansion:</strong> Heritage and cultural tourism expected to grow at 15% annually</li>
                <li><strong>Digital Transformation:</strong> Virtual tours and augmented reality experiences will complement physical visits</li>
                <li><strong>Rural Tourism Development:</strong> Government initiatives focusing on developing rural tourism infrastructure</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
