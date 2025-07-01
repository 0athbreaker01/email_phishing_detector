import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def load_and_prepare_data():
    try:
        df = pd.read_csv("emails.csv")
        print(f"Dataset loaded successfully with {len(df)} emails")

        X = df["text"]
        y = df["label"]

        print(f"Label distribution:")
        print(f"Legitimate emails (0): {sum(y == 0)}")
        print(f"Phishing emails (1): {sum(y == 1)}")

        return X, y

    except FileNotFoundError:
        print("Error: emails.csv not found. Please run create_dataset.py first.")
        return None, None


def create_and_train_pipeline(X_train, y_train):
    pipeline = Pipeline(
        [
            (
                "vectorizer",
                TfidfVectorizer(
                    max_features=5000,
                    stop_words="english",
                    ngram_range=(1, 2),
                    lowercase=True,
                    strip_accents="ascii",
                ),
            ),
            (
                "classifier",
                LogisticRegression(
                    random_state=42,
                    max_iter=1000,
                    C=1.0,
                ),
            ),
        ]
    )

    print("Training the model...")

    pipeline.fit(X_train, y_train)

    print("Model training completed!")

    return pipeline


def evaluate_model(pipeline, X_test, y_test):
    y_pred = pipeline.predict(X_test)
    y_pred_proba = pipeline.predict_proba(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Evaluation:")
    print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")

    print("\nClassification Report:")
    print(
        classification_report(y_test, y_pred, target_names=["Legitimate", "Phishing"])
    )

    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    print("\nSample Predictions:")
    for i in range(min(5, len(X_test))):
        email_text = (
            X_test.iloc[i][:100] + "..."
            if len(X_test.iloc[i]) > 100
            else X_test.iloc[i]
        )
        actual_label = "Phishing" if y_test.iloc[i] == 1 else "Legitimate"
        predicted_label = "Phishing" if y_pred[i] == 1 else "Legitimate"
        confidence = max(y_pred_proba[i]) * 100

        print(f"\nEmail: {email_text}")
        print(
            f"Actual: {actual_label}, Predicted: {predicted_label}, Confidence: {confidence:.1f}%"
        )


def save_model(pipeline, filename="phishing_model.joblib"):
    try:
        joblib.dump(pipeline, filename)
        print(f"\nModel saved successfully as '{filename}'")
        print(
            "This file contains both the TfidfVectorizer and LogisticRegression components."
        )
    except Exception as e:
        print(f"Error saving model: {e}")


def main():
    print("=" * 50)
    print("PHISHING EMAIL DETECTOR - MODEL TRAINING")
    print("=" * 50)

    X, y = load_and_prepare_data()

    if X is None or y is None:
        return

    print("\nSplitting data into train/test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    print(f"Training set: {len(X_train)} emails")
    print(f"Testing set: {len(X_test)} emails")

    pipeline = create_and_train_pipeline(X_train, y_train)

    evaluate_model(pipeline, X_test, y_test)

    save_model(pipeline)

    print("\n" + "=" * 50)
    print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
    print("You can now run the Streamlit app: streamlit run app.py")
    print("=" * 50)


if __name__ == "__main__":
    main()
