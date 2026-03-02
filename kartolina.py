import streamlit as st
st.set_page_config(page_title="Kartolin per & Mars")
st.subheder("Nje kartolin per ty")
urim_per_mesuesit={
    "Xheni":"Ju falenderojm per dijet qe na jepni ne teknologji",
    "Gjadiolja":"JU falenderoj per dijet qe na jepni ne anglisht",
    "Andon":"JU falenderoj per dijet qe na jepni ne art"
    "Luli":"JU falenderoj per dijet qe na jepni ne biologji"
    "Luiza":"JU falenderoj per dijet qe na jepni ne matematik"
}

st.text_input("Vendosni emrin tuaj: ")
st.button("🌷Shfaq urimin🌷"):
    if not emri:
        st.warning("ju lutem plotesoni emrin tuaj")
    elif emri not in urim_per_mesuesit:
        st.error("Ky mesues nuk punon ne shkollen 22 Tetori")
        else:
            urimi_personal=urim_per_mesuesit[emri]
            st.markdown(f"""
            <div style="
            text-align:center;
            background: linear-gradient(135deg,
                #d4edda, #e6f7e6);
                padding:20px;
                box-shadow:0 6px 15 px rgba(0,0,0,0.15);
                ">
                
                <h4> GEZUAR FESTEN! </h4> <br>
                <p> {urimi_personal} </p> <br>
                <p> Me dashuri nga Klubi i Kodimit </p>
                <p>Shkolla "22 Tetori" </p>
                </div>

                  """, unsafe_allow_html=True)

