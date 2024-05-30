import streamlit as st
import pandas as pd
import openpyxl
import os
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import geopandas as gpd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu
from streamlit.logger import get_logger
from streamlit.elements.lib.column_types import Column
from streamlit.elements.map import Data
from PIL import Image


st.set_page_config(page_title="Bulawayo Mapping Software", page_icon=":🗺:", layout="wide", initial_sidebar_state="expanded")

st.title("Mthoe Saps Construction Technologies Bulawayo Mapping Survey Engine")

#__sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ("Home", "Bulawayo Mapping","Remote Sensing","Machine Learning & AI", "Contact me"),
        menu_icon="box",
        icons=("house", "map","map","tools", "controller", "telephone" ),
        )
    
if selected == "Home":
    with st.container(border=False):
           coq1, coq2 = st.columns(2)
           with coq1:
               with st.container(border=False):
                   img = ("bulawayo_mapping_software/images/Blue Orange Vintage and Retro Construction Badge Logo_20240401_174631_0000.png")
                   st.image(img, width=350)
           with coq2:
               with st.container(border=True):
                   st.subheader("""🗺 This web application uses geospatial data in order to simulate real time data that can be used in the fields of:
                                """)
               with st.container(border=True):    
                   st.write("""Property Development and Estate Management, Town planning, Land Surveying, Civil and Structural 
                            Engineering as well as implimenting the use of this technology in Environmental Management Agencies for EMA.
                            """)
               #with st.container(border=True):
                   #st.subheader("Get ready to explore the most exciting and effective GIS and Remote Sensing beta project in Zimbabwe")
                   #st.write("You can support and sponsor my research by clicking on the Buy a Me Coffee button below to make a donation 🤓")
                   #st.markdown("""
                               #<a href="https://www.buymeacoffee.com/mthoko"><img src="https://img.buymeacoffee.com/button-api/?text=Support my work&emoji=🌍&slug=mthoko&button_colour=2ce22f&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00" /></a>
                               #""",
                               #unsafe_allow_html=True)

if selected == "Bulawayo Mapping":
    with st.container(border=True):
        st.subheader("Bulawayo Mapping System", divider=True)
    
        

    st.text("Use the select box below to analyse the Bulawayo Mapping System, all maps are fully interactive.")
    menu = ["Bulawayo open-street-map", "Bulawayo carto-positron map", "Bulawayo carto-darkmatter map"]
    choice = st.selectbox("Analyse Bulawayo Interactive Maps",menu)
    if choice == "Bulawayo open-street-map":
        st.subheader("Bulawayo open-street-map display of Low, Medium and High density suburbs")
        df = pd.read_excel('bulawayo_mapping_software/bulawayo maps database/bulawayo_map 20240331_101353_update1.xlsx')
        fig = px.scatter_mapbox(df, lat="latitude ", lon="longitude",
                                hover_name="Suburb",
                                text=None,
                                hover_data=None,
                                custom_data=None,
                                size=None,
                                animation_frame=None,
                                animation_group=None,
                                category_orders=None,
                                labels=None,
                                color_discrete_sequence=None,
                                color_discrete_map=None,
                                color_continuous_scale=None,
                                range_color=None,
                                color_continuous_midpoint=None,
                                opacity=None,
                                size_max=None,
                                center=None,
                                mapbox_style=None,
                                title=None,
                                template=None,
                                width=None,
                                #color="Suburb",
                                zoom=10,
                                height=400)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig)
    
    if choice == "Bulawayo carto-positron map":
        st.subheader("Bulawayo carto-positron map")
        df = pd.read_excel('bulawayo_mapping_software/bulawayo maps database/bulawayo_map 20240331_101353_update1.xlsx')
        fig = px.scatter_mapbox(df, lat="latitude ", lon="longitude",
                            hover_name="Suburb",
                            text=None,
                            hover_data=None,
                            custom_data=None,
                            size=None,
                            animation_frame=None,
                            animation_group=None,
                            category_orders=None,
                            labels=None,
                            color_discrete_sequence=None,
                            color_discrete_map=None,
                            color_continuous_scale=None,
                            range_color=None,
                            color_continuous_midpoint=None,
                            opacity=None,
                            size_max=None,
                            center=None,
                            mapbox_style=None,
                            title=None,
                            template=None,
                            width=350,
                            #color="Suburb",
                            zoom=10,
                            height=400)
        fig.update_layout(mapbox_style="carto-positron")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig)
    
    if choice == "Bulawayo carto-darkmatter map":
        st.subheader("Bulawayo carto-darkmatter map")
        df = pd.read_excel('bulawayo_mapping_software/bulawayo maps database/bulawayo_map 20240331_101353_update1.xlsx')
        fig = px.scatter_mapbox(df, lat="latitude ", lon="longitude",
                            hover_name="Suburb",
                            text=None,
                            hover_data=None,
                            custom_data=None,
                            size=None,
                            animation_frame=None,
                            animation_group=None,
                            category_orders=None,
                            labels=None,
                            color_discrete_sequence=None,
                            color_discrete_map=None,
                            color_continuous_scale=None,
                            range_color=None,
                            color_continuous_midpoint=None,
                            opacity=None,
                            size_max=None,
                            center=None,
                            mapbox_style=None,
                            title=None,
                            template=None,
                            width=None,
                            #color="Suburb",
                            zoom=10,
                            height=400)
        fig.update_layout(mapbox_style="carto-darkmatter")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig)
    
    #st.subheader("Bulawayo stamen-watercolor map")
    #df = pd.read_excel('bulawayo_mapping_software/bulawayo maps database/bulawayo_map 20240331_101353_update1.xlsx')
    #fig = px.scatter_mapbox(df, lat="latitude ", lon="longitude",
     #                       hover_name="Suburb",
      #                      text=None,
       #                     hover_data=None,
        #                    custom_data=None,
         #                   size=None,
          #                  animation_frame=None,
           #                 animation_group=None,
            #                category_orders=None,
             #               labels=None,
             #               color_discrete_sequence=None,
              #              color_discrete_map=None,
               #             color_continuous_scale=None,
                #            range_color=None,
                 #           color_continuous_midpoint=None,
                  #          opacity=None,
                   #         size_max=None,
                    #        center=None,
                     #       mapbox_style=None,
                      #  zoom=10,
                       #     height=400)
    #fig.update_layout(mapbox_style="stamen-watercolor")
    #fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    #st.plotly_chart(fig)

#   df = pd.read_excel('bulawayo_mapping_software/bulawayo maps database/bulawayo_map 20240331_101353_update1.xlsx')
 #   fig = px.scatter_mapbox(df, lat="latitude ", lon="longitude",
  #                          hover_name="Suburb",
   #                         text=None,
    #                        hover_data=None,
     #                       custom_data=None,
      #                      size=None,
       #                     animation_frame=None,
        #                    animation_group=None,
         #                   category_orders=None,
          #                  labels=None,
           #                 color_discrete_sequence=None,
            #                color_discrete_map=None,
             #               color_continuous_scale=None,
              #              range_color=None,
               #             color_continuous_midpoint=None,
                #            opacity=None,
                 #           size_max=None,
                  #          center=None,
                   #         mapbox_style=None,
                    #        title=None,
                     #       template=None,
                      #      width=None,
                       #     color="Suburb",
                        #    zoom=10,
                            #height=400)
    #fig.update_layout(mapbox_style="stamen-toner")
    #fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    #st.plotly_chart(fig)
    
    #st.subheader("Bulawayo stamen- terrain map")
    #df = pd.read_excel('bulawayo_mapping_software/bulawayo maps database/bulawayo_map 20240331_101353_update1.xlsx')
    #fig = px.scatter_mapbox(df, lat="latitude ", lon="longitude",
    #                        hover_name="Suburb",
     #                       text=None,
      #                      hover_data=None,
       #                     custom_data=None,
        #                    size=None,
         #                   animation_frame=None,
          #                  animation_group=None,
           #                 category_orders=None,
            #                labels=None,
             #               color_discrete_sequence=None,
              #              color_discrete_map=None,
               #             color_continuous_scale=None,
                #            range_color=None,
                 #           color_continuous_midpoint=None,
                  #          opacity=None,
                   #         size_max=None,
                    #        center=None,
                     ##      title=None,
                       #     template=None,
                        #    width=None,
                         #   color="Suburb",
                          #  zoom=10,
                           # height=400)
    #fig.update_layout(mapbox_style="stamen- terrain")
    #fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    #st.plotly_chart(fig)
    

    #st.subheader("Bulawayo Choropleth map")
    #df = pd.read_excel('bulawayo_mapping_software/bulawayo maps database/bulawayo_map 20240331_101353_update1.xlsx')
    #fig = px.choropleth_mapbox(data_frame=df,
     #                          geojson=None,
      #                         featureidkey=None,
       #                        locations="Suburb",
        #                       color=None,
         #                      hover_name=None,
          #                     hover_data=None,
           #                    custom_data=None,
            #                   animation_frame=None,
             #                  animation_group=None,
              #                 category_orders=None,
               #                labels=None,
                #               color_discrete_sequence=None,
                 #              color_discrete_map=None,
                  #             color_continuous_scale=None,
                   #            range_color=None,
                    #           color_continuous_midpoint=None,
                     #          opacity=None,
                      #         zoom=8,
                       #        center=None,
                        #       title=None,
                         #      template=None,
                          #     width=None,
                           #    height=None)
    #fig.update_layout(mapbox_style="open-street-map")
    #fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    #st.plotly_chart(fig)


    #st.subheader("Bulawayo density_contour map")
    #df = pd.read_excel('bulawayo_mapping_software/bulawayo maps database/bulawayo_map 20240331_101353_update1.xlsx')
    #fig = px.density_contour(data_frame=None, x=None, y=None, z=None, color=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, orientation=None, color_discrete_sequence=None, color_discrete_map=None, marginal_x=None, marginal_y=None, trendline=None, trendline_options=None, trendline_color_override=None, trendline_scope='trace', log_x=False, log_y=False, range_x=None, range_y=None, histfunc=None, histnorm=None, nbinsx=None, nbinsy=None, text_auto=False, title=None, template=None, width=None, height=None)
    #fig.update_layout(mapbox_style="stamen-watercolor")
    #fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    #st.plotly_chart(fig) #__this code created a contour map of BULAWAYO

if selected == "Remote Sensing":
    st.subheader("Use this Remote Sensing software to get geolocated data, all maps are fully interactive.")
    menu = ["Physidal dataset Remote Sensing", "Cultural basemaps remote sensing", "World Remote sensing datasets"]
    choice = st.selectbox("Analyse Bulawayo Interactive Maps",menu)
    if choice == "Physidal dataset Remote Sensing":
        st.write("""Plotly Geo maps have a built-in base map layer composed of 'physical' and 'cultural' (i.e. administrative border) data from the Natural Earth Dataset. Various lines and area fills can be shown or hidden, and their color and line-widths specified. In the default plotly template, a map frame and physical features such as a coastal outline and filled land areas are shown, at a small-scale 1:110m resolution:\
                 Here is a map with all physical features enabled and styled, at a larger-scale 1:50m resolution:""")
        fig = go.Figure(go.Scattergeo())
        fig.update_geos(
            resolution=50,
            showcoastlines=True, coastlinecolor="RebeccaPurple",
            showland=True, landcolor="LightGreen",
            showocean=True, oceancolor="LightBlue",
            showlakes=True, lakecolor="Blue",
            showrivers=True, rivercolor="Blue"
            )
        fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)
        st.subheader("Disabling Base Maps")
        st.write("In certain cases, such as large scale choropleth maps, the default physical map can be distracting. In this case the layout.geo.visible attribute can be set to False to hide all base map attributes except those which are explicitly set to true. For example in the following map we hide all physical features except rivers and lakes, neither of which are shown by default:")
        fig = go.Figure(go.Scattergeo())
        fig.update_geos(
            visible=False,
            resolution=50,
            showlakes=True, lakecolor="Blue",
            showrivers=True, rivercolor="Blue"
            )
        fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)
    
    if choice == "Cultural basemaps remote sensing":
        st.write("In addition to physical base map features, a 'cultural' base map is included which is composed of country borders and selected sub-country borders such as states. Here is a map with only cultural features enabled and styled, at a 1:50m resolution, which includes only country boundaries. See below for country sub-unit cultural base map features:")
        fig = go.Figure(go.Scattergeo())
        fig.update_geos(
            visible=False, resolution=50,
            showcountries=True, countrycolor="RebeccaPurple"
            )
        fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)


        st.subheader("Named Map Scopes and Country Sub-Units")
        fig = go.Figure(go.Scattergeo())
        fig.update_geos(
            visible=False, resolution=50, scope="africa",  #__The available scopes are: 'world', 'usa', 'europe', 'asia', 'africa', 'north america', 'south america'.
            showcountries=True, countrycolor="Black",
            showsubunits=True, subunitcolor="Blue"
            )
        fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)
    

        st.subheader("Graticules (Latitude and Longitude Grid Lines)")
        st.write("A graticule can be drawn using layout.geo.lataxis.showgrid and layout.geo.lonaxis.showgrid with options similar to 2d cartesian ticks.")
        fig = go.Figure(go.Scattergeo())
        fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
        fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig)

    if choice == "World Remote sensing datasets":
        st.subheader("World Earth Quake datase")
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')
        fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                            center=dict(lat=0, lon=180), zoom=0,
                            mapbox_style="open-street-map")
        st.plotly_chart(fig)
        st.subheader("Interactive map for the world dataset for gdpPerCap and population from 1952-2007", divider=True)
        country_data = px.data.gapminder()
        country_data.tail()
        map_fig = px.scatter_geo(country_data,
                                 locations="iso_alpha",
                                 projection="orthographic",
                                 color="continent",
                                 opacity=0.8,
                                 hover_name="country",
                                 hover_data=["lifeExp", "pop", "gdpPercap"]
                                 )
        st.plotly_chart(map_fig)
    
    

if selected == "Machine Learning & AI":
    with st.container(border=False):
        st.subheader("Machine Learning and AI in GIS and Remote Sensing", divider=True)
        st.write("*Use the select box below to obtain more information about Machine Learning and AI for this project.*")
        menu = ["Machine Learning in GIS and Remote Sensing", "Application and uses", "More on this topic"]
        choice = st.selectbox("Menu",menu)
        if choice == "Machine Learning in GIS and Remote Sensing":
            with st.container(border=True):    
                st.write("""Imagine giving a cartographer the world’s most powerful magnifying glass. That’s what machine learning does for GIS.
                Uncovering Hidden Patterns: Machine learning enables us to extract hidden patterns from geographic data, turning landscapes into libraries of spatial intelligence.
                Noise Reduction: It makes sense out of noisy data, revealing patterns we might not have even considered.
                Software That Writes Software: Instead of using pre-built functions, ML learns from experience and adapts to new situations.""")
        if choice == "Application and uses":
            with st.container(border=True):
                st.write("""Applications include:
                Agriculture: Monitoring crop health, yield prediction, and precision farming.
                Urban Planning: Assessing land use, infrastructure, and population dynamics.
                Disaster Response: Identifying affected areas and assessing damage.
                Environmental Monitoring: Tracking deforestation, pollution, and habitat changes.""")
        if choice == "More on this topic":
            with st.container(border=True):
                st.write("""Here are some of the most advanced machine learning algorithms I am currently working on. We will use Scikit-learn to split and preprocess our data
                and train various regression models. Scikit-learn is a popular Machine Learning (ML) library that offers various tools for creating and training ML algorithms, feature engineering, data cleaning, and evaluating and testing models.""")
   
    df = px.data.tips()
    X = df.total_bill.values.reshape(-1, 1)
    x_range = np.linspace(X.min(), X.max(), 100)
    # Model #1
    knn_dist = KNeighborsRegressor(10, weights='distance')
    knn_dist.fit(X, df.tip)
    y_dist = knn_dist.predict(x_range.reshape(-1, 1))
    # Model #2
    knn_uni = KNeighborsRegressor(10, weights='uniform')
    knn_uni.fit(X, df.tip)
    y_uni = knn_uni.predict(x_range.reshape(-1, 1))
    fig = px.scatter(df, x='total_bill', y='tip', color='sex', opacity=0.65)
    fig.add_traces(go.Scatter(x=x_range, y=y_uni, name='Weights: Uniform'))
    fig.add_traces(go.Scatter(x=x_range, y=y_dist, name='Weights: Distance'))
    st.plotly_chart(fig)
    st.subheader("More techiques of Machine Learning")
    st.write("""Train a k-Nearest Neighbors (kNN) classifier. First, the model records the label of each training sample. Then, whenever we give it a new sample, it will look at the k closest samples from the training set to find the most common label, 
    and assign it to our new sample.""")
    st.subheader("Display training and test splits", divider=True)

    # Load and split data
    X, y = make_moons(noise=0.3, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y.astype(str), test_size=0.25, random_state=0)
    trace_specs = [
        [X_train, y_train, '0', 'Train', 'square'],
        [X_train, y_train, '1', 'Train', 'circle'],
        [X_test, y_test, '0', 'Test', 'square-dot'],
        [X_test, y_test, '1', 'Test', 'circle-dot']
        ]
    fig = go.Figure(data=[
        go.Scatter(
            x=X[y==label, 0], y=X[y==label, 1],
            name=f'{split} Split, Label {label}',
            mode='markers', marker_symbol=marker
            )
        for X, y, label, split, marker in trace_specs
        ])
    fig.update_traces(
        marker_size=12, marker_line_width=1.5,
        marker_color="lightyellow"
        )
    st.plotly_chart(fig)

    st.subheader("Visualize predictions on test split", divider=True)
    # Load and split data
    X, y = make_moons(noise=0.3, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y.astype(str), test_size=0.25, random_state=0)

    # Fit the model on training data, predict on test data
    clf = KNeighborsClassifier(15)
    clf.fit(X_train, y_train)   
    y_score = clf.predict_proba(X_test)[:, 1]

    fig = px.scatter(
        X_test, x=0, y=1,
        color=y_score, color_continuous_scale='RdBu',
        symbol=y_test, symbol_map={'0': 'square-dot', '1': 'circle-dot'},
        labels={'symbol': 'label', 'color': 'score of <br>first class'}
        )
    fig.update_traces(marker_size=12, marker_line_width=1.5)
    fig.update_layout(legend_orientation='h')
    st.plotly_chart(fig)

    st.subheader("Probability Estimates with go.Contour", divider=True)
    mesh_size = .02
    margin = 0.25
    # Load and split data
    X, y = make_moons(noise=0.3, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y.astype(str), test_size=0.25, random_state=0)
    # Create a mesh grid on which we will run our model
    x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
    y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
    xrange = np.arange(x_min, x_max, mesh_size)
    yrange = np.arange(y_min, y_max, mesh_size)
    xx, yy = np.meshgrid(xrange, yrange)
    # Create classifier, run predictions on grid
    clf = KNeighborsClassifier(15, weights='uniform')
    clf.fit(X, y)
    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
    Z = Z.reshape(xx.shape)
    # Plot the figure
    fig = go.Figure(data=[
        go.Contour(
            x=xrange,
            y=yrange,
            z=Z,
            colorscale='RdBu'
            )
        ])
    st.plotly_chart(fig)
    with st.container(border=True):
        st.write("""*Combining our go.Contour plot with the first scatter plot of our data points, so that we can visually compare the 
        confidence of our model with the true labels.*""")
    mesh_size = .02
    margin = 0.25
    # Load and split data
    X, y = make_moons(noise=0.3, random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y.astype(str), test_size=0.25, random_state=0)
    # Create a mesh grid on which we will run our model
    x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
    y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
    xrange = np.arange(x_min, x_max, mesh_size)
    yrange = np.arange(y_min, y_max, mesh_size)
    xx, yy = np.meshgrid(xrange, yrange)

    # Create classifier, run predictions on grid
    clf = KNeighborsClassifier(15, weights='uniform')
    clf.fit(X, y)
    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
    Z = Z.reshape(xx.shape)
    trace_specs = [
        [X_train, y_train, '0', 'Train', 'square'],
        [X_train, y_train, '1', 'Train', 'circle'],
        [X_test, y_test, '0', 'Test', 'square-dot'],
        [X_test, y_test, '1', 'Test', 'circle-dot']
        ]
    fig = go.Figure(data=[
        go.Scatter(
            x=X[y==label, 0], y=X[y==label, 1],
            name=f'{split} Split, Label {label}',
            mode='markers', marker_symbol=marker
            )
        for X, y, label, split, marker in trace_specs
        ])
    fig.update_traces(
        marker_size=12, marker_line_width=1.5,
        marker_color="lightyellow"
        )
    fig.add_trace(
        go.Contour(
            x=xrange,
            y=yrange,
            z=Z,
            showscale=False,
            colorscale='RdBu',
            opacity=0.4,
            name='Score',
            hoverinfo='skip'
            )
        )
    st.plotly_chart(fig)


    

if selected == "Contact me":
    st.subheader("Contact me info", divider=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Use the buttons below to get in touch with me", divider=True )
        st.link_button("Contact me on WhatsApp", "https://wa.me/263777932721") 
        st.link_button("View my LinkedIn Profile", "https://www.linkedin.com/in/mthokozisi-sapuwa-1ab2151ab?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app") 
        st.link_button("Find me on Instagram", "https://www.instagram.com/mthoe.zw?utm_source=qr&igsh=MTlrZWlvdW1pNGI4bA")
        st.link_button("Check me out Facebook", "https://www.facebook.com/mthokozisi.sapuwa.50?mibextid=kFxxJD")
    with col2:
        #st.subheader("Use the text input form below to leave a comment on my project", divider=True)
        st.empty()
        #st.divider()


with st.sidebar:
    with st.form("my_form", clear_on_submit=True):
        st.write("**Rate my software**")
        slider_val = st.slider("How do you rate this tool", help="Slide to the desired precentage(%)")
        checkbox_val = st.checkbox("Did you find this tour useful?", help="Check the box if True")
        submitted = st.form_submit_button("Submit")
        if submitted: st.write("Rating", slider_val, "Helpful", checkbox_val)
