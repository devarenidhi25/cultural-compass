# Cultural Compass: Discover India's Heritage

A Streamlit application that allows users to explore India's cultural heritage through various interactive features.

## Features

- **Map Explorer**: Interactive map showing heritage sites across India
- **Cultural Calendar**: Google Calendar-style view of festivals and events
- **Trend Dashboard**: Tourism statistics and data visualization
- **Story Cards**: Information about art forms and traditions
- **Sustainability Tips**: Guidance for responsible tourism

## Installation

1. Clone this repository
2. Install the required packages:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`
3. Run the application:
   \`\`\`
   streamlit run app.py
   \`\`\`

## Project Structure

- `app.py`: Main application file
- `utils/`: Utility functions
  - `data_loader.py`: Functions to load data
  - `styles.py`: CSS styling and dark mode toggle
- `components/`: Reusable UI components
  - `header.py`: App header
  - `hero.py`: Hero section
  - `stats_section.py`: Statistics section with animated counters
  - `featured_destinations.py`: Featured destinations section
  - `sidebar.py`: Sidebar with filters
  - `footer.py`: App footer
- `pages/`: Individual tab content
  - `map_explorer.py`: Map Explorer tab
  - `cultural_calendar.py`: Cultural Calendar tab with Google Calendar style
  - `trend_dashboard.py`: Trend Dashboard tab
  - `story_cards.py`: Story Cards tab
  - `sustainability_tips.py`: Sustainability Tips tab

## Dark Mode

The application includes a dark mode toggle in the sidebar. This feature changes the color scheme to be easier on the eyes in low-light environments.

## Data Sources

The application uses sample data for demonstration purposes. In a production environment, this would be connected to real data sources.
\`\`\`

```text file="requirements.txt"
streamlit==1.28.0
pandas==2.1.1
numpy==1.26.0
plotly==5.17.0
folium==0.14.0
streamlit-folium==0.13.0
