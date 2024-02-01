# Team Process Mapping Take-Home Task: Pranshu Kumar

Goal: In this pre-test, you will first read brief selections from two social science papers (Step 1). You will then go through an end-to-end implementation of a feature and apply it to a dataset of team conversations (Step 2). Finally, you will write a reflection on how well you think this feature extractor performed on the data, as well as how well it performs in operationalizing social science constructs (Step 3).

The idea behind this task is to give you a flavor of the scope of our work — to show how we take inspiration from social science, then apply these ideas in a computational way.

Please write your reflection in this README document.

## 1. High-Level Questions
1a. Which dataset did you choose?

> I ran the feature extractor on both datasets, however my answers below pertain to only CSOP data.

1b. What method(s) did you choose? In 1-2 sentences each, describe your sentiment analysis method(s).

> I employed the Roberta Model from Hugging Face for sentiment analysis. This model utilizes a deep neural network architecture pretrained on a large corpus of text data and fine-tuned for sentiment prediction tasks. It leverages transformer-based attention mechanisms to capture contextual information and relationships within the input text, enabling robust sentiment analysis. \
> In addition to the Roberta Model from Hugging Face, I also incorporated the SentimentIntensityAnalyzer from the nltk library. This method utilizes a lexicon-based approach to analyze sentiment, providing sentiment scores for positive, negative, and neutral sentiments based on the intensity of sentiment words in the input text. The combined approach aims to capture sentiment information from both deep contextual embeddings and lexicon-based analysis, enhancing the overall sentiment analysis performance. 
> **The output for this is on a separate branch**

1c. Does your method capture any of the ideas from Troth et al. and West et al.? If so, which ones?

> My way of analyzing sentiments using the Roberta Model and the SentimentIntensityAnalyzer matches Troth et al.'s focus on emotions and how they impact team communication. The Roberta Model digs deep into the emotions' nuances, while the SentimentIntensityAnalyzer adds a layer by looking at emotions through a set of predefined words.  \
> This sentiment analysis method also connects with West et al.'s work because it considers the positive side of things. The scores, especially the positive ones, might reflect the positive qualities in teams, like optimism. So, by using both methods, we get a thorough understanding of sentiments, covering both detailed context and predefined emotional terms.

1d. Compared to how Troth et al. and West et al. measured positivity, what are some strengths and weaknesses of your approach?

> ## Strengths:
> 1. **Contextual Nuance:** The Roberta Model captures detailed emotional nuances, providing a rich understanding of sentiment in context.
>2. **Comprehensive View:** The dual-method approach combines Roberta's context understanding with predefined emotional terms, offering a well-rounded sentiment analysis.
>3. **Positive Aspect Consideration:** By including positive sentiment scores, the approach aligns with West et al.'s emphasis on positive human strengths, like optimism.
>## Weaknesses:
>1. **Complexity:** The use of Roberta, a deep learning model, may introduce complexity, making it resource-intensive and potentially less straightforward to interpret.
>2. **Subjectivity:** Sentiment analysis is subjective, and the predefined lexicon used may not capture all contextual subtleties accurately.
>3. **Training Data Dependence:** The performance of the Roberta Model relies heavily on the quality and relevance of the training data, which could introduce bias if not representative.

## 2. Method evaluation
Next, we would like you to consider how you would evaluate your method. How do you know the classification or quantification of emotion is “right?” Try to think critically!

2a. Open up your output CSV and look at the columns you generated. Do the values “make sense” intuitively? Why or why not?

> ## Chat Level Analysis:
> - **Message Content:** The "message" column contains the actual text of the messages exchanged in a conversation.
> - **Sentiment Scores:** The sentiment scores (positive, negative, neutral) indicate the emotional tone of each message. The values make sense intuitively, with higher positive sentiment scores for positive messages like "looks good" and lower positive scores for neutral queries like "can we get d to the highest score."
> - **Other (Existing) Columns:** Columns like "num_words," "num_chars," and "num_messages" provide quantitative information about each message.
>## Conversation Level Analysis:
> - **Gini Coefficient:** Indicates the inequality in the distribution of words and characters across messages in a conversation. The values seem to be within a reasonable range.
> - **Average and Standard Deviation:** Statistics like average and standard deviation for various metrics (num_words, num_chars, num_messages, sentiment scores) provide insights into the distribution and variation in the conversation.
> - **Other Columns:** Batch information, visual and verbal capabilities, team size, and difficulty level are also included.
>## Overall Assessment:
>- The values in the columns appear to make sense intuitively, representing characteristics of messages and conversations. For instance, higher positive sentiment scores align with positive messages, and metrics like num_words and num_chars provide insights into the length of messages.
>- It would be helpful to have additional information about the specific scale or range for some columns to make a more precise assessment.


2b. Propose an evaluation mechanism for your method(s). What metric would you use (e.g., F1, AUC, Accuracy, Precision, Recall)?

> **Ground Truth Comparison:**
> - Obtain or create ground truth dataset.
> - Compare model predictions for accuracy, precision, recall, and F1 score. \
> 
> **Correlation Analysis:**
> - Calculate correlation with predicted sentiments.
>
> **Visualization:**
> - Generate scatter plots and line charts.
> - Explore graphical patterns for insights.
>
> **Hypothesis Testing:**
> - Formulate hypotheses on sentiment-performance links.
> - Conduct statistical tests for validation.
>
> **Case Studies:**
> - Analyze extreme cases with high/low positive sentiments.
> - Provide qualitative insights on contextual factors.

2c. Describe the steps you would take in evaluating this method. Be as specific as possible.

> **Accuracy Assessment:**
> - *Comparing Predictions with Ground Truth:* Measure how accurately the model predicts sentiments by comparing its output with actual sentiments (if available).
> - *Quantifying Precision, Recall, and F1 Score:* Evaluate the model's precision (accuracy of positive predictions), recall (coverage of actual positives), and F1 score (a balance between precision and recall) to gauge its proficiency in identifying positive, negative, and neutral sentiments. \
>
> **Correlation Analysis:**
> - *Linking Sentiments to Performance Metrics:* Examine the correlation between predicted sentiments and performance metrics, specifically scores and efficiency, as outlined in the research data. This helps understand if sentiment predictions align with task performance.
>
> **Visualization Techniques:**
> - *Graphical Representation of Relationships:* Employ scatter plots and line charts to visually depict the connections between predicted sentiments and performance metrics. This visualization aids in intuitively grasping patterns and trends.
>
> **Hypothesis Testing:**
> - *Stating and Verifying Hypotheses:* Develop hypotheses based on expected relationships, such as the anticipation that higher positive sentiments correlate with increased normalized scores and efficiency.
> - *Statistical Validation:* Execute hypothesis tests to confirm or refute these hypotheses, offering statistical evidence for the assumed relationships.
>
> **Case Studies:**
> - *In-Depth Analysis of Extreme Cases:* Investigate specific instances with extremely positive sentiments and assess how they align with corresponding performance metrics. Similarly, analyze cases with lower positive sentiments. This qualitative exploration adds context to quantitative findings.

2d. Given the nature of these datasets, what challenges do you anticipate that you may encounter during evaluation? How would you go about resolving them?

> **Sparse Ground Truth:**
> - *Challenge:* Limited availability of ground truth sentiments.
> - *Resolution:* Implement semi-supervised learning or active learning to enhance labeled data.
>
> **Subjectivity in Sentiments:**
> - *Challenge:* Ambiguity in human sentiments, specially given that they are occurring over chat/instant-messaging form.
> - *Resolution:* Limit the words that can be used during chat by not providing a free text form. Instead, possibly conduct experiment to gather data by providing one-word buttons (which could possibly give more insight into the **actual** sentiment, and rule out words like "asshole" that the participants in the jury conversation frequently use but not in a negative way).
>
> **Performance Metric Variability:**
> - *Challenge:* Diverse metrics may exhibit different sentiment correlations.
> - *Resolution:* Conduct a sensitivity analysis on chosen performance metrics and explore multiple regression models.

## 3. Overall reflection
3a. How much time did it take you to complete this task? (Please be honest; we are looking for feedback to make sure the task is scoped appropriately, as this is one of the first times we’re using this task.)

> I took about 16-17 hours to complete the task (from reading the papers to completing this README)

3b. Finally, provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? If you had more time, what are additional extensions, improvements, or tests that you would want to implement?

> - I had a great time completing this task. I am really interested in reading about organization behavior, and I am glad I got an opportunity to complete this task. Reading through previous research in this field and interpreting the findings always intrigues me.\
> - I feel positive about having been able to apply a HuggingFace model, and a basic NLTK model to the data provided. I approached the task closely following the document provided. In addition to implementing two sentiment analysis models on both datasets, I also modified the `calculate_chat_level_features.py` to split up the sentiment score object. I saw that this further enabled a statistical analysis of the sentiment on a conversation level.\
> - While I believe I was able to follow the document closely and complete the task, I would have definitely loved to spend time on performing some visualizations, correlation analysis and test some hypothesis of team sentiment and the score they obtained on the task. In addition, I believe I would have spent some more time understanding the data better to choose a more appropriate model for performing the sentiment analysis
