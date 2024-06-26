import streamlit as st
import pandas as pd
import reveal_slides as rs
import datetime
from datetime import timedelta
import sqlite3
from sqlite3 import Connection



# Establish connection to the database
connection = sqlite3.connect("quiz.db")
cursor = connection.cursor()

cursor.execute(
        """CREATE TABLE IF NOT EXISTS results
            (
                NAME VARCHAR,
                SCORE INT
            );"""
    )





# # Define your Google Sheets credentials JSON file (replace with your own)
# credentials_path = 'dreamteam-410510-f5750e00bbd9.json'
    
# # Authenticate with Google Sheets using the credentials
# credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=['https://spreadsheets.google.com/feeds'])
    
# # Authenticate with Google Sheets using gspread
# gc = gspread.authorize(credentials)
    
# # Your Google Sheets URL
# url = "https://docs.google.com/spreadsheets/d/1c9ZVdhfrTDME7wjCgxkDeb7GRzgg43JCJPP3D_C__to/edit#gid=0"
    
# # Open the Google Sheets spreadsheet
# worksheet = gc.open_by_url(url).worksheet("i07")

# # Read data from the Google Sheets worksheet
# data_frame = worksheet.get_all_values()
    
# # Prepare data for Plotly
# headers = data_frame[0]
# data_frame = data_frame[1:]

# df = pd.DataFrame(data_frame, columns=headers)



tab1, tab2, tab3 = st.tabs(["📈 Presentation", "Quiz", "🗃 Records"])

with tab1:

    sample_markdown = r"""
    #### Collins in a nutshell
    - What do I do
    - Any past experience
    ---

    #### Opportunities for Actuarial Science Graduates
    - Insurance <!-- .element: class="fragment" data-fragment-index="0" -->
    - Consultancy <!-- .element: class="fragment" data-fragment-index="1" -->
    - Software Development <!-- .element: class="fragment" data-fragment-index="2" -->
    - Data <!-- .element: class="fragment" data-fragment-index="3" -->
    - Banking and Audit <!-- .element: class="fragment" data-fragment-index="4" -->
    - Unlimited opportunities to be honest <!-- .element: class="fragment" data-fragment-index="5" -->
    ---

    #### Insurance Industry Actuarial Departments
    | Company      | Actuarial Department |  
    |--------------|:-----:|
    | UAP Old Mutual |  20 |      
    | APA      |  10 |    
    | Jubilee  | 15  |   
    |  |  |

    ---

    #### Market Players in the Insurance Ecosystem
    - Insurance Companies - APA , Old Mutual , Heritage , Fidelity , Jubilee <!-- .element: class="fragment" data-fragment-index="0" -->
    - Re-Insurance Companies - Africa Re , WAICA Re , Kenya Re , ZEP Re <!-- .element: class="fragment" data-fragment-index="1" -->
    - Brokers - Gras Savoye-WTW , AON-Minet , Zamara , Kenbright , Acentria <!-- .element: class="fragment" data-fragment-index="2" -->
    - Consultancy - BIG 4 , ActServe , Zamara ,  Kenbright, Lux <!-- .element: class="fragment" data-fragment-index="3" -->
    - Regulator - IRA <!-- .element: class="fragment" data-fragment-index="4" -->
    ---

    #### Tips on How to Breakthrough
    - Luck  😂 😂 <!-- .element: class="fragment" data-fragment-index="0" -->
    - Education <!-- .element: class="fragment" data-fragment-index="1" -->
    - Skills <!-- .element: class="fragment" data-fragment-index="2" -->
    - Experience - Internship <!-- .element: class="fragment" data-fragment-index="3" -->
    - Networking <!-- .element: class="fragment" data-fragment-index="4" -->
    - Passion ❤️❤️<!-- .element: class="fragment" data-fragment-index="5" -->

    ---

    #### Thank You For Your Time

    """
    st.markdown("#### UoN I07 Career Talk - Chete")
    with st.sidebar:
        st.header("Component Parameters")
        theme = st.selectbox("Theme", ["serif", "simple", "solarized"])
        height = st.number_input("Height", value=400)
        st.subheader("Slide Configuration")
        transition = st.selectbox("Transition", ["slide", "convex", "concave", "zoom", "none"])
        plugins = st.multiselect("Plugins", ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
        overview = st.checkbox("Show Overview", value=False)
        paused = st.checkbox("Pause", value=False)

    # Add the streamlit-reveal-slide component to the Streamlit app.                    
    currState = rs.slides(sample_markdown, 
                        height=height, 
                        theme=theme, 
                        config={
                                "transition": transition,
                                "plugins": plugins
                                }, 
                        initial_state={
                                        
                                        "paused": paused, 
                                        "overview": overview 
                                        }, 
                        markdown_props={"data-separator-vertical":"^--$"}, 
                        key="foo")

    if currState["indexh"] == 0:
        st.markdown("follow me on Github @ chete-py")
    elif currState["indexh"] == 6:
        st.markdown("follow me on Github @ chete-py")
    elif currState["indexh"] == 2:
        if currState["indexf"] == 0:
            st.markdown("_(see later slides for details and examples)_")
        elif currState["indexf"] == 1:
            st.markdown("(see later slides for details and examples)")
        elif currState["indexf"] == 2:
            st.markdown("")
        elif currState["indexf"] == 3:
            st.markdown("(see later slides for details and examples)")
        elif currState["indexf"] == 4:
            st.markdown("_(see later slides for details and examples)_")


with tab2:
    def evaluate_score(user_answers):
        correct_answers = {
        "Question 1": "Minet",
        "Question 2": "Around 3%",
        "Question 3": "AIG",
    
        }

        user_score = 0
        for question, user_answer in user_answers.items():
            correct_answer = correct_answers[question]
            if user_answer == correct_answer:
                user_score += 1

        return user_score


    
    st.title("The Lucky Fella!!")
    user_name = st.text_input("Enter your name:")
    

    # QuestionS
    q1_choices = ["APA ", "Sanlam", "Minet", "Britam", "Heritage"]   
    q1_answer = st.radio("Question 1: Which of the following is not an insurance company in Kenya?", q1_choices)

    q2_choices = ["Around 0.5%", "Around 10%", "Around 50%", " Around 25%",  "Around 3%"]   
    q2_answer = st.radio("Question 2: Which of the following is closest to the current level of insurance penetration in Kenya? ", q2_choices)

    q3_choices = ["Deloite", "Ernst & Young ", "AIG", "KPMG"]   
    q3_answer = st.radio("Question 3: Which of the following companies is not part of the BIG4? ", q3_choices)

    
    # Submit button
    if st.button("Submit"):
        answers = {
            "Question 1": q1_answer,
            "Question 2": q2_answer,
            "Question 3": q3_answer
        }


        # Evaluate user score
        user_score = evaluate_score(answers)
    
        
        
        # Display the user's score
        st.success(f"Answers submitted successfully! Your score: {user_score}")
    
        if user_name:

            # Calculate the current time plus three hours
            submission_time = (datetime.datetime.now()).strftime("%H:%M")

                
                            
        # Create a download button with customized file name
    
            if st.download_button:
                new_data = [user_name, user_score, submission_time]

                 # Append the new row of data to the worksheet
                connection = sqlite3.connect("quiz.db")
                cursor2 = connection.cursor()

                cursor2.execute("INSERT INTO results (NAME, SCORE) VALUES (?, ?)", (user_name, user_score))
                
                st.success("Data inserted successfully!")
                            
    else:
        st.warning("Please enter your name to generate the report.")


with tab3:
    connection = sqlite3.connect("quiz.db")
    query = "SELECT * FROM results"
    db_df = pd.read_sql_query(query, connection)
    st.dataframe(db_df)























# import streamlit as st
# import pandas as pd
# import reveal_slides as rs
# import datetime
# from datetime import timedelta





# sample_markdown = r"""
# #### Collins in a nutshell
# - What do I do
# - Any past experience
# ---

# #### Opportunities for Actuarial Science Graduates
# - Insurance <!-- .element: class="fragment" data-fragment-index="0" -->
# - Consultancy <!-- .element: class="fragment" data-fragment-index="1" -->
# - Software Development <!-- .element: class="fragment" data-fragment-index="2" -->
# - Data <!-- .element: class="fragment" data-fragment-index="3" -->
# - Banking and Audit <!-- .element: class="fragment" data-fragment-index="4" -->
# - Unlimited opportunities to be honest <!-- .element: class="fragment" data-fragment-index="5" -->
# ---

# #### Insurance Industry Actuarial Departments
# | Company      | Actuarial Department |  
# |--------------|:-----:|
# | UAP Old Mutual |  20 |      
# | APA      |  10 |    
# | Jubilee  | 15  |   
# |  |  |

# ---

# #### Market Players in The Insurance Ecosystem
# - Insurance Companies - APA , Old Mutual , Heritage , Fidelity , Jubilee <!-- .element: class="fragment" data-fragment-index="0" -->
# - Re-Insurance Companies - Africa Re , WAICA Re , Kenya Re , ZEP Re <!-- .element: class="fragment" data-fragment-index="1" -->
# - Brokers  <!-- .element: class="fragment" data-fragment-index="2" -->
# - Consultancy - BIG 4 , ActServe , Zamara ,  Kenbright, Lux <!-- .element: class="fragment" data-fragment-index="3" -->
# - Regulator - IRA <!-- .element: class="fragment" data-fragment-index="4" -->
# ---

# #### Roles of Intermediaries In The Insurance Ecosystem
# - What are Intermediaries and types of intermediaries? <!-- .element: class="fragment" data-fragment-index="0" -->
# - Examples of Intermediaries in the Insurance Landscape in Kenya? <!-- .element: class="fragment" data-fragment-index="1" -->
# - GRAS SAVOYE - WTW ,  AON MINET, ACENTRIA, ZAMARA <!-- .element: class="fragment" data-fragment-index="2" -->    
# - Key attributes to excel in this space? <!-- .element: class="fragment" data-fragment-index="3" -->
# - How descent is the salary? <!-- .element: class="fragment" data-fragment-index="4" -->

# ---

# #### Tips on How to Breakthrough
# - Luck  😂 😂 <!-- .element: class="fragment" data-fragment-index="0" -->
# - Education <!-- .element: class="fragment" data-fragment-index="1" -->
# - Skills <!-- .element: class="fragment" data-fragment-index="2" -->
# - Experience - Internship <!-- .element: class="fragment" data-fragment-index="3" -->
# - Networking <!-- .element: class="fragment" data-fragment-index="4" -->
# - Passion ❤️❤️<!-- .element: class="fragment" data-fragment-index="5" -->

# ---

# #### Thank You For Your Time

# """
# st.markdown("#### UoN I07 Career Talk - Collins Chetekei")
# st.markdown("###### Role of Intermediaries In Insurance")
# with st.sidebar:
#     st.header("Component Parameters")
#     theme = st.selectbox("Theme", ["serif", "simple", "solarized"])
#     height = st.number_input("Height", value=400)
#     st.subheader("Slide Configuration")
#     transition = st.selectbox("Transition", ["slide", "convex", "concave", "zoom", "none"])
#     plugins = st.multiselect("Plugins", ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
#     overview = st.checkbox("Show Overview", value=False)
#     paused = st.checkbox("Pause", value=False)

# # Add the streamlit-reveal-slide component to the Streamlit app.                    
# currState = rs.slides(sample_markdown, 
#                     height=height, 
#                     theme=theme, 
#                     config={
#                             "transition": transition,
#                             "plugins": plugins
#                             }, 
#                     initial_state={
                                    
#                                     "paused": paused, 
#                                     "overview": overview 
#                                     }, 
#                     markdown_props={"data-separator-vertical":"^--$"}, 
#                     key="foo")

# if currState["indexh"] == 0:
#         st.markdown("_(follow me on Github @ chete-py)_")


