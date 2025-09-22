
import os
from PIL import Image
import streamlit as st

def afficher_zone(zone):    
    img_path = os.path.join(image_folder, zone["image"])
    st.write(zone["texte"], unsafe_allow_html=True)
    if os.path.exists(img_path):
        st.image(Image.open(img_path), use_container_width =True)
    else:
        st.warning(f"Image non trouvée : {zone['image']}")
    st.subheader(zone["titre"])


# Configuration de la page
st.set_page_config(page_title="DIABLO, the review, by AjaxxxProMax", layout="wide")
st.markdown("""
    <h1 style='color: #8A0303; font-family: Verdana; font-size: 48px;'>DIABLO</h1>
""", unsafe_allow_html=True)



# 📁 Dossier contenant les images
image_folder = "images"
st.markdown("""
    <h1 style='color: #000000; font-family: Traffic Violation; font-size: 18px;'>DIRECTED BY ERNESTO DIAZ ESPINOZA </h1>
Casting: Scott Adkins, Marko Zaror, Lucho Velasco, Alanna De La Rossa, Jason Gurvitz
""", unsafe_allow_html=True)

zones = [
    {"titre": "EL CORVO", "image": "ELCORVO.JPG", "texte": "<div style='text-align: justify; background-color: #FFFACD; padding: 20px; border-radius: 10px; text-align: justify; color: #333;'><h1 style='color: #8A0303; font-family: Traffic Violation; font-size: 14px;'> In a dark mind riddled with vice, El Corvo prowls like a specter. Cold, solitary, sociopathic, and sadistic, he lives only for the thrill of control and the pleasure of suffering.His empty gaze pierces souls, and his actions leave behind only silence and blood. The day his path crosses that of Kris, a nimble thief with a still beating heart of humanity, a man who steals without taking a life. <br>Their meeting, at first fortuitous, becomes the prelude to a perverse game orchestrated by Vincente, another thief, but this one a seasoned killer and accomplice in the shadows. While Kris struggles to preserve his integrity, El Corvo, fascinated by the moral flaws of this incomplete thief, enjoys pushing him towards the abyss, with Vincente lying in wait, ready to sever the thread of pity. <br>This unstable trio becomes the setting for a descent into hell where innocence wavers and cruelty reigns. Elissa grew up in a smooth, flawless world, where every detail seemed perfectly orchestrated. </h1></div>"},
    {"titre": "JUDAH and VINCENTE", "image": "VincenteJudas.PNG", "texte": "<div style='text-align: justify; background-color: #FFFACD; padding: 20px; border-radius: 10px; font-family:  text-align: justify; color: #333;'><h1 style='color: #8A0303; font-family: Traffic Violation; font-size: 14px;'> This world, which she believed to be her own, was in reality the one her father had crafted for her, a sanitized, controlled universe where freedom was nothing but a carefully maintained mirage. She smiled, laughed, believed she loved, believed she was loved. But all of this was just a backdrop, a skillfully constructed illusion. The day Kris kidnaps her, everything changes. <br>What she initially takes to be a tragedy gradually becomes a brutal revelation.</h1></div>"},
    {"titre": "KRIS", "image": "ELISSAKRIS.PNG", "texte": "<div style='text-align: justify; background-color: #FFFACD; padding: 20px; border-radius: 10px; font-family:  text-align: justify; color: #333;'><h1 style='color: #8A0303; font-family: Traffic Violation; font-size: 14px;'> Torn from her gilded cage, Elissa discovers pain, doubt, fear, but also the truth. She understands that the man she thought was her protector, her safe haven, was in reality her jailer. Her father, the man she thought she loved more than anything, knew nothing about love. He had never offered her anything other than a prison disguised as paradise. Kris, despite his violence, becomes the catalyst for her awakening. Elissa no longer knows who to believe or where to go, but she now knows that happiness cannot be born from lies. And that freedom, even painful, is worth more than the illusion of a love that never existed. </h1></div>"},
    {"titre": "ELISSA", "image": "ELISSA.PNG", "texte": "<div style='text-align: justify; background-color: #FFFACD; padding: 20px; border-radius: 10px; text-align: justify; color: #333;'><h1 style='color: #8A0303; font-family: Traffic Violation; font-size: 14px;'>Nick is the invisible catalyst of the play taking place in Bogota, the one without whom nothing would happen. Unlike the other characters: Elissa, Kris, El Corvo, and Vincent, this modern-day Juda seeks neither to flee nor to dominate: he observes, he understands, he orchestrates.He is an enigmatic character, both director and actor in spite of himself, whose presence triggers the others to move.</h1></div>"},
    {"titre": "JUDA", "image": "JUDA.PNG", "texte": "<div style='text-align: justify; background-color: #FFFACD; padding: 20px; border-radius: 10px; text-align: justify; color: #333;'><h1 style='color: #8A0303; font-family: Traffic Violation; font-size: 14px;'>Judah doesn't speak much, but every word he utters seems to carry the weight of a past unknown to the others. He is the one who sees beyond the masks, who senses Elissa's flaws, Kris's rage, El Corvo's shadows, and Vincent's silences. <br>By bringing these dissonant souls together, Juda seeks not to create harmony, but to reveal a truth. He is the mirror everyone avoids, the common thread that connects wounds, lies, and desires. His strength lies in his lucidity, his ability to bring out the chaos necessary for catharsis.Without Juda, the play would remain frozen, the characters prisoners of their illusions. With him, the theater becomes a place of revelation, of rupture, and perhaps, of rebirt</h1></div>"},
]

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)
for i, col in enumerate([col1, col2]):
    with col:
        afficher_zone(zones[i])

for i, col in enumerate([col3, col4, col5], start=2):
    with col:
        afficher_zone(zones[i])


        
st.markdown("""
    <div style='text-align: justify; background-color: #FFFACD; padding: 20px; border-radius: 10px; text-align: justify; color: #333;'>
<h1 style='color: #8A0303; font-family: Traffic Violation; font-size: 14px;'>
By AjaxxxProMax
</h1>
<h1 style='color: #8A0303; font-family: Traffic Violation; font-size: 24px;'>
<br>© DIABLO 2025
</h1>
</div>

""", unsafe_allow_html=True)
