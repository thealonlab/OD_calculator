import streamlit as st
import math

# Define the pick and probability functions

def calc_generations(OD_start,OD_end):
    ratio = OD_end / OD_start
    log_ratio = math.log(ratio)
    log_2 = math.log(2)
    return round(log_ratio / log_2,2)

# Streamlit App
def main():
    st.title("Generation time calculator")

    # Streamlit input widgets
    OD_start = st.number_input("Enter the OD at the start of the interval:", min_value=0.01, value=0.25, step=0.1)
    OD_end = st.number_input("Enter the OD at the end of the interval:", min_value=0.01, value=0.5, step=0.1)
    Time_delta = st.number_input("Enter the time interval in minutes:", min_value=5, value=60, step=5)

    if st.button("Calculate"):
        # Calculate insert concentration
        n_generations = calc_generations(OD_start,OD_end)
        per_hour = round(n_generations * 60 / Time_delta,2)

        st.write(f"### The number of generations is {n_generations}")
        st.write(f"### The number of generations per hour is {per_hour}")

    st.title("Estimate time to harvest/induce")

    desired_OD = st.number_input("Enter the desired OD:", min_value=0.01, value=0.5, step=0.1)
    current_OD = st.number_input("Enter the current OD:", min_value=0.01, value=0.25, step=0.1)
    growth_rate = st.number_input("Enter the growth rate in generations per hour:", min_value=0.01, value=3.0, step=0.1)

    if st.button("Time to target"):
        # Calculate insert concentration
        generations_to_target = calc_generations(current_OD,desired_OD)
        time = generations_to_target / growth_rate

        st.write(f"### The time to target is {time} hours, or {time * 60} minutes")


if __name__ == "__main__":
    main()
