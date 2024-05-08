import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import resample
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix 
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

##############################################################################

st.set_page_config(layout="wide")

df = pd.read_csv('./Churn_Modelling.csv')
df_c = df.copy()
df=df.drop(columns=['RowNumber','CustomerId'])
df=df.drop_duplicates()
st.title('Analyzing Churn Rate')
df1 = df.drop(columns=['Surname'])
encoder = LabelEncoder()
categorical_columns = ['Geography', 'Gender']
for x in categorical_columns:
        df1[x] = encoder.fit_transform(df1[x])

#############################################################################


# Sidebar for user inputs

st.sidebar.header('User Input Features')

# Default selections for selectbox and multiselect
default_gender = df['Gender'].mode()[0]
default_geos = df['Geography'].unique().tolist()

selected_gender = st.sidebar.selectbox('Gender', options=df['Gender'].unique(), index=df['Gender'].unique().tolist().index(default_gender))
selected_geo = st.sidebar.multiselect('Geography', options=df['Geography'].unique(), default=default_geos)

# Filter data based on selections
filtered_data = df[(df['Gender'] == selected_gender) & (df['Geography'].isin(selected_geo))]

if st.sidebar.checkbox('Show Age vs Balance Scatter Plot', value=True):
    fig = px.scatter(filtered_data, x='Age', y='Balance', color='Exited', title='Age vs Balance Scatter Plot')
    st.plotly_chart(fig, use_container_width=True)

##############################################################################

df1 = df.drop(columns=['Surname'])
encoder = LabelEncoder()
categorical_columns = ['Geography', 'Gender']
for x in categorical_columns:
        df1[x] = encoder.fit_transform(df1[x])
    
rf_classifier = RandomForestClassifier(n_estimators=27)
exited = df1[df1.Exited==1]
no_exit = df1[df1.Exited == 0]
upsampled_exited = resample(exited, replace=True, n_samples=len(no_exit))
rf_model = pd.concat([upsampled_exited,no_exit])
X=rf_model.drop(columns=['Exited'])
y=rf_model['Exited']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=717)
rf_classifier.fit(X_train,y_train)

#######



#######

col1, col2 = st.columns([5,5])
with col1:
    if st.sidebar.checkbox('Show Feature Importance', value=True):
        feature_importances = pd.DataFrame({
        'Features': X.columns,
        'Importance': rf_classifier.feature_importances_
        }).sort_values(by='Importance', ascending=True)
   

        # Create the chart
        fig1 = px.bar(feature_importances, x='Importance', y='Features', orientation='h',
                 text='Importance', color='Importance', 
                 color_continuous_scale=px.colors.sequential.Viridis)
    
        # Customize text labels for visibility
        fig1.update_traces(texttemplate='%{text:.2f}', textposition='inside', textfont_size=16)
      
        # Update the layout for better readability
        fig1.update_layout(
        title={
            'text': "Feature Importance Analysis", 
            'x':.2,
            'font': dict(
                family="Arial, sans-serif",  # Font family
                size=24,  # Increase font size here
                color="white"  # Font color
            )
        },
        xaxis_title="Importance Score",
        yaxis_title=None,
        plot_bgcolor='rgba(0,0,0,0)',  # Set transparent background
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=16, color="white"),  # Larger font size for overall readability
        margin=dict(l=0, r=0, t=40, b=20)  # Adjust margins to fit the layout
    )
        st.plotly_chart(fig1, use_container_width=True)

#########

with col2:
    plt.figure(figsize=(12,9))  # This line seems unnecessary for Plotly and should be removed.

    churn_by_country_df = df_c.pivot_table(index='Geography', columns='Exited', values='CustomerId', aggfunc='count', fill_value=0)
    churn_by_country_df.columns = ['Non_Churned', 'Churned']  # Assuming 'Exited' has two categories: 0 and 1

    churn_by_country_df.columns = ['Non_Churned', 'Churned']  # Renaming columns for clarity

    fig_churn = px.bar(churn_by_country_df.reset_index(), x='Geography', y=['Non_Churned', 'Churned'],
                   color='variable',  # This assumes that 'variable' differentiates 'Non_Churned' and 'Churned'
                   barmode='group', title='Churn by Country',
                   color_discrete_map={'Non_Churned': 'cyan', 'Churned': 'yellow'})  # Example colors
    
    fig_churn.update_layout(
     title={
        'text': "Churn Volume by Country",  # Chart title
        'y':.99,  # Title's y position
        'x':.2,  # Title's x position (center)
        'font': dict(
            family="Arial, sans-serif",  # Font family
            size=24,  # Increase font size here
            color="white"  # Font color
        )
    },
    xaxis_title="Country",
    yaxis_title="Count of Churned Customers",
    title_font_size=24,
    showlegend=True  
)

    
    # Displaying the chart in Streamlit
    st.plotly_chart(fig_churn, use_container_width=True)
 
#############   
# Calculate the correlation matrix from the updated df1
corr_matrix = df1.corr()

fig = px.imshow(corr_matrix, 
                text_auto=True, 
                aspect="wide",
                color_continuous_scale='viridis',  # Red to Blue, reversed color scale
                labels=dict(color="Correlation Coefficient"))
  
fig.update_layout(title_text='Correlation Matrix Heatmap', width=1170, title_font_size=35)

# Display the heatmap in Streamlit
st.plotly_chart(fig, use_container_width=True)

#########

import plotly.express as px

# Assuming df is your DataFrame and it includes a 'Churn' column where 1 indicates churned
fig = px.histogram(df, x='Age', color='Exited', barmode='overlay',
                   histnorm='percent', title='Distribution of Age for Churned and Retained Customers')
fig.update_layout(bargap=0.1)
st.plotly_chart(fig, use_container_width=True)

##########
import streamlit as st
import plotly.express as px
import pandas as pd

# Assuming you've already loaded your DataFrame 'df'
# If your DataFrame is not loaded, uncomment the next line and replace the path
# df = pd.read_csv('./Churn_Modelling.csv')

def load_data():
    # Adjust the path if necessary
    df = pd.read_csv('./Churn_Modelling.csv')
    df = df.drop(columns=['RowNumber', 'CustomerId', 'Surname'])  # Drop unwanted columns
    return df

def show_violin_plot():
    df = load_data()
    # This line creates a violin plot
    fig = px.violin(df, y='Age', x='Exited', color='Exited', 
                    labels={'Exited': 'Churn Status', 'Age': 'Age of Customers'},
                    title='Distribution of Age by Churn Status',
                    box=True,  # This adds a box plot inside the violin plot
                    points="all")  # This displays all points within the violin plot

    # Display the plot in the Streamlit app
    st.plotly_chart(fig, use_container_width=True)

def main():
    st.title('Churn Analysis with Violin Plot')
    show_violin_plot()

if __name__ == '__main__':
    main()



###################


def prepare_data(df):
    df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 30, 40, 50, 60, 100], labels=['Under 30', '30-40', '40-50', '50-60', 'Over 60'], right=False)
    df['Exited'] = df['Exited'].map({0: 'Non Churned', 1: 'Churned'})
    summary = df.groupby(['Geography', 'Gender', 'AgeGroup', 'Exited']).size().reset_index(name='Count')
    return summary

def create_tree_map(df):
    fig = px.treemap(df, path=['Geography', 'Gender', 'AgeGroup', 'Exited'], values='Count',
                     color='Exited', color_discrete_map={'Churned': 'red', 'Non Churned': 'green'}, 
                     title='Churn Distribution Across Demographics')
    return fig

def main():
    st.title('Detailed Churn Analysis Using Tree Map')
    df = load_data()
    prepared_data = prepare_data(df)
    fig = create_tree_map(prepared_data)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == '__main__':
    main()

