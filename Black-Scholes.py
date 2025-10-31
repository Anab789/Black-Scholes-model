import math
from scipy.stats import norm
def black_scholes_price(S, X, T, r, sigma, option_type):
    """Calculates the European option price using the Black-Scholes formula."""
    T = max(T, 0.000000000001)
    d1 = (math.log(S/X) + (r+(sigma**2)/2)*T)/(sigma*math.sqrt(T))
    d2 = (math.log(S/X) + (r-(sigma**2)/2)*T)/(sigma*math.sqrt(T))
    if option_type == "call":
        price = (S*norm.cdf(d1))-X*math.exp(-r*T)*norm.cdf(d2)
    else:
        price = (X*math.exp(-r*T))*norm.cdf(-d2)-S*norm.cdf(-d1)
    return price
#Taking user inputs
try:
    S = float(input("Enter current stock price: "))
    X = float(input("Enter the strike price: "))
    T = float(input("Enter the time to maturity in years: "))
    r = float(input("Enter the risk-free rate as a decimal (for example, 0.05): "))
    sigma = float(input("Enter the volatility as a decimal (for example, 0.15): "))
    option_type = input("Enter the option type (for example 'call' or 'put'): ").lower()
    price = black_scholes_price(S, X, T, r, sigma, option_type)
    print("The fair options price is: ", price)
except ValueError:
    print("Please enter valid inputs.")
