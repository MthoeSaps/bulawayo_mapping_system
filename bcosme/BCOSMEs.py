import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
import time

from streamlit.logger import get_logger
from streamlit_option_menu import option_menu

from streamlit_extras.colored_header import colored_header
#from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.streaming_write import write
from streamlit_extras.badges import badge

LOGGER = get_logger(__name__)

def BCOME():
    st.set_page_config(page_title="BCOSME", page_icon=":🛍:", initial_sidebar_state="collapsed")     
    st.toast("BCOSME", icon="🛍")

    colored_header(
        label = "**Bulawayo Chamber Of Small & Medium Enterprises**",
        description = "**Empowering Zimbabwe Small & Medium Enterprises For Global Competetiveness**",
        color_name = "blue-70"
    )

    tab1,tab2,tab3,tab4,tab5 = st.tabs([":blue[**Home**]", ":blue[**Become A Member**]", ":blue[**About**]", ":blue[**FAQ**]",":blue[**Geo Location**]"])

    with tab1:
         st.title(
            ":orange[**Home**]",
            help=("This is our home page, Enjoy")
        )
         cola, cola2 = st.columns(2)
         with cola2:
            with st.container(border=False):
                 st.empty()
                 #video_file = open('bcosme/videos/video1.mp4', 'rb')
                 #video_bytes = video_file.read()
                 #st.video(video_bytes, start_time= 0 ,loop=True)
            with cola:
                with st.container(border=False):
                   st.write("Welcome to our online portal. This portal was genarated in complience with our perfomance values, proving that we are dedicated to serving you.")
         st.divider() 
         inspiration = """
         
         - “what do you need to start/ grow a business? Three simple things: know your product better than anyone, know your customer, and have a burning desire to succeed”. Dave Thomas, Founder of Wendy’s 
"""
            
         def preview():
            for word in inspiration.split():
                yield word + " "
                time.sleep(0.05)
                
         if st.button("A little Inspiration",help="These messages loop every 24 hours. Today this what we have for you"):
                write(preview) 
         st.divider()

         #switch_page(page_name="Membership Application.py")
         st.markdown("""
                     :orange[💹BUSINESS MANAGEMENT]
                    
                     
                     - :gray[*Business management training Financial Literacy Training Company registration Participation in seminars, training programmes, conference and meetings.*] 
                     

                     :orange[⚔FORMALISATION] 


                     - :gray[*Engage partners for SME formalization Tender notification updates Export market facilitation*]
                     

                     :orange[🎙ADVOCACY & LOBBYING]


                     - :gray[*Facilitate workspaces for decent work and easier access by clients. Taxation Issues Women and youth in business*]

                     
                     :orange[🔗PERFORMANCE]

                     - :gray[*Improve your business performance by linking to financial institutions, technological organisations and also doing technical skills training and trade tests. Engaging local retailers and wholesalers to market SME products.*]
                     
                     """)      

    with tab2:
        st.title(":orange[Become A  Member]", help="We have built a form algorithm to manage the signup digitally")
        st.info("Head over to our sidebar and start signing up now", icon="📝")
        st.divider()

        long_text = "Lorem ipsum. " * 1000
        with st.container(border=True,height=500):
            st.subheader("Read with care")
            st.write("""
        
                  - The main mandate is to promote the business interests of our members, and to represent those same interests while empowering the SMEs for global competitiveness. 
                 
                  - Membership will enhance your network by creating relationships to support and help one another in reaching professional and business goals. 
                 
                  - BCSME provides a trusted environment where like –minded individuals can come together to share ideas, strengthen ties, collaborate and make connections. 
                
                  - Membership also means immediate access to new or developments that affect your business and the sector as a whole. 
                
                  - (BCSME allows you to not only find news but also disseminate your own company’s news).
                 
                  - SMEs have common issues that impact nearly all businesses that operate within the space- including different laws, regulations and policies that may prevent your business from growing to its full potential.
                
                  - BCSME regularly lobbies the relevant authorities on behalf of member SMEs to ensure their interests are protected. 
                 
                  - The combined resources and numbers of the members are used to lobby policy makers and sway opinion more positively towards the goals of the SMEs than any one company can hope to achieve, irrespective of its size. 
               
                  - Membership enables this. Continued education and personal development is crucial in getting to the top of any industry and BCSME prioritizes this.
                 
                  - The chamber facilitates workshops, seminars and conferences to up-skill members so they can stay competitive. 
                 
                  - Whatever your primary reason for wanting to join BCSME, if membership is actively used there are many benefits it will bring. 
                 
                  - Its important to understand that BCSME should not solely be seen as a sales / lead generation organization, ( we can however guide you if this is what you are seeking). 
                 
                  - We can assist you with brand elevation and promotion through a variety of activities. 
                 
                  - To get the maximum benefit out of the membership we encourage our members to become proactively engaged, this will bring a greater awareness of both your brand and the product or services you offer- all helping to drive you new business and growth.

""")
        #switch_page(page_name="Membership Application.py")
    with tab3:
        option = ["About Bulawayo Chamber Of Small & Medium Enterprises","User Manual", "Developer"]
        choice = st.selectbox("About Us",option)
        st.write(f":orange[**You're viewing the {choice} section**]")

        if choice == "About Bulawayo Chamber Of Small & Medium Enterprises":
            st.title(":blue[**About Bulawayo Chamber Of Small & Medium Enterprises.**]")
            st.write(":blue[**Private Limited Company**]")

            selected = option_menu(
                menu_title="BCOFME. Company Tree",
                options= ["Home", "Services", "Metric Data", "Affiliated Partners"],
                menu_icon="tree",
                icons=["house", "tools", "controller", "person-circle"],
                orientation="horizontal",
                styles={
                    "container": {"padding": "initial","background-color": 'ffffff', "boarder-color": 'orange'},
                    "icon": {"color":"grey","font-size": "15px"},
                    "nav-link": {"color":"grey","font-size": "12px", "text-align": "initial", "margin":"10px"},
                    "nav-link-selected": {"background-color": "white"},
                    }
                    )
            
            if selected == "Home":
                st.subheader(":blue[Welcome to the BCOSME. (PVT) LTD Online Informatics Platform]")
                st.write("""
                         
                        (BCSME) is a association that was established in 2011 and is a member of the Zimbabwe Chamber of Small and Medium Enterprises (ZCSMEs) which is an apex body representing the interests of SMEs at a national level. The BCSME is a provincial structure among other nine provisional chapters initiated to represent the interests of SME entrepreneurs, as well as to be the voice of SMEs all over Zimbabwe. The Bulawayo Chamber of SMEs’ mission is to serve entrepreneurs, SMEs, cooperatives, SME clusters and other stakeholders through coordinated advocacy, access to working space, access to finance and markets, business management training, access to information, linkages, networking that supports growth and formalization of small businesses. Its services are designed to enhance SME competitiveness and profitability across different value chains. The Chamber has the following objectives and benefits for its members… 
                          
                         
                         1. Creating a comprehensive database of all SMEs in the metropolitan area. 


                         2. Registering and training of SMEs in business management, products development, marketing strategies’ and linkages. 


                         3. Advocating and lobbying for formal operational workspace for SMEs 


                         4. Facilitating access to financial services for SMEs and to improve and scale up their businesses.

 
                         5. Importing local, regional and international best practices. 


                         6. Linking SMEs to financial and business development institutions.

 
                         7. Facilitate graduation of SMEs from micro to small and medium, and informality to formality. 


                         8. Partnering with development partners and donors for SME growth.
                         """)

            if selected == "Metric Data":
                st.write(":blue[Saint Inc. stock market dashboard]")
                st.write(":orange[Metric Dashboard]")

                col1, col2, col3, = st.columns(3)
                col1.metric(label="MS ConTech share(%)", value="$405.00", delta=1.00, help=" %")
                col2.metric(label="Terra Vista Licencing share(%)", value="$720.00", delta=3.57, help=" %")
                col3.metric(label="Northveil Inc.(%)", value="N/A", delta= -1, help=" %")
                df = pd.read_excel("Data\pc.xlsx")
                def preview():
                    yield pd.DataFrame(df)
                if st.button("Preview"):
                    write(preview)

                st.write(":orange[**Bar Graph Stock Display**]")
                fig = px.bar(
                    df,
                    x="Project Name ",
                    y="Project Value (USD)",
                    color="Cost Per Share ($ per 1%)"
          )
                st.plotly_chart(fig)

                st.write(":orange[**Pie Chart Stocks Display**]")
                chart2 = px.sunburst(
                df,
                path=["Project Name ", "Project Value (USD)"],
                values="Max Number of Investors",
                color="Share Percentage Available (%)"
                )
                st.plotly_chart(chart2)
                
                st.write(":orange[**Area Stock Chart**]")
                fig = px.area(
                  df,
                  x="Project Name ",
                  y="Project Value (USD)",
                  color="Cost Per Share ($ per 1%)",
                  line_group="Share Percentage Available (%)"
                  )
                st.plotly_chart(fig)

        if choice == "User Manual":
            st.empty()
        if choice == "Developer":
            st.empty()
    with tab4:
          st.title(":orange[**Frequently Asked Question**]")
          st.write("- :blue[**Our filter Team has found these Requests and Reviews pressing**]")

          avatar = """
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Saint" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
        """

          faq1 = """
- **1.  When are guys giving us the directions ft?**
"""
          faq2 = """
- **2.  How much do you guys charge for deliveries**
"""
          faq3 = """
- **3.  Can i view your prices offline**
"""
          faq4 = """
- **4.  How original are the products you produce**
"""     
          with st.expander(faq1):
            st.markdown(avatar,unsafe_allow_html=True)
            st.write(":orange[**Am not into spoilers but probably next month you'll see**]")
          with st.expander(faq2):
            st.markdown(avatar,unsafe_allow_html=True)
            st.write(":blue[**Its absolutely freee, we value our customers that much**]")
          with st.expander(faq3):
            st.markdown(avatar,unsafe_allow_html=True)
            st.write(":blue[**[Pricinglist](wa.me/+263782012633)🪐 This is our whatsapp business catalog, tap the link**]")
          with st.expander(faq4):
            st.markdown(avatar,unsafe_allow_html=True)
            st.write(":orange[**All our products are from original sources, promotion or contract sales are also original products from our trusted sources dont worry**]")

def footer():
     with st.sidebar:
          st.header(":blue[**Bulawayo Chamber Of Small & Medium Enterprises. 2024**]")
    #footer
     st.divider()
     st.write(":gray[**For More Info Contact Us**]")
     q,w,e = st.columns(3)
     with q:
         with st.container(border=True):
          st.write("[📍 This is our location](https://earth.app.goo.gl/?apn=com.google.earth&isi=293622097&ius=googleearth&link=https%3a%2f%2fearth.google.com%2fweb%2fsearch%2fbulawayo%2bChamber%2bof%2bsmes%2f%40-20.1642267,28.5771922,1360.97605786a,1960.36053092d,35y,0h,0t,0r%2fdata%3dCigiJgokCYdeHDITHjTAEUhRWQrmHzTAGeYzr00ngzxAIV0XPAg4gDxA)")
     with w:
         with st.container(border=True):
          st.write("📞 [08644300594](08644300594)")
     with e:
         with st.container(border=True):
          st.write("📩 [Email Us](byochamberofsmes@gmail.com)")
         
     with st.container(border=True):
        st.write(":gray[**Report a bug**]")
        st.write("""- **Talk to our team of active developers if youre having trouble with the app**""")
        badge(type="github", name = "Crazypapi6" ,url="https://github.com/Crazypapi6")

     with st.container(border=True):
        st.write(":gray[**Donate to our cause**]")
        st.write("""- **10% of the women and children in the world go to be hungry, Its our vision to see them fed**""")
        st.markdown("""
<a href="https://www.buymeacoffee.com/supremecro7"><img src="https://img.buymeacoffee.com/button-api/?text=Feed a soul&emoji=🐼&slug=supremecro7&button_colour=5F7FFF&font_colour=ffffff&font_family=Arial&outline_colour=000000&coffee_colour=FFDD00" /></a>
                     """,
                     unsafe_allow_html=True)
    
     op,op2,op3 = st.columns(3)
     with op:
        st.write("- [Terms of sale](https://github.com/Crazypapi6)")
        st.write("- [Terms of use](https://github.com/Crazypapi6)")
     with op2:
        st.write("- [Privacy Statement](https://github.com/Crazypapi6)")
        st.write("- [Service Agreement](https://github.com/Crazypapi6)")
     with op3:
        st.write("- [Software License](https://github.com/Crazypapi6)")
        st.write("- [Trademarks](https://github.com/Crazypapi6)")    
    
if __name__ == "__main__":
    BCOME()

if __name__ == "__main__":
    footer()