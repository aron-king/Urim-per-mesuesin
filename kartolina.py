import streamlit as st
st.set_page_config(page_title="Kartolin per 7 mars")
st.subheder("Nje kartolin per ty")
urim_per_mesuesit={
    "Xheni":"Ju falenderojm per dijet qe na jepni ne teknologji",
    "Gjadiolja":"JU falenderoj per dijet qe na jepni ne anglisht",
    "Andon":"JU falenderoj per dijet qe na jepni ne art",
    "Luli":"JU falenderoj per dijet qe na jepni ne biologji",
    "Luiza":"JU falenderoj per dijet qe na jepni ne matematik",
     "Yllka":"JU falenderoj per dijet qe na jepni ne biologji",
     "Andi":"JU falenderoj per dijet qe na jepni ne muzik",
     "Loreta":"JU falenderoj per dijet qe na jepni ne qytetari",
     "Laura":"JU falenderoj per dijet qe na jepni ne matematik",
     "Rexhina":"JU falenderoj per dijet qe na jepni ne fizik",
     "Albana Bega":"JU falenderoj per drejtimin e shkolles ne nje menyr te drejt",
     "Albana Agalliu":"JU falenderoj per mbeshtetjen dhe keshillat qe na jep",
     "Aibana":"JU falenderoj per dijet qe na jepni ne frengjisht",
     "Majlinda":"JU falenderoj per dijet qe na jepni ne gjuhe shqipe",
     "Luli":"JU falenderoj per dijet qe na jepni ne biologji dhe kimi",
     "Genta":"JU falenderoj per mbikqyrjen dhe prezencen qe keni ne drejtori",
     "Arta":"JU falenderoj per kontrollin dhe mbeshtetjen qe na jepni",
     "Paçi":"JU falenderoj per dijet qe na jepni ne aftesim teknologjik",
     "Zeni":"JU falenderoj per dijet qe na jepni ne fizkultur"
     "Egla":"JU falenderoj per dijet qe na jepni ne gjuhe shqipe",
     "Erdita":"JU falenderoj per dijet qe na jepni ne gjuhe shqipe",
     "Vojsava":"JU falenderoj per dijet qe na jepni ne histori",
     "Margarita":"JU falenderoj per dijet qe na jepni ne gjuhe shqipe",
     "Anila":"JU falenderoj per dijet qe na jepni ne gjografi",

}
emri=st.text_inpup("Vendosni emrin tuaj: ")
if st.button("🌷Shfaq urimin🌷"):
    if not emri:
        st.warning("Ju lutem plotesoni emrin tuaj")
    elif emri not in urim_per_mesuesit:
        st.error("Ky mesues nuk punon ne shkollen tone")
    else:
            urimi_personal = urim_per_mesuesit[emri]
            st.success(urimi_personal)
            st.markdown(f"""
            <div style="
            text-align:center;
            background: linear-gradient(135deg,
                #d4edda, #e6f7e6);
                padding:20px;
                border-radius:20px;
                border:3px solid #28a745;
                font-size:20px;
                box-shadow:0 6px 15 px rgba(0,0,0,0.15);
                ">
                
                <h4> GEZUAR FESTEN! </h4> <br>
                <p> {urimi_personal} </p> <br>
                <p> Me dashuri nga Klubi i Kodimit </p>
                <p>Shkolla "22 Tetori" </p>
                </div>

                  """, unsafe_allow_html=True)












