import streamlit as st
import joblib
import numpy as np
from lime import lime_text
from lime.lime_text import LimeTextExplainer
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SecureGuard Email Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_resource
def load_model():
   
    try:
        model = joblib.load("phishing_model.joblib")
        return model
    except FileNotFoundError:
        st.error("❌ Model file 'phishing_model.joblib' not found!")
        st.error(
            "Please run 'python train_model.py' first to train and save the model."
        )
        return None
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None


def predict_email(model, email_text):
    
    try:
        prediction = model.predict([email_text])[0]

        probabilities = model.predict_proba([email_text])[0]

        return prediction, probabilities
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        return None, None


def explain_prediction(model, email_text, num_features=10):
   
    try:
        explainer = LimeTextExplainer(
            class_names=["Legitimate", "Phishing"],
            feature_selection="auto",
            verbose=True,
        )

        explanation = explainer.explain_instance(
            text_instance=email_text,
            classifier_fn=model.predict_proba,
            num_features=num_features,
            labels=[0, 1],  
        )

        return explanation
    except Exception as e:
        st.error(f"Error generating explanation: {e}")
        return None


def display_prediction_results(prediction, probabilities):
    """
    Display the prediction results in a professional format.
    """
    st.markdown('<div class="analysis-section">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">Threat Assessment Results</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        if prediction == 1:
            st.markdown(
                """
            <div style='background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); 
                        color: white; padding: 1.5rem; border-radius: 8px; 
                        border: 1px solid #ef4444; margin-bottom: 1rem;'>
                <div style='font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem;'>
                    THREAT DETECTED
                </div>
                <div style='font-size: 0.875rem; opacity: 0.9;'>
                    This email exhibits characteristics consistent with phishing attacks
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
            <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                        color: white; padding: 1.5rem; border-radius: 8px; 
                        border: 1px solid #10b981; margin-bottom: 1rem;'>
                <div style='font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem;'>
                    LEGITIMATE EMAIL
                </div>
                <div style='font-size: 0.875rem; opacity: 0.9;'>
                    No suspicious patterns detected in this communication
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with col2:
        legitimate_prob = probabilities[0] * 100
        phishing_prob = probabilities[1] * 100

        st.markdown("**Confidence Metrics**")

        st.markdown(
            f"""
        <div style='background: #f8fafc; padding: 1rem; border-radius: 6px; border: 1px solid #e2e8f0; margin-bottom: 0.5rem;'>
            <div style='display: flex; justify-content: space-between; margin-bottom: 0.25rem;'>
                <span style='font-weight: 500;'>Legitimate</span>
                <span style='font-weight: 700; color: #059669;'>{legitimate_prob:.1f}%</span>
            </div>
            <div style='background: #e2e8f0; height: 6px; border-radius: 3px;'>
                <div style='background: #059669; height: 6px; border-radius: 3px; width: {legitimate_prob}%;'></div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
        <div style='background: #f8fafc; padding: 1rem; border-radius: 6px; border: 1px solid #e2e8f0;'>
            <div style='display: flex; justify-content: space-between; margin-bottom: 0.25rem;'>
                <span style='font-weight: 500;'>Phishing</span>
                <span style='font-weight: 700; color: #dc2626;'>{phishing_prob:.1f}%</span>
            </div>
            <div style='background: #e2e8f0; height: 6px; border-radius: 3px;'>
                <div style='background: #dc2626; height: 6px; border-radius: 3px; width: {phishing_prob}%;'></div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


def display_lime_explanation(explanation):
    
    st.markdown('<div class="analysis-section">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">Feature Analysis & Model Interpretation</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div style='background: #f1f5f9; padding: 1rem; border-radius: 6px; border-left: 4px solid #3b82f6; margin-bottom: 1rem;'>
        <div style='font-weight: 600; color: #1e40af; margin-bottom: 0.5rem;'>Analysis Methodology</div>
        <div style='font-size: 0.875rem; color: #475569;'>
            This visualization shows word-level feature importance using LIME (Local Interpretable Model-agnostic Explanations).
            Each word's influence on the classification decision is color-coded and weighted.
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🔴 Red highlights:** Phishing indicators")
    with col2:
        st.markdown("**🟢 Green highlights:** Legitimate indicators")

    explanation_html = explanation.as_html()

    custom_css = """
    <style>
    body {
        background-color: white !important;
        color: black !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    .lime-explanation {
        background-color: #ffffff !important;
        color: #000000 !important;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        line-height: 1.6;
        margin: 10px 0;
    }
    .lime-explanation table {
        background-color: white !important;
        color: black !important;
        border-collapse: collapse;
        width: 100% !important;
        margin: 10px 0 !important;
    }
    .lime-explanation th, .lime-explanation td {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ddd !important;
        padding: 12px !important;
        text-align: left !important;
        font-size: 14px !important;
    }
    .lime-explanation th {
        background-color: #f8f9fa !important;
        font-weight: bold !important;
        color: #495057 !important;
    }
    .lime-explanation .legend, .lime-explanation div {
        background-color: #f9f9f9 !important;
        color: black !important;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    /* Ensure text highlighting is visible with better contrast */
    .lime-explanation span[style*="background-color"] {
        padding: 3px 6px !important;
        border-radius: 4px !important;
        font-weight: bold !important;
        border: 1px solid rgba(0,0,0,0.1) !important;
        color: black !important;
    }
    /* Improve visibility of charts/graphs */
    .lime-explanation svg {
        background-color: white !important;
    }
    .lime-explanation svg text {
        fill: black !important;
        font-size: 12px !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }
    /* Make sure all text is black and readable */
    .lime-explanation *, .lime-explanation p, .lime-explanation div {
        color: black !important;
        font-size: 14px !important;
    }
    /* Improve bar chart visibility */
    .lime-explanation .legend-label {
        color: black !important;
        font-weight: bold !important;
    }
    /* Ensure proper spacing and readability */
    .lime-explanation h1, .lime-explanation h2, .lime-explanation h3 {
        color: #333 !important;
        margin: 15px 0 10px 0 !important;
    }
    /* Fix any text that might be invisible */
    .lime-explanation span, .lime-explanation p, .lime-explanation td {
        color: #000 !important;
    }
    </style>
    """

    enhanced_html = f"""
    {custom_css}
    <div class="lime-explanation">
        {explanation_html}
    </div>
    """

    components.html(enhanced_html, height=900, scrolling=True)
    st.markdown("</div>", unsafe_allow_html=True)


def display_feature_importance(explanation):
    """
    Display feature importance in a professional table format.
    """
    st.markdown('<div class="analysis-section">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">Detailed Feature Analysis</div>',
        unsafe_allow_html=True,
    )

    explanation_list = explanation.as_list()

    if explanation_list:
        st.markdown("**Word-level influence ranking and impact scores:**")

        import pandas as pd

        features_data = []
        for word, importance in explanation_list:
            influence = "Phishing" if importance > 0 else "Legitimate"
            features_data.append(
                {
                    "Feature": word,
                    "Impact Score": f"{importance:.4f}",
                    "Classification Bias": influence,
                    "Confidence": f"{abs(importance):.3f}",
                }
            )

        df = pd.DataFrame(features_data)
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "Feature": st.column_config.TextColumn("Feature", width="medium"),
                "Impact Score": st.column_config.NumberColumn(
                    "Impact Score", format="%.4f"
                ),
                "Classification Bias": st.column_config.TextColumn(
                    "Classification Bias", width="small"
                ),
                "Confidence": st.column_config.ProgressColumn(
                    "Confidence", min_value=0, max_value=1
                ),
            },
        )

    st.markdown("</div>", unsafe_allow_html=True)


def main():
   
    st.markdown(
        """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 0;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 10px 10px;
    }
    
    .header-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
        color: white;
        text-align: center;
    }
    
    .header-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: white;
    }
    
    .header-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        font-weight: 400;
        opacity: 0.9;
        margin-bottom: 1rem;
    }
    
    .security-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        backdrop-filter: blur(10px);
    }
    
    .stats-container {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        text-align: center;
    }
    
    .stat-item {
        background: white;
        padding: 1rem;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
    }
    
    .stat-number {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2563eb;
        margin-bottom: 0.25rem;
    }
    
    .stat-label {
        font-size: 0.875rem;
        color: #64748b;
        font-weight: 500;
    }
    
    .analysis-section {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .section-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 0.5rem;
    }
    
    .sidebar .sidebar-content {
        background: #f1f5f9;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Custom button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: transform 0.2s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="main-header">
        <div class="header-content">
            <h1 class="header-title">SecureGuard Email Intelligence</h1>
            <p class="header-subtitle">Advanced Threat Detection with Machine Learning Analytics</p>
            <div class="security-badge">Enterprise-Grade Security • Real-time Analysis • Explainable AI</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="stats-container">
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-number">95.8%</div>
                <div class="stat-label">Detection Accuracy</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">240</div>
                <div class="stat-label">Training Samples</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">10</div>
                <div class="stat-label">Threat Categories</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">&lt;2s</div>
                <div class="stat-label">Analysis Time</div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    model = load_model()

    if model is None:
        st.stop()

    st.sidebar.markdown("### Test Samples")
    st.sidebar.markdown("Select pre-configured email samples for testing:")

    phishing_samples = [
        "Urgent action required: your account has been suspended. Click here to verify your details immediately.",
        "CONGRATULATIONS! You've won $50,000 in our monthly lottery! Click here to claim your prize before it expires in 24 hours.",
        "Security Alert: We've detected suspicious activity on your PayPal account. Please login immediately to secure your account at paypal-security.fake-link.com",
        "Your credit card ending in 4567 has been charged $899.99 for an iPhone purchase. If this wasn't you, click here to dispute the charge immediately.",
        "Final Notice: Your subscription to Netflix will be cancelled unless you update your payment information within 12 hours. Click here to update now.",
    ]

    legitimate_samples = [
        "Here is the meeting summary from yesterday. Please review the action items and let me know if you have questions.",
        "Your monthly statement for December 2024 is now available in your online banking portal. You can access it by logging into your account.",
        "Thank you for your order #ORD-2024-5678. Your package has been shipped and will arrive within 3-5 business days. Track your order using the provided tracking number.",
        "Reminder: Our quarterly team meeting is scheduled for Friday at 2:00 PM in Conference Room B. Please bring your project updates and Q4 reports.",
        "The system maintenance scheduled for this weekend has been completed successfully. All services are now fully operational. Thank you for your patience.",
    ]

    if "phishing_index" not in st.session_state:
        st.session_state.phishing_index = 0
    if "legitimate_index" not in st.session_state:
        st.session_state.legitimate_index = 0

    if st.sidebar.button("Load Threat Sample", type="secondary"):
        st.session_state.email_text = phishing_samples[st.session_state.phishing_index]
        st.session_state.phishing_index = (st.session_state.phishing_index + 1) % len(
            phishing_samples
        )

    if st.sidebar.button("Load Legitimate Sample", type="secondary"):
        st.session_state.email_text = legitimate_samples[
            st.session_state.legitimate_index
        ]
        st.session_state.legitimate_index = (
            st.session_state.legitimate_index + 1
        ) % len(legitimate_samples)

    with st.sidebar.expander("Sample Database"):
        st.write(f"**Threat Samples:** {len(phishing_samples)}")
        st.write(f"**Legitimate Samples:** {len(legitimate_samples)}")
        st.write("*Samples rotate automatically*")

    st.sidebar.markdown("### Analysis Configuration")
    num_features = st.sidebar.slider(
        "Feature Analysis Depth",
        min_value=5,
        max_value=20,
        value=10,
        help="Number of words to analyze in the explanation",
    )

    with st.sidebar.expander("System Information"):
        st.write("**Model:** Logistic Regression + TF-IDF")
        st.write("**Framework:** scikit-learn")
        st.write("**Explainability:** LIME")
        st.write("**Last Training:** Latest Dataset")

    st.markdown('<div class="analysis-section">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">Email Security Analysis</div>',
        unsafe_allow_html=True,
    )

    default_text = st.session_state.get("email_text", "")

    email_text = st.text_area(
        "Email Content",
        value=default_text,
        height=200,
        placeholder="Paste email content here for analysis...",
        help="Input the complete email content including headers, subject, and body text",
        label_visibility="collapsed",
    )

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        analyze_button = st.button("Run Security Analysis", type="primary")
    with col2:
        clear_button = st.button("Clear", type="secondary")
    with col3:
        if email_text:
            st.metric("Characters", len(email_text))

    if clear_button:
        st.session_state.email_text = ""
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    if analyze_button and email_text.strip():
        with st.spinner("Processing security analysis..."):
            prediction, probabilities = predict_email(model, email_text)

            if prediction is not None and probabilities is not None:
                display_prediction_results(prediction, probabilities)

                explanation = explain_prediction(model, email_text, num_features)

                if explanation is not None:
                    tab1, tab2 = st.tabs(["Visual Analysis", "Data Export"])

                    with tab1:
                        display_lime_explanation(explanation)

                    with tab2:
                        display_feature_importance(explanation)

    elif analyze_button and not email_text.strip():
        st.error("Please provide email content for analysis.")

    st.markdown("---")
    st.markdown(
        """
    <div style='background: #f8fafc; padding: 2rem; margin: 2rem -1rem -1rem -1rem; border-top: 1px solid #e2e8f0;'>
        <div style='max-width: 1200px; margin: 0 auto; text-align: center;'>
            <div style='color: #64748b; font-size: 0.875rem; margin-bottom: 1rem;'>
                <strong>SecureGuard Email Intelligence</strong> | Enterprise Security Platform
            </div>
            <div style='color: #94a3b8; font-size: 0.75rem;'>
                Powered by Machine Learning • LIME Explainability • Real-time Threat Detection
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()


