print(1)
def streamlit_window():
    import streamlit as st
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import time
    # --- 1. Set up the UI ---
    st.title("Interactive Matplotlib Plotter")
    st.markdown("Use the input box below to set the frequency of the sine wave, then click the button to plot it.")

    # --- 2. Input Element ---
    # Get a number from the user for the frequency (number of cycles)
    frequency = st.number_input(
        label="Enter Sine Wave Frequency (Number of Cycles):",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )

    # --- 3. The Button Trigger ---
    # Check if the user has clicked the button
    if st.button("Generate and Display Plot"):
        # --- 4. Logic (Calculation) ---
        st.subheader(f"Plotting a Sine Wave with {frequency} cycles")

        # Generate data for the plot
        x = np.linspace(0, 2 * np.pi, 500)
        # The 'frequency' variable controls how many cycles appear
        y = np.sin(x * frequency)

        # --- 5. Matplotlib Plotting ---
        # Create the figure and axes objects
        fig, ax = plt.subplots()

        # Plot the data
        ax.plot(x, y, color='dodgerblue', linewidth=2)

        # Add labels and title
        ax.set_title(f"Sine Wave (Frequency: {frequency})")
        ax.set_xlabel("x (radians)")
        ax.set_ylabel("sin(x)")
        ax.grid(True, linestyle='--', alpha=0.6)

        # --- 6. Display the Plot in Streamlit ---
        st.pyplot(fig)

        # Optional: Display the data used for the plot
        if st.checkbox("Show Raw Data"):
            data = pd.DataFrame({'x': x, 'y': y})
            st.dataframe(data)
        time.sleep(10)
    # --- End of script ---
streamlit_window()