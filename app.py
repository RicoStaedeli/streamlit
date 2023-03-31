import streamlit as st
import pandas as pd
import numpy as np

# Daten einlesen
iris_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Durchschnittliche Abmessungen nach Art berechnen
avg_dims = iris_df.groupby("species").mean()

# Streamlit-App definieren
def app():
    st.title("Iris-Datensatzanalyse")

    # Slider-Widget definieren
    view_option = st.slider(
        "Ansicht auswählen", 0, 3, 0, 1
    )

    # Daten entsprechend Slider-Position auswählen
    if view_option == 0:
        data = iris_df
        st.subheader("Alle Daten")
    else:
        species = avg_dims.index[view_option - 1]
        data = iris_df[iris_df["species"] == species]
        st.subheader(f"Durchschnittliche Abmessungen von {species.title()}")

    # Daten anzeigen
    st.write(data)

    # Liniendiagramm anzeigen
    chart_data = data.groupby("species").mean().reset_index(drop=True)
    chart_data = chart_data.T

    st.line_chart(chart_data, use_container_width=True)

app()