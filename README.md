# UNBLOCK
![logo](https://github.com/Jerric1801/Prototype_MILKBUNS/assets/114668650/102ba8d3-8f64-4167-82e5-984bfb792c61)

## Description
Our solution aims to make the berthing process more efficient, by coming up with the best recommendations for your berthing port/terminal, based on trends and seasonal demand. We trained our model with data that we aim to store using blockchain technology, which we have simulated in our prototype. We have opted to use blockchain technology due to its secure and easy tracing of new shipment activity, with the potential of paving way for new collaboration between shipping companies in the future. By increasing visibility of such information, we aim to aid stakeholders in making informed decisions for shipping, to reduce congestion, prevent waste of resources and lower operation costs.

## Link
[UNBLOCK](https://unblock-by-milkbuns-9b127424f40e.herokuapp.com/)

## How to use
Upon loading the page, simply enter your shipping details and click on find, which will bring up a list of recommendations along with a map to visualise the location of recommended ports.
We have included a 'Blockchain' page which you can access through the navigation bar at the top, which is a visualisation of the blockchain technology that we have simulated. You are able to view the shipment data as well as the block hash of each block. Feel free to experiment by adding your own inputs.

## Challenges
Due to cost and time constraints, it is not really feasible for us to implement an actual blockchain database to store our data. Hence, we have opted to simulate it by creating a simple model.


## AI Model
Initially we wanted to use a neural network to predict the likelihood of the port being congested on a given day. However, due to time constraints we instead opted to use Holt-Winters triple exponential smoothing method. Due to the lack of free public vessel data sets, we opted to create our own set of data. The dataset included unique ships and their date of arrival to Singapore’s port. There were 36000 unique observations from 2020 to 2022 in our data set with a seasonal trend during the months of September to November. 

<img width="961" alt="Screenshot 2023-10-01 at 10 45 38 PM" src="https://github.com/Jerric1801/Prototype_MILKBUNS/assets/59726668/63178f7d-09d5-4b65-87fd-a4ddbd15006d">

From our data set, the initial plot showed an obvious seasonal trend in ship arrivals. Due to this seasonality, we decided to use the Holt-Winters model with trend and seasonality. After creating the model, we generated expected ship arrivals and used this data to determine the availability of berths in our application. 

<img width="731" alt="Screenshot 2023-10-01 at 10 46 14 PM" src="https://github.com/Jerric1801/Prototype_MILKBUNS/assets/59726668/17cc1001-2162-46ab-afb9-a38f230ce5e1">
