import streamlit as st
import math

# Function to calculate the number of generations
def calc_generations(OD_start, OD_end):
    if OD_start <= 0 or OD_end <= 0:
        return None
    ratio = OD_end / OD_start
    log_ratio = math.log(ratio)
    log_2 = math.log(2)
    return round(log_ratio / log_2, 2)

# Streamlit App
def main():
    st.set_page_config(
        page_title="Growth Calculator",
        page_icon="📈",
        layout="wide",
    )

    # Add a sidebar for inputs
    st.sidebar.title("Inputs")
    st.sidebar.info("Provide input values in the sections below to calculate growth metrics.")

    st.title("Generation Time and Growth Estimation")
    st.markdown("This app helps calculate the number of generations and the time required to reach a target OD.")

    # Section 1: Generation Time Calculator
    st.header("📈 Generation Time Calculator")
    with st.container():
        col1, col2, col3 = st.columns(3)

        # Input fields
        with col1:
            OD_start = st.number_input(
                "OD at start:",
                min_value=0.01,
                value=0.25,
                step=0.1,
                help="The optical density (OD) reading at the start of the interval."
            )
        with col2:
            OD_end = st.number_input(
                "OD at end:",
                min_value=0.01,
                value=0.5,
                step=0.1,
                help="The optical density (OD) reading at the end of the interval."
            )
        with col3:
            Time_delta = st.number_input(
                "Time interval (minutes):",
                min_value=5,
                value=60,
                step=5,
                help="The time (in minutes) for the interval."
            )

        growth_rate = None  # Initialize the growth rate variable

        if st.button("Calculate Generations"):
            # Validate inputs
            if OD_start >= OD_end:
                st.error("OD at the start must be less than OD at the end!")
            else:
                # Perform calculations
                n_generations = calc_generations(OD_start, OD_end)
                growth_rate = round(n_generations * 60 / Time_delta, 2)

                # Display metrics
                col1.metric(label="Generations", value=n_generations)
                col2.metric(label="Generations per hour", value=growth_rate)

    # Section 2: Time to Target OD
    st.header("⏱ Estimate Time to Target OD")
    with st.container():
        col4, col5, col6 = st.columns(3)

        # Input fields
        with col4:
            current_OD = st.number_input(
                "Current OD:",
                min_value=0.01,
                value=0.25,
                step=0.1,
                help="The current optical density (OD) of the culture."
            )
        with col5:
            desired_OD = st.number_input(
                "Desired OD:",
                min_value=0.01,
                value=1.0,
                step=0.1,
                help="The target optical density (OD) for harvesting or induction."
            )
        with col6:
            # Use the calculated growth rate as the default value, if available
            default_growth_rate = growth_rate if growth_rate is not None else 3.0
            growth_rate_input = st.number_input(
                "Growth rate (gen/hr):",
                min_value=0.01,
                value=default_growth_rate,
                step=0.1,
                help="The growth rate of the culture in generations per hour. Automatically populated from previous step if available."
            )

        if st.button("Time to Target"):
            # Validate inputs
            if current_OD >= desired_OD:
                st.error("Current OD must be less than the desired OD!")
            else:
                # Perform calculations
                generations_to_target = calc_generations(current_OD, desired_OD)
                time = round(generations_to_target / growth_rate_input, 2)

                # Display results
                st.success(f"Time to target: {time} hours ({time * 60} minutes)")

    # Footer
    st.markdown("---")

if __name__ == "__main__":
    main()
