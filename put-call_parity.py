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

# Add input for actual market put price
market_P = st.number_input("Actual Market Put Price (P) - Optional", min_value=0.0, value=0.0, step=0.1, 
                          help="Enter the actual market put price to compare with fair value")

# Add Calculate button
calculate_button = st.button("🧮 Calculate Fair Put Price", type="primary", use_container_width=True)

# Only show results when button is clicked
if calculate_button:
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
        # Check if market price is provided for comparison
        if market_P > 0:
            difference = market_P - P
            percentage_diff = (difference / P) * 100 if P > 0 else 0
            
            if market_P > P:
                # Market price is higher than fair value - OVERVALUED (RED)
                st.markdown(f"""
                <div style="background-color: #ff4444; padding: 20px; border-radius: 10px; color: white;">
                    <h3 style="margin: 0;">Fair Put Option Price (P) = ₹{P:.2f}</h3>
                    <p style="margin: 10px 0 0 0; font-size: 16px;">
                        <strong>Market Put Price: ₹{market_P:.2f}</strong><br>
                        Status: <strong>OVERVALUED</strong> by ₹{difference:.2f} ({percentage_diff:.2f}%)<br>
                        The market put is priced higher than the fair value.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            elif market_P < P:
                # Market price is lower than fair value - UNDERVALUED (GREEN)
                st.markdown(f"""
                <div style="background-color: #28a745; padding: 20px; border-radius: 10px; color: white;">
                    <h3 style="margin: 0;">Fair Put Option Price (P) = ₹{P:.2f}</h3>
                    <p style="margin: 10px 0 0 0; font-size: 16px;">
                        <strong>Market Put Price: ₹{market_P:.2f}</strong><br>
                        Status: <strong>UNDERVALUED</strong> by ₹{abs(difference):.2f} ({abs(percentage_diff):.2f}%)<br>
                        The market put is priced lower than the fair value.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Prices are equal - FAIRLY VALUED (BLUE)
                st.markdown(f"""
                <div style="background-color: #007bff; padding: 20px; border-radius: 10px; color: white;">
                    <h3 style="margin: 0;">Fair Put Option Price (P) = ₹{P:.2f}</h3>
                    <p style="margin: 10px 0 0 0; font-size: 16px;">
                        <strong>Market Put Price: ₹{market_P:.2f}</strong><br>
                        Status: <strong>FAIRLY VALUED</strong><br>
                        The market put price matches the fair value.
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            # No market price provided - show default green success
            st.success(f"Fair Put Option Price (P) = ₹{P:.2f}")
            st.info("💡 Enter the actual market put price above to see if it's overvalued or undervalued.")
    
    st.write("""
    > **Note**: This assumes **European options** on a **non-dividend-paying stock**.  
    > If the actual market put price differs significantly, it may indicate an arbitrage opportunity.
    """)
