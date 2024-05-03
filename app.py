import streamlit as st
import pandas as pd
import reveal_slides as rs
import datetime
from datetime import timedelta





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

#### Market Players in The Insurance Ecosystem
- Insurance Companies - APA , Old Mutual , Heritage , Fidelity , Jubilee <!-- .element: class="fragment" data-fragment-index="0" -->
- Re-Insurance Companies - Africa Re , WAICA Re , Kenya Re , ZEP Re <!-- .element: class="fragment" data-fragment-index="1" -->
- Brokers  <!-- .element: class="fragment" data-fragment-index="2" -->
- Consultancy - BIG 4 , ActServe , Zamara ,  Kenbright, Lux <!-- .element: class="fragment" data-fragment-index="3" -->
- Regulator - IRA <!-- .element: class="fragment" data-fragment-index="4" -->
---

#### Roles of Intermediaries In The Insurance Ecosystem
- What are Intermediaries and types of intermediaries? <!-- .element: class="fragment" data-fragment-index="0" -->
- Examples of Intermediaries in the Insurance Landscape in Kenya? <!-- .element: class="fragment" data-fragment-index="1" -->
    . GRAS SAVOYE - WTW <!-- .element: class="fragment" data-fragment-index="0" -->
    . AON MINET <!-- .element: class="fragment" data-fragment-index="1" -->
    . ACENTRIA <!-- .element: class="fragment" data-fragment-index="2" -->
    . ZAMARA <!-- .element: class="fragment" data-fragment-index="3" -->
- How do we earn our money? <!-- .element: class="fragment" data-fragment-index="2" -->
- Key attributes to excel in this space? <!-- .element: class="fragment" data-fragment-index="3" -->
- How descent is the salary? <!-- .element: class="fragment" data-fragment-index="4" -->

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
st.markdown("#### UoN I07 Career Talk - Collins Chetekei")
st.markdown("###### Role of Intermediaries In Insurance")
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
        st.markdown("_(follow me on Github @ chete-py)_")


