# Twitter Algorithm Explorer - UI Application

A comprehensive web-based user interface to explore and understand Twitter's (X) open-source recommendation algorithms.

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Install required dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

Run the Streamlit application:

```bash
streamlit run ui_app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

## 📖 Features

The UI Application provides interactive exploration of the following algorithm components:

### 🏠 Home
- Welcome page with overview
- Quick statistics
- Navigation guide

### 🔍 Overview
- System architecture
- Core components breakdown
- Data flow visualization
- Component categorization

### 🌐 SimClusters
- Community detection algorithm
- Sparse embeddings
- Use cases and applications
- Example visualizations

### 🕸️ TwHIN Embeddings
- Dense graph embeddings
- Heterogeneous information networks
- Training process
- Comparison with SimClusters

### 🛡️ Trust & Safety
- NSFW content detection
- Toxicity detection models
- Abusive behavior identification
- Content moderation pipeline

### 👥 Real Graph
- User interaction prediction
- Feature engineering
- Applications in ranking
- Personalization benefits

### ⭐ TweepCred
- PageRank-based reputation
- Score calculation
- Influence factors
- Use cases

### 📊 Search & Ranking
- Earlybird search engine
- Light ranking models
- Heavy ranking neural networks
- Multi-stage pipeline

### 💡 Recommendations
- Push notification system
- Follow recommendations
- GraphJet technology
- Real-time processing

### 📈 Timeline Architecture
- End-to-end For You Timeline
- Candidate sourcing
- Ranking stages
- Filtering and mixing
- Performance metrics

## 🎯 Use Cases

This UI application is useful for:

- **Learning**: Understand how Twitter's recommendation algorithms work
- **Research**: Study social media recommendation systems
- **Development**: Reference for building similar systems
- **Documentation**: Interactive documentation of the algorithm
- **Education**: Teaching tool for ML and recommendation systems

## 🏗️ Technical Details

### Technology Stack

- **Frontend Framework**: Streamlit
- **Language**: Python 3.8+
- **Styling**: Custom CSS
- **Data Visualization**: Pandas DataFrames

### Project Structure

```
.
├── ui_app.py          # Main Streamlit application
├── requirements.txt   # Python dependencies
└── UI_README.md      # This file
```

## 🤝 Contributing

The Twitter Algorithm is an open-source project. Contributions to improve the UI application are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📚 Resources

- [Twitter Engineering Blog](https://blog.x.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm)
- [Main Repository README](./README.md)
- [Algorithm Documentation](./docs/)

## 📄 License

This project follows the same license as the main Twitter Algorithm repository. See [COPYING](./COPYING) for details.

## 🐛 Issues

If you encounter any issues with the UI application, please:

1. Check that all dependencies are installed
2. Ensure you're using Python 3.8 or higher
3. Try clearing Streamlit cache: `streamlit cache clear`
4. Report issues on the GitHub repository

## 💡 Tips

- Use the sidebar to navigate between different algorithm components
- Each page provides detailed explanations and visualizations
- The application is read-only and safe to explore
- Refresh the page to reset to the home screen

## 🎨 Customization

You can customize the UI by modifying:

- **Colors**: Edit the CSS in `ui_app.py` under the `st.markdown()` with custom styles
- **Content**: Update the text and descriptions in each page function
- **Layout**: Modify the Streamlit components and layout structure

## 🔧 Troubleshooting

### Application won't start
- Verify Python version: `python --version` (should be 3.8+)
- Reinstall dependencies: `pip install -r requirements.txt --upgrade`

### Page doesn't load
- Check browser console for errors
- Try a different browser
- Clear browser cache

### Missing content
- Ensure you're in the correct directory
- Verify all files are present

## 📞 Support

For questions or support:
- Review the main [README.md](./README.md)
- Check the [official blog post](https://blog.x.com/en_us/topics/company/2023/a-new-era-of-transparency-for-twitter)
- Open an issue on GitHub

---

**Built with ❤️ for the open-source community**
