"""
Twitter (X) Algorithm Explorer - UI Application
A comprehensive web interface to explore and understand Twitter's recommendation algorithms
"""

import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Twitter Algorithm Explorer",
    page_icon="🐦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1DA1F2;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #14171A;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .algorithm-card {
        background-color: #F7F9FA;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1DA1F2;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #E8F5FE;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application entry point"""
    
    # Sidebar navigation
    st.sidebar.title("🐦 Twitter Algorithm Explorer")
    st.sidebar.markdown("---")
    
    page = st.sidebar.radio(
        "Navigate to:",
        [
            "🏠 Home",
            "🔍 Overview",
            "🌐 SimClusters",
            "🕸️ TwHIN Embeddings",
            "🛡️ Trust & Safety",
            "👥 Real Graph",
            "⭐ TweepCred",
            "📊 Search & Ranking",
            "💡 Recommendations",
            "📈 Timeline Architecture"
        ]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **About**: This UI application provides an interactive way to explore 
    Twitter's (X) open-source recommendation algorithms and understand 
    how content is ranked and surfaced across the platform.
    """)
    
    # Route to appropriate page
    if page == "🏠 Home":
        show_home()
    elif page == "🔍 Overview":
        show_overview()
    elif page == "🌐 SimClusters":
        show_simclusters()
    elif page == "🕸️ TwHIN Embeddings":
        show_twhin()
    elif page == "🛡️ Trust & Safety":
        show_trust_safety()
    elif page == "👥 Real Graph":
        show_real_graph()
    elif page == "⭐ TweepCred":
        show_tweepcred()
    elif page == "📊 Search & Ranking":
        show_search_ranking()
    elif page == "💡 Recommendations":
        show_recommendations()
    elif page == "📈 Timeline Architecture":
        show_timeline_architecture()

def show_home():
    """Home page with welcome message and quick stats"""
    st.markdown('<h1 class="main-header">🐦 Twitter Algorithm Explorer</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Welcome to the Twitter (X) Recommendation Algorithm Explorer!
    
    This interactive application helps you understand how Twitter's recommendation 
    algorithms work to surface content across the platform.
    """)
    
    # Create three columns for key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Algorithm Components", "10+", "Core Systems")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Product Surfaces", "5+", "Including For You Timeline")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Open Source", "2023", "Public Release")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🚀 Quick Start
    
    Use the **sidebar navigation** to explore different components of the algorithm:
    
    - **Overview**: High-level architecture and data flow
    - **SimClusters**: Community detection and embeddings
    - **TwHIN**: Dense graph embeddings for users and posts
    - **Trust & Safety**: Models for content moderation
    - **Real Graph**: User interaction predictions
    - **TweepCred**: User reputation system
    - **Search & Ranking**: How posts are discovered and ranked
    - **Recommendations**: Notification and content suggestions
    - **Timeline Architecture**: End-to-end For You Timeline system
    
    ### 📖 About the Algorithm
    
    Twitter's Recommendation Algorithm is a set of services and jobs responsible 
    for serving feeds of posts and content across all Twitter product surfaces. 
    The algorithm uses machine learning models, graph analysis, and real-time 
    processing to personalize each user's experience.
    """)

def show_overview():
    """Overview page with architecture diagram and components"""
    st.title("📊 Algorithm Overview")
    
    st.markdown("""
    ## System Architecture
    
    Twitter's recommendation system is built on a sophisticated architecture that 
    combines multiple data sources, ML models, and software frameworks.
    """)
    
    # Show architecture components
    st.markdown('<h2 class="sub-header">📦 Core Components</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Data Components", "ML Models", "Software Frameworks"])
    
    with tab1:
        st.markdown("""
        ### Data Infrastructure
        
        The foundation of the recommendation system:
        """)
        
        data_components = pd.DataFrame({
            "Component": ["Tweetypie", "Unified User Actions", "User Signal Service"],
            "Purpose": [
                "Core service for reading/writing post data",
                "Real-time stream of user actions",
                "Centralized platform for user signals"
            ],
            "Type": ["Service", "Stream", "Service"]
        })
        st.dataframe(data_components, use_container_width=True, hide_index=True)
    
    with tab2:
        st.markdown("""
        ### Machine Learning Models
        
        Sophisticated models that power recommendations:
        """)
        
        ml_models = pd.DataFrame({
            "Model": ["SimClusters", "TwHIN", "Trust & Safety", "Real Graph", "TweepCred"],
            "Function": [
                "Community detection & sparse embeddings",
                "Dense graph embeddings",
                "NSFW & abusive content detection",
                "User interaction prediction",
                "User reputation (PageRank)"
            ],
            "Category": ["Embedding", "Embedding", "Safety", "Prediction", "Reputation"]
        })
        st.dataframe(ml_models, use_container_width=True, hide_index=True)
    
    with tab3:
        st.markdown("""
        ### Software Frameworks
        
        Scalable systems for serving recommendations:
        """)
        
        frameworks = pd.DataFrame({
            "Framework": ["Navi", "Product Mixer", "Timelines Aggregation", "TWML"],
            "Description": [
                "High-performance ML model serving (Rust)",
                "Framework for building content feeds",
                "Real-time feature aggregation",
                "Legacy ML framework (TensorFlow v1)"
            ],
            "Language": ["Rust", "Scala", "Scala", "Python"]
        })
        st.dataframe(frameworks, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🔄 Data Flow
    
    The recommendation system processes data through multiple stages:
    
    1. **Data Collection**: User actions, post metadata, social graphs
    2. **Feature Engineering**: Extract and aggregate features
    3. **Candidate Generation**: Identify potential posts to show
    4. **Ranking**: Score and order candidates
    5. **Filtering**: Apply safety and quality filters
    6. **Serving**: Deliver personalized timeline
    """)

def show_simclusters():
    """SimClusters algorithm page"""
    st.title("🌐 SimClusters - Community Detection")
    
    st.markdown("""
    ## What is SimClusters?
    
    SimClusters is Twitter's community detection algorithm that identifies groups 
    of users with similar interests and creates sparse embeddings based on these communities.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🎯 Purpose
        
        - Detect communities of users with shared interests
        - Create interpretable user and post embeddings
        - Power recommendations across multiple surfaces
        - Enable "similar to" and "people also viewed" features
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🔧 How It Works
        
        1. Analyze user follow graphs
        2. Identify dense subgraphs (communities)
        3. Assign users to communities
        4. Create sparse embedding vectors
        5. Use embeddings for similarity matching
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📊 Community Representation
    
    SimClusters represents users and posts as sparse vectors where each dimension 
    corresponds to a community. The values indicate the strength of association 
    with that community.
    """)
    
    # Example visualization
    st.markdown("### Example Community Embedding")
    
    example_data = pd.DataFrame({
        "Community ID": [1, 5, 12, 23, 45],
        "Community Theme": ["Tech", "Sports", "Politics", "Entertainment", "Gaming"],
        "User Score": [0.85, 0.12, 0.03, 0.45, 0.67],
        "Post Score": [0.92, 0.05, 0.01, 0.38, 0.71]
    })
    
    st.dataframe(example_data, use_container_width=True, hide_index=True)
    
    st.markdown("""
    ### 🎯 Applications
    
    - **For You Timeline**: Find posts from communities you engage with
    - **Who to Follow**: Suggest users from your interest communities
    - **Similar Posts**: Identify related content
    - **Topic Detection**: Automatically categorize posts
    """)

def show_twhin():
    """TwHIN embeddings page"""
    st.title("🕸️ TwHIN - Dense Graph Embeddings")
    
    st.markdown("""
    ## Twitter Heterogeneous Information Network (TwHIN)
    
    TwHIN creates dense, low-dimensional embeddings for users and posts by 
    modeling the entire Twitter graph as a heterogeneous information network.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🌟 Key Features
        
        - **Dense Embeddings**: Compact vector representations
        - **Multi-Type Nodes**: Users, posts, topics, hashtags
        - **Multiple Edge Types**: Follows, likes, retweets, replies
        - **Contextual**: Captures complex relationships
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🔍 Advantages Over SimClusters
        
        - More compact representation
        - Captures nuanced relationships
        - Better for cold-start users
        - Handles multiple entity types
        - Learns from diverse interactions
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🏗️ Architecture
    
    TwHIN uses graph neural networks to learn embeddings that preserve 
    structural and semantic information from the Twitter graph.
    """)
    
    st.markdown("""
    ### Training Process:
    
    1. **Graph Construction**: Build heterogeneous graph from Twitter data
    2. **Sampling**: Generate training samples using random walks
    3. **Model Training**: Learn embeddings using graph neural networks
    4. **Serving**: Deploy embeddings for real-time recommendations
    
    ### Use Cases:
    
    - **Similarity Search**: Find similar users or posts
    - **Recommendation**: Suggest content based on embedding similarity
    - **Clustering**: Group related entities
    - **Representation Learning**: Input features for downstream models
    """)

def show_trust_safety():
    """Trust and Safety models page"""
    st.title("🛡️ Trust & Safety Models")
    
    st.markdown("""
    ## Content Moderation & Safety
    
    Twitter's Trust & Safety models protect users by detecting and filtering 
    inappropriate, harmful, or policy-violating content.
    """)
    
    tab1, tab2, tab3 = st.tabs(["NSFW Detection", "Toxicity Detection", "Abuse Detection"])
    
    with tab1:
        st.markdown("""
        ### 🔞 NSFW (Not Safe For Work) Detection
        
        Identifies and filters adult or sensitive content to protect users.
        """)
        
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        #### Detection Types:
        - **NSFW Media**: Images and videos containing adult content
        - **NSFW Text**: Posts with explicit language or themes
        - **Sensitive Media**: Violence, gore, or disturbing content
        
        #### Actions:
        - Content warnings
        - Opt-in viewing
        - Age restrictions
        - Complete removal for policy violations
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        ### ☠️ Toxicity Detection
        
        Identifies toxic, hateful, or abusive language in posts.
        """)
        
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        #### Model Features:
        - Multi-label classification
        - Context-aware analysis
        - Multiple severity levels
        - Language-specific models
        
        #### Toxicity Categories:
        - Harassment
        - Hate speech
        - Threats
        - Self-harm
        - Spam
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        ### 🚫 Abusive Behavior Detection
        
        Identifies patterns of abusive behavior and coordinated manipulation.
        """)
        
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        #### Detection Areas:
        - Coordinated harassment campaigns
        - Spam and bot networks
        - Impersonation
        - Platform manipulation
        - Ban evasion
        
        #### Response Actions:
        - Account suspension
        - Content removal
        - Rate limiting
        - Search/recommendation filtering
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🔬 Technical Approach
    
    Trust & Safety models use:
    - **Deep Learning**: Neural networks for content classification
    - **Ensemble Methods**: Multiple models for robust detection
    - **Human Review**: Escalation to human moderators
    - **Continuous Learning**: Models updated with new patterns
    """)

def show_real_graph():
    """Real Graph algorithm page"""
    st.title("👥 Real Graph - User Interaction Prediction")
    
    st.markdown("""
    ## Predicting User Interactions
    
    Real Graph is a machine learning model that predicts the likelihood of 
    user A interacting with user B's content.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 📊 Predicted Interactions
        
        - **Retweets**: Will user retweet?
        - **Replies**: Will user reply?
        - **Likes**: Will user like?
        - **Clicks**: Will user click?
        - **Profile Visits**: Will user view profile?
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🎯 Input Features
        
        - Historical interactions
        - Social graph connections
        - Content similarity
        - Temporal patterns
        - User preferences
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🔄 How It's Used
    
    Real Graph scores are used throughout the recommendation pipeline:
    """)
    
    usage_data = pd.DataFrame({
        "Stage": ["Candidate Generation", "Ranking", "Filtering", "Follow Recommendations"],
        "Purpose": [
            "Find users whose content you're likely to engage with",
            "Boost posts from users with high interaction probability",
            "Filter out low-quality connections",
            "Suggest users you're likely to engage with"
        ],
        "Impact": ["High", "Very High", "Medium", "High"]
    })
    
    st.dataframe(usage_data, use_container_width=True, hide_index=True)
    
    st.markdown("""
    ### 💡 Key Benefits
    
    - **Personalization**: Tailored to each user's interaction patterns
    - **Dynamic**: Updates as relationships evolve
    - **Predictive**: Anticipates future interactions
    - **Scalable**: Efficient computation for millions of users
    """)

def show_tweepcred():
    """TweepCred algorithm page"""
    st.title("⭐ TweepCred - User Reputation System")
    
    st.markdown("""
    ## PageRank-Based User Reputation
    
    TweepCred is Twitter's implementation of the PageRank algorithm, adapted 
    to calculate user reputation scores based on the social graph.
    """)
    
    st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 📐 Algorithm Basics
    
    TweepCred uses a modified PageRank algorithm where:
    - **Nodes**: Twitter users
    - **Edges**: Follow relationships
    - **Score**: Reputation based on followers' reputation
    - **Damping**: Prevents manipulation and ensures convergence
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✨ What Influences TweepCred?
        
        **Positive Factors:**
        - Being followed by high-reputation users
        - Follower quality over quantity
        - Organic growth patterns
        - Engagement from credible accounts
        
        **Negative Factors:**
        - Spam-like behavior
        - Bot followers
        - Sudden unnatural growth
        - Low engagement rates
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Applications
        
        **Recommendation Systems:**
        - Boost content from high-reputation users
        - Filter low-quality accounts
        - Prioritize credible sources
        
        **Trust & Safety:**
        - Identify suspicious accounts
        - Detect coordinated networks
        - Anti-spam measures
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📊 Score Distribution
    
    TweepCred scores follow a power-law distribution, where most users have 
    relatively low scores and a small percentage have very high scores.
    """)
    
    score_ranges = pd.DataFrame({
        "Score Range": ["0-10", "10-50", "50-100", "100-500", "500+"],
        "Percentile": ["0-50%", "50-80%", "80-95%", "95-99%", "99-100%"],
        "Description": [
            "New or low-activity users",
            "Regular users with modest following",
            "Active users with engaged audience",
            "Influential users in niches",
            "Highly influential accounts"
        ]
    })
    
    st.dataframe(score_ranges, use_container_width=True, hide_index=True)

def show_search_ranking():
    """Search and ranking page"""
    st.title("📊 Search & Ranking Systems")
    
    st.markdown("""
    ## How Posts Are Discovered and Ranked
    
    Twitter's search and ranking systems determine which posts appear in 
    search results and how they're ordered.
    """)
    
    tab1, tab2, tab3 = st.tabs(["Earlybird Search", "Light Ranker", "Heavy Ranker"])
    
    with tab1:
        st.markdown("""
        ### 🔍 Earlybird - Real-Time Search Index
        
        Earlybird is Twitter's custom-built real-time search engine.
        """)
        
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        #### Key Features:
        - **Real-Time Indexing**: Posts searchable within seconds
        - **In-Network Search**: Find posts from followed accounts
        - **Distributed Architecture**: Scales to billions of posts
        - **Temporal Ordering**: Recent posts prioritized
        
        #### Capabilities:
        - Full-text search
        - Hashtag search
        - User search
        - Advanced filters (date, media, etc.)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        ### ⚡ Light Ranker - Fast Initial Ranking
        
        The Light Ranker quickly scores candidates to reduce the pool for heavy ranking.
        """)
        
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        #### Purpose:
        - Reduce candidates from thousands to hundreds
        - Fast inference (< 1ms per post)
        - Balance quality and performance
        - Pre-filter obviously irrelevant content
        
        #### Features Used:
        - Post recency
        - Author reputation (TweepCred)
        - Basic engagement signals
        - Static features
        - Simple interaction patterns
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        ### 🎯 Heavy Ranker - Deep Neural Ranking
        
        The Heavy Ranker is a sophisticated neural network that produces final rankings.
        """)
        
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        #### Architecture:
        - Multi-task learning
        - Deep neural networks
        - Thousands of features
        - Personalized predictions
        
        #### Predicted Outcomes:
        - Probability of like
        - Probability of retweet
        - Probability of reply
        - Probability of negative feedback
        - Probability of report
        - Time spent viewing
        
        #### Feature Categories:
        - User features (history, preferences)
        - Post features (content, metadata)
        - Author features (reputation, stats)
        - Graph features (social connections)
        - Real-time features (trending, virality)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🔄 Ranking Pipeline
    
    1. **Query Processing**: Parse and understand search query
    2. **Candidate Retrieval**: Fetch relevant posts from Earlybird
    3. **Light Ranking**: Quick scoring to reduce candidates
    4. **Feature Enrichment**: Compute additional features
    5. **Heavy Ranking**: Deep model inference
    6. **Post-Processing**: Apply business logic and filters
    7. **Serving**: Return ranked results
    """)

def show_recommendations():
    """Recommendations page"""
    st.title("💡 Recommendation Systems")
    
    st.markdown("""
    ## Serving Personalized Content
    
    Twitter's recommendation systems power multiple surfaces including 
    notifications, who to follow, and topic suggestions.
    """)
    
    tab1, tab2, tab3 = st.tabs(["Push Notifications", "Follow Recommendations", "GraphJet"])
    
    with tab1:
        st.markdown("""
        ### 📱 Push Notification Recommendations
        
        The Push Service determines which notifications users receive.
        """)
        
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        #### Notification Types:
        - **Post Recommendations**: Tweets you might like
        - **Topic Updates**: News in your interests
        - **Social Updates**: Activity from connections
        - **Engagement**: Replies, likes on your posts
        - **Trending**: Popular topics and events
        
        #### Ranking Models:
        - **Light Ranker**: Fast filtering of candidates
        - **Heavy Ranker**: Multi-task model predicting:
          - Open probability
          - Engagement probability
          - Negative feedback probability
        
        #### Optimization Goals:
        - Maximize user engagement
        - Respect notification preferences
        - Avoid notification fatigue
        - Deliver timely, relevant content
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        ### 👤 Follow Recommendations Service (FRS)
        
        Suggests accounts users might want to follow.
        """)
        
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        #### Candidate Sources:
        - **Social Graph**: Friends of friends
        - **SimClusters**: Users in same communities
        - **Real Graph**: High interaction probability
        - **Topic-Based**: Users posting about your interests
        - **Trending**: Popular accounts gaining traction
        
        #### Ranking Factors:
        - Real Graph score
        - TweepCred reputation
        - Content quality
        - Mutual connections
        - Topic overlap
        - Recent activity
        
        #### Surfaces:
        - Who to Follow module
        - Profile visit suggestions
        - Onboarding flow
        - Related accounts
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        ### 🚀 GraphJet - In-Memory Graph Processing
        
        GraphJet powers real-time recommendations using in-memory graph traversal.
        """)
        
        st.markdown('<div class="algorithm-card">', unsafe_allow_html=True)
        st.markdown("""
        #### Technology:
        - **In-Memory**: Entire graph in RAM for speed
        - **Real-Time Updates**: Ingests actions immediately
        - **Graph Traversal**: Efficient path finding
        - **Temporal**: Considers recency of interactions
        
        #### Applications:
        - **UTEG** (User-Tweet-Entity-Graph): Post recommendations
        - **User-User Graph**: Follow suggestions
        - **User-Video Graph**: Video recommendations
        - **User-Tweet Graph**: Related tweets
        
        #### Advantages:
        - Extremely low latency (<10ms)
        - Captures latest trends
        - Personalized in real-time
        - Scalable to billions of edges
        """)
        st.markdown('</div>', unsafe_allow_html=True)

def show_timeline_architecture():
    """Timeline architecture page"""
    st.title("📈 For You Timeline Architecture")
    
    st.markdown("""
    ## End-to-End Timeline Generation
    
    The For You Timeline is Twitter's main product surface, powered by a complex 
    pipeline that combines multiple algorithms and services.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🔄 Pipeline Stages
    """)
    
    stages = [
        {
            "stage": "1️⃣ Candidate Sourcing",
            "description": "Generate initial pool of candidate posts",
            "components": [
                "**In-Network**: Posts from followed accounts (Earlybird)",
                "**Out-of-Network**: Posts from non-followed accounts",
                "**UTEG**: Graph-based candidates (GraphJet)",
                "**FRS**: Candidates from recommended users",
                "**SimClusters**: Community-based candidates"
            ]
        },
        {
            "stage": "2️⃣ Light Ranking",
            "description": "Quick filtering to manageable size",
            "components": [
                "**Fast Model**: Simple features, quick inference",
                "**Goal**: Reduce from ~1500 to ~500 candidates",
                "**Time Budget**: ~1ms per candidate",
                "**Features**: Static and cached features"
            ]
        },
        {
            "stage": "3️⃣ Heavy Ranking",
            "description": "Deep neural network ranking",
            "components": [
                "**Complex Model**: Thousands of features",
                "**Multi-Task**: Predicts engagement types",
                "**Goal**: Final ordering of candidates",
                "**Time Budget**: ~50ms total",
                "**Output**: Ranked list with scores"
            ]
        },
        {
            "stage": "4️⃣ Heuristics & Filtering",
            "description": "Apply business logic and filters",
            "components": [
                "**Visibility Filters**: Remove policy-violating content",
                "**Diversity**: Ensure author and content diversity",
                "**Freshness**: Balance new and relevant posts",
                "**In-Network Bias**: Favor followed accounts",
                "**Feedback**: Apply user feedback signals"
            ]
        },
        {
            "stage": "5️⃣ Mixing & Serving",
            "description": "Final timeline assembly",
            "components": [
                "**Blending**: Mix in-network and out-of-network",
                "**Insertion**: Add ads and other content",
                "**Personalization**: Apply user preferences",
                "**Caching**: Cache for quick delivery",
                "**A/B Testing**: Experiment with variations"
            ]
        }
    ]
    
    for stage_info in stages:
        with st.expander(stage_info["stage"] + " - " + stage_info["description"], expanded=False):
            for component in stage_info["components"]:
                st.markdown("- " + component)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📊 Key Metrics
    
    The timeline optimization focuses on multiple metrics:
    """)
    
    metrics_data = pd.DataFrame({
        "Metric": ["Positive Engagement", "Negative Feedback", "Time Spent", "Retention", "Diversity"],
        "Definition": [
            "Likes, retweets, replies, bookmarks",
            "Mutes, blocks, 'not interested', reports",
            "Total time viewing timeline",
            "User returns to app",
            "Variety of authors and topics"
        ],
        "Optimization": ["Maximize", "Minimize", "Maximize", "Maximize", "Maximize"]
    })
    
    st.dataframe(metrics_data, use_container_width=True, hide_index=True)
    
    st.markdown("""
    ## ⚡ Performance Requirements
    
    The For You Timeline must meet strict performance requirements:
    - **Latency**: < 1 second end-to-end
    - **Throughput**: Millions of requests per second
    - **Freshness**: Index new posts within seconds
    - **Availability**: 99.9%+ uptime
    - **Personalization**: Unique for each user
    """)
    
    st.markdown("---")
    
    st.info("""
    **💡 Fun Fact**: The For You Timeline processes billions of candidates per day 
    and evaluates hundreds of millions of ML model predictions to surface the 
    most relevant content to each user!
    """)

if __name__ == "__main__":
    main()
