
# import functions from the modsim.py module
from modsim import *



# SIRDA Implementation

# terms used are as follows:
    
#   S - Susceptible, I - Infected, R - Recovered, D - Diagnosed, A - Ailing
  
# Terms defined from: https://www.nature.com/articles/s41591-020-0883-7 and from the lecture
 
# Population of Santa Clara County is 1.928M , Assuming 10% susceptible, S = 0.1 * 1.928M = 192800

# Confirmed cases within the last 2 weeks is 916, so D = 916

# Assuming 15% more cases that are undiagnosed and ailing, therefore A = 916 * 0.15 = 137

# This means total infected is the sum of diagnosed and ailing, I = A + D = 916 + 137 = 1053

# Total cases in Santa Clara County is 119k, w/ 2089 deaths, so R = 119000 - 2089 = 116911

init = State(S=192800, D=916, A=137, I=1053, R=116911)


# We Divide all terms by the total to normalize the information, making it easier to work with

init /= sum(init)


# Creating System

def make_system(alpha, beta, gamma, epsilon, zeta, lambd, rho, kappa):
    
    init = State(S=192800, D=916, A=137, I=1053, R=116911)
    init /= sum(init)
    
    t0 = 0
    t_end = 7 * 15  # 15 more weeks
    
    return System(init=init, t0=t0, t_end=t_end, 
                  alpha=alpha, beta=beta, gamma=gamma,
                  epsilon=epsilon, zeta=zeta, lambd=lambd,
                  rho=rho, kappa=kappa)


# Applying values to our rates

tci = 3         # time between contact infected -> susceptible (days)
tcd = 10        # time between contact diagnosed -> susceptible (days)
tca = 5         # time between contact ailing -> susceptible (days)
td = 2          # time between infected -> diagnosis (days)
tz = 5          # time between infected -> symptoms (days)
tri = 14        # time to recover from infected (days)
trd = 12        # time to recover from diagnosed (days)
tra = 9         # time to recover from ailing (days)

alpha =  1/tci  # transmission rate infected -> susceptible
beta = 1/tcd    # transmission rate diagnosed -> susceptible
gamma = 1/tca   # transmission rate ailing -> susceptible
epsilon = 1/td  # diagnosis rate
zeta = 1/tz     # symptom rate
lambd = 1/tri   # recovery rate of infected
rho = 1/trd     # recovery rate of diagnosed
kappa =  1/tra  # recovery rate of ailing

system = make_system(alpha, beta, gamma, epsilon, zeta, lambd, rho, kappa)


# Updating the function (one step)

def update_func(state, t, system):
    s, i, r, d, a = state
    
    
    infected = s * (system.alpha * i + system.beta * d + system.gamma * a) - (system.epsilon + system.zeta + system.lambd) * i
    diagnosed = system.epsilon * i - system.rho * d
    ailing = system.zeta * i - system.kappa * a
    recovered = system.lambd * i + system.rho * d + system.kappa * a
    
    s -= infected
    i += infected - recovered - ailing - diagnosed
    r += recovered
    d += diagnosed - recovered
    a += ailing - recovered

    return State(S=s, I=i, R=r, D=d, A=a)


# Calling update function to run single step
state = update_func(init, 0, system)


# Creating time series simulation of system

def run_simulation(system, update_func):

    S = TimeSeries()
    I = TimeSeries()
    R = TimeSeries()
    D = TimeSeries()
    A = TimeSeries()
    
    state = system.init
    t0 = system.t0
    S[t0], I[t0], R[t0], D[t0], A[t0] = state
    
    for t in linrange(system.t0, system.t_end):
        state = update_func(state, t, system)
        S[t+1], I[t+1], R[t+1], D[t+1], A[t+1] = state
        
    return S, I, R, D, A


# Calling the simulation

S, I, R, D, A = run_simulation(system, update_func)


# Plotting the results

def plot_results(S, I, R, D, A):
    
    plot(S, 'r--', label='Susceptible')
    plot(I, '-', label='Infected')
    plot(R, ':', label='Recovered')
    plot(D, 'b--', label='Diagnosed')
    plot(A, 'y:', label='Ailing')
    decorate(xlabel='Time (days)', ylabel='Fraction of Population')
    

# Calling the plotting function

plot_results(S, I, R, D, A)
savefig('SIRDA_Fig.png')







