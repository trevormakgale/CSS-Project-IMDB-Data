import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Tshepho Makgale - Research Profile",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #3B82F6;
        border-bottom: 3px solid #3B82F6;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .profile-img {
        border-radius: 50%;
        border: 5px solid #3B82F6;
        width: 200px;
        height: 200px;
        object-fit: cover;
    }
    .contact-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        border-left: 5px solid #3B82F6;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("# 🔬 Tshepho Makgale")
    st.markdown("### Research Scientist")
    st.markdown("---")
    
    st.markdown("### 📍 Quick Links")
    st.page_link("https://scholar.google.com", label="Google Scholar", icon="📚")
    st.page_link("https://linkedin.com", label="LinkedIn", icon="💼")
    st.page_link("https://github.com", label="GitHub", icon="🐙")
    st.page_link("https://orcid.org", label="ORCID", icon="🆔")
    
    st.markdown("---")
    st.markdown("### 📞 Contact")
    st.markdown("📧 tshepho.makgale@research.edu")
    st.markdown("📱 +27 XX XXX XXXX")
    st.markdown("🏛️ University Research Center")
    
    st.markdown("---")
    st.markdown("### 📊 Research Metrics")
    st.metric(label="Publications", value="24")
    st.metric(label="Citations", value="312")
    st.metric(label="h-index", value="9")
    st.metric(label="Projects", value="7")

# Main content
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Profile Photo")
    # Placeholder image - replace with actual image URL
    st.image("https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&h=400&q=80", 
             caption="Tshepho Makgale, PhD", use_column_width=True)
    
    st.markdown("### 🎓 Education")
    st.markdown("""
    - **PhD in Computational Sciences**  
      University of Cape Town (2020-2024)
    
    - **MSc in Data Science**  
      University of Pretoria (2018-2020)
    
    - **BSc Honors in Computer Science**  
      University of Johannesburg (2014-2017)
    """)

with col2:
    st.markdown('<h1 class="main-header">Dr. Tshepho Makgale</h1>', unsafe_allow_html=True)
    st.markdown("### Computational Scientist & AI Researcher")
    
    st.markdown("""
    Welcome to my research profile! I'm a passionate computational scientist specializing in 
    **machine learning applications in environmental science** and **AI for sustainable development**. 
    My research focuses on developing innovative computational models to address pressing 
    environmental challenges and promote sustainable solutions.
    """)
    
    # Research Interests
    st.markdown('<div class="sub-header">🎯 Research Interests</div>', unsafe_allow_html=True)
    
    interests_cols = st.columns(3)
    with interests_cols[0]:
        st.markdown('<div class="card">\
                    <h4>🌿 Environmental AI</h4>\
                    <p>Machine learning for climate modeling and ecological monitoring</p>\
                    </div>', unsafe_allow_html=True)
    
    with interests_cols[1]:
        st.markdown('<div class="card">\
                    <h4>📊 Computational Sustainability</h4>\
                    <p>Optimization algorithms for renewable energy systems</p>\
                    </div>', unsafe_allow_html=True)
    
    with interests_cols[2]:
        st.markdown('<div class="card">\
                    <h4>🤖 Deep Learning</h4>\
                    <p>Neural networks for remote sensing and satellite imagery analysis</p>\
                    </div>', unsafe_allow_html=True)

# Recent Publications
st.markdown('<div class="sub-header">📚 Recent Publications</div>', unsafe_allow_html=True)

publications = pd.DataFrame({
    'Year': [2024, 2023, 2023, 2022, 2022],
    'Title': [
        "Deep Learning for Climate Pattern Recognition in Southern Africa",
        "Optimizing Solar Farm Placement using Reinforcement Learning",
        "AI-driven Water Quality Monitoring in Urban Areas",
        "Machine Learning Models for Predicting Crop Yields",
        "Computational Approaches to Biodiversity Conservation"
    ],
    'Journal': ['Nature Climate AI', 'Renewable Energy', 'Environmental Science', 'Agriculture AI', 'Conservation Biology'],
    'Citations': [45, 32, 28, 51, 39]
})

# Display publications
for idx, pub in publications.iterrows():
    with st.expander(f"📖 {pub['Title']}"):
        st.markdown(f"""
        **Journal:** *{pub['Journal']}* | **Year:** {pub['Year']} | **Citations:** {pub['Citations']}
        
        **Abstract:** This study presents innovative approaches to {pub['Title'].split(' ')[-2:][0].lower()} 
        using advanced computational methods. Our findings contribute significantly to the field 
        and demonstrate practical applications for sustainable development.
        """)

# Current Projects
st.markdown('<div class="sub-header">🚀 Current Research Projects</div>', unsafe_allow_html=True)

project_cols = st.columns(3)
with project_cols[0]:
    st.markdown("""
    **AI for Climate Resilience**  
    *2023-2025 | $500,000 grant*  
    Developing ML models to predict climate impacts on agriculture
    """)

with project_cols[1]:
    st.markdown("""
    **Smart Water Management**  
    *2024-2026 | $350,000 grant*  
    IoT and AI for real-time water quality monitoring
    """)

with project_cols[2]:
    st.markdown("""
    **Renewable Energy Optimization**  
    *2022-2024 | $420,000 grant*  
    Grid optimization using deep reinforcement learning
    """)

# Skills & Technologies
st.markdown('<div class="sub-header">🛠️ Technical Skills</div>', unsafe_allow_html=True)

skills = {
    'Programming': ['Python', 'R', 'Julia', 'SQL'],
    'ML Frameworks': ['TensorFlow', 'PyTorch', 'Scikit-learn', 'XGBoost'],
    'Data Tools': ['Pandas', 'NumPy', 'Plotly', 'D3.js'],
    'Cloud & DevOps': ['AWS', 'Docker', 'Git', 'Streamlit']
}

skill_cols = st.columns(4)
for idx, (category, skill_list) in enumerate(skills.items()):
    with skill_cols[idx]:
        st.markdown(f"**{category}**")
        for skill in skill_list:
            st.markdown(f"- {skill}")

# Research Timeline
st.markdown('<div class="sub-header">📅 Research Timeline</div>', unsafe_allow_html=True)

timeline_data = pd.DataFrame({
    'Year': [2017, 2018, 2020, 2021, 2022, 2023, 2024],
    'Event': [
        'BSc Graduation',
        'MSc Research - ML Applications',
        'PhD Started - Computational Sustainability',
        'First Major Publication',
        'Climate AI Project Launch',
        'International Conference Keynote',
        'PhD Defense & Postdoc Position'
    ],
    'Significance': [1, 2, 3, 4, 5, 4, 5]
})

fig = px.line(timeline_data, x='Year', y='Significance', markers=True,
              title='Research Journey Timeline',
              hover_data=['Event'])
st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
footer_cols = st.columns(3)
with footer_cols[1]:
    st.markdown("""
    <div style='text-align: center;'>
        <p>© 2024 Tshepho Makgale | All Rights Reserved</p>
        <p>Last updated: """ + datetime.now().strftime("%Y-%m-%d") + """</p>
    </div>
    """, unsafe_allow_html=True)
