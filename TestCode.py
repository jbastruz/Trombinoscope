import pandas as pd
import streamlit as st
import webbrowser

#st.set_page_config(layout="wide", page_title="TEST")

test = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vQ2OZ6qprKlwb8Dq5etxii3n61G-HkxAr-cuuRlqNtyzyn4ThliS2yqTf8cSie3D18Et-lIZeqJ3id6/pub?output=xlsx')

st.image("https://asadassistance.com/wp-content/uploads/2024/07/avij-des-savoie-logo.png")

st.markdown("<h1 style='text-align: center;'>Trombinoscope</h1>", unsafe_allow_html=True)

COL1, ColStat, ColLieu, COL2 = st.columns(4)
with ColStat:
    Stat = st.selectbox('statut', list(set(test['Statut'])), index = None)
with ColLieu:
    Loc = st.selectbox('lieu', list(set(test['Lieu'])), index = None)

if Stat == None and Loc == None:
    filtered = test
elif Stat == None and Loc != None:
    filtered = test[test['Lieu'] == Loc]
elif Loc == None and Stat != None:
    filtered = test[test['Statut'] == Stat]
elif Stat != None and Loc != None:
    filtered = test[(test['Statut'] == Stat) & (test['Lieu'] == Loc)]

col1, col2, col3, col4= st.columns(4)

for i, element in enumerate(filtered['Nom']):
    col = col1 if i % 4 == 0 else col2 if i % 4 == 1 else col3 if i % 4 == 2 else col4

    mailto_link= f"mailto:{filtered['Mail'].iloc[i]}"

    with col.container(border=True):
        if pd.isna(filtered['Image'].iloc[i])==False: st.image(filtered['Image'].iloc[i]) 
        elif filtered['Image'].iloc[i] == 'Homme' : st.image('https://asadassistance.com/wp-content/uploads/2024/07/avatar-homme.jpg')
        else : st.image('https://asadassistance.com/wp-content/uploads/2024/07/avatar-femme.jpg')
        st.write(filtered['Nom'].iloc[i]+' '+filtered['Prenom'].iloc[i])
        if pd.isna(filtered['Poste'].iloc[i])==False : st.caption(filtered['Poste'].iloc[i])
        else: st.caption('Poste non renseignée')
        st.markdown(f'<a href={mailto_link}>Mail</a>', unsafe_allow_html=True)