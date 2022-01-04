README

MODULE 9

Ethan Miller

011075077

Before running, please run pip install pint in the console or in anaconda powershell

Make sure that Module9.py and modsim.py are both in the same directory

OVERVIEW:

This project is a simulation based on and leveraged from the lecture, as well as from the website: https://www.nature.com/articles/s41591-020-0883-7

This is a expanded SIR model, which adds on the parameters of Ailing and Diagnosed to the parameters already in place, particularly Susceptible, Infected, and Recovered. The values used to describe our initial state come from the current stage of the Covid-19 virus in Santa Clara county. More specifically, we are currently experiencing fewer confirmed cases, with a large amount of people recovered from the virus. The logic for how I chose these values is explained in the comments of the program. 

In the program, I used a total of 8 factors used to describe the various rates of infection, contact, recovery, etc... The description of each term is also in the comments of the code. The simulation was done by means of time series, which was also described and structured in the lecture notes provided by the professor.

RUNNING THE PROGRAM:

Please run the program. After running, open the 'Plots' tab of python to observe the results of our simulation. The plot of the simulated results can also be found in the directory as 'SIRDA_fig.png'. The simulation shows each parameter over the course of 100 days, given our factors being applied to various differential equations. This accurately visualizes the behavior of these parameters, and can be logically understood. Primarily, we note that all parameters decrease over time until they reach a steady value. Infected, Diagnosed, and Ailing all eventually fall to zero which makes sense. likewise, Recovered increases until it reaches its own steady value. Finally, Susceptible falls and reaches a steady value. This is only accurate as we did not specify that the Susceptible population would decline due to other factors such as herd immunity, which would eventually be reached under this simulation. If the module were to be further altered, the Susceptible population would eventually reach a low enough value for it to be not worth noting, and the Recovered population would become much larger. 
