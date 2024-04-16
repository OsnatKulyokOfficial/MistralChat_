# MistralChat.

# Self-Correcting Chatbot Project

## Project Overview

Developed a Python-based chatbot using the transformers library, incorporating user feedback to enhance conversational accuracy over time. This chatbot leverages state-of-the-art NLP models for dynamic interaction and self-improvement through a sophisticated feedback loop.

## Technological Journey

Hugging Face was a completely new area for me, and I used the following diagram to understand what I was up against:
![image](https://github.com/OsnatKulyokOfficial/MistralChat_/assets/129261751/6593ae3c-8dc9-4cf3-a5b8-b5fc4280756f)

![WhatsApp Image 2024-04-15 at 00 35 36](https://github.com/OsnatKulyokOfficial/MistralChat/assets/129261751/64ee4232-f1cf-498d-85de-8c2fe37de465)

### Hugging Face & Transformers Introduction

Learning with Hugging Face's transformers library; understood basic functionalities by interacting with pre-trained models and simulating AI-driven conversations, deepening the grasp of conversational AI systems.

### Full Stack Development: Streamlit and FastAPI

Created a streamlined user interface with Streamlit and integrated FastAPI for backend operations. Ensured robust communication between frontend and backend, and used Postman to ensure that the server was functioning properly
Second step was sending requests to chatGPT4 using a secret OpenAI key in order to understand how to connect a backend AI model with a frontend interface.

### Basic Conversational AI

Implemented basic conversational structures using the Transformers conversation pipeline. This setup served as a foundation for more advanced conversational capabilities, illustrating the practical use of pre-trained models.

### Advanced NLP with DistilBERT and GPT-2

Employed DistilBERT for efficient question-answering, effectively balancing computational demands with performance, and explored manual handling of inputs and outputs using GPT-2, which advanced my understanding of nuanced AI interactions and taught me about the model's capabilities in context understanding and relevant information extraction

### Exploring Conversational Depth with DialogGPT, 01-ai/Yi-34B-Chat, CohereForAI/c4ai-command-r-plus

Utilized DialogGPT along with other models such as 01-ai/Yi-34B-Chat and CohereForAI/c4ai-command-r-plus to simulate detailed and interactive human-like dialogues. These models were instrumental in refining the chatbot's responses, enhancing realism, and maintaining consistency and coherence in user interactions. This step was an educational dive into the complexities of transformer models like GPT-2, particularly focusing on the processing of inputs and generation of responses, which is crucial for customizing AI behavior and ensuring dialogue continuity.

### Cross-modal AI Capabilities with CLIP & Della.

Expanding your exposure to AI innovation by exploring cross-modal capabilities of AI models. Learning about CLIP & Della enhances my understanding of how AI can process and comprehend not just text but also images in relation. Integrated CLIP for cross-modal understanding, demonstrating the ability to incorporate advanced AI techniques that bridge text and visual content, expanding the chatbot’s functionality.

### API Integration and Web Scraping

External APIs and web scraping techniques were utilized to enrich the chatbot’s data sources, demonstrating how real-time, external data can be seamlessly integrated to enhance AI responsiveness and accuracy. These methods are essential for teaching how to fetch and integrate external data into applications, particularly for projects that depend on up-to-date or large-scale data sourced from the internet. They also illustrate how to extract specific information from large data sets, improving AI understanding and outputs with real-world information.

### ChatGPT4

I explored integrating the open-source implementation of ChatGPT4's code and encountered hardware complexity due to CPU constraints and local processor limitations. This project showcases a comprehensive integration of advanced AI technologies, leveraging GPT-4 for interactive and diverse AI interactions.

### TRL, Dataset, Trainer and RewardMethodology:

In the project, I investigated various training and reward methodologies, utilizing datasets such as the Cornell Movie-Dialogs Corpus. Additionally, I explored additional datasets on platforms like Kaggle and previous projects for practical insights. I established scaled-down environments and experimented with implementing Trainer models and reward mechanisms to understand their functionality. Subsequently, I attempted to embed and apply TRL files to evaluate slightly more sophisticated models, aiming to deploy them on method-trained models with smaller data segments. However, the complexity of the task became evident due to the need for additional computational resources, emphasizing the importance of efficient resource management when implementing advanced AI models.

The file sequence in the project represents a structured progression from basic AI implementations to more sophisticated applications, providing insights into both fundamental concepts and advanced techniques in AI and machine learning.
This journey offers a well-rounded understanding of AI development, from foundational principles to complex real-world scenarios. This progression not only strengthens technical proficiency but also cultivates a deeper comprehension of how diverse AI technologies can be combined to tackle novel challenges and create innovative solutions.

# MistralCHAT

## Project Overview

MistralChat leverages the advanced Mistral-7B model through Gradio on the Hugging Face platform to facilitate dynamic and natural language conversations.
This model is a designed to generate responses that are contextually appropriate and engaging, enhancing the user experience in conversational applications.

### System Design Document

### Architecture Overview

The MistralChat system integrates:
**Gradio for User Interface**: Ensures an accessible and interactive user experience.
**Hugging Face for Model Hosting**: Manages backend operations, providing robust model performance.
**Feedback Mechanism**: Continuously improves the model based on user interactions, enhancing accuracy and contextual relevance over time.

### Feedback Incorporation Mechanism

**Detailed Implementation**: Feedback from users is systematically collected, analyzed, and used to adjust the model's training and response strategies, ensuring the system evolves to meet user expectations.

### Installation Instructions

```
git clone https://github.com/OsnatKulyokOfficial/MistralChat..git
pip install -r requirements.txt
python app.py
```

Set HUGGINGFACE_TOKEN in your environment variables for API integration.

### Evaluation Report

**Methodology**
To assess the self-correcting capability of the Mistral-7B chatbot, we implemented a structured testing framework that measures performance before and after user feedback. The process involves:

**Initial Interaction**: Users interact with the chatbot, and their queries along with the chatbot's responses are recorded.
**Feedback Incorporation**: Users provide specific feedback on the responses they find unsatisfactory or incorrect. This feedback is manually fed into the system to adjust the response algorithms.
**Follow-Up Interaction**: Users re-engage with similar queries to evaluate whether the chatbot has incorporated the feedback effectively, aiming for improved responses.

**Testing Scenarios**
Several scenarios were created to test the chatbot's learning capabilities across different domains such as general knowledge, customer service, and technical support. Each scenario involves specific questions designed to challenge the chatbot's understanding and adaptability.

### Performance Metrics

Performance was measured using the following metrics:

**Accuracy**: The correctness of the chatbot’s responses, pre and post-feedback.
**Responsiveness**: The time taken to generate responses, noting any improvements.
**User Satisfaction**: Gathered through direct user ratings and feedback on the chatbot's answers.

### Results

The initial tests showed that the chatbot could accurately incorporate feedback into its response mechanisms.

**For example:**
In a general knowledge test about geographical facts, the accuracy improved from 70% to 90% after users corrected misconceptions.
Customer service scenario responses became more empathetic and contextually appropriate after feedback about tone and detail was applied.

### Chatbot Evolution Through User Feedback: A Visual Showcase

Visualization depicting the chatbot's learning from user feedback

1. Before
   ![1](https://github.com/OsnatKulyokOfficial/MistralChat_/assets/129261751/7b4c9127-f90f-4eb8-8481-3b0a1e21dbf1)
   After
![2](https://github.com/OsnatKulyokOfficial/MistralChat_/assets/129261751/e5595f8e-aa98-4b6d-85bb-5a5a73a69bba)

2. Before
   ![3](https://github.com/OsnatKulyokOfficial/MistralChat_/assets/129261751/4f9de280-103c-4fcc-975e-9979cb0784d2)

   After
   ![4](https://github.com/OsnatKulyokOfficial/MistralChat_/assets/129261751/463f6cb4-3659-431b-ade5-e86411db63d5)

3. Before
![5](https://github.com/OsnatKulyokOfficial/MistralChat_/assets/129261751/6be6d4db-418d-4e5a-9292-6e0402c47153)

   After
  ![6](https://github.com/OsnatKulyokOfficial/MistralChat_/assets/129261751/cd18bb22-2fce-412d-8c55-4041a1fd03b3)


### Discussion

The evaluation highlighted the chatbot’s robust capability to learn from interactions and improve its responses. However, some challenges remain:

**Complex Queries**: The chatbot occasionally struggles with complex multi-part questions, requiring further refinement of its parsing and understanding mechanisms.
**Speed**: While accuracy improved, the response time increased slightly, suggesting a need for optimization in handling feedback.

**Areas for Improvement**
To enhance the chatbot's performance further, the following steps are recommended:

**Algorithm Optimization:** Improve the efficiency of feedback incorporation to maintain quick response times without sacrificing accuracy.
**Extended Training:** Regular updates to the training dataset with new feedback to broaden the chatbot’s exposure to diverse interactions.
**User Interface**: Simplify the feedback process through the user interface to encourage more interactive and constructive feedback from users.

### For more information

[Hugging Face Mistral-7b-chat](https://huggingface.co/spaces/ehristoforu/mistral-7b-chat)
