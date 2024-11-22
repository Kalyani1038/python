import streamlit as st
import math

# Define Elec_Power function
def Elec_Power(V, I, PF):
    """
    Calculate active power (P), reactive power (Q), and apparent power (S)
    
    Parameters:
    V (float): Voltage
    I (float): Current
    PF (float): Power factor
    
    Returns:
    P (float): Active power
    Q (float): Reactive power
    S (float): Apparent power
    """
    phi = math.acos(PF)  # Calculate phase angle
    P = V * I * math.cos(phi)  # Active power (eq. 1)
    Q = V * I * math.sin(phi)  # Reactive power (eq. 2)
    S = V * I  # Apparent power (eq. 3)
    return P, Q, S

# Build Streamlit Web Application
st.title("Electric power_2205A21038")  

# Input parameters
st.subheader("Input Parameters")
V = st.number_input("Voltage (V)", min_value=100, value=100)
I = st.number_input("Current (I)", min_value=10.0, value=10.0)
PF = st.number_input("Power Factor", min_value=0.90, max_value=1.0, value=0.90)

# Calculate and display results
if st.button("Calculate"):
    P, Q, S = Elec_Power(V, I, PF)
    st.subheader("Results")
    st.write(f"Active Power (P): {P:.2f} W")
    st.write(f"Reactive Power (Q): {Q:.2f} VAR")
    st.write(f"Apparent Power (S):{S:.2f}VA")
