

## 📈 Steps Followed

1. **Data Preprocessing**
   - Loaded CSV file
   - Removed unnecessary columns (e.g., ID)
   - Converted target labels (M = 1, B = 0)

2. **Train-Test Split**
   - 80% training and 20% testing

3. **Feature Scaling**
   - Standardized all feature columns using StandardScaler

4. **Model Training**
   - Trained a LogisticRegression model on scaled data

5. **Evaluation Metrics**
   - Confusion Matrix
   - Precision & Recall
   - ROC-AUC Score
   - Classification Report
   - ROC Curve

6. **Threshold Tuning**
   - Adjusted threshold from default `0.5` to `0.3`
   - Compared performance and confusion matrix

7. **Sigmoid Function**
   - Visualized sigmoid function to explain logistic regression

---

## ✅ Results Summary

| Metric         | Value      |
|----------------|------------|
| Precision      | 0.9762     |
| Recall         | 0.9535     |
| ROC-AUC Score  | 0.9974     |

Precision: ~0.97 — most predicted malignant tumors were correct.

Recall: ~0.95 — most actual malignant tumors were caught.

ROC AUC: ~0.99 — model is highly effective in separating benign and malignant classes.
