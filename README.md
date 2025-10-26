# Put-Call Parity: Fair Put Price Calculator

This Streamlit app calculates the **fair price of a European put option** using the **put-call parity** principle for non-dividend-paying stocks. It’s especially useful for traders and students in markets like India, with inputs in **Rupees (₹)** and **days to expiration**.

---

## 📌 What is Put-Call Parity?

Put-call parity defines a no-arbitrage relationship between European call and put options with the same strike price and expiration:

\[
C - P = S - \frac{K}{(1 + r)^T}
\quad \Rightarrow \quad
P = C - S + \frac{K}{(1 + r)^T}
\]

Where:
- \(C\) = Call option price  
- \(P\) = Put option price (to be calculated)  
- \(S\) = Current stock price  
- \(K\) = Strike price  
- \(r\) = Annual risk-free interest rate (as a decimal)  
- \(T\) = Time to expiration in **years**

This formula ensures that a portfolio of a **long call + cash** is equivalent to a **long put + long stock** .

> 💡 For continuous compounding (common in theory), the formula uses \(K e^{-rT}\), but this app uses discrete annual compounding \(\frac{K}{(1 + r)^T}\) for simplicity and practicality.

---

## 🚀 Features

- Input time to expiration in **days** (automatically converted to years)
- All values displayed in **Indian Rupees (₹)**
- Real-time fair put price calculation
- Warning for negative (non-realistic) put prices
- Clean, intuitive interface built with **Streamlit**

---

## ▶️ How to Run

1. **Install dependencies**:
   ```bash
   pip install streamlit
   ```

2. **Save the code** as `put_call_parity.py`

3. **Run the app**:
   ```bash
   streamlit run put_call_parity.py
   ```

4. Open the URL shown in your terminal (usually `http://localhost:8501`)

---

## 📊 Example Use Case

Suppose:
- Stock price (\(S\)) = ₹100  
- Strike (\(K\)) = ₹100  
- Call price (\(C\)) = ₹10  
- Risk-free rate (\(r\)) = 5% → `0.05`  
- Days to expiry = 365  

The app computes:
- \(T = 365 / 365 = 1.0\) year  
- \(PV(K) = 100 / (1.05)^1 ≈ 95.24\)  
- \(P = 10 - 100 + 95.24 = ₹5.24\)

✅ **Fair put price = ₹5.24**

---

## ⚠️ Important Notes

- **Applies only to European options** (no early exercise).
- Assumes **no dividends** during the option’s life.
- In real markets, small deviations may exist due to bid-ask spreads, liquidity, or transaction costs.
- A negative put price indicates **arbitrage opportunity** or **input error**.

---

## 📚 References

- Put-call parity for non-dividend-paying stocks: \(p = c - S + Xe^{-r(T-t)}\) .
- The relationship ensures no risk-free arbitrage between synthetic and actual positions .

---

## 🛠️ Customization

Feel free to modify the code to:
- Use continuous compounding (`PV_K = K * exp(-r * T)`)
- Add dividend yield support
- Include arbitrage detection logic

---

Made with 💡 for traders, students, and finance enthusiasts in India and beyond!# Put-Call_Parity
