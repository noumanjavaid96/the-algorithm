# X's Recommendation Algorithm - Interactive UI

This is an interactive web-based UI application that provides comprehensive documentation and visualization of X's (formerly Twitter) open-source recommendation algorithm.

## Overview

The UI application showcases:
- **8 Core Algorithms**: SimClusters, TwHIN, Real Graph, TweepCred, Trust & Safety Models, GraphJet, Heavy Ranker, and Light Ranker
- **System Architecture**: Visual flow diagram of the "For You" timeline
- **Key Services**: Data services, candidate sources, and infrastructure components
- **Interactive Details**: Click on any algorithm card to view detailed information

## How to Run

### Option 1: Direct File Opening
Simply open the `index.html` file in your web browser:
```bash
# Navigate to the ui directory
cd ui

# Open in your default browser (Linux/Mac)
open index.html    # Mac
xdg-open index.html    # Linux

# Or just double-click index.html in your file explorer
```

### Option 2: Using a Local Web Server (Recommended)
For the best experience, run a local web server:

**Using Python 3:**
```bash
cd ui
python3 -m http.server 8000
```
Then open http://localhost:8000 in your browser.

**Using Python 2:**
```bash
cd ui
python -m SimpleHTTPServer 8000
```
Then open http://localhost:8000 in your browser.

**Using Node.js (http-server):**
```bash
# Install http-server globally
npm install -g http-server

cd ui
http-server -p 8000
```
Then open http://localhost:8000 in your browser.

**Using PHP:**
```bash
cd ui
php -S localhost:8000
```
Then open http://localhost:8000 in your browser.

## Features

### 1. Algorithm Cards
- Click on any algorithm card to see detailed information
- Each card includes:
  - Algorithm name and description
  - Category tag (e.g., Clustering, Graph Neural Network, etc.)
  - Hover effects for better interactivity

### 2. Algorithm Details Modal
When you click an algorithm card, a modal window displays:
- **Description**: What the algorithm does
- **How It Works**: Step-by-step explanation
- **Use Cases**: Practical applications
- **Technical Details**: Implementation specifics
- **Source Code Location**: Direct link to GitHub repository

### 3. System Architecture
- Visual flow diagram showing how the "For You" timeline is constructed
- Four main stages:
  1. Candidate Sources (Search Index, UTEG, FRS, Tweet Mixer)
  2. Ranking (Light Ranker, Heavy Ranker)
  3. Mixing & Filtering (Home Mixer, Visibility Filters)
  4. Final Timeline Delivery

### 4. Services Overview
- **Data Services**: TweetyPie, Unified User Actions, User Signal Service
- **Candidate Sources**: Search Index, UTEG, Follow Recommendations
- **Infrastructure**: Navi, Product Mixer, TWML

### 5. Responsive Design
- Fully responsive layout that works on desktop, tablet, and mobile devices
- Smooth scrolling navigation
- Animated card appearances on scroll

## File Structure

```
ui/
├── index.html    # Main HTML file
├── styles.css    # Styling and layout
├── script.js     # Interactive functionality
└── README.md     # This file
```

## Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS Grid, Flexbox, and animations
- **JavaScript (ES6)**: Interactive features and DOM manipulation
- **No external dependencies**: Pure vanilla JavaScript for simplicity

## Browser Compatibility

The UI is compatible with all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Opera (latest)

## Customization

You can easily customize the UI by editing:
- **styles.css**: Change colors, fonts, spacing, etc.
- **script.js**: Modify algorithm details, add new algorithms, or change behavior
- **index.html**: Update content, add sections, or reorganize layout

### Adding a New Algorithm

To add a new algorithm to the UI:

1. Add an algorithm card in `index.html`:
```html
<div class="algorithm-card" onclick="showAlgorithmDetail('your-algorithm')">
    <h3>Your Algorithm</h3>
    <p>Brief description</p>
    <span class="algorithm-tag">Category</span>
</div>
```

2. Add algorithm details in `script.js`:
```javascript
const algorithmDetails = {
    // ... existing algorithms
    'your-algorithm': {
        title: "Your Algorithm",
        description: "...",
        howItWorks: ["...", "..."],
        useCases: ["...", "..."],
        technicalDetails: "...",
        codeLocation: "path/to/code/"
    }
};
```

## Contributing

This UI application is part of X's open-source recommendation algorithm repository. For contributions, please refer to the main repository's contribution guidelines.

## License

This project follows the same license as the main X algorithm repository.

## Links

- [Main Repository](https://github.com/twitter/the-algorithm)
- [X Engineering Blog](https://blog.x.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm)
- [Algorithm ML Repository](https://github.com/twitter/the-algorithm-ml)

## Screenshots

The UI includes:
- A hero section with project overview
- 8 interactive algorithm cards
- A system architecture visualization
- Service component documentation
- Detailed modal views for each algorithm

Enjoy exploring X's recommendation algorithm! 🚀
