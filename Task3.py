import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage


st.title("Airline Chatbot")
st.write("Welcome to our airline! 😊")
load_dotenv()

llm = ChatGoogleGenerativeAI (model="gemini-1.5-pro-latest")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
instruction= '''
help user with baggage queries and calculate costof baggage for them.
If user has not given source or destination or travel class, we have to prompt the user to get all the three
If user has given only source , we have to prompt the user to give destination and travel class
If user has given only destination, we have to prompt the user to give source and travel class
If user has given source and destination alone, we have to prompt the user to give travel class
Once you have all the information, then only proceed to answer user question.'''

context='''
Have you checked your baggage?
If you’re someone who values bringing all your essentials on board, discover all you need to know about checked baggage allowances for a seamless air travel experience on our domestic and international flights.

Domestic flights
Cabin Class	Brand	Baggage
Economy	Comfort	15 kg/33 lb
Comfort Plus	15 kg/33 lb
Flex	25 kg/55.1 lb
Premium economy	Comfort Plus	15 kg/33 lb
Flex	25 kg/55.1 lb
Business	Comfort Plus	25 kg/55.1 lb
Flex	35 kg/77.1 lb
First	First	40 kg/88.1 lb
 

Points to remember:

The above allowances apply only to Air India-operated flights and not to Air India Express or codeshare flights. 
Passengers flying on Air India domestic or international sectors on the same ticket will have the baggage allowance of the international sector applied.
Passengers holding separate tickets for Air India domestic and connecting international flights can take advantage of Free Baggage Allowance (FBA), if:
The connection flight is within 24 hours.
Both flights are operated by Air India.
Star Alliance Gold members can carry an additional 20 kg/44 lb of baggage in economy class.
Members of premium clubs and our Flying Returns programme will get additional baggage.
Infants are entitled to one collapsible stroller/carrycot/infant car seat.
The maximum weight permissible for a single piece of baggage is 32 kg/71 lb. This rule applies to the entire Air India network.
Passengers can carry assistive devices free of charge as additional baggage subject to the limitation of the aircraft as per Directorate General of Civil Aviation (DGCA) guidelines.
 

Rules for baggage dimensions
Cabin Class	Baggage Dimension Allowance 
Economy  	Total combined dimensions (length + breadth + height) of both pieces should not exceed 272 cm/107 in and that of each piece should not exceed 157 cm/62 in.
First/Business	Total combined dimensions (length + breadth + height) of each piece should not exceed 157 cm/62 in.
 

International flights
Cabin

Economy

Premium Economy

Business

First

From

To

Comfort
 (RBD: S/T/U/L)

Comfort Plus
 (RBD: G/W/V/Q/K)

Flex
 (RBD: H/M/B/Y)

Comfort Plus
 (RBD: N)

Flex
 (RBD: A/R)

Comfort Plus
 (RBD: Z/J)

Flex
 (RBD: D/C)

First
 (RBD: F)

INDIA

India (IN)

15 kg/ 33 lb

15 kg/ 33 lb

25 kg/ 55.1 lb

15 kg/ 33 lb

25 kg/ 55.1 lb

25 kg/ 55.1 lb

35 kg/ 77.1 lb

40 kg/ 88.1 lb

Sri Lanka (LK)

30 kg/ 66.1 lb

30 kg/ 66.1 lb

40 kg/ 88.1 lb

30 kg/ 66.1 lb

40 kg/ 88.1 lb

40 kg/ 88.1 lb

45 kg/ 99.2 lb

45 kg/ 99.2 lb

Bangladesh (BD)

30 kg/ 66.1 lb

30 kg/ 66.1 lb

35 kg/ 77.1 lb

30 kg/ 66.1 lb

35 kg/ 77.1 lb

35 kg/ 77.1 lb

40 kg/ 88.1 lb

40 kg/ 88.1 lb

Nepal, Myanmar, Maldives

20 kg/ 44 lb

20 kg/ 44 lb

30 kg/ 66.1 lb

20 kg/ 44 lb

30 kg/ 66.1 lb

35 kg/ 77.1 lb

40 kg/ 88.1 lb

40 kg/ 88.1 lb

Israel

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Middle East and Gulf region

25 kg/ 55.1 lb

30 kg/ 66.1 lb

35 kg/ 77.1 lb

30 kg/ 66.1 lb

35 kg/ 77.1 lb

40 kg/ 88.1 lb

45 kg/ 99.2 lb

45 kg/ 99.2 lb

Thailand (TH)/ Singapore (SG)/ Hongkong (HK)

25 kg/ 55.1 lb

30 kg/ 66.1 lb

35 kg/ 77.1 lb

30 kg/ 66.1 lb

35 kg/ 77.1 lb

40 kg/ 88.1 lb

45 kg/ 99.2 lb

45 kg/ 99.2 lb

Japan (JP)/ South Korea (KR)

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Australia and New Zealand

25 kg/ 55.1 lb

30 kg/ 66.1 lb

35 kg/ 77.1 lb

30 kg/ 66.1 lb

35 kg/ 77.1 lb

40 kg/ 88.1 lb

45 kg/ 99.2 lb

45 kg/ 99.2 lb

Europe

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Africa

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

United States and Canada

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 23 kg/ 50.7 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Two pieces of up to 32 kg/ 70.5 lb each

Travel to and from Africa
Travel to and from Australia and Far East-Southeast Asia
Travel to and from Canada/USA
Travel to and from Europe/UK/Israel
Travel to and from Gulf and Middle East
Travel to and from SAARC Countries
Travel to and from Saudi Arabia
 

Piece and weight concept
Cabin Class	Maximum Sum of Dimensions	Maximum Weight Allowed per Piece
First/Business	157cm/62 in	32 kg/71 lb
Economy	271 cm/107 in (both pieces combined)	23 kg/51 lb
 
Additional allowance for Flying Returns members
Flying Returns members can bring additional baggage on flights operated by Air India and Star Alliance member airlines. The additional allowance is based on the tier status of Flying Returns members for weight concept and piece concept sectors.

Flying Returns Tier	Piece Concept Flights	Weight Concept Flights
Platinum (Star Gold)	One piece upto 23 kg	20 kg/44 lb
Gold (Star Gold)	One piece upto 23 kg	20 kg/44 lb
Silver	 	10 kg/22 lb
Red	Nil	Nil
Terms and conditions apply. Extra baggage allowance and lounge access is subject to change as per government directive.

 

Baggage rules for an interline journey
As per the International Air Transport Association (IATA), baggage rules for an interline journey are as follows:

Step 1: If the published provisions for baggage allowance among all participating carriers are the same, then those provisions will apply.

Step 2: When one or more published baggage provisions differ between participating carriers, apply any common provisions. When all provisions differ, apply the published baggage provisions of the Most Significant Carrier (MSC). In the case of codeshare flights, this will be the operating carrier unless that carrier publishes a rule stipulating that it will be the marketing carrier.

Step 3: If the MSC does not publish baggage provisions for the journey concerned, apply the published baggage provisions of the carrier accepting the baggage at check-in.

Step 4: Determine the MSC:

For travel between two or more IATA areas, the carrier on the first sector crosses from one area to another. 
Exception: IATA Area 1/2/3 only, the carrier providing carriage on the first sector crosses between IATA Area 1 and IATA Area 2.
For travel between IATA tariff sub-areas, the carrier in the first sector crosses from one sub-area to another.
For travel within an IATA tariff sub-area, it is the carrier in the first international sector.
When a passenger chooses to take a stopover at a connecting point, a new baggage assessment and charges may apply from the point of departure following the stopover.

Here are some more things to keep in mind:

Infants in all classes are eligible for baggage allowance of up to 10 kg/22 lb of one piece.
The maximum weight permissible for a single piece of baggage is 32 kg/71 lb. This rule applies to the entire Air India network.
For tickets issued effective 01 April 2019, free baggage allowance in economy class between India and Newark (EWR) is one piece of up to 23 kg/51 lb.
 

Baggage allowance on codeshare flights
Please refer to their websites for free baggage allowances, excess baggage charges, and optional/ancillary fees charged by our codeshare partners operating from and to the USA

Lufthansa	Chicago/Denver/Detroit/Los Angeles/Washington, DC-Frankfurt and vice versa, Frankfurt-India and vice versa.	Click here  for the details of the operating carrier Lufthansa.
Singapore Airlines	Los Angeles/San Francisco-Singapore	Click Here for the details of operating carrier Singapore Airlines
 

Points to remember:

Additional baggage allowance is not given on Air India flights operated with ATR/CRJ aircraft, airline partners’ flights, and Air India codeshare flights.
Silver members are eligible for additional baggage allowance on flights operated by Air India only, whereas Gold and Platinum members (corresponding to Star Gold) are eligible for additional baggage allowance on Star Alliance flights as well.
There is a ban on the carriage of lithium battery-powered self-balancing devices in cabin baggage. Power banks cannot be carried in checked baggage but in cabin baggage only.
Samsung Galaxy Note 7 is banned and cannot be carried on flights in either baggage.




VISA, DOCUMENTS AND TRAVEL TIPS
All You Need to Know About Visa, Documents, and Travel Tips
We are excited about your upcoming trip with us, and we promise to make it memorable and seamless. Before leaving for the airport, please check if you have your documents in place. Also, read Air India’s travel advisory for various airports and cities across India and the world.

one-vasco
OneVasco
Get personalised visa application assistance from OneVasco's team of experts. With our help, you can trust that your application will be handled with care and attention to detail.

Learn More
Documents to carry 
Documents to carry
Ensure you carry all necessary documents, including domestic or international flight tickets. If you’re flying to an international destination, please have a valid visa and passport.

Learn More
Travelling to India
Travelling to India
The Indian government provides information about visa requirements and the online application process. If you’re an Indian citizen travelling to Mizoram, Imphal, Lakshadweep, or Andaman and Nicobar Islands, you will require an entry permit and other permissions to travel.

Go To E-Visa Information View Permit Requirements
overseas-citizen-of-india
Overseas citizen of India
The Indian government has eased rules for overseas citizen of India (OCI) cardholders travelling to or from India. Find out about the regulations and renewal norms that apply to OCI cardholders.

Learn More
Travelling through multiple airports 
Travelling through multiple airports
Are you flying to another country via multiple airports? Not sure what necessary details you need to check before your travel? Needn't worry. Let's simplify your travel through multiple airports. Read our transit rules and have a hassle-free journey.

Learn More
Travel to Canada, the US, and Gulf countries
Get the details on visa requirements, entry guidelines, baggage allowances, and more before your travel.

Canada
Canada
Learn More
United States
United States
Learn More
Gulf Countries
Gulf Countries
Learn More
Guidelines and regulations by country
Find out country-specific guidelines regarding visa, boarding, and carrying funds.



Australia
Are you planning to carry funds in or out of Australia?

Here are some pointers you should know:  

If asked by a customs or police officer, please report traveller’s cheques, cheques, money orders or any other bearer negotiable instrument (BNI) of any amount. 
Always inform if you carry more than AUD 10,000 or foreign currency equivalent in cash using a form issued by Customs. 
The funds you can take in or out of Australia are unlimited. 
For more information, visit www.austrac.gov.au. 



Iraq


Male


Nepal


New Zealand


Russia


Thailand


UK




FIRST-TIME FLYERS, CHILDREN AND PETS
Before you takeoff
If you are a first-time flyer or your child travels alone, do not worry! We will take care of everything. Your safety and comfort are our top priorities.

We also welcome your furry friends on board and promise to take good care of them.


first-time-flyers
First-time flyers
Nervous about your first flight? Don't be. Air India has a team that will help you every step of the way.

Learn More
Children
When it comes to our young passengers, we go above and beyond to guarantee they have a secure, comfortable, and unforgettable journey with us. We take care of everything from the security check to ensuring they meet their designated guardian at the arrival airport, making the entire process hassle-free.

Unaccompanied minors 
Unaccompanied minors
Pack some toys and send them off with a hug, we will take care of the rest.

Learn More
Young passengers
Young passengers
Got a child flying alone? Here’s what your ultimate checklist must look like.

Learn More
Expectant mothers and newborns
Expectant Mothers and Infants
When you travel with your future little globe-trotter, leave all the worrying to us.

Learn More
Carriage of pets
Carriage of pets
We know your pets are like your family, and you want them to be on your trips. We allow small pets like dogs and cats in the cabin or cargo hold of our domestic flights.

Learn More




HEALTH & MEDICAL ASSISTANCE​
 

Comfortable Travel, Accessible Journeys
We are committed to making the travel of our guests with special needs as comfortable and hassle-free as possible.

 

Health-medical-assistance
Special Assistance Services
Medical Needs and Clearance Requirements
Medical needs and clearance requirements
Whether it's medical care in the air or conditions that need attention, we are here to care.

Learn More
Disability Assistance 
Special needs assistance
Please learn about our accessible travel services for passengers with reduced mobility or visual and hearing impairments.

Learn More
Passengers that require a wheelchair
Passengers who require a wheelchair
If you need a wheelchair, let us know at the time of your reservation, ticketing, or reconfirmation of the booking.
Learn More
flying
Flying with medical conditions
Medical clearance is required for medical conditions that raise concerns about completing the flight safely or pose a risk to other guests.

Learn More
Flying with a Service Dog
Travelling with a Service Dog
Flying with a loyal companion by your side? Read about the requirements and guidelines when travelling with your service dog.
'''

template='''
You are a helpful Airline Chat bot who greets the user and interacts with them professionaly.You can answer to any queries regarding the airlines.
You has access to the following details: {context} and instructions: {instruction}.
prompt the user for necessary details and if the user gives source and destination classify the flight as domestic or international.
You have access to the chat history: {Chat_history}
User question: {question}
'''

st.markdown("""
    <style>
    .user-message {
        text-align: right;
        background-color: #d1e7dd;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        color: black;
        margin-left: auto;
        width: 60%;
    }
    .bot-message {
        text-align: left;
        background-color: #f8d7da;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        color: black;
        margin-right: auto;
        width: 60%;
    }
    </style>
""", unsafe_allow_html=True)


prompt= ChatPromptTemplate.from_template(template)

output_parser= StrOutputParser()  

def get_response(question):
    chain= prompt | llm | output_parser
    formatted_prompt = {
        "context":context,
        "question": question,
        "instruction":instruction,
        "Chat_history": st.session_state.messages
    }
    result= chain.invoke(formatted_prompt)
    clean_result= result.strip(" AIMessage(content='")
    return result

question = st.chat_input("Input text here")
if question:
    st.session_state.messages.append(HumanMessage(content=question))
    ai_response = get_response(question)
    st.session_state.messages.append(AIMessage(content=ai_response))

for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        st.markdown(f"<div class='user-message'>You: {message.content}</div>", unsafe_allow_html=True)
    elif isinstance(message, AIMessage):
        st.markdown(f"<div class='bot-message'>Airlines: {message.content}</div>", unsafe_allow_html=True)   