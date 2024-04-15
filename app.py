# Importing necessary libraries from huggingface_hub and gradio
from huggingface_hub import InferenceClient
import gradio as gr


# Include your Hugging Face API token here
api_token = "your_hugging_face_api_token"

# Initializing the inference client with the specified model and authentication token
client = InferenceClient(
    "mistralai/Mistral-7B-Instruct-v0.1",
    token=api_token  # Pass the token to the client
)

# Function to format the prompt based on the user input and bot response history
def format_prompt(message, history):
  prompt = "<s>"
  for user_prompt, bot_response in history:
    prompt += f"[INST] {user_prompt} [/INST]"  # Add user prompt to the prompt string
    prompt += f" {bot_response}</s> " # Add bot response to the prompt string
  prompt += f"[INST] {message} [/INST]"   # Add current message to the prompt string
  return prompt

# Function to generate text based on the formatted prompt and given parameters
def generate(
    prompt, history, temperature=0.9, max_new_tokens=256, top_p=0.95, repetition_penalty=1.0,
):
    temperature = float(temperature)  # Convert temperature to float for processing
    if temperature < 1e-2:  # Set a minimum value for temperature to prevent too low values
        temperature = 1e-2   # Convert top_p to float for processing
    top_p = float(top_p)

    # Dictionary to hold keyword arguments for the text generation API call
    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=42,
    )

    # Format the prompt using the provided message and history
    formatted_prompt = format_prompt(prompt, history)

     # Call to the Hugging Face API to generate text based on the formatted prompt and other parameters
    stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

     # Iterate over the generated stream of tokens and concatenate them to form the full
    for response in stream:
        output += response.token.text
        yield output  # Yield each token as it's generated (useful for real-time updates in UI)
    return output


# List of additional Gradio interface inputs to control generation parameters
additional_inputs=[
    gr.Slider(
        label="Temperature",
        value=0.9,
        minimum=0.0,
        maximum=1.0,
        step=0.05,
        interactive=True,
        info="Higher values produce more diverse outputs",
    ),
    gr.Slider(
        label="Max new tokens",
        value=256,
        minimum=0,
        maximum=1048,
        step=64,
        interactive=True,
        info="The maximum numbers of new tokens",
    ),
    gr.Slider(
        label="Top-p (nucleus sampling)",
        value=0.90,
        minimum=0.0,
        maximum=1,
        step=0.05,
        interactive=True,
        info="Higher values sample more low-probability tokens",
    ),
    gr.Slider(
        label="Repetition penalty",
        value=1.2,
        minimum=1.0,
        maximum=2.0,
        step=0.05,
        interactive=True,
        info="Penalize repeated tokens",
    )
]


# Initializing the Gradio Chat Interface with the generate function and additional inputs
gr.ChatInterface(
    fn=generate,
    chatbot=gr.Chatbot(show_label=False, show_share_button=False, show_copy_button=True, likeable=True, layout="panel"),
    additional_inputs=additional_inputs,
    title="Mistral 7B"
).launch(share=True, show_api=False) # Launch the interface with sharing enabled and API hidden


