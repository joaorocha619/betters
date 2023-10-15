import streamlit as st

from mclebets import  Circuit
from mclebets import Stymulus

def main():
    team1 = st.text_area("Home Team", "")
    team2 = st.text_area("Away Team", "")

    # Button to place the bet 
    if st.button("Research"):
        

        circuit = Circuit(10)
        stymulus = Stymulus()


        odds = circuit.analyze(stymulus, team1, team2)

        st.write(f"Odds: {1/(2*odds-1)}")


if __name__ == "__main__":
    main()