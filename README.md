*This repo. serves as a hub for the 'Visualization Application' final project assigned in MGT4250B2403 - 'Data Visualization & Storytelling'*

[<img width="313" alt="image" src="https://github.com/mvilla1111/Data-Viz-Project/assets/168783485/c6bc2755-b499-4182-8fd9-aa0d897245cf">](https://www.elon.edu/)



The Churn Visualization Dashboard can be found [here](https://data-viz-project-cnbxhynmgeszujvn53t2vx.streamlit.app/ )


# Original Proposal:
For this project, my aim was to improve existing business strategies by leveraging customer segmentation data. When translated, this information provides significant value by granting firms a means of optimizing existing strategies or aid in developing new targeted strategies. Identifying critical aspects of consumer preferences will enable firms to precisely tailor their products and services, while maximizing customer engagement.

By analyzing demographic attributes, we gain a thorough understanding of consumer behavior. A greater understanding of consumer behaviors will enhance an organization’s ability to target a specific demographic—optimizing marketing campaigns to a target audience.  Better known as behavioral economics, a thorough understanding enables marketing teams to connect the psychological approach of consumer choice to economic models of consumer choice/market activity. 

Speaking broadly, my focus is on the customer. The questions I aim to answer are as follows: 

*1)	Who is my ideal customer?
 The purpose of this question is to identify the key characteristics associated with high spending/repeat segments. By looking at attributes such as frequency, income, and age—I can create a robust customer profile for the purpose of developing aimed market strategies and retention.*

*2)	Are there underserved markets?
By finding the ideal customer, we may also expose underserved segments in the market. Identifying such segments creates an opportunity to grow the customer base and or improve customer engagement.*

*Both questions rely on customer patterns over time. Monitoring the evolution of consumer preferences enables organizations to meet future challenges or opportunities. All of which contribute to strategic (and powerful) decision making.*


# Early Challenges & Scope Change

As it stands, the project scope has been slightly altered. Our original data set did not include a churn variable of its own requiring us to engineer our own. Unfortunately, doing so proved difficult. When tested with various models, the new [churn] attribute resulted in a disproportionate amount 
of bias and heavy correlation to the purchase history variable. Thus, rendering further use of this particular data set virtually impossible. 

Rather than pursue attempts to refine the data/models, we opted to introduce a new data set altogether. So long as it met two requirements. First, it should closely resemble our previous data set in order to preserve the work accomplished to date. Second, the data set must include a predefined churn variable. 

#### *Scope Change*
Early interpretations of this dataset led to the belief that this information could be utilized to aid in identifying the ‘ideal’ and or ‘underserved’ customer bases. While it may still serve that purpose, a redefined version of the latter question may be appropriate to pursue. Where uncovering patterns tied to churning behavior provides the greatest amount of value. As Identifying the key characteristics will allow us to effectively predict a banking customer’s probability of exiting. 

From a business standpoint, retaining customers is far less expensive than acquiring new ones. Thus, developing a predictive model capable of prematurely identifying this type of customer is the new focus of our team. 

The concept is summarized [here](https://arxiv.org/pdf/2303.00960) in a study conducted by International Journal of Computer Science Trends and Technology (IJCST). This journal highlights the importance of integrating new innovative ways of proactively tracking consumer behavior. Additionally, emphasizes the importance of converging technical and business processes in order to seamlessly integrate the two domains. With transparency and interpretability servings as critical aspects of success. As the true value of consumer insights lies in their conversion to actionable decision-making and strategy development.

# Data
Sourced from Kaggle, we found that the ‘Bank Customer Churn Prediction’ perfectly matched our requirements. The only difference is that the new set focuses on banking customers rather than insurance policy member. The ‘Bank Customer Churn Prediction’ data set contains information on two types on customers—existing and former customers who no longer utilize the bank’s services. 

Included in the churn_modelling dataset are the following attributes:

1. *CustomerId*: unique identifier for each customer
2. *Surname*:	The customer's surname or last name
3. *CreditScore*:	A numerical value representing the customer's credit score
4. *Geography*:	The country where the customer resides (France, Spain or Germany)
5. *Gender*:	The customer's gender (Male or Female)
6. *Age*:	The customer's age
7. *Tenure*:	The number of years the customer has been with the bank
8. *Balance*:	The customer's account balance
9. *NumOfProducts*:	The number of bank products the customer uses 
10. *HasCrCard*:	Whether the customer has a credit card (1 = yes, 0 = no)
11. *IsActiveMember*:	Whether the customer is an active member (1 = yes, 0 = no)
12. *EstimatedSalary*:	The estimated salary of the customer
13. *Exited*:	Whether the customer has churned (1 = yes, 0 = no)

# Visualizations - 
*Note:* These are charts are interactable when accessed via the [visualization dashboard](https://data-viz-project-cnbxhynmgeszujvn53t2vx.streamlit.app/) 

## 

### Age vs Balance Scatter Plot

This chart illustrates the relationship between *age* and account *balance* as it pertains to churn rate. Although *balance* maintains a seemingly random effect, *age* displays a noticeable pattern. Where a concentration of consumers from older age groups is evident. Particularly in the 40-60 age group. As opposed to consumers below 30, where churn is far less likely. 
<img width="976" alt="image" src="https://github.com/mvilla1111/Data-Viz-Project/assets/168783485/b0723274-f29b-4fb7-9b66-3257f97ec895">
##

<img width="1045" alt="image" src="https://github.com/mvilla1111/Data-Viz-Project/assets/168783485/47fe4a10-927b-4373-962f-5e4e39b2e006">

<img width="1031" alt="image" src="https://github.com/mvilla1111/Data-Viz-Project/assets/168783485/cdf38830-299d-4b2c-afb5-ff3f390b9f2a">

<img width="1025" alt="image" src="https://github.com/mvilla1111/Data-Viz-Project/assets/168783485/3a50b85a-9a66-4be9-81cb-43ed5fbb3c56">

<img width="1011" alt="image" src="https://github.com/mvilla1111/Data-Viz-Project/assets/168783485/f6a4d461-e986-4607-8840-219e51c05e88">

<img width="1031" alt="image" src="https://github.com/mvilla1111/Data-Viz-Project/assets/168783485/6893161d-e6ad-4dbf-b703-fddab40afefb">



