# Chatbot for airline
##Objective
Create a chatbot that effectively handles user queries about baggage allowances by gathering all necessary information before providing specific responses.

## Requirements
Information Gathering
Prompt for Missing Information:

Ask the user for their source (departure city), destination (arrival city), and travel class (e.g., Economy, Business, First) if these details are not provided.
Ensure that the chatbot does not ask for information that has already been provided by the user.

## Specific Responses:
Provide baggage information tailored to the source and destination countries.
Avoid providing generic baggage allowance information.

Implementation
User Interface
**Technology**: Streamlit
**Purpose**: Create an intuitive user interface for interacting with the chatbot.
Baggage Allowance Data
Store baggage allowance data in the chatbot's context to ensure quick and accurate responses.
