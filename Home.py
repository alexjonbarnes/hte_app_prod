import streamlit as st

st.set_page_config(
    page_title="Home",
)

st.title("HTE Web App")

st.subheader("Data Visualisation")
st.write("""
    Generates visualisations from an MNova results CSV file, with two modes available in a single page:
""")
st.markdown("""
- **Pie Chart** – visualise component distributions across the plate, with customisable species selection and colours.
- **Heatmap** – visualise data as a heatmap, either as a ratio of a species to an internal standard, or based on a single column in the results file.
""")

st.subheader("Top-Up Dosing")
st.write("""
    Upload and analyse dosing job files exported from Chronos, with the following outputs:
""")
st.markdown("""
- **Total Dosing Jobs** – combines all uploaded dosing files into a single chronologically ordered table.
- **Actual vs. Target Per Substance Per Well** – summarises the total actual and target doses for each substance per well, with percentage difference calculated.
- **Overdose / Underdose Per Substance Per Well** – flags any wells where the actual dose deviates by more than ±25% from the target.
""")
