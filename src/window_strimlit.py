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

    frequency = st.number_input(
        label="Enter Sine Wave Frequency (Number of Cycles):",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )

    if st.button("Generate and Display Plot"):
        st.subheader(f"Plotting a Sine Wave with {frequency} cycles")
        x = np.linspace(0, 2 * np.pi, 500)
        y = np.sin(x * frequency)
        fig, ax = plt.subplots()
        ax.plot(x, y, color='dodgerblue', linewidth=2)
        ax.set_title(f"Sine Wave (Frequency: {frequency})")
        ax.set_xlabel("x (radians)")
        ax.set_ylabel("sin(x)")
        ax.grid(True, linestyle='--', alpha=0.6)
        st.pyplot(fig)
        if st.checkbox("Show Raw Data"):
            data = pd.DataFrame({'x': x, 'y': y})
            st.dataframe(data)
        time.sleep(10)
streamlit_window()