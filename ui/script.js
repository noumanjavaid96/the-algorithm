// Algorithm details data
const algorithmDetails = {
    simclusters: {
        title: "SimClusters",
        description: "SimClusters is a community detection algorithm that creates sparse embeddings by grouping similar users and content into communities.",
        howItWorks: [
            "Identifies communities of users with similar interests",
            "Assigns users and tweets to multiple communities with varying strengths",
            "Uses these communities as dimensions for embedding spaces",
            "Enables efficient similarity calculations between users and content"
        ],
        useCases: [
            "Finding similar tweets and users",
            "Candidate generation for recommendations",
            "Topic modeling and clustering",
            "Personalized content discovery"
        ],
        technicalDetails: "SimClusters uses a custom implementation of community detection algorithms on the Twitter social graph. It processes billions of edges and identifies thousands of communities that represent different interests and topics on the platform.",
        codeLocation: "src/scala/com/twitter/simclusters_v2/"
    },
    twhin: {
        title: "TwHIN (Twitter Heterogeneous Information Network)",
        description: "TwHIN creates dense knowledge graph embeddings for users and tweets using graph neural networks.",
        howItWorks: [
            "Models the Twitter graph as a heterogeneous network with multiple node and edge types",
            "Uses graph neural network techniques to learn dense embeddings",
            "Captures complex relationships between users, tweets, and other entities",
            "Generates embeddings that encode semantic similarity"
        ],
        useCases: [
            "Semantic similarity search",
            "Cross-entity recommendations",
            "Content understanding and classification",
            "User interest modeling"
        ],
        technicalDetails: "TwHIN leverages state-of-the-art graph neural network architectures to learn from the heterogeneous Twitter graph containing billions of interactions. The model is trained on large-scale distributed systems.",
        codeLocation: "External repository: github.com/twitter/the-algorithm-ml/projects/twhin/"
    },
    realgraph: {
        title: "Real Graph",
        description: "Real Graph predicts the likelihood of meaningful interactions between users on the platform.",
        howItWorks: [
            "Analyzes historical interaction patterns between users",
            "Uses machine learning to predict future interactions",
            "Considers multiple types of engagements (replies, retweets, likes)",
            "Updates predictions in near real-time"
        ],
        useCases: [
            "Follow recommendations",
            "Content ranking and filtering",
            "Network quality assessment",
            "Spam and abuse detection"
        ],
        technicalDetails: "The Real Graph model uses logistic regression and gradient boosted decision trees to predict interaction probabilities. It processes features from the graph structure, user behavior, and content characteristics.",
        codeLocation: "src/scala/com/twitter/interaction_graph/"
    },
    tweepcred: {
        title: "TweepCred",
        description: "TweepCred is a PageRank-based algorithm that calculates user reputation scores on the platform.",
        howItWorks: [
            "Applies PageRank algorithm to the Twitter follow graph",
            "Weights edges based on interaction quality",
            "Iteratively computes reputation scores",
            "Produces a single reputation score per user"
        ],
        useCases: [
            "Ranking search results",
            "Spam and bot detection",
            "Content quality signals",
            "Recommendation filtering"
        ],
        technicalDetails: "TweepCred runs as a batch job on the entire Twitter graph using MapReduce. It incorporates signals about account age, verification status, and engagement patterns to refine the basic PageRank calculation.",
        codeLocation: "src/scala/com/twitter/graph/batch/job/tweepcred/"
    },
    "trust-safety": {
        title: "Trust & Safety Models",
        description: "A suite of machine learning models designed to detect and filter harmful content including NSFW material, abusive language, and other policy violations.",
        howItWorks: [
            "Analyzes text, images, and video content",
            "Uses deep learning classifiers for content classification",
            "Provides probability scores for different violation types",
            "Runs in real-time and batch modes"
        ],
        useCases: [
            "NSFW content detection in images and videos",
            "Toxic and abusive language detection",
            "Automated content moderation",
            "Policy violation enforcement"
        ],
        technicalDetails: "The trust and safety models use convolutional neural networks for image analysis and transformer-based models for text analysis. They are trained on large labeled datasets and continuously updated with new examples.",
        codeLocation: "trust_and_safety_models/"
    },
    graphjet: {
        title: "GraphJet",
        description: "GraphJet is a real-time graph processing engine that maintains in-memory graphs of user interactions for fast traversal and recommendation generation.",
        howItWorks: [
            "Maintains multiple in-memory graphs of user-content interactions",
            "Updates graphs in real-time as users interact with content",
            "Performs fast graph traversals for recommendation generation",
            "Supports various graph algorithms like random walks and SALSA"
        ],
        useCases: [
            "Real-time tweet recommendations",
            "User-Tweet-Entity Graph (UTEG) candidate generation",
            "Follow recommendations",
            "Trending content detection"
        ],
        technicalDetails: "GraphJet is implemented in Java and uses custom memory management for efficient graph storage. It can handle billions of edges and millions of queries per second with sub-millisecond latency.",
        codeLocation: "External repository: github.com/twitter/GraphJet"
    },
    "heavy-ranker": {
        title: "Heavy Ranker",
        description: "A sophisticated neural network model that ranks candidate tweets for the For You timeline using thousands of features.",
        howItWorks: [
            "Takes candidates from multiple sources (~1500 tweets)",
            "Extracts thousands of features per tweet",
            "Uses a deep neural network to predict engagement probabilities",
            "Predicts multiple engagement types (likes, retweets, replies, etc.)",
            "Combines predictions into a single ranking score"
        ],
        useCases: [
            "Final ranking for For You timeline",
            "Personalized content ordering",
            "Quality filtering",
            "Engagement optimization"
        ],
        technicalDetails: "The Heavy Ranker is a multi-task learning model implemented in TensorFlow. It uses a deep feed-forward architecture with BatchNorm and is trained on billions of examples of user engagements.",
        codeLocation: "External repository: github.com/twitter/the-algorithm-ml/projects/home/recap/"
    },
    "light-ranker": {
        title: "Light Ranker",
        description: "A fast, lightweight ranking model used for initial candidate filtering before heavy ranking.",
        howItWorks: [
            "Processes thousands of candidate tweets quickly",
            "Uses a smaller set of features than Heavy Ranker",
            "Employs efficient model architecture for speed",
            "Filters candidates down to a manageable set for Heavy Ranker"
        ],
        useCases: [
            "Pre-filtering search results",
            "Initial candidate ranking in notifications",
            "Fast quality assessment",
            "Computational efficiency optimization"
        ],
        technicalDetails: "The Light Ranker uses logistic regression or small neural networks for fast inference. It runs at high throughput to handle millions of candidates efficiently.",
        codeLocation: "src/python/twitter/deepbird/projects/timelines/scripts/models/earlybird/"
    }
};

// Show algorithm detail in modal
function showAlgorithmDetail(algorithmKey) {
    const modal = document.getElementById('algorithmModal');
    const modalBody = document.getElementById('modalBody');
    const algorithm = algorithmDetails[algorithmKey];
    
    if (!algorithm) return;
    
    const detailHTML = `
        <div class="algorithm-detail">
            <h2>${algorithm.title}</h2>
            <p><strong>${algorithm.description}</strong></p>
            
            <h3>How It Works</h3>
            <ul>
                ${algorithm.howItWorks.map(item => `<li>${item}</li>`).join('')}
            </ul>
            
            <h3>Use Cases</h3>
            <ul>
                ${algorithm.useCases.map(item => `<li>${item}</li>`).join('')}
            </ul>
            
            <h3>Technical Details</h3>
            <p>${algorithm.technicalDetails}</p>
            
            <h3>Source Code</h3>
            <p>Location: <code>${algorithm.codeLocation}</code></p>
            ${algorithm.codeLocation.startsWith('External repository:') 
                ? `<a href="https://${algorithm.codeLocation.replace('External repository: ', '')}" 
                     target="_blank" 
                     class="code-link">View on GitHub</a>`
                : `<a href="https://github.com/twitter/the-algorithm/tree/main/${algorithm.codeLocation}" 
                     target="_blank" 
                     class="code-link">View on GitHub</a>`
            }
        </div>
    `;
    
    modalBody.innerHTML = detailHTML;
    modal.style.display = 'block';
}

// Close modal
function closeModal() {
    const modal = document.getElementById('algorithmModal');
    modal.style.display = 'none';
}

// Close modal when clicking outside
window.addEventListener('click', function(event) {
    const modal = document.getElementById('algorithmModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

// Close modal when pressing Escape key
window.addEventListener('keydown', function(event) {
    const modal = document.getElementById('algorithmModal');
    if (event.key === 'Escape' && modal.style.display === 'block') {
        closeModal();
    }
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add scroll-based navbar background
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.15)';
    } else {
        navbar.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
    }
});

// Add animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all algorithm cards and service cards
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.algorithm-card, .service-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s, transform 0.6s';
        observer.observe(card);
    });
    
    // Add keyboard support for algorithm cards
    document.querySelectorAll('.algorithm-card').forEach(card => {
        card.addEventListener('keydown', function(event) {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                this.click();
            }
        });
    });
});
