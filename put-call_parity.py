import streamlit as st

st.title("Put-Call Parity: Fair Put Price Calculator")

st.write("""
This app uses the **put-call parity** relationship for European options on a non-dividend-paying stock:

$$
C - P = S - \\frac{K}{(1 + r)^T}
\\quad \\Rightarrow \\quad
P = C - S + \\frac{K}{(1 + r)^T}
$$

Where:  
- $C$ = Call price  
- $P$ = Put price (calculated)  
- $S$ = Current stock price  
- $K$ = Strike price  
- $r$ = Annual risk-free interest rate (e.g., 0.05 for 5%)  
- $T$ = Time to expiration in **years** (you'll input in **days**, converted automatically)
""")

# Inputs
S = st.number_input("Current Stock Price (S)", min_value=0.0, value=100.0, step=1.0)
K = st.number_input("Strike Price (K)", min_value=0.0, value=100.0, step=1.0)
C = st.number_input("Call Option Price (C)", min_value=0.0, value=10.0, step=0.1)
r = st.number_input("Annual Risk-Free Rate (r) as decimal (e.g., 0.05)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
days = st.number_input("Time to Expiration in Days", min_value=0, value=365, step=1)

# Convert days to years
T = days / 365.0 if days > 0 else 0.0

# Calculate fair put price
if T > 0:
    PV_K = K / ((1 + r) ** T)
    P = C - S + PV_K
else:
    # If T = 0 (expiring today), PV(K) = K
    P = C - S + K

# Display result
st.subheader("Result")
if P < 0:
    st.warning(f"Calculated put price is negative (₹{P:.2f}), which is not realistic. Check inputs for arbitrage or errors.")
else:
    st.success(f"Fair Put Option Price (P) = ₹{P:.2f}")

st.write("""
> **Note**: This assumes **European options** on a **non-dividend-paying stock**.  
> If the actual market put price differs significantly, it may indicate an arbitrage opportunity.
""")
