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