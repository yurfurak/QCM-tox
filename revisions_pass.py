import random
import streamlit as st

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Entrainement PASS", page_icon="💊")
# --- IMAGE DE FOND ---
def ajouter_arriere_plan(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        /* Pour rendre le texte plus lisible, on ajoute un fond blanc semi-transparent aux zones de texte */
        div[data-testid="stExpander"] {{
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Lien vers une image (tu peux changer ce lien par n'importe quelle image sur internet)
# J'ai mis une image style "Laboratoire/Science" assez douce
url_image = "https://i.redd.it/1920x1080-topography-wallpapers-made-by-me-request-for-v0-j8m6ykh6ar1a1.jpg?width=1920&format=pjpg&auto=webp&s=a616adb937a963b9aabdbcd2a21e2696b9533be7"

ajouter_arriere_plan(url_image)

# --- STYLE CSS (Pour rendre ça un peu plus joli) ---
st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #0083B8;
        color: white;
        font-size: 20px;
        padding: 10px 24px;
        border-radius: 8px;
    }
    .success {
        color: #2e7d32;
        font-weight: bold;
        padding: 10px;
        background-color: #e8f5e9;
        border-radius: 5px;
    }
    .error {
        color: #c62828;
        font-weight: bold;
        padding: 10px;
        background-color: #ffebee;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- ZONE DE DONNÉES (Tes futures questions iront ici) ---
questions = questions = questions = questions = [
    # --- PARTIE 1 : ALCOOLISME ---
    {
        "titre": "Concernant l'épidémiologie et la mortalité liée à l'alcool en France :",
        "type": "vraies",
        "items": {
            "A": "L'alcool est la première cause de mortalité prématurée en France.",
            "B": "En 2015, 41 000 décès étaient imputables à l'alcool.",
            "C": "La part de décès attribuables à l'alcool est plus élevée chez les femmes que chez les hommes.",
            "D": "La consommation d'alcool a augmenté régulièrement en France depuis 40 ans.",
            "E": "Il existe une frange de gros buveurs (10% de la population) qui consomme 58% de l'alcool total."
        },
        "correctes": ["B", "E"],
        "explication": "A est Faux : C'est la 2ème cause (après le tabac). B est Vrai (30 000 hommes, 11 000 femmes). C est Faux : 11% des décès masculins contre 4% féminins. D est Faux : Elle a diminué (26L en 1961 contre 12L en 2017) puis stagné. E est Vrai : C'est une donnée majeure de santé publique."
    },
    {
        "titre": "À propos des définitions et dosages des boissons alcoolisées (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Un verre standard (dose bar) contient environ 10g d'alcool pur.",
            "B": "Un demi de bière (25cl à 5°) contient deux fois moins d'alcool qu'un whisky (2,5cl à 40°).",
            "C": "Le 'French Paradox' a prouvé qu'un verre de vin par jour protège du cancer.",
            "D": "Les repères de consommation sont : max 10 verres/semaine et max 2 verres/jour.",
            "E": "Il est recommandé d'avoir au moins 2 jours d'abstinence par semaine."
        },
        "correctes": ["B", "C"],
        "explication": "Ici on cherchait les FAUX. B est Faux : Ils contiennent la même quantité d'alcool pur (~10g). C est Faux : Le French Paradox n'existe pas, même une faible consommation augmente le risque de cancer (sein, etc.). A, D, E sont Vrais."
    },
    {
        "titre": "Concernant l'absorption et la pharmacocinétique de l'éthanol :",
        "type": "vraies",
        "items": {
            "A": "L'absorption est principalement gastrique.",
            "B": "Le passage se fait par diffusion passive.",
            "C": "La prise d'un repas retarde le pic de concentration sanguine (Cmax).",
            "D": "À jeun, le pic est atteint en 45 minutes environ.",
            "E": "70 à 80% de l'alcool est absorbé au niveau de l'intestin grêle."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : L'absorption est majoritairement intestinale (jéjunum/duodénum) et non gastrique. Le reste est vrai : la nourriture ferme le pylore et ralentit le passage vers l'intestin, donc retarde l'absorption."
    },
    {
        "titre": "Quelles sont les affirmations FAUSSES concernant le métabolisme de l'éthanol ?",
        "type": "fausses",
        "items": {
            "A": "La voie principale passe par l'Alcool Déshydrogénase (ADH).",
            "B": "L'ADH est une enzyme mitochondriale.",
            "C": "Le système MEOS (CYP2E1) est une voie accessoire inductible.",
            "D": "L'acétaldéhyde produit est moins toxique que l'éthanol.",
            "E": "L'élimination pulmonaire et rénale représente 50% de l'élimination totale."
        },
        "correctes": ["B", "D", "E"],
        "explication": "B est Faux : L'ADH est cytosolique. D est Faux : L'acétaldéhyde est beaucoup plus toxique et réactif (adduits). E est Faux : L'élimination par le rein/poumon est marginale (3 à 5%), 90%+ est métabolisé par le foie."
    },
    {
        "titre": "Concernant la variabilité génétique des enzymes de l'alcool (ADH/ALDH) :",
        "type": "vraies",
        "items": {
            "A": "L'allèle ADH2*2 code pour une enzyme très active (rapide).",
            "B": "L'allèle ALDH2*2 code pour une enzyme inactive.",
            "C": "La combinaison ADH rapide + ALDH inactive provoque une accumulation d'acétaldéhyde.",
            "D": "Le 'Flush syndrome' (rougeurs, tachycardie) favorise la consommation d'alcool.",
            "E": "Ces polymorphismes sont fréquents dans la population asiatique."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Au contraire, le 'Flush syndrome' est très désagréable (effet antabuse naturel) et protège contre l'alcoolisme car les gens évitent de boire."
    },
    {
        "titre": "Quelles sont les conséquences métaboliques de l'oxydation de l'alcool ?",
        "type": "vraies",
        "items": {
            "A": "L'oxydation de l'alcool augmente le rapport NADH/NAD+.",
            "B": "L'excès de NADH favorise la néoglucogenèse.",
            "C": "L'excès de NADH favorise la synthèse des acides gras (lipogenèse).",
            "D": "L'alcool inhibe la beta-oxydation des lipides.",
            "E": "Cela conduit à une stéatose hépatique (foie gras)."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : L'excès de NADH bloque la néoglucogenèse à partir du pyruvate, ce qui entraîne un risque d'hypoglycémie chez l'alcoolique à jeun."
    },
    {
        "titre": "Concernant la toxicité hépatique de l'alcool, indiquez les propositions FAUSSES :",
        "type": "fausses",
        "items": {
            "A": "La stéatose est irréversible.",
            "B": "La cirrhose est définie par une fibrose mutilante et des nodules de régénération.",
            "C": "Les cellules étoilées du foie jouent un rôle clé dans la fibrose.",
            "D": "L'hépatite alcoolique aiguë est toujours asymptomatique.",
            "E": "Le carcinome hépatocellulaire survient le plus souvent sur un foie sain."
        },
        "correctes": ["A", "D", "E"],
        "explication": "A est Faux : La stéatose est réversible à l'arrêt. D est Faux : L'hépatite aiguë est grave, avec ictère, fièvre et risque de décès. E est Faux : Le cancer survient quasi toujours sur un foie cirrhotique."
    },
    {
        "titre": "Quels sont les liens avérés entre Alcool et Cancer ?",
        "type": "vraies",
        "items": {
            "A": "L'alcool est classé cancérogène certain pour l'homme.",
            "B": "Le risque de cancer du sein augmente de 10% par verre d'alcool quotidien.",
            "C": "L'effet cancérogène est lié à l'acétaldéhyde et au stress oxydant.",
            "D": "Pour les VADS (bouche/gorge), l'association Tabac + Alcool multiplie les risques.",
            "E": "L'alcool protège contre le cancer de la prostate."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'alcool ne protège pas, la relation n'est pas établie ou est à risque. Pour le sein et les VADS, le lien est avéré et fort (synergie avec le tabac)."
    },
    {
        "titre": "À propos du Syndrome d'Alcoolisation Fœtale (SAF) :",
        "type": "vraies",
        "items": {
            "A": "Il n'y a pas de dose seuil de sécurité pendant la grossesse.",
            "B": "Le SAF complet associe dysmorphie, retard de croissance et atteinte neuro-cognitive.",
            "C": "La dysmorphie faciale inclut des fentes palpébrales larges.",
            "D": "Le philtrum est bombé et la lèvre supérieure épaisse.",
            "E": "L'alcool est la première cause de handicap mental non génétique."
        },
        "correctes": ["A", "B", "E"],
        "explication": "C et D sont Faux : C'est l'inverse ! Fentes palpébrales étroites, philtrum lisse (effacé) et lèvre supérieure mince."
    },
    {
        "titre": "Concernant les complications nerveuses et le sevrage (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "L'encéphalopathie de Wernicke est due à une carence en Vitamine B12.",
            "B": "Le syndrome de Korsakoff se caractérise par une amnésie antérograde et des fabulations.",
            "C": "Le Delirium Tremens est la forme mineure du sevrage.",
            "D": "Les crises convulsives de sevrage surviennent souvent 48h après l'arrêt.",
            "E": "Les hallucinations du sevrage peuvent être visuelles ou tactiles (zoopsies)."
        },
        "correctes": ["A", "C"],
        "explication": "A est Faux : Carence en Vitamine B1 (Thiamine), pas B12. C est Faux : Le Delirium Tremens est la forme GRAVE et mortelle (urgence absolue)."
    },
    {
        "titre": "Quels sont les marqueurs biologiques de l'alcoolisme chronique ?",
        "type": "vraies",
        "items": {
            "A": "Le VGM (Volume des globules rouges) augmente en cas d'alcoolisme chronique.",
            "B": "Les Gamma-GT (GGT) sont très spécifiques de l'alcool.",
            "C": "La CDT (Carbohydrate Deficient Transferrin) est le marqueur le plus spécifique.",
            "D": "Une augmentation des transaminases ASAT > ALAT évoque une origine alcoolique.",
            "E": "Les triglycérides peuvent augmenter massivement."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Les GGT sont sensibles mais peu spécifiques (augmentent avec médicaments, diabète, obésité). La CDT est le meilleur marqueur de spécificité (>90%)."
    },
    {
        "titre": "Concernant la législation routière de l'alcool en France :",
        "type": "vraies",
        "items": {
            "A": "Taux limite permis probatoire : 0,2 g/L.",
            "B": "Taux limite conducteur confirmé : 0,5 g/L.",
            "C": "Le seuil délictuel est fixé à 0,8 g/L.",
            "D": "L'éthylomètre a une valeur légale de preuve.",
            "E": "La méthode de Cordebard est utilisée pour le dosage sanguin officiel."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Toutes ces propositions sont exactes. L'éthylotest sert au dépistage, l'éthylomètre et la prise de sang servent à la mesure légale."
    },
    {
        "titre": "Quels sont les effets de l'alcool sur le tube digestif (hors foie) ?",
        "type": "vraies",
        "items": {
            "A": "L'alcool est une cause fréquente de pancréatite aiguë et chronique.",
            "B": "L'alcool favorise la gastrite.",
            "C": "L'alcool améliore l'absorption des nutriments (vitamines).",
            "D": "La diarrhée motrice est fréquente chez l'alcoolique.",
            "E": "L'alcool est un facteur protecteur des cancers de l'œsophage."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Il cause une malabsorption et des carences. E est Faux : C'est un facteur de risque majeur du cancer de l'œsophage."
    },
    {
        "titre": "À propos des questionnaires de repérage (AUDIT/DETA) - Cochez les ERREURS :",
        "type": "fausses",
        "items": {
            "A": "Le questionnaire DETA comporte 10 questions.",
            "B": "Le questionnaire AUDIT a été validé par l'OMS.",
            "C": "Un score AUDIT > 12 suggère une dépendance.",
            "D": "La question 'Avez-vous besoin d'alcool le matin ?' fait partie du DETA.",
            "E": "Le DETA permet de quantifier précisément la consommation en grammes."
        },
        "correctes": ["A", "E"],
        "explication": "A est Faux : Le DETA (CAGE) ne fait que 4 questions. E est Faux : Le DETA repère la dépendance/problème, pas la quantité (c'est l'AUDIT-C ou la déclaration qui quantifie)."
    },
    {
        "titre": "Concernant le Binge Drinking (Alcoolisation Ponctuelle Importante) :",
        "type": "vraies",
        "items": {
            "A": "Défini par une consommation rapide (> 5-6 verres) pour atteindre l'ivresse.",
            "B": "Concerne environ 50% des jeunes de 17 ans (sur le dernier mois).",
            "C": "Augmente le risque ultérieur d'alcoolodépendance.",
            "D": "Est sans danger pour le cerveau en développement.",
            "E": "Peut entraîner des comas éthyliques."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le cerveau des jeunes (jusqu'à 25 ans) est très vulnérable à la neurotoxicité du binge drinking (troubles mémoire, apprentissage)."
    },
    {
        "titre": "Quelles sont les interactions médicamenteuses notables avec l'alcool ?",
        "type": "vraies",
        "items": {
            "A": "L'alcool potentialise l'effet sédatif des benzodiazépines.",
            "B": "L'alcool inhibe le CYP2E1 en prise chronique.",
            "C": "L'alcool augmente la toxicité du paracétamol via le CYP2E1.",
            "D": "L'effet 'Antabuse' se manifeste par une hypotension et des bouffées de chaleur.",
            "E": "La prise aiguë d'alcool peut déstabiliser un traitement AVK."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : En chronique, l'alcool INDUIT (augmente) le CYP2E1, ce qui accélère le métabolisme de certains médicaments et augmente la production de toxiques."
    },
    {
        "titre": "Concernant la physiopathologie de la fibrose hépatique alcoolique :",
        "type": "vraies",
        "items": {
            "A": "Le stress oxydant favorise l'inflammation.",
            "B": "L'acétaldéhyde stimule la production de collagène.",
            "C": "La dysbiose intestinale augmente le passage de LPS (endotoxines).",
            "D": "Le LPS active les cellules de Kupffer via le récepteur TLR4.",
            "E": "Les cellules de Kupffer produisent du TNF-alpha."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tout est vrai. C'est la cascade complexe qui mène de l'alcool à la cirrhose : Dysbiose -> LPS -> Kupffer -> Inflammation -> Activation cellules étoilées -> Fibrose."
    },
    {
        "titre": "À propos du sevrage alcoolique et du Delirium Tremens :",
        "type": "vraies",
        "items": {
            "A": "Le Delirium Tremens survient immédiatement à l'arrêt de l'alcool (1h).",
            "B": "Il associe confusion, agitation, hallucinations et signes végétatifs.",
            "C": "La mortalité sans traitement peut atteindre 35%.",
            "D": "Les benzodiazépines sont le traitement de référence.",
            "E": "L'hydratation n'est pas nécessaire."
        },
        "correctes": ["B", "C", "D"],
        "explication": "A est Faux : Il survient généralement après 48-72h. E est Faux : L'hydratation est cruciale car le patient sue énormément et est en hyperthermie."
    },
    {
        "titre": "Concernant les effets cardio-vasculaires de l'alcool (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "La cardiomyopathie alcoolique est une forme restrictive.",
            "B": "L'alcool peut provoquer une fibrillation auriculaire (Holiday Heart Syndrome).",
            "C": "Une consommation modérée a un effet protecteur potentiel sur les cardiopathies ischémiques.",
            "D": "L'alcool baisse la pression artérielle de manière chronique.",
            "E": "La cardiomyopathie nécessite une consommation importante (>80g/j) et prolongée."
        },
        "correctes": ["A", "D"],
        "explication": "A est Faux : C'est une cardiomyopathie DILATÉE (le cœur grossit et pompe mal). D est Faux : L'alcool est hypertenseur (augmente la tension)."
    },
    {
        "titre": "Comment l'alcool est-il excrété de l'organisme ?",
        "type": "vraies",
        "items": {
            "A": "95% de l'alcool est métabolisé par le foie.",
            "B": "L'élimination pulmonaire suit une constante par rapport au sang (1/2100).",
            "C": "L'alcool passe dans le lait maternel.",
            "D": "Le rein élimine 50% de l'alcool ingéré.",
            "E": "La sueur élimine une petite partie de l'alcool."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le rein n'élimine que 2 à 5% de l'alcool sous forme inchangée."
    },
    {
        "titre": "Concernant la prise en charge de l'hépatite alcoolique aiguë :",
        "type": "vraies",
        "items": {
            "A": "Le sevrage total est indispensable.",
            "B": "La corticothérapie est indiquée dans les formes sévères (Score de Maddrey élevé).",
            "C": "La nutrition entérale est souvent nécessaire.",
            "D": "La transplantation est proposée en première intention en phase aiguë.",
            "E": "La survie à 5 ans d'une cirrhose décompensée est faible."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : On ne greffe pas en phase aiguë d'hépatite alcoolique (règle des 6 mois d'abstinence souvent appliquée, bien que débattue, mais jamais en 1ere intention dans l'urgence infectieuse/inflammatoire)."
    },
    {
        "titre": "Quels sont les signes cliniques d'imprégnation alcoolique chronique ?",
        "type": "vraies",
        "items": {
            "A": "Érythrose faciale et varicosités.",
            "B": "Maladie de Dupuytren (rétraction des doigts).",
            "C": "Hypertrophie des parotides.",
            "D": "Tremblements des extrémités.",
            "E": "Gynécomastie chez l'homme."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tous ces signes sont des classiques de l'examen clinique de l'alcoolodépendant chronique."
    },
    {
        "titre": "Quels sont les critères cliniques de la dépendance ?",
        "type": "vraies",
        "items": {
            "A": "Tolérance (besoin d'augmenter les doses).",
            "B": "Syndrome de sevrage à l'arrêt.",
            "C": "Perte de contrôle de la consommation.",
            "D": "Désir persistant mais infructueux de diminuer.",
            "E": "Poursuite de la consommation malgré les conséquences nocives."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Ce sont les critères DSM classiques de l'addiction/dépendance."
    },
    {
        "titre": "Concernant l'alcool et l'accidentologie routière :",
        "type": "vraies",
        "items": {
            "A": "L'alcool est responsable de 30% de la mortalité routière.",
            "B": "Le risque d'accident mortel est multiplié par 17,8 chez les conducteurs positifs.",
            "C": "Les accidents avec alcool sont moins graves que les autres.",
            "D": "L'alcool rétrécit le champ visuel.",
            "E": "L'alcool augmente le temps de réaction."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Ils sont plus graves (vitesse, absence de freinage). D et E expliquent pourquoi les accidents arrivent (vision tunnel + réflexes lents)."
    },
    {
        "titre": "Quels sont les effets hématologiques de l'alcool ?",
        "type": "vraies",
        "items": {
            "A": "Macrocytose (augmentation de la taille des globules rouges).",
            "B": "Thrombopénie (baisse des plaquettes) par toxicité directe.",
            "C": "Leucopénie possible.",
            "D": "Anémie carentielle (folates).",
            "E": "L'alcool augmente l'agrégation plaquettaire."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'alcool diminue l'agrégation plaquettaire (effet 'fluidifiant' à faible dose, mais risque hémorragique à forte dose)."
    },
    {
        "titre": "À propos de l'Encéphalopathie de Gayet-Wernicke :",
        "type": "vraies",
        "items": {
            "A": "C'est une urgence médicale.",
            "B": "Elle associe confusion, ataxie (troubles équilibre) et troubles oculomoteurs.",
            "C": "Elle est due à une toxicité directe de l'éthanol sur le cervelet.",
            "D": "Elle nécessite une injection de vitamine B1 avant tout apport glucosé.",
            "E": "Elle peut évoluer vers un syndrome de Korsakoff."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Elle est due à la carence en Vitamine B1, pas à la toxicité directe. Il faut donner la B1 AVANT le sucre pour éviter d'aggraver les lésions."
    },
    {
        "titre": "Concernant le coût social de l'alcool :",
        "type": "vraies",
        "items": {
            "A": "Le coût social est estimé à 120 milliards d'euros (2015).",
            "B": "Les recettes des taxes couvrent largement le coût social.",
            "C": "Le coût inclut les pertes de production et les vies humaines perdues.",
            "D": "Le coût du tabac est supérieur à celui de l'alcool.",
            "E": "Les dépenses de soins représentent la majorité du coût."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : Les taxes (3-4 milliards) sont ridicules par rapport au coût (120 milliards). Le coût social est bien supérieur aux recettes."
    },
    {
        "titre": "Concernant la méthode de dosage de Cordebard (Chimie) :",
        "type": "vraies",
        "items": {
            "A": "C'est une méthode de dosage officielle.",
            "B": "Elle utilise l'oxydation de l'éthanol par le bichromate de potassium.",
            "C": "La réaction se fait en milieu basique.",
            "D": "On dose l'excès de bichromate par iodométrie.",
            "E": "C'est une méthode enzymatique."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Milieu ACIDE (acide sulfurique). E est Faux : C'est une méthode CHIMIQUE (oxydoréduction), pas enzymatique."
    },
    {
        "titre": "Quels sont les délais de normalisation des marqueurs biologiques après sevrage ?",
        "type": "vraies",
        "items": {
            "A": "L'alcoolémie s'annule en quelques heures.",
            "B": "La CDT se normalise en 2 à 4 semaines.",
            "C": "Le VGM se normalise très vite (1 semaine).",
            "D": "Les GGT diminuent de moitié en 2 semaines environ.",
            "E": "Le VGM nécessite 3 mois (renouvellement des globules rouges) pour se normaliser."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Le VGM est le marqueur le plus lent à se normaliser (la vie d'un globule rouge est de 120 jours)."
    },
    {
        "titre": "Quels facteurs influencent le taux d'alcoolémie ?",
        "type": "vraies",
        "items": {
            "A": "Le sexe (plus élevée chez la femme à dose égale).",
            "B": "Le poids (plus élevée chez les petits poids).",
            "C": "La prise de nourriture (diminue le pic).",
            "D": "La vitesse de consommation.",
            "E": "Le type de boisson (bulles accélèrent l'absorption)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tous ces facteurs modifient la pharmacocinétique de l'alcool."
    },

    # --- PARTIE 2 : DOPAGE ---
    {
        "titre": "Concernant la définition et les structures de lutte contre le dopage (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Le dopage ne concerne que les compétitions.",
            "B": "L'AMA (WADA) édicte le Code Mondial Antidopage.",
            "C": "L'AFLD est l'agence française chargée des contrôles.",
            "D": "Une conduite dopante peut concerner un étudiant ou un musicien.",
            "E": "La liste des produits interdits est fixe et ne change jamais."
        },
        "correctes": ["A", "E"],
        "explication": "A est Faux : Le dopage concerne aussi l'entraînement et les contrôles hors compétition. E est Faux : La liste est mise à jour chaque année (au 1er janvier)."
    },
    {
        "titre": "Concernant la classe S1 (Agents anabolisants) dans la liste des interdictions :",
        "type": "vraies",
        "items": {
            "A": "La testostérone est le chef de file.",
            "B": "Ils augmentent la synthèse des protéines musculaires.",
            "C": "Ils n'ont aucun effet androgénique.",
            "D": "Le Stanozolol et la Nandrolone sont des exemples.",
            "E": "Les précurseurs (DHEA) sont autorisés."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Ils sont tous androgéniques (virilisants) à divers degrés. E est Faux : Les précurseurs sont interdits (S1)."
    },
    {
        "titre": "Quels sont les effets secondaires des stéroïdes anabolisants (S1) ?",
        "type": "vraies",
        "items": {
            "A": "Arrêt de la croissance chez l'adolescent (soudure des épiphyses).",
            "B": "Atrophie testiculaire et stérilité.",
            "C": "Gynécomastie chez l'homme.",
            "D": "Rauicité de la voix irréversible chez la femme.",
            "E": "Risque cardiovasculaire et hépatique (adénomes)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tableau complet des effets secondaires graves des anabolisants."
    },
    {
        "titre": "Concernant la classe S2 (Hormones peptidiques et facteurs de croissance) :",
        "type": "vraies",
        "items": {
            "A": "L'EPO stimule l'érythropoïèse (globules rouges).",
            "B": "L'hormone de croissance (hGH) est anabolisante et lipolytique.",
            "C": "L'hCG (gonadotrophine) est utilisée pour relancer la testostérone.",
            "D": "Les mimétiques de l'EPO (CERA) sont autorisés.",
            "E": "L'abus d'EPO entraîne un risque de thrombose (sang visqueux)."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Tous les mimétiques et dérivés de l'EPO sont strictement interdits."
    },
    {
        "titre": "À propos des Bêta-2 Agonistes (S3) (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Le Salbutamol (Ventoline) est un bronchodilatateur.",
            "B": "Ils sont tous interdits, quelle que soit la dose.",
            "C": "À forte dose, ils ont un effet anabolisant.",
            "D": "Le Clenbutérol est une substance anabolisante de cette classe.",
            "E": "L'usage par inhalation est toléré sous certains seuils."
        },
        "correctes": ["B"],
        "explication": "B est Faux : Le Salbutamol inhalé est autorisé jusqu'à un certain seuil (1600 mcg/24h). Au-delà, c'est un résultat anormal."
    },
    {
        "titre": "Concernant la classe S4 (Modulateurs hormonaux et métaboliques) :",
        "type": "vraies",
        "items": {
            "A": "Les anti-aromatases empêchent la transformation de testostérone en œstrogène.",
            "B": "Le Tamoxifène est un modulateur des récepteurs aux œstrogènes (SERM).",
            "C": "L'insuline est utilisée pour reconstituer les stocks de glycogène.",
            "D": "Le Meldonium est un modulateur du métabolisme cardiaque.",
            "E": "Ces produits sont utilisés pour contrer les effets secondaires des stéroïdes."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tout est vrai. S4 est une classe 'fourre-tout' qui inclut insuline, anti-oestrogènes et modulateurs métaboliques."
    },
    {
        "titre": "Concernant la classe S5 (Diurétiques et agents masquants) :",
        "type": "vraies",
        "items": {
            "A": "Ils sont interdits en et hors compétition.",
            "B": "Ils permettent une perte de poids rapide (catégories de poids).",
            "C": "Ils diluent les urines pour fausser les tests.",
            "D": "Le Furosémide est un diurétique de l'anse.",
            "E": "Le Probénécide bloque l'excrétion rénale de certains dopants."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Classe S5 très utilisée pour masquer la prise d'autres produits ou 'faire le poids'."
    },
    {
        "titre": "Concernant la classe S6 (Stimulants) :",
        "type": "vraies",
        "items": {
            "A": "Ils sont interdits uniquement en compétition.",
            "B": "La cocaïne et les amphétamines en font partie.",
            "C": "Ils reculent le seuil de fatigue.",
            "D": "Ils augmentent l'agressivité et la vigilance.",
            "E": "La pseudoéphédrine (rhume) est surveillée."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Attention à la pseudoéphédrine (Actifed, etc.) qui peut rendre positif un contrôle en compétition."
    },
    {
        "titre": "Concernant les Narcotiques et Cannabinoïdes (S7 et S8) :",
        "type": "vraies",
        "items": {
            "A": "Les narcotiques (Morphine) masquent la douleur.",
            "B": "Le Cannabis est interdit en compétition.",
            "C": "Le Cannabis améliore les réflexes.",
            "D": "Le CBD est interdit.",
            "E": "Les narcotiques entraînent une forte dépendance."
        },
        "correctes": ["A", "B", "E"],
        "explication": "C est Faux : Il altère les réflexes. D est Faux : Le CBD n'est plus interdit, mais le THC reste interdit en compétition."
    },
    {
        "titre": "Concernant la classe S9 (Glucocorticoïdes) :",
        "type": "vraies",
        "items": {
            "A": "Ils ont un effet anti-inflammatoire et euphorisant.",
            "B": "Ils augmentent la glycémie (diabétogènes).",
            "C": "Ils favorisent la fonte musculaire (catabolisme).",
            "D": "Ils sont interdits par voie orale, intraveineuse, intramusculaire ou rectale en compétition.",
            "E": "Ils fragilisent les tendons (risque de rupture)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Effets classiques des corticoïdes. En dopage, on cherche l'effet stimulant/anti-douleur malgré l'effet catabolique musculaire."
    },
    {
        "titre": "Concernant les Méthodes Interdites (M1, M2, M3) :",
        "type": "vraies",
        "items": {
            "A": "M1 concerne le dopage sanguin (transfusion, transporteurs O2).",
            "B": "M2 concerne la manipulation chimique et physique (falsification d'urine).",
            "C": "M3 concerne le dopage génétique.",
            "D": "L'injection intraveineuse de plus de 100mL est interdite (sauf hôpital).",
            "E": "La transfusion autologue (son propre sang) est autorisée."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Toute transfusion (autologue ou homologue) est interdite sans raison médicale vitale."
    },
    {
        "titre": "Concernant le déroulement du Contrôle Antidopage (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Le sportif est convoqué par une notification.",
            "B": "Il a 24h pour se présenter au poste de contrôle.",
            "C": "Le prélèvement urinaire doit être observé directement par un contrôleur du même sexe.",
            "D": "Le sang et l'urine sont répartis en deux flacons (A et B).",
            "E": "Le sportif doit signaler les médicaments pris dans les 7 derniers jours."
        },
        "correctes": ["B"],
        "explication": "B est Faux : Il doit se présenter IMMÉDIATEMENT (ou dans un délai très court justifié, genre podium/presse, mais sous escorte). Pas 24h !"
    },
    {
        "titre": "Concernant les AUT et la Responsabilité :",
        "type": "vraies",
        "items": {
            "A": "Le principe de 'Responsabilité Objective' s'applique au sportif.",
            "B": "Le sportif est responsable de toute substance trouvée dans son corps.",
            "C": "Une AUT permet d'utiliser un produit interdit pour raison médicale.",
            "D": "L'AUT peut être rétroactive dans tous les cas.",
            "E": "La contamination d'un complément alimentaire est une excuse acceptée pour annuler la sanction."
        },
        "correctes": ["A", "B", "C"],
        "explication": "D est Faux : Rétroactive seulement en cas d'urgence vitale. E est Faux : C'est une circonstance atténuante, mais la sanction tombe quand même (responsabilité objective)."
    },
    {
        "titre": "À propos du Profil Biologique du Sportif (Passeport) :",
        "type": "vraies",
        "items": {
            "A": "Il suit les variations individuelles des paramètres sanguins et urinaires.",
            "B": "Il permet de détecter les effets du dopage sans trouver la substance.",
            "C": "Le module hématologique surveille l'hémoglobine et les réticulocytes.",
            "D": "Le module stéroïdien surveille le ratio Testostérone/Epitestostérone.",
            "E": "C'est une preuve indirecte de dopage."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Outil puissant pour le ciblage et la sanction indirecte."
    },
    {
        "titre": "Concernant les Bêta-bloquants (P1) :",
        "type": "vraies",
        "items": {
            "A": "Ils sont interdits dans tous les sports.",
            "B": "Ils sont utilisés pour réduire le tremblement et le stress.",
            "C": "Ils sont spécifiques aux sports de précision (Tir, Golf, Automobile...).",
            "D": "Ils ralentissent le cœur (bradycardie).",
            "E": "Ils sont contre-productifs dans les sports d'endurance intense."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : Ils ne sont interdits QUE dans certains sports spécifiques (P = Particulier)."
    },
    {
        "titre": "Quels sont les risques liés à l'hormone de croissance (hGH) ?",
        "type": "vraies",
        "items": {
            "A": "Diabète.",
            "B": "Acromégalie (déformation os visage/mains).",
            "C": "Cancer (colorectal, etc.).",
            "D": "Cardiomyopathie.",
            "E": "Hypoglycémie sévère."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "L'hGH est hyperglycémiante (anti-insuline), donc risque de diabète, pas d'hypoglycémie."
    },
    {
        "titre": "Connaissances spécifiques sur certaines substances dopantes :",
        "type": "vraies",
        "items": {
            "A": "Le Roxadustat stimule les facteurs HIF (érythropoïèse).",
            "B": "L'EPO recombinante est identique à l'EPO naturelle.",
            "C": "Le Clenbutérol a des effets anabolisants et brûle-graisse.",
            "D": "La THG (The Clear) était un stéroïde de synthèse indétectable.",
            "E": "Le Cobalt est utilisé pour stimuler l'érythropoïèse."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : L'EPO recombinante a des profils de glycosylation différents de la naturelle, ce qui permet de la détecter (bandes isoélectriques)."
    },
    {
        "titre": "Qu'est-ce que le dopage génétique (M3) ?",
        "type": "vraies",
        "items": {
            "A": "Utilisation de vecteurs viraux pour modifier l'ADN.",
            "B": "Peut cibler le gène de l'EPO ou de l'IGF-1.",
            "C": "L'inhibition de la myostatine permet d'augmenter la masse musculaire.",
            "D": "Repoxygen était un produit de thérapie génique détourné.",
            "E": "C'est facilement détectable par analyse d'urine standard."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : C'est extrêmement difficile à détecter, nécessite des méthodes spécifiques (PCR digitale, etc.)."
    },
    {
        "titre": "Statistiques et Compléments alimentaires (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Les stéroïdes anabolisants représentent environ 50% des contrôles positifs.",
            "B": "Les compléments alimentaires sont sûrs à 100%.",
            "C": "La majorité des produits dopants sont achetés sur Internet.",
            "D": "Le trafic de dopants génère plus d'argent que le trafic de drogue.",
            "E": "Les produits du marché noir sont souvent sous-dosés ou contaminés."
        },
        "correctes": ["B", "D"],
        "explication": "B est Faux : 15-25% sont contaminés/non conformes. D est Faux : C'est une affirmation souvent dite mais fausse, le trafic de drogue reste économiquement supérieur, bien que le dopage soit très lucratif."
    },
    {
        "titre": "Concernant la localisation et les acteurs de la lutte antidopage :",
        "type": "vraies",
        "items": {
            "A": "L'AMA est basée à Montréal.",
            "B": "Le laboratoire français accrédité est à Châtenay-Malabry (LNDD).",
            "C": "Les douanes collaborent à la lutte antidopage.",
            "D": "Un médecin prescripteur risque des sanctions pénales.",
            "E": "Le sportif risque jusqu'à 4 ans de suspension pour une première infraction lourde."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est partiellement vrai/faux selon la date (il déménage à Saclay), mais historiquement associé à Châtenay. Disons Vrai pour le contexte PASS classique sauf info contraire récente. (Le labo est l'AFLD)."
    },
    {
        "titre": "Quelles sont les cibles physiologiques des anabolisants ?",
        "type": "vraies",
        "items": {
            "A": "Muscle squelettique (hypertrophie).",
            "B": "Cerveau (agressivité, libido).",
            "C": "Peau (acné, séborrhée).",
            "D": "Os (densité osseuse).",
            "E": "Cordes vocales (mue)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Les récepteurs aux androgènes sont présents partout, d'où la multitude d'effets secondaires."
    },
    {
        "titre": "Concernant l'EPO et la physiologie sanguine :",
        "type": "vraies",
        "items": {
            "A": "L'EPO est produite par le rein en réponse à l'hypoxie.",
            "B": "Elle agit sur la moelle osseuse.",
            "C": "Elle augmente le nombre de réticulocytes.",
            "D": "Elle augmente l'Hématocrite.",
            "E": "Elle fluidifie le sang."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Elle ÉPAISSIT le sang (augmente la viscosité), d'où le risque de thrombose/AVC."
    },
    {
        "titre": "Concernant l'historique du Dopage :",
        "type": "vraies",
        "items": {
            "A": "Le dopage existe depuis l'antiquité.",
            "B": "Le décès de Tom Simpson (Tour de France 1967) a été un déclic.",
            "C": "L'affaire Festina (1998) a mené à la création de l'AMA.",
            "D": "Le dopage d'état en Russie a été révélé après les JO de Sotchi.",
            "E": "La lutte antidopage a commencé au 19ème siècle."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La lutte structurée commence dans les années 1960 (premiers tests JO 1968)."
    },
    {
        "titre": "À propos du Cannabis dans le cadre du dopage :",
        "type": "vraies",
        "items": {
            "A": "C'est la substance la plus détectée en compétition en France (hors anabolisants).",
            "B": "Le seuil de détection est élevé (150 ng/ml) pour éviter les cas de tabagisme passif.",
            "C": "Il diminue le stress mais altère la coordination.",
            "D": "Il est autorisé à l'entraînement.",
            "E": "Il est lipophile et reste longtemps dans l'organisme."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tout est vrai. Le cannabis est l'un des produits les plus festifs détectés, interdit seulement en compétition."
    },
    {
        "titre": "Quels sont les effets recherchés par l'usage de Glucocorticoïdes ?",
        "type": "vraies",
        "items": {
            "A": "Augmentation de la masse musculaire.",
            "B": "Recul du seuil de fatigue.",
            "C": "Effet stimulant psychique.",
            "D": "Action anti-douleur et anti-inflammatoire.",
            "E": "Meilleure récupération."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : Ils sont CATABOLIQUES (ils détruisent le muscle), c'est leur principal inconvénient sportif."
    },
    {
        "titre": "Quelles sont les méthodes de masquage physique (M2) ?",
        "type": "vraies",
        "items": {
            "A": "Sondage vésical pour introduire une urine propre.",
            "B": "Utilisation d'un faux pénis (whizzinator).",
            "C": "Ajout de protéases dans le flacon.",
            "D": "Échange d'échantillons.",
            "E": "Ces méthodes sont autorisées si déclarées."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "Ce sont toutes des méthodes de triche physique/chimique strictement interdites."
    },
    {
        "titre": "À propos des Stimulants du SNC (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "La cocaïne bloque la recapture de la dopamine.",
            "B": "Les amphétamines favorisent la libération de noradrénaline.",
            "C": "Ils diminuent la température corporelle.",
            "D": "Ils masquent les signaux d'alarme de la fatigue.",
            "E": "Le risque de mort subite est nul."
        },
        "correctes": ["C", "E"],
        "explication": "C est Faux : Ils provoquent une HYPERTHERMIE maligne d'effort (coup de chaleur). E est Faux : Risque élevé de mort subite par trouble du rythme."
    },
    {
        "titre": "Concernant les Antennes Médicales de Prévention du Dopage (AMPD) :",
        "type": "vraies",
        "items": {
            "A": "L'antenne médicale propose un suivi psychologique.",
            "B": "Elle aide au sevrage des produits.",
            "C": "Elle délivre les sanctions sportives.",
            "D": "Elle est soumise au secret médical.",
            "E": "Elle peut délivrer des attestation de suivi."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : L'AMPD est un lieu de SOIN, pas de sanction (rôle de l'AFLD/Fédérations). Séparation des pouvoirs soin/police."
    },
    {
        "titre": "Quels sont les liens entre Alcool et Dopage ?",
        "type": "vraies",
        "items": {
            "A": "L'alcool était autrefois interdit dans certains sports (Tir, etc.).",
            "B": "Depuis 2018, l'alcool n'est plus sur la liste des interdictions de l'AMA.",
            "C": "L'alcool a un effet anxiolytique (tremblements).",
            "D": "L'alcool est un diurétique (inhibe l'ADH).",
            "E": "L'alcool améliore la récupération musculaire."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'alcool nuit gravement à la récupération (déshydratation, sommeil perturbé, synthèse protéique bloquée)."
    },
    {
        "titre": "Synthèse sur l'éthique et le dopage :",
        "type": "vraies",
        "items": {
            "A": "La créatine est un produit dopant.",
            "B": "La caféine est sur la liste de surveillance mais pas interdite.",
            "C": "Le dopage est contraire à l'esprit sportif.",
            "D": "La protection de la santé de l'athlète est une priorité du Code.",
            "E": "Les sportifs amateurs ne sont pas concernés par la loi antidopage."
        },
        "correctes": ["B", "C", "D"],
        "explication": "A est Faux : La créatine est autorisée. E est Faux : La loi s'applique à tous (détention, trafic), même si les contrôles ciblent l'élite."
    },
    
    # --- PARTIE 3 : GAZ ET INHALANTS ---
    {
        "titre": "Concernant les généralités sur les gaz et solvants inhalés :",
        "type": "vraies",
        "items": {
            "A": "Ce sont des produits chimiques volatils.",
            "B": "Ils sont souvent choisis pour leur faible coût et leur légalité.",
            "C": "Ils n'induisent pas d'effets psychotropes.",
            "D": "On les trouve dans de nombreux produits ménagers et industriels.",
            "E": "La consommation concerne majoritairement les personnes âgées."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Ils sont recherchés justement pour leurs effets euphorisants/psychotropes. E est Faux : Cela concerne surtout les jeunes adultes et adolescents."
    },
    {
        "titre": "À propos des modes de consommation des inhalants :",
        "type": "vraies",
        "items": {
            "A": "Le 'Sniffing' consiste à inhaler le produit dans un sac plastique.",
            "B": "Le 'Huffing' (inhalation forcée) utilise un chiffon imbibé collé sur le nez/bouche.",
            "C": "Le 'Bagging' est l'inhalation via un sac.",
            "D": "Le 'Sniffing' est la pulvérisation directe ou le reniflage.",
            "E": "Ces modes de consommation modifient la quantité absorbée."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : L'inhalation dans un sac s'appelle le 'Bagging'. Le Sniffing est l'inhalation directe."
    },
    {
        "titre": "Concernant la classification des hydrocarbures volatils :",
        "type": "vraies",
        "items": {
            "A": "Les solvants volatils incluent les colles et les marqueurs.",
            "B": "Les aérosols contiennent des gaz propulseurs.",
            "C": "Le Toluène est un solvant fréquent.",
            "D": "Les gaz incluent le protoxyde d'azote uniquement.",
            "E": "Les anesthésiques médicaux (éther, chloroforme) font partie des gaz inhalés."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Les gaz incluent aussi le butane (briquets), le propane, et les fluides frigorigènes."
    },
    {
        "titre": "Quel est le mécanisme d'action des solvants volatils ?",
        "type": "vraies",
        "items": {
            "A": "Le mécanisme est similaire à celui des stimulants (cocaïne).",
            "B": "Le mécanisme est similaire à celui de l'alcool et des sédatifs.",
            "C": "Ce sont des neuro-dépresseurs.",
            "D": "Le dichlorométhane est métabolisé en monoxyde de carbone (CO).",
            "E": "Le méthanol est métabolisé en acide formique."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : Ce ne sont pas des stimulants purs, mais des dépresseurs du système nerveux central (comme l'éthanol), provoquant une ivresse."
    },
    {
        "titre": "Quels sont les effets initiaux (phase d'ivresse) des inhalants ?",
        "type": "vraies",
        "items": {
            "A": "Euphorie et désinhibition.",
            "B": "Hallucinations possibles.",
            "C": "Amélioration de la coordination motrice.",
            "D": "Somnolence et confusion.",
            "E": "La durée des effets est toujours très longue (plusieurs jours)."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : On observe des troubles de la démarche et de l'équilibre. E est Faux : Les effets sont brefs (quelques secondes à quelques heures)."
    },
    {
        "titre": "Concernant les Nitrites d'alkyles (Poppers), cochez les ERREURS :",
        "type": "fausses",
        "items": {
            "A": "La formule générale est R-NO2.",
            "B": "Ils incluent le nitrite d'amyle et de butyle.",
            "C": "Ce sont des liquides volatils souvent vendus en petits flacons.",
            "D": "Ils sont utilisés pour nettoyer les têtes de lecture vidéo (usage détourné).",
            "E": "Ce sont des vasoconstricteurs puissants."
        },
        "correctes": ["E"],
        "explication": "E est Faux : Ce sont des VASODILATATEURS puissants (relâchement des muscles lisses), d'où les bouffées de chaleur et la baisse de tension."
    },
    {
        "titre": "Quel est le mécanisme d'action pharmacologique des Poppers ?",
        "type": "vraies",
        "items": {
            "A": "Ils libèrent du Monoxyde d'Azote (NO).",
            "B": "Ils activent la guanylate cyclase.",
            "C": "Ils augmentent le taux de GMP cyclique (GMPc).",
            "D": "Ils provoquent une contraction des muscles lisses.",
            "E": "Le mécanisme est proche de celui de la trinitrine."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Ils provoquent une RELAXATION des muscles lisses (vasodilatation, relâchement sphinctérien)."
    },
    {
        "titre": "Quels sont les effets recherchés lors de la consommation de Poppers ?",
        "type": "vraies",
        "items": {
            "A": "Brève bouffée vertigineuse (Rush).",
            "B": "Sensation de chaleur interne.",
            "C": "Amélioration de l'érection (vasodilatation).",
            "D": "Contraction du sphincter anal.",
            "E": "Ralentissement de la perception temporelle."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Ils dilatent (relâchent) le sphincter anal, ce qui facilite la pénétration (usage Chemsex)."
    },
    {
        "titre": "Concernant la toxicité aiguë des solvants (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Risque de vertiges et somnolence.",
            "B": "Risque de 'Gueule de bois' (céphalées).",
            "C": "L'overdose est impossible avec ces produits.",
            "D": "Risque de 'Mort subite du renifleur'.",
            "E": "Risque d'asphyxie (si sac plastique sur la tête)."
        },
        "correctes": ["C"],
        "explication": "C est Faux : Le risque de décès est réel, par trouble du rythme cardiaque ou asphyxie."
    },
    {
        "titre": "À propos du phénomène de 'Mort subite du renifleur' :",
        "type": "vraies",
        "items": {
            "A": "Peut survenir même lors d'une première utilisation.",
            "B": "Est causée par une sensibilisation du myocarde aux catécholamines.",
            "C": "Est due à une arythmie cardiaque fatale.",
            "D": "Est provoquée par une réaction allergique cutanée.",
            "E": "Le stress ou l'effort physique peut précipiter l'arrêt cardiaque."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "Le cœur devient hyper-sensible à l'adrénaline, et un stress soudain (peur, effort) déclenche une fibrillation ventriculaire."
    },
    {
        "titre": "Quels sont les risques de toxicité chronique des solvants ?",
        "type": "vraies",
        "items": {
            "A": "Neurotoxicité sévère (cerveau et nerfs périphériques).",
            "B": "Atteintes rénales et hépatiques.",
            "C": "Toxicité pour la moelle osseuse (leucémie, anémie).",
            "D": "Le syndrome fœtal lié aux solvants ressemble au SAF (Alcool).",
            "E": "Amélioration des capacités cognitives à long terme."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Au contraire, on observe une démence et des troubles cognitifs."
    },
    {
        "titre": "Concernant la toxicité aiguë des Poppers (Nitrites) :",
        "type": "vraies",
        "items": {
            "A": "Hypertension artérielle sévère.",
            "B": "Augmentation de la pression intra-oculaire.",
            "C": "Maux de tête et vertiges.",
            "D": "Hypotension artérielle avec risque de syncope.",
            "E": "Formation de méthémoglobine (sang bleu)."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : C'est un vasoDILATATEUR, donc il provoque une HYPOtension (chute de tension)."
    },
    {
        "titre": "Quelles lésions spécifiques sont liées à l'usage chronique de Poppers ?",
        "type": "vraies",
        "items": {
            "A": "Croûtes jaunâtres autour du nez et des lèvres (brûlures chimiques).",
            "B": "Rétinopathie (atteinte de la vision).",
            "C": "Méthémoglobinémie (anémie fonctionnelle).",
            "D": "Amélioration durable de la fonction érectile.",
            "E": "Dépression respiratoire."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : À long terme, ils peuvent causer une dysfonction érectile."
    },
    {
        "titre": "Concernant la prise en charge d'une intoxication aux solvants (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Il faut décontaminer la peau et les vêtements.",
            "B": "On doit administrer de l'adrénaline (sympathomimétique) en urgence.",
            "C": "Les bêta-bloquants peuvent être utilisés pour stabiliser le cœur.",
            "D": "Il faut surveiller les fonctions hépatiques et rénales.",
            "E": "Il n'existe pas d'antidote spécifique universel."
        },
        "correctes": ["B"],
        "explication": "B est Faux : SURTOUT PAS d'adrénaline ! Le cœur est hyper-sensibilisé, cela provoquerait un arrêt cardiaque immédiat."
    },
    {
        "titre": "Quelles sont les méthodes d'analyse toxicologique des gaz/solvants ?",
        "type": "vraies",
        "items": {
            "A": "Le prélèvement sanguin doit être fait dans un flacon hermétique.",
            "B": "La technique de référence est la CPG par espace de tête (Headspace GC-MS).",
            "C": "L'urine est la matrice de choix pour doser les gaz volatils.",
            "D": "On peut doser certains métabolites (ex: acide formique pour le méthanol) dans l'urine.",
            "E": "Les produits volatils s'évaporent vite, rendant l'analyse difficile."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : L'urine est peu intéressante pour les gaz eux-mêmes car ils sont éliminés par les poumons, sauf pour leurs métabolites."
    },
    {
        "titre": "À propos de produits spécifiques (Protoxyde d'azote, Butane, etc.) :",
        "type": "vraies",
        "items": {
            "A": "Le protoxyde d'azote est un gaz hilarant.",
            "B": "Le butane est utilisé dans les briquets.",
            "C": "Les colles contiennent souvent du Toluène.",
            "D": "Le trichloréthylène est un solvant de nettoyage.",
            "E": "Le fréon est un gaz propulseur d'aérosol."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux (piège subtil) : Le Fréon est un fluide frigorigène (frigo/clim), pas un gaz propulseur classique d'aérosol grand public (remplacé par d'autres)."
    },
    {
        "titre": "Quels facteurs influencent la toxicité des inhalants ?",
        "type": "vraies",
        "items": {
            "A": "La méthode d'inhalation (sac vs tissu) influe sur la concentration.",
            "B": "L'association avec d'autres drogues modifie le risque.",
            "C": "L'état cardiaque préexistant n'a aucune importance.",
            "D": "La ré-inhalation de l'air expiré (sac) augmente le risque d'hypoxie/asphyxie.",
            "E": "La tolérance ne se développe jamais."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Un cœur fragile est plus à risque. E est Faux : Tolérance et dépendance existent."
    },
    {
        "titre": "Concernant l'interaction Poppers + Viagra (Danger) :",
        "type": "vraies",
        "items": {
            "A": "L'association Poppers + Viagra (inhibiteur PDE5) est dangereuse.",
            "B": "Cela provoque une hypertension sévère.",
            "C": "Cela provoque une hypotension sévère et un collapsus.",
            "D": "Le risque est cardiaque.",
            "E": "L'association est sans risque."
        },
        "correctes": ["A", "C", "D"],
        "explication": "Cumul de deux vasodilatateurs = chute de tension massive = danger de mort."
    },
    {
        "titre": "Quels sont les symptômes cutanés liés à l'usage d'inhalants ?",
        "type": "vraies",
        "items": {
            "A": "Eczéma de contact autour de la bouche ('Glue sniffer's rash').",
            "B": "Brûlures chimiques par les nitrites.",
            "C": "Teint grisâtre.",
            "D": "Odeur chimique de l'haleine ou des vêtements.",
            "E": "Acne sévère."
        },
        "correctes": ["A", "B", "D"],
        "explication": "L'irritation péri-orale est un signe clinique classique chez le consommateur chronique."
    },
    {
        "titre": "Concernant l'épidémiologie des inhalants :",
        "type": "vraies",
        "items": {
            "A": "Touchent souvent les populations précaires ou jeunes.",
            "B": "La disponibilité est faible.",
            "C": "Le coût est élevé.",
            "D": "C'est souvent une drogue d'initiation.",
            "E": "L'usage est souvent collectif."
        },
        "correctes": ["A", "D", "E"],
        "explication": "Disponibilité grande et coût très faible (produits ménagers)."
    },
    {
        "titre": "Toxicité spécifique du Méthanol et du Dichlorométhane :",
        "type": "vraies",
        "items": {
            "A": "Le méthanol est toxique pour le nerf optique (cécité).",
            "B": "Le dichlorométhane provoque une intoxication au monoxyde de carbone (CO).",
            "C": "L'acide formique est le métabolite toxique du méthanol.",
            "D": "Le traitement du méthanol inclut l'éthanol ou le fomépizole.",
            "E": "Ces produits sont inoffensifs."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "Ce sont des solvants à toxicité spécifique très grave."
    },
    {
        "titre": "Quels sont les effets hématologiques des solvants et nitrites ?",
        "type": "vraies",
        "items": {
            "A": "Le benzène est leucémogène (leucémie).",
            "B": "Les nitrites transforment l'hémoglobine en méthémoglobine.",
            "C": "La méthémoglobine transporte mieux l'oxygène.",
            "D": "L'anémie aplasique est un risque des solvants (benzène).",
            "E": "Le sang devient rouge cerise en cas de méthémoglobinémie."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : La méthémoglobine ne transporte plus l'oxygène (asphyxie). E est Faux : Le sang devient brun/chocolat (cyanose)."
    },
    {
        "titre": "Concernant le Chemsex et l'usage de Poppers :",
        "type": "vraies",
        "items": {
            "A": "Le poppers est utilisé pour faciliter la pénétration anale.",
            "B": "Il est souvent associé à d'autres substances (méthamphétamine, etc.).",
            "C": "Il permet de prolonger l'orgasme.",
            "D": "C'est une pratique sans risque infectieux.",
            "E": "Il induit une désinhibition sexuelle."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "La désinhibition augmente les conduites à risque (MST/VIH)."
    },
    {
        "titre": "En quoi consiste l'analyse par Espace de Tête (Headspace) ?",
        "type": "vraies",
        "items": {
            "A": "On chauffe l'échantillon dans un flacon fermé.",
            "B": "On analyse le liquide au fond du flacon.",
            "C": "On analyse les vapeurs (gaz) au-dessus du liquide.",
            "D": "C'est idéal pour les composés volatils.",
            "E": "Cela permet d'éviter d'injecter du sang dans la machine."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : On prélève justement le gaz ('tête') pour ne pas encrasser l'appareil avec le sang."
    },
    {
        "titre": "Détails sur les risques cardiaques des inhalants :",
        "type": "vraies",
        "items": {
            "A": "Sensibilisation aux catécholamines endogènes.",
            "B": "Bradycardie réflexe.",
            "C": "Tachycardie induite par les poppers.",
            "D": "Fibrillation ventriculaire possible avec les solvants.",
            "E": "L'arrêt cardiaque est toujours précédé de signes avant-coureurs."
        },
        "correctes": ["A", "C", "D"],
        "explication": "E est Faux : La mort subite (Sudden Sniffing Death) est brutale et imprévisible."
    },
    {
        "titre": "Comparaison entre l'Alcool et les Solvants inhalés :",
        "type": "vraies",
        "items": {
            "A": "Tous deux sont des dépresseurs du SNC.",
            "B": "Tous deux peuvent causer une cirrhose ou atteinte hépatique.",
            "C": "Le syndrome fœtal est similaire.",
            "D": "Les solvants agissent plus lentement que l'alcool.",
            "E": "L'ivresse aux solvants dure moins longtemps."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Les solvants (inhalés) agissent quasi instantanément (poumon -> cerveau), plus vite que l'alcool (digestion)."
    },
    {
        "titre": "Concernant l'addiction aux inhalants :",
        "type": "vraies",
        "items": {
            "A": "La dépendance psychologique existe.",
            "B": "La tolérance (besoin d'augmenter les doses) existe.",
            "C": "Il n'y a jamais de syndrome de sevrage.",
            "D": "L'usage chronique peut mener à la démence.",
            "E": "C'est une addiction rare chez les jeunes."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Un syndrome de sevrage (irritabilité, troubles sommeil) est possible."
    },
    {
        "titre": "Quelles sont les propriétés physico-chimiques des inhalants ?",
        "type": "vraies",
        "items": {
            "A": "Les inhalants sont liposolubles (aiment le gras).",
            "B": "Ils passent facilement la barrière hémato-encéphalique.",
            "C": "Ils s'accumulent dans les tissus riches en graisses (cerveau).",
            "D": "Ils sont très solubles dans l'eau.",
            "E": "Ils sont volatils à température ambiante."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Ils sont lipophiles, pas hydrophiles."
    },
    {
        "titre": "Concernant la législation et la prévention des solvants/poppers :",
        "type": "vraies",
        "items": {
            "A": "La vente de solvants est interdite aux mineurs.",
            "B": "Le poppers est actuellement légal en France (sous conditions).",
            "C": "L'usage détourné est difficile à contrôler car les produits sont domestiques.",
            "D": "Il n'y a pas de dépistage routier systématique pour les solvants.",
            "E": "Les fabricants ajoutent parfois des amérisants pour éviter l'ingestion."
        },
        "correctes": ["B", "C", "D"],
        "explication": "Les poppers ont eu un statut juridique fluctuant mais sont en vente libre actuellement. Le dépistage routier cible l'alcool et les stups classiques."
    },
    {
        "titre": "Synthèse sur les Gaz et Inhalants (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Toxicité immédiate cardiaque (arythmie).",
            "B": "Toxicité chronique neurologique.",
            "C": "Les poppers sont des vasoconstricteurs.",
            "D": "L'analyse se fait par CPG espace de tête.",
            "E": "Le traitement est symptomatique (pas d'adrénaline).",
        },
        "correctes": ["C"],
        "explication": "C est Faux : Ce sont des vasodilatateurs."
    },
    # --- PARTIE 4 : ADDICTOLOGIE GÉNÉRALITÉS ---
    {
        "titre": "Concernant l'histoire et l'étymologie de l'addiction :",
        "type": "vraies",
        "items": {
            "A": "Le terme vient du latin 'addicere' (dire à).",
            "B": "En droit romain, l'addictus était un esclave pour dettes.",
            "C": "Au Moyen-Âge, cela désignait une relation d'apprentissage.",
            "D": "Le concept psychiatrique moderne inclut uniquement les substances.",
            "E": "Le terme a toujours eu une connotation médicale."
        },
        "correctes": ["A", "B", "C"],
        "explication": "D est Faux : Le concept moderne inclut les addictions comportementales (sans substance). E est Faux : C'était un terme juridique avant d'être médical."
    },
    {
        "titre": "À propos de la physiopathologie et du circuit de la récompense :",
        "type": "vraies",
        "items": {
            "A": "Le circuit impliqué est le circuit méso-cortico-limbique.",
            "B": "Le neurotransmetteur clé est la Sérotonine.",
            "C": "L'Aire Tegmentale Ventrale (ATV) envoie de la dopamine vers le Nucleus Accumbens.",
            "D": "L'hippocampe gère la mémoire des sensations.",
            "E": "Le cortex préfrontal gère la prise de décision."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Le neurotransmetteur roi du circuit de la récompense est la DOPAMINE (pas la sérotonine)."
    },
    {
        "titre": "Quelle est la définition actuelle de l'Addiction (Concepts actuels) ?",
        "type": "vraies",
        "items": {
            "A": "C'est une pathologie cérébrale chronique.",
            "B": "Elle se caractérise par la perte de contrôle.",
            "C": "Le sujet poursuit la consommation malgré la connaissance des risques.",
            "D": "Le symptôme central est le Craving.",
            "E": "Elle ne concerne que les drogues illicites."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Elle concerne aussi les produits licites (alcool, tabac) et les comportements (jeu, sexe, achats)."
    },
    {
        "titre": "À propos du Craving (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "C'est un besoin compulsif et irrépressible de consommer.",
            "B": "Il est perçu comme approprié et voulu par le patient.",
            "C": "Il peut être déclenché par des stimuli (indices) environnementaux.",
            "D": "C'est un facteur prédictif de rechute.",
            "E": "Son intensité varie au cours du temps (oscillation)."
        },
        "correctes": ["B"],
        "explication": "B est Faux : Le craving est perçu comme INAPPROPRIÉ, intrusif et subit par le patient (il veut arrêter mais le besoin est plus fort)."
    },
    {
        "titre": "Concernant la Tolérance (Notion pharmacologique) :",
        "type": "vraies",
        "items": {
            "A": "C'est la nécessité d'augmenter les doses pour obtenir le même effet.",
            "B": "C'est une diminution de l'effet à dose constante.",
            "C": "Elle disparaît à l'arrêt de la consommation.",
            "D": "Elle est synonyme de dépendance psychique.",
            "E": "Il peut y avoir une tolérance croisée entre molécules proches."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : La tolérance est un mécanisme d'adaptation physique/pharmacologique, elle ne suffit pas à définir l'addiction (ex: morphinique pour la douleur)."
    },
    {
        "titre": "Qu'est-ce que le Sevrage ?",
        "type": "vraies",
        "items": {
            "A": "C'est l'ensemble des symptômes survenant à l'arrêt du produit.",
            "B": "Les symptômes sont identiques pour tous les produits.",
            "C": "Le sevrage témoigne d'une dépendance physique.",
            "D": "Les symptômes poussent le sujet à reconsommer (renforcement négatif).",
            "E": "Le sevrage aux opiacés est différent du sevrage à l'alcool."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Les symptômes physiques sont spécifiques au produit (ex: tremblements pour l'alcool, douleurs pour l'héroïne)."
    },
    {
        "titre": "Comparaison Dépendance Physique vs Psychique (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "La dépendance physique se traduit par la tolérance et le sevrage.",
            "B": "La dépendance psychique est la nécessité de consommer pour se sentir bien.",
            "C": "La dépendance physique est constante et dure toute la vie.",
            "D": "La dépendance psychique (Craving) est le moteur de l'addiction sur le long terme.",
            "E": "La dépendance physique disparaît assez vite après l'arrêt."
        },
        "correctes": ["C"],
        "explication": "C est Faux : La dépendance physique disparaît rapidement (quelques jours/semaines). C'est la dépendance PSYCHIQUE qui est durable et cause les rechutes lointaines."
    },
    {
        "titre": "Concernant la classification des substances selon leurs effets :",
        "type": "vraies",
        "items": {
            "A": "Psycholeptiques : Sédatifs, apaisants (Alcool, Opiacés).",
            "B": "Psychoanaleptiques : Excitants (Cocaïne, Amphétamines).",
            "C": "Psychodysleptiques : Perturbateurs/Hallucinogènes (LSD, Cannabis).",
            "D": "Le Tabac est un psychodysleptique.",
            "E": "L'Héroïne est un psycholeptique."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le tabac (Nicotine) est classé dans les stimulants (Psychoanaleptiques) mineurs."
    },
    {
        "titre": "Concernant la classification CIM-10 des usages :",
        "type": "vraies",
        "items": {
            "A": "L'usage simple n'est défini que pour l'alcool.",
            "B": "L'usage nocif est défini par l'existence de dommages (santé physique/mentale).",
            "C": "La dépendance nécessite au moins 3 critères sur 12 mois.",
            "D": "Les conséquences sociales suffisent à poser le diagnostic de dépendance.",
            "E": "L'usage à risque est une consommation susceptible d'entraîner des complications."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : En CIM-10, les conséquences sociales ne suffisent pas (contrairement au DSM-5). Il faut des signes de dépendance (tolérance, sevrage, perte de contrôle)."
    },
    {
        "titre": "À propos du schéma trivarié de l'Addiction (Facteurs de risque) :",
        "type": "vraies",
        "items": {
            "A": "Le risque dépend de l'interaction Produit x Individu x Environnement.",
            "B": "Les facteurs génétiques n'ont aucun rôle.",
            "C": "L'adolescence est une période de vulnérabilité.",
            "D": "La disponibilité du produit est un facteur environnemental.",
            "E": "La voie d'administration (IV vs Orale) modifie le potentiel addictif."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Il y a une forte héritabilité génétique pour certaines addictions (40-60%)."
    },
    {
        "titre": "Quels sont les facteurs de vulnérabilité individuels (Tempérament/Caractère) ?",
        "type": "vraies",
        "items": {
            "A": "Le tempérament est acquis et changeant.",
            "B": "Le caractère est inné et génétique.",
            "C": "La recherche de nouveauté est un facteur de risque.",
            "D": "L'évitement du danger est un facteur de risque.",
            "E": "La personnalité est l'interaction entre tempérament et caractère."
        },
        "correctes": ["C", "D", "E"],
        "explication": "A et B sont Faux : C'est l'inverse ! Tempérament = Inné/Biologique/Stable. Caractère = Acquis/Éducatif/Évolutif."
    },
    {
        "titre": "Quelles comorbidités psychiatriques sont liées aux addictions ?",
        "type": "vraies",
        "items": {
            "A": "Les troubles bipolaires sont un facteur de risque d'addiction.",
            "B": "L'anxiété sociale (phobie sociale) favorise l'usage d'alcool (anxiolyse).",
            "C": "La schizophrénie est souvent associée au tabagisme et au cannabis.",
            "D": "Le TDAH (Déficit de l'attention) n'est pas un facteur de risque.",
            "E": "Les troubles de la personnalité (borderline, antisociale) sont fréquents."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le TDAH est un facteur de risque majeur d'addiction (impulsivité)."
    },
    {
        "titre": "Concernant les facteurs environnementaux (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "La famille peut être un facteur de risque (conflits, carences).",
            "B": "L'influence des pairs est majeure à l'adolescence.",
            "C": "La précocité de l'exposition (âge de début) est un facteur de protection.",
            "D": "La disponibilité et le coût du produit influencent la consommation.",
            "E": "L'exposition prénatale (grossesse) augmente le risque futur."
        },
        "correctes": ["C"],
        "explication": "C est Faux : Plus on commence JEUNE, plus le risque d'addiction est ÉLEVÉ (cerveau immature)."
    },
    {
        "titre": "Quel est le potentiel addictif des différentes substances ?",
        "type": "vraies",
        "items": {
            "A": "Le tabac (nicotine) a un fort potentiel addictif.",
            "B": "L'héroïne a un potentiel addictif très fort.",
            "C": "Le cannabis a un potentiel addictif faible par rapport à l'héroïne.",
            "D": "L'alcool a un potentiel addictif nul.",
            "E": "La cocaïne a un fort potentiel addictif."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : L'alcool a un potentiel addictif intermédiaire à fort, certainement pas nul."
    },
    {
        "titre": "Quels paramètres pharmacocinétiques influencent l'addiction ?",
        "type": "vraies",
        "items": {
            "A": "Plus le pic plasmatique est rapide (Flash), plus le produit est addictogène.",
            "B": "La voie intraveineuse (IV) est plus addictive que la voie orale.",
            "C": "La voie fumée (inhalée) arrive très vite au cerveau.",
            "D": "Une demi-vie longue favorise l'effet de manque brutal.",
            "E": "La répétition des prises renforce l'addiction."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : C'est l'inverse. Une demi-vie COURTE provoque une chute brutale et un manque intense (ex: Crack vs Méthadone)."
    },
    {
        "titre": "Quels sont les critères du caractère envahissant de l'addiction ?",
        "type": "vraies",
        "items": {
            "A": "Le temps passé à se procurer le produit augmente.",
            "B": "Les activités de loisirs et sociales sont abandonnées.",
            "C": "La vie sentimentale et familiale est préservée.",
            "D": "Le sujet consomme même dans des situations dangereuses (conduite).",
            "E": "L'addiction finit par occuper toute la 'bulle' du patient."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : L'addiction envahit et détruit progressivement la vie sociale, familiale et affective."
    },
    {
        "titre": "Concernant la classification des types d'usage :",
        "type": "vraies",
        "items": {
            "A": "L'usage expérimental est un essai ponctuel.",
            "B": "L'usage récréatif est souvent lié à la fête et aux pairs.",
            "C": "L'usage régulier peut être une automédication (anxiété).",
            "D": "L'abstinence secondaire est un non-usage après une période de consommation.",
            "E": "Tout usage régulier est une addiction."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : On peut avoir un usage régulier sans perte de contrôle ni craving (ex: un verre de vin à table, café le matin), même si le risque existe."
    },
    {
        "titre": "Concernant les Critères de Dépendance (CIM-10 / DSM) (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Désir puissant et compulsif (Craving).",
            "B": "Difficulté à contrôler la durée ou la quantité.",
            "C": "Apparition d'un sevrage à l'arrêt.",
            "D": "Augmentation de la tolérance.",
            "E": "La quantité consommée seule suffit à faire le diagnostic."
        },
        "correctes": ["E"],
        "explication": "E est Faux : Ce n'est pas la quantité qui définit l'addiction, mais le rapport au produit (perte de liberté, conséquences), bien que la quantité soit souvent élevée."
    },
    {
        "titre": "Quelles sont les structures neurobiologiques impliquées dans l'addiction ?",
        "type": "vraies",
        "items": {
            "A": "L'Amygdale gère les émotions et le conditionnement.",
            "B": "Le Nucleus Accumbens est le centre de la motivation/plaisir.",
            "C": "Le Cortex préfrontal permet le contrôle inhibiteur (le frein).",
            "D": "L'Hippocampe stocke les souvenirs liés au produit.",
            "E": "L'addiction est une simple faiblesse de la volonté."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : C'est une maladie neurobiologique complexe, pas un manque de volonté. Le 'frein' cortical est dysfonctionnel."
    },
    {
        "titre": "Concernant le traitement et la prise en charge :",
        "type": "vraies",
        "items": {
            "A": "La prise en charge doit être multidisciplinaire (bio-psycho-sociale).",
            "B": "L'alliance thérapeutique est essentielle.",
            "C": "La RDRD signifie 'Réduction Des Risques et des Dommages'.",
            "D": "L'hospitalisation est systématique.",
            "E": "Les TCC (Thérapies Cognitivo-Comportementales) sont efficaces."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : L'hospitalisation n'est pas systématique, beaucoup de suivis se font en ambulatoire (CSAPA)."
    },
    {
        "titre": "Quelles sont les addictions sans substance reconnues ?",
        "type": "vraies",
        "items": {
            "A": "Le jeu pathologique (Gambling) est reconnu comme addiction.",
            "B": "L'addiction aux écrans (Cyberaddiction) existe.",
            "C": "L'addiction au sport s'appelle la Bigorexie.",
            "D": "Les achats compulsifs sont une forme d'addiction.",
            "E": "Ces addictions n'activent pas le circuit de la récompense."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Elles activent exactement les mêmes circuits dopaminergiques que les drogues."
    },
    {
        "titre": "Quels sont les facteurs de protection contre l'addiction ?",
        "type": "vraies",
        "items": {
            "A": "Bonne estime de soi.",
            "B": "Compétences psychosociales développées.",
            "C": "Soutien familial et cohésion.",
            "D": "Réussite scolaire.",
            "E": "Isolement social."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'isolement est un facteur de risque majeur."
    },
    {
        "titre": "Concernant le Pic de dopamine et le mode d'administration :",
        "type": "vraies",
        "items": {
            "A": "Le tabac fumé provoque un pic rapide (bolus) au cerveau.",
            "B": "Le crack (fumé) agit plus vite que la cocaïne sniffée.",
            "C": "L'injection IV donne un effet immédiat (Flash).",
            "D": "L'ingestion orale donne un pic retardé et moins intense.",
            "E": "La vitesse d'arrivée au cerveau n'influe pas sur l'addiction."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Plus ça monte vite et fort, plus le cerveau apprend l'association et plus le risque addictif est élevé."
    },
    {
        "titre": "Quels sont les risques spécifiques à l'adolescence ?",
        "type": "vraies",
        "items": {
            "A": "Le cerveau adolescent est immature (cortex préfrontal).",
            "B": "Les adolescents sont moins sensibles aux effets sociaux.",
            "C": "La recherche de sensations est forte à cet âge.",
            "D": "Le 'Pruning' (élagage synaptique) a lieu à cette période.",
            "E": "L'exposition précoce modifie durablement le cerveau."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Les adolescents sont HYPER sensibles au regard des pairs et à l'influence sociale."
    },
    {
        "titre": "Concernant les concepts de Renforcement Positif et Négatif :",
        "type": "vraies",
        "items": {
            "A": "Renforcement Positif : Recherche du plaisir (High).",
            "B": "Renforcement Négatif : Évitement du déplaisir (Manque/Stress).",
            "C": "Au début de l'addiction, le renforcement positif prédomine.",
            "D": "À la fin (addiction installée), le renforcement négatif prédomine (boire pour ne pas trembler).",
            "E": "Le renforcement négatif est la recherche de sensations fortes."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Le renforcement négatif, c'est le soulagement d'une souffrance (physique ou psychique)."
    },
    {
        "titre": "À propos du lien causal des comorbidités :",
        "type": "vraies",
        "items": {
            "A": "L'addiction peut causer un trouble psychiatrique (ex: psychose cannabique).",
            "B": "Un trouble psychiatrique peut favoriser l'addiction (automédication).",
            "C": "Les deux troubles peuvent évoluer indépendamment.",
            "D": "Il faut traiter les deux conjointement (double diagnostic).",
            "E": "Il faut toujours attendre le sevrage complet pour traiter la dépression."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : C'est une vieille idée. Aujourd'hui, on traite les deux en parallèle car la dépression empêche le maintien du sevrage."
    },
    {
        "titre": "Concernant la RDRD (Réduction des Risques) :",
        "type": "vraies",
        "items": {
            "A": "Vise à limiter les dommages sans exiger l'abstinence immédiate.",
            "B": "Inclut l'échange de seringues (prévention VIH/VHC).",
            "C": "Inclut les traitements de substitution aux opiacés (Méthadone).",
            "D": "Encourage la consommation de drogues.",
            "E": "Est une étape vers le soin."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : C'est une démarche pragmatique de santé publique pour garder les gens en vie, pas un encouragement."
    },
    {
        "titre": "Quelles psychothérapies sont utilisées en addictologie ?",
        "type": "vraies",
        "items": {
            "A": "L'entretien motivationnel aide le patient à résoudre son ambivalence.",
            "B": "Les TCC travaillent sur les conditionnements et les croyances.",
            "C": "La psychoéducation informe le patient sur sa maladie.",
            "D": "La thérapie familiale est utile, surtout chez les jeunes.",
            "E": "La psychanalyse est le seul traitement validé."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les TCC et l'entretien motivationnel sont les mieux validés scientifiquement dans les addictions."
    },
    {
        "titre": "Distinction Addiction vs Habitude (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "L'habitude est un comportement répété mais contrôlable.",
            "B": "L'addiction implique une perte de liberté.",
            "C": "On peut arrêter une habitude sans souffrance majeure.",
            "D": "L'habitude a toujours des conséquences graves sur la santé.",
            "E": "L'addiction envahit la vie du sujet."
        },
        "correctes": ["D"],
        "explication": "D est Faux : Une habitude (ex: lire le journal, boire un café) n'est pas forcément nocive. L'addiction se définit par les dommages et la perte de contrôle."
    },
    {
        "titre": "Concernant l'Épigénétique :",
        "type": "vraies",
        "items": {
            "A": "L'environnement peut modifier l'expression des gènes.",
            "B": "Le stress précoce peut rendre plus vulnérable aux addictions.",
            "C": "Ces modifications sont irréversibles.",
            "D": "Cela explique pourquoi des jumeaux peuvent être différents face à l'addiction.",
            "E": "C'est l'interaction Gène x Environnement."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : L'épigénétique est potentiellement réversible (c'est l'espoir des thérapies), contrairement à la séquence d'ADN pure."
    },
    
    # --- PARTIE 5 : DROGUES, TOXICOLOGIE & PRISE EN CHARGE ---
    {
        "titre": "Concernant la pharmacologie du Cannabis :",
        "type": "vraies",
        "items": {
            "A": "Le THC est le principal responsable des effets psychoactifs.",
            "B": "Les récepteurs CB1 sont situés principalement en périphérie (système immunitaire).",
            "C": "Les récepteurs CB2 sont situés principalement dans le système nerveux central.",
            "D": "Le THC a une demi-vie très courte (quelques minutes).",
            "E": "Le THC est très lipophile et se stocke dans les graisses."
        },
        "correctes": ["A", "E"],
        "explication": "B et C sont Faux : C'est l'inverse ! CB1 = Central (Cerveau), CB2 = Périphérique (Immunité). D est Faux : Demi-vie longue (44-60h) et relargage tardif."
    },
    {
        "titre": "Concernant le dépistage du Cannabis (Permis/Travail) :",
        "type": "vraies",
        "items": {
            "A": "On peut retrouver du cannabis dans les urines jusqu'à 3 semaines après l'arrêt chez un gros fumeur.",
            "B": "Un test urinaire positif prouve une ivresse cannabique au moment du contrôle.",
            "C": "Seul le dosage sanguin prouve l'emprise immédiate.",
            "D": "Le cannabis n'est pas considéré comme un produit dopant.",
            "E": "La médecine du travail peut dépister le cannabis à l'embauche."
        },
        "correctes": ["A", "C", "E"],
        "explication": "B est Faux : Les urines marquent l'usage passé (métabolites), pas l'état actuel. D est Faux : C'est un dopant interdit en compétition (gardiens de but, etc.)."
    },
    {
        "titre": "À propos de la Cocaïne et du Crack :",
        "type": "vraies",
        "items": {
            "A": "La cocaïne inhibe la recapture de la dopamine, noradrénaline et sérotonine.",
            "B": "Le Crack est obtenu en mélangeant la cocaïne avec du bicarbonate ou de l'ammoniaque.",
            "C": "Le Crack se consomme par injection intraveineuse uniquement.",
            "D": "Les effets du Crack sont plus lents à apparaître que ceux de la cocaïne sniffée.",
            "E": "Le risque cardiovasculaire (infarctus) est majeur."
        },
        "correctes": ["A", "B", "E"],
        "explication": "C est Faux : Le Crack se fume (inhalation des vapeurs) ou s'injecte. D est Faux : Les effets du Crack/fumé sont fulgurants (5-10 secondes), plus rapides que le sniff ou l'IV."
    },
    {
        "titre": "Concernant la pharmacologie des Opiacés :",
        "type": "vraies",
        "items": {
            "A": "L'activation des récepteurs Mu entraîne analgésie et dépression respiratoire.",
            "B": "L'activation des récepteurs Kappa entraîne une mydriase (pupilles dilatées).",
            "C": "L'héroïne est un dépresseur du système nerveux central.",
            "D": "L'antidote en cas de surdosage (overdose) est la Naloxone.",
            "E": "Le myosis (pupilles serrées) est un signe d'imprégnation opiacée."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Les opiacés (Mu et Kappa) entraînent un MYOSIS (pupilles en tête d'épingle). La mydriase est liée au manque ou aux récepteurs Delta (agitation)."
    },
    {
        "titre": "Concernant les Traitements de substitution aux opiacés (TSO) :",
        "type": "vraies",
        "items": {
            "A": "La Méthadone est un agoniste pur des récepteurs Mu.",
            "B": "La Buprénorphine (Subutex) est un agoniste partiel Mu et antagoniste Kappa.",
            "C": "Ces traitements doivent être injectés pour être efficaces.",
            "D": "Le Suboxone associe Buprénorphine + Naloxone pour éviter le détournement par injection.",
            "E": "La Méthadone ne peut pas entraîner de dépendance."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Ils s'administrent par voie ORALE (sirop, comprimé). E est Faux : La méthadone entraîne une forte dépendance physique, mais elle est contrôlée et stabilise le patient."
    },
    {
        "titre": "Concernant les définitions (Pharmakon & Addiction) :",
        "type": "vraies",
        "items": {
            "A": "Pharmakon signifie à la fois remède et poison.",
            "B": "L'addiction est définie uniquement par la quantité consommée.",
            "C": "L'addiction est la perte de contrôle de l'usage malgré les conséquences négatives.",
            "D": "La dépendance physique suffit à définir l'addiction.",
            "E": "Le terme drogue désigne toute substance modifiant l'activité neuronale (SPA)."
        },
        "correctes": ["A", "C", "E"],
        "explication": "B est Faux : La quantité n'est pas le critère principal (cf DSM-5). D est Faux : On peut être dépendant physiquement (ex: traitement morphine) sans être addict (pas de perte de contrôle/craving)."
    },
    {
        "titre": "À propos des Critères DSM-5 (Sévérité) - Cochez les ERREURS :",
        "type": "fausses",
        "items": {
            "A": "Il y a 11 critères diagnostiques.",
            "B": "Présence de 2 à 3 critères = Addiction faible.",
            "C": "Présence de 4 à 5 critères = Addiction modérée.",
            "D": "Présence de 6 critères ou plus = Addiction sévère.",
            "E": "Une addiction sévère nécessite obligatoirement 10 critères."
        },
        "correctes": ["E"],
        "explication": "E est Faux : Dès 6 critères, l'addiction est classée comme sévère."
    },
    {
        "titre": "Concernant l'Alcool et la Neurobiologie :",
        "type": "vraies",
        "items": {
            "A": "L'alcool est un dépresseur du système nerveux central.",
            "B": "En chronique, le cerveau développe une hyperexcitabilité (neuroadaptation).",
            "C": "Le sevrage brutal peut entraîner des crises convulsives.",
            "D": "L'alcool agit principalement en stimulant le système Glutamate.",
            "E": "L'alcool agit en stimulant le système GABA (inhibiteur)."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : L'alcool STIMULE le GABA (inhibiteur) et INHIBE le Glutamate (excitateur). En chronique, le cerveau compense en augmentant le Glutamate, d'où l'hyperexcitabilité au sevrage."
    },
    {
        "titre": "Quelles sont les interactions médicamenteuses majeures avec l'alcool ?",
        "type": "vraies",
        "items": {
            "A": "L'alcool potentialise l'effet sédatif des benzodiazépines.",
            "B": "L'alcool augmente le risque d'hémorragie avec les AVK (anticoagulants).",
            "C": "L'alcool peut provoquer un effet antabuse avec certains antibiotiques.",
            "D": "L'alcool annule l'effet retard (LP) de certaines formes galéniques (Dose Dumping).",
            "E": "L'alcool diminue le risque d'hypoglycémie chez le diabétique."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'alcool AUGMENTE le risque d'hypoglycémie (inhibition néoglucogenèse)."
    },
    {
        "titre": "Concernant les traitements de l'alcoolodépendance :",
        "type": "vraies",
        "items": {
            "A": "Les Benzodiazépines sont utilisées pour le sevrage (prévention Delirium Tremens).",
            "B": "L'Acamprosate aide au maintien de l'abstinence (balance GABA/Glutamate).",
            "C": "Le Baclofène est un agoniste GABA-B utilisé pour réduire le craving.",
            "D": "Le Disulfiram est le traitement de première intention aujourd'hui.",
            "E": "La Naltrexone bloque les récepteurs opioïdes pour réduire le plaisir de boire."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le Disulfiram (effet antabuse violent) est très peu utilisé car dangereux si re-consommation."
    },
    {
        "titre": "À propos du Tabac et de la Chicha :",
        "type": "vraies",
        "items": {
            "A": "Le tabac est la première cause de mortalité évitable.",
            "B": "Une session de chicha équivaut à fumer 1 ou 2 cigarettes.",
            "C": "La chicha délivre beaucoup plus de monoxyde de carbone (CO) que la cigarette.",
            "D": "La nicotine agit sur les récepteurs nicotiniques cholinergiques.",
            "E": "Le Snus est un sachet de tabac à sucer (gencive)."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Une session de chicha équivaut à 20-25 cigarettes (voire plus en volume de fumée et CO)."
    },
    {
        "titre": "Concernant les nouvelles drogues et pratiques :",
        "type": "vraies",
        "items": {
            "A": "Le Purple Drank est un mélange de codéine et d'antihistaminique.",
            "B": "Le Protoxyde d'azote est sans danger neurologique.",
            "C": "Le GHB provoque une amnésie antérograde (drogue du violeur).",
            "D": "La Kétamine peut provoquer des troubles urinaires graves.",
            "E": "Les Cathinones de synthèse miment les effets de la cocaïne/MDMA."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Le Protoxyde d'azote provoque des atteintes neurologiques graves (myélite, sclérose) par carence en Vitamine B12."
    },
    {
        "titre": "Concernant le Score de Cushman (Alcool) - Cochez les ERREURS :",
        "type": "fausses",
        "items": {
            "A": "Il évalue l'intensité du syndrome de sevrage alcoolique.",
            "B": "Il prend en compte le pouls et la pression artérielle.",
            "C": "Il prend en compte les tremblements et les sueurs.",
            "D": "Un score élevé indique un sevrage léger.",
            "E": "Il prend en compte l'agitation et les troubles sensoriels."
        },
        "correctes": ["D"],
        "explication": "D est Faux : Un score élevé (>15) indique un sevrage SÉVÈRE avec risque de Delirium Tremens."
    },
    {
        "titre": "À propos des Comorbidités et Pathologies Duelles :",
        "type": "vraies",
        "items": {
            "A": "Une pathologie duelle associe une addiction et un trouble psychiatrique.",
            "B": "50% des patients addicts ont une pathologie duelle.",
            "C": "Le TDAH est rarement associé aux addictions.",
            "D": "Les troubles du comportement alimentaire (TCA) sont considérés comme des addictions.",
            "E": "L'alcoolisme peut induire une dépression."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : 20% des patients en addictologie ont un TDAH, c'est une comorbidité fréquente."
    },
    {
        "titre": "Concernant l'Arbre des dépendances (Concept) :",
        "type": "vraies",
        "items": {
            "A": "Les branches représentent les objets d'addiction (alcool, jeu, tabac...).",
            "B": "Les racines représentent le terrain (génétique, trauma, éducation).",
            "C": "Couper une branche (arrêter un produit) suffit à guérir l'addiction.",
            "D": "Il faut traiter le sol et les racines pour éviter le déplacement de l'addiction.",
            "E": "Une personne peut avoir plusieurs addictions (plusieurs branches)."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Si on ne traite pas le fond (racines), une autre addiction remplacera la première."
    },
    {
        "titre": "Quelles sont les conséquences somatiques de l'alcool (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "Pancréatite chronique calcifiante.",
            "B": "Varices œsophagiennes.",
            "C": "Rhinophyma (gros nez rouge).",
            "D": "Maladie de Dupuytren (rétraction des doigts).",
            "E": "Hypertrophie des testicules."
        },
        "correctes": ["E"],
        "explication": "E est Faux : L'alcool entraîne une atrophie testiculaire et une féminisation (gynécomastie)."
    },
    {
        "titre": "Concernant le traitement de la Cocaïne :",
        "type": "vraies",
        "items": {
            "A": "Il existe un traitement de substitution officiel pour la cocaïne.",
            "B": "La N-acétylcystéine à forte dose a montré une certaine efficacité.",
            "C": "Le Topiramate (antiépileptique) est parfois utilisé.",
            "D": "La prise en charge repose beaucoup sur la psychothérapie.",
            "E": "Le sevrage de la cocaïne est physiquement mortel (comme l'alcool)."
        },
        "correctes": ["B", "C", "D"],
        "explication": "A est Faux : Aucun traitement de substitution validé. E est Faux : Le sevrage cocaïne est épuisant (crash) et dépressif, mais rarement mortel physiquement, contrairement au sevrage alcool/BZD."
    },
    {
        "titre": "À propos des Benzodiazépines et de leur demi-vie :",
        "type": "vraies",
        "items": {
            "A": "Les BZD à demi-vie courte sont plus addictogènes (effet pic).",
            "B": "Le Seresta (Oxazépam) a une demi-vie rapide/courte.",
            "C": "Le Prazépam (Lysanxia) a une demi-vie longue.",
            "D": "On utilise les BZD à demi-vie longue pour le sevrage dégressif.",
            "E": "L'effet 'toit d'usine' favorise l'accrochage."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tout est vrai. On préfère les molécules à demi-vie longue pour le sevrage afin de lisser les taux plasmatiques."
    },
    {
        "titre": "Comparaison Héroïne vs Méthadone (Pharmacocinétique) :",
        "type": "vraies",
        "items": {
            "A": "L'héroïne a une demi-vie courte et un effet flash.",
            "B": "La méthadone a une demi-vie longue (24h et plus).",
            "C": "La méthadone provoque des variations brutales de la concentration plasmatique.",
            "D": "Le but de la méthadone est de supprimer le manque sans donner d'euphorie.",
            "E": "L'héroïne s'injecte, la méthadone se boit."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : La méthadone donne un plateau stable, ce qui permet la réinsertion sociale, contrairement aux pics/vallées de l'héroïne."
    },
    {
        "titre": "Statistiques des drogues en France (Cochez les ERREURS) :",
        "type": "fausses",
        "items": {
            "A": "47 millions de français boivent de l'alcool.",
            "B": "13 millions de fumeurs quotidiens.",
            "C": "L'héroïne est la drogue la plus consommée.",
            "D": "Le cannabis compte environ 1 million d'usagers quotidiens.",
            "E": "La cocaïne compte environ 600 000 usagers annuels (chiffre en hausse)."
        },
        "correctes": ["C"],
        "explication": "C est Faux : L'héroïne a un marché très faible (50 000 à 600 000 selon les sources, mais bien moins que Cannabis/Cocaine). C'est le Cannabis la drogue illicite la plus consommée."
    },
    {
        "titre": "Concernant le Syndrome d'alcoolisme fœtal :",
        "type": "vraies",
        "items": {
            "A": "Il est la première cause de handicap mental non génétique.",
            "B": "Il se voit par une dysmorphie faciale (oreilles basses, philtrum lisse).",
            "C": "Il n'y a aucun risque durant le dernier trimestre de grossesse.",
            "D": "L'alcool est tératogène.",
            "E": "Toute consommation d'alcool est proscrite pendant la grossesse."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Le cerveau se développe jusqu'à la fin, l'alcool est toxique tout le temps."
    },
    {
        "titre": "Quels sont les rôles des neuromédiateurs de l'addiction ?",
        "type": "vraies",
        "items": {
            "A": "Dopamine = Plaisir, Récompense.",
            "B": "Sérotonine = Régulation de l'humeur, Impulsivité, Compulsion.",
            "C": "Noradrénaline = Vigilance, Énergie.",
            "D": "L'addiction entraîne un découplage entre Sérotonine et Noradrénaline.",
            "E": "Le manque de produit restaure immédiatement l'équilibre."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Le manque crée une souffrance et le déséquilibre persiste longtemps, poussant à la rechute."
    },
    {
        "titre": "Concernant l'Ecstasy (MDMA) :",
        "type": "vraies",
        "items": {
            "A": "C'est un psychostimulant et un perturbateur.",
            "B": "Elle favorise la libération massive de sérotonine.",
            "C": "Elle est souvent consommée en milieu festif.",
            "D": "Elle ne présente aucun risque de déshydratation.",
            "E": "La 'descente' peut s'accompagner d'une dépression passagère."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Risque majeur de déshydratation et d'hyperthermie en milieu festif."
    },
    {
        "titre": "À propos des formes cliniques du sevrage alcoolique :",
        "type": "vraies",
        "items": {
            "A": "Forme mineure : tremblements, anxiété, sueurs.",
            "B": "Forme moyenne : halluicinations (zoopsies), confusion.",
            "C": "Delirium Tremens : Urgence vitale, hyperthermie, agitation majeure.",
            "D": "Le Delirium Tremens a une mortalité spontanée élevée (sans traitement).",
            "E": "Les crises d'épilepsie surviennent toujours après le Delirium."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les crises (Grand Mal) surviennent souvent au début du sevrage (24-48h), parfois avant le DT."
    },
    {
        "titre": "Cas pratique : Calculs d'alcoolémie :",
        "type": "vraies",
        "items": {
            "A": "Un verre standard fait monter l'alcoolémie d'environ 0,20 à 0,25 g/L.",
            "B": "Il faut environ 1h30 à 2h pour éliminer un verre d'alcool.",
            "C": "Le taux d'élimination est d'environ 0,15 g/L par heure.",
            "D": "Manger gras avant de boire annule l'alcoolémie.",
            "E": "La formule de calcul prend en compte le degré et le volume."
        },
        "correctes": ["A", "C", "E"],
        "explication": "B est Faux : Il faut environ 1h pour éliminer un verre (0,15 à 0,20 g/L éliminés par heure). D est Faux : Ça ralentit l'absorption (pic moins haut) mais n'annule pas la quantité d'alcool."
    },
    {
        "titre": "Concernant l'interaction Cocaïne et Alcool (Cocaéthylène) :",
        "type": "vraies",
        "items": {
            "A": "Le mélange forme un métabolite spécifique : le Cocaéthylène.",
            "B": "Ce composé est moins toxique que la cocaïne seule.",
            "C": "Ce composé est plus cardiotoxique.",
            "D": "Ce composé a une demi-vie plus longue.",
            "E": "C'est une interaction dangereuse."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Le cocaéthylène est BEAUCOUP plus toxique pour le cœur."
    },
    {
        "titre": "Quiz : Associez Substances et Récepteurs :",
        "type": "vraies",
        "items": {
            "A": "Nicotine -> Récepteurs nicotiniques à l'acétylcholine.",
            "B": "Cannabis -> Récepteurs CB1 et CB2.",
            "C": "Alcool -> Agoniste GABA et Antagoniste NMDA (Glutamate).",
            "D": "Opiacés -> Récepteurs Mu, Kappa, Delta.",
            "E": "Cocaïne -> Agoniste des récepteurs GABA."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La cocaïne bloque la recapture des monoamines (DA, NA, 5HT), elle n'agit pas directement sur le GABA."
    },
    {
        "titre": "Quels marqueurs biologiques spécifiques sont utilisés ?",
        "type": "vraies",
        "items": {
            "A": "CDT (Transferrine déficiente en carbohydrate) pour l'alcool chronique.",
            "B": "VGM et Gamma-GT pour l'alcool (moins spécifiques).",
            "C": "Cotinine urinaire pour le tabac.",
            "D": "THC-COOH dans les urines pour le cannabis.",
            "E": "Glycémie pour la cocaïne."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La glycémie n'est pas un marqueur de consommation de cocaïne."
    },
    {
        "titre": "Quels sont les risques infectieux liés aux drogues ?",
        "type": "vraies",
        "items": {
            "A": "L'injection intraveineuse expose au VIH et au VHC.",
            "B": "Le partage de paille (sniff) peut transmettre le VHC (Hépatite C).",
            "C": "Le partage de pipe à crack peut transmettre le VHC.",
            "D": "Les rapports sexuels non protégés (Chemsex) sont un risque majeur.",
            "E": "L'alcoolisation chronique diminue l'immunité."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Le VHC est très résistant et se transmet par le sang (micro-lésions nasales ou lèvres brûlées par la pipe)."
    },
    {
        "titre": "Concernant les traitements d'urgence (Antidotes) :",
        "type": "vraies",
        "items": {
            "A": "Naloxone pour l'overdose d'héroïne/opiacés.",
            "B": "Flumazénil pour l'overdose de Benzodiazépines.",
            "C": "N-acétylcystéine pour le paracétamol.",
            "D": "Il n'y a pas d'antidote direct pour l'overdose de cocaïne.",
            "E": "L'alcool est l'antidote du cannabis."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'alcool aggrave les effets du cannabis (potentialisation)."
    },# --- PARTIE 6 : ANNALES (Questions types Examens) ---
    {
        "titre": "Annales : Repères de consommation d'alcool (SPF 2017)",
        "type": "vraies",
        "items": {
            "A": "Maximum 10 verres par semaine.",
            "B": "Maximum 2 verres par jour.",
            "C": "Des jours sans consommation dans la semaine.",
            "D": "Maximum 3 verres par occasion pour les hommes.",
            "E": "Ces repères garantissent l'absence totale de risque."
        },
        "correctes": ["A", "B", "C"],
        "explication": "D est Faux : Les repères sont 10/semaine, 2/jour et des jours off. E est Faux : C'est une réduction des risques, le risque zéro n'existe pas."
    },
    {
        "titre": "Annales : Seuil de risque de cirrhose alcoolique",
        "type": "vraies",
        "items": {
            "A": "Le risque augmente fortement au-delà de 20g/jour chez la femme.",
            "B": "Le seuil est estimé à 30g/jour chez la femme.",
            "C": "Le seuil est estimé à 50g/jour chez l'homme.",
            "D": "La durée d'exposition doit être d'au moins 10 à 15 ans.",
            "E": "La cirrhose survient dès la première année de consommation excessive."
        },
        "correctes": ["B", "C", "D"],
        "explication": "Le risque de cirrhose devient important pour une consommation > 30g (F) ou 50g (H) pendant une durée prolongée (10-15 ans)."
    },
    {
        "titre": "Annales : Métabolisme de l'éthanol et Polymorphisme",
        "type": "vraies",
        "items": {
            "A": "L'éthanol est transformé en acétaldéhyde par l'ADH.",
            "B": "L'acétaldéhyde est transformé en acétate par l'ALDH.",
            "C": "Le polymorphisme génétique concerne surtout les populations caucasiennes.",
            "D": "L'allèle ALDH2*2 (enzyme inactive) entraîne une accumulation d'acétaldéhyde.",
            "E": "Ce polymorphisme explique la sensibilité accrue (Flush) des sujets d'origine asiatique."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Ce polymorphisme est caractéristique des populations asiatiques (Flush syndrome)."
    },
    {
        "titre": "Annales : Toxicité de la Cocaïne et du Crack",
        "type": "vraies",
        "items": {
            "A": "Risque d'infarctus du myocarde par vasoconstriction coronaire.",
            "B": "Risque de perforation de la cloison nasale (sniff).",
            "C": "Complications infectieuses (VIH, VHC) en cas d'injection.",
            "D": "Effet tératogène (malformations) chez la femme enceinte.",
            "E": "La consommation chronique calme l'anxiété et la paranoïa."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La consommation chronique INDUIT de l'anxiété, de l'irritabilité et de la paranoïa."
    },
    {
        "titre": "Annales : Toxicité aiguë et chronique du Cannabis",
        "type": "vraies",
        "items": {
            "A": "Toxicité aiguë : Bad trip, attaque de panique.",
            "B": "Toxicité aiguë : Troubles de la coordination et risque routier.",
            "C": "Toxicité chronique : Syndrome amotivationnel.",
            "D": "Toxicité chronique : Augmentation du risque de schizophrénie sur terrain vulnérable.",
            "E": "Syndrome d'hyperémèse cannabique (vomissements soulagés par l'eau chaude)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Toutes ces propositions correspondent à la toxicité décrite (aigüe et chronique)."
    },
    {
        "titre": "Annales : Protoxyde d'azote (Gaz hilarant)",
        "type": "vraies",
        "items": {
            "A": "L'usage chronique peut entraîner une carence en Vitamine B12.",
            "B": "La complication redoutée est l'atteinte de la moelle épinière (myélite).",
            "C": "Peut provoquer des chutes et des syncopes.",
            "D": "Il n'y a aucun risque de brûlure par le froid.",
            "E": "C'est une cause d'AVC chez le sujet jeune."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le gaz est stocké sous pression liquide, sa libération crée un froid intense (brûlure grave)."
    },
    {
        "titre": "Annales : Dopage à l'EPO",
        "type": "vraies",
        "items": {
            "A": "Effet recherché : Augmentation de l'oxygénation musculaire (VO2max).",
            "B": "Effet recherché : Augmentation de la vigilance.",
            "C": "Effet indésirable : Augmentation de la viscosité sanguine (Hématocrite).",
            "D": "Effet indésirable : Hypertension artérielle.",
            "E": "Effet indésirable : Risque de thrombose et d'AVC."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : L'EPO agit sur l'endurance aérobie, pas comme un stimulant psychique type amphétamine."
    },
    {
        "titre": "Annales : Critères de l'Addiction (DSM-5) - Les Erreurs",
        "type": "fausses",
        "items": {
            "A": "Perte de contrôle (consommer plus ou plus longtemps que prévu).",
            "B": "Efforts infructueux pour arrêter.",
            "C": "Craving (besoin impérieux).",
            "D": "Usage poursuivi malgré les problèmes physiques/psychologiques.",
            "E": "La quantité consommée doit être supérieure à un seuil toxique précis."
        },
        "correctes": ["E"],
        "explication": "E est Faux : Le diagnostic repose sur le COMPORTEMENT (perte de contrôle, conséquences), pas sur une dose seuil précise."
    },
    {
        "titre": "Annales : Intoxication au Monoxyde de Carbone (via Solvants)",
        "type": "vraies",
        "items": {
            "A": "Peut être secondaire au métabolisme du Dichlorométhane.",
            "B": "Signes cliniques : Céphalées, vertiges, nausées.",
            "C": "Signes de gravité : Perte de connaissance, coma.",
            "D": "Le biomarqueur est la carboxyhémoglobine (HbCO).",
            "E": "Le traitement repose sur l'oxygénothérapie."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "Le dichlorométhane (solvant) se métabolise en CO, provoquant une intoxication retardée."
    },
    {
        "titre": "Annales : Nouveaux Produits de Synthèse (NPS)",
        "type": "vraies",
        "items": {
            "A": "Les cathinones de synthèse miment les effets de la cocaïne/MDMA.",
            "B": "Les cannabinoïdes de synthèse miment les effets du THC.",
            "C": "Leur structure chimique est modifiée pour contourner la législation.",
            "D": "Ils sont souvent vendus sur internet.",
            "E": "Leur toxicité est toujours inférieure aux produits naturels."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Leur toxicité est souvent IMPRÉVISIBLE et parfois bien supérieure (puissance élevée)."
    },
    {
        "titre": "Annales : Réglementation anti-asthmatiques (Dopage)",
        "type": "vraies",
        "items": {
            "A": "Le Salbutamol est interdit au-dessus d'un certain seuil urinaire.",
            "B": "Les Bêta-2 agonistes par inhalation sont totalement libres d'usage.",
            "C": "À forte dose, ils ont un effet anabolisant.",
            "D": "La Terbutaline nécessite une AUT (Autorisation d'Usage Thérapeutique).",
            "E": "L'usage systémique (comprimé, injection) est interdit."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Ils sont soumis à des seuils stricts (ex: 1000ng/mL pour salbutamol), même en inhalation."
    },
    {
        "titre": "Annales : Traitement nicotinique de substitution",
        "type": "vraies",
        "items": {
            "A": "Vise à soulager les symptômes de sevrage.",
            "B": "Existe sous forme de patchs et formes orales.",
            "C": "La Varénicline est un agoniste partiel des récepteurs nicotiniques.",
            "D": "La cigarette électronique est considérée comme un outil de réduction des risques.",
            "E": "Il est interdit de fumer avec un patch."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Il n'est pas interdit de fumer avec un patch, on adapte la dose."
    },
    {
        "titre": "Annales : Marqueurs biologiques de l'alcool (Erreurs)",
        "type": "fausses",
        "items": {
            "A": "La CDT est le marqueur le plus spécifique de la consommation chronique.",
            "B": "Le VGM augmente précocement (en quelques jours).",
            "C": "Les Gamma-GT (GGT) manquent de spécificité.",
            "D": "L'éthylglucuronide (EtG) dans les cheveux montre une consommation passée.",
            "E": "Le taux d'alcoolémie reflète la consommation récente."
        },
        "correctes": ["B"],
        "explication": "B est Faux : Le VGM met 2 à 3 mois à augmenter (renouvellement des globules rouges), c'est un marqueur tardif."
    },
    {
        "titre": "Annales : Toxicité du Benzène (Solvants)",
        "type": "vraies",
        "items": {
            "A": "C'est un hydrocarbure aromatique volatil.",
            "B": "Il est hématotoxique (toxique pour le sang).",
            "C": "Il peut provoquer des aplasies médullaires.",
            "D": "C'est un cancérogène avéré (Leucémies).",
            "E": "Il est principalement toxique pour le foie."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Sa toxicité majeure cible la MOELLE OSSEUSE (sang)."
    },
    {
        "titre": "Annales : Traitement de substitution aux opiacés",
        "type": "vraies",
        "items": {
            "A": "Méthadone : Agoniste pur, distribution contrôlée.",
            "B": "Buprénorphine (Subutex) : Agoniste partiel, prescription en ville.",
            "C": "L'objectif est de supprimer le craving et le manque.",
            "D": "La Méthadone a une demi-vie courte nécessitant plusieurs prises par jour.",
            "E": "Le risque de mésusage (injection) existe avec le Subutex."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : La Méthadone a une demi-vie LONGUE, ce qui permet une seule prise par jour et une stabilité."
    },
    {
        "titre": "Annales : Mécanisme d'action de la Cocaïne",
        "type": "vraies",
        "items": {
            "A": "Elle bloque la recapture de la Dopamine.",
            "B": "Elle bloque la recapture de la Noradrénaline.",
            "C": "Elle bloque la recapture de la Sérotonine.",
            "D": "Elle agit comme un agoniste direct des récepteurs GABA.",
            "E": "Elle provoque une accumulation massive de neurotransmetteurs dans la fente synaptique."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Elle n'agit pas sur le GABA, mais sur les transporteurs des monoamines."
    },
    {
        "titre": "Annales : Score de Cushman",
        "type": "vraies",
        "items": {
            "A": "Utilisé pour évaluer le sevrage alcoolique.",
            "B": "Prend en compte la fréquence cardiaque et la tension artérielle.",
            "C": "Prend en compte les tremblements et l'agitation.",
            "D": "Un score > 15 indique un sevrage sévère.",
            "E": "Il est spécifique au sevrage des opiacés."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : C'est le score spécifique de l'ALCOOL."
    },
    {
        "titre": "Annales : Effets du Cannabis sur la conduite",
        "type": "vraies",
        "items": {
            "A": "Ralentissement des réflexes.",
            "B": "Mauvaise coordination motrice.",
            "C": "Altération de la perception du temps et de l'espace.",
            "D": "Le risque d'accident est multiplié par 2 environ (seul).",
            "E": "L'association avec l'alcool a un effet additif simple."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'association Alcool + Cannabis a un effet POTENTIALISATEUR (x15 ou x20 le risque)."
    },
    {
        "titre": "Annales : Complications du sniffing (Colles/Solvants)",
        "type": "vraies",
        "items": {
            "A": "Eczéma péri-oral ('Glue sniffer's rash').",
            "B": "Troubles du rythme cardiaque.",
            "C": "Atteinte des nerfs périphériques (Polynévrite).",
            "D": "Amélioration des fonctions cognitives.",
            "E": "Risque d'asphyxie par le sac plastique."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Cela entraîne une détérioration cognitive (démence)."
    },
    {
        "titre": "Annales : Classification des drogues (Pelletier/Delay)",
        "type": "vraies",
        "items": {
            "A": "Psycholeptiques (Sédatifs) : Alcool, Benzodiazépines, Opiacés.",
            "B": "Psychoanaleptiques (Stimulants) : Cocaïne, Amphétamines, Tabac.",
            "C": "Psychodysleptiques (Perturbateurs) : Cannabis, LSD.",
            "D": "L'Ecstasy est uniquement un sédatif.",
            "E": "Les solvants sont des psychodysleptiques."
        },
        "correctes": ["A", "B", "C"],
        "explication": "D est Faux : L'Ecstasy est un stimulant et perturbateur. E est Faux : Les solvants sont des psycholeptiques (dépresseurs)."
    },
    {
        "titre": "Annales : Traitement d'urgence de l'overdose",
        "type": "vraies",
        "items": {
            "A": "Naloxone pour les opiacés (Héroïne, Morphine).",
            "B": "Flumazénil pour les Benzodiazépines.",
            "C": "N-acétylcystéine pour le Paracétamol.",
            "D": "Adrénaline pour l'intoxication aux solvants.",
            "E": "L'intoxication aux poppers (méthémoglobine) se traite par le Bleu de Méthylène."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Contre-indication absolue de l'adrénaline avec les solvants (cœur hyperexcitable)."
    },
    {
        "titre": "Annales : Le Chemsex",
        "type": "vraies",
        "items": {
            "A": "Consommation de produits pour prolonger/intensifier les rapports sexuels.",
            "B": "Produits fréquents : Cathinones (3-MMC), GHB/GBL, Métamphétamine.",
            "C": "Associe souvent l'injection (Slam).",
            "D": "Risque infectieux (VIH/VHC) et psychiatrique élevé.",
            "E": "Concerne exclusivement l'alcool."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'alcool est accessoire, les produits phares sont les stimulants de synthèse et le GHB."
    },
    {
        "titre": "Annales : Poppers et Mécanisme",
        "type": "vraies",
        "items": {
            "A": "Ce sont des nitrites d'alkyle.",
            "B": "Ils libèrent du Monoxyde d'Azote (NO).",
            "C": "Ils provoquent une vasodilatation intense.",
            "D": "Ils sont utilisés comme antidote du cyanure.",
            "E": "Ils provoquent une hypertension artérielle."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Ils provoquent une HYPOtension brutale."
    },
    {
        "titre": "Annales : Sevrage tabagique",
        "type": "vraies",
        "items": {
            "A": "La dépendance physique est liée à la nicotine.",
            "B": "Le craving est un signe de manque.",
            "C": "La substitution nicotinique double les chances d'arrêt.",
            "D": "La prise de poids est une crainte fréquente à l'arrêt.",
            "E": "Il n'existe aucun traitement médicamenteux en dehors de la nicotine."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La Varénicline (Champix) et le Bupropion (Zyban) existent."
    },
    {
        "titre": "Annales : Neurobiologie du plaisir",
        "type": "vraies",
        "items": {
            "A": "Le circuit de la récompense part de l'Aire Tegmentale Ventrale (ATV).",
            "B": "Il projette vers le Noyau Accumbens.",
            "C": "Le neurotransmetteur principal est l'Acétylcholine.",
            "D": "Les drogues piratent ce système naturel.",
            "E": "Le cortex préfrontal joue un rôle de frein (contrôle)."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : C'est la DOPAMINE."
    },
    {
        "titre": "Annales : Législation stupéfiants",
        "type": "vraies",
        "items": {
            "A": "L'usage de stupéfiants est un délit en France.",
            "B": "La conduite sous stupéfiants est interdite (tolérance zéro).",
            "C": "Le trafic est puni de peines de prison.",
            "D": "Le CBD est considéré comme un stupéfiant.",
            "E": "La détention pour usage personnel est autorisée."
        },
        "correctes": ["A", "B", "C"],
        "explication": "D est Faux (le CBD est légal). E est Faux (la détention est interdite, même pour usage perso)."
    },
    {
        "titre": "Annales : Toxicité cardiaque de la Cocaïne",
        "type": "vraies",
        "items": {
            "A": "Tachycardie.",
            "B": "Hypertension artérielle.",
            "C": "Vasoconstriction des coronaires.",
            "D": "Risque d'IDM (Infarctus) même chez le sujet jeune.",
            "E": "Risque de troubles du rythme (arythmie)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tout est vrai. C'est la toxicité majeure de la cocaïne."
    },
    {
        "titre": "Annales : Syndrome de sevrage aux Benzodiazépines",
        "type": "vraies",
        "items": {
            "A": "Anxiété de rebond.",
            "B": "Insomnie.",
            "C": "Tremblements.",
            "D": "Risque de crises convulsives à l'arrêt brutal.",
            "E": "Le sevrage doit être progressif."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "L'arrêt brutal des BZD expose à un risque vital (épilepsie)."
    },
    {
        "titre": "Annales : Facteurs de risque d'addiction",
        "type": "vraies",
        "items": {
            "A": "Début précoce de la consommation.",
            "B": "Traumatismes dans l'enfance.",
            "C": "Facteurs génétiques.",
            "D": "Disponibilité du produit.",
            "E": "Tous les individus sont égaux face au risque."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Il y a une forte inégalité individuelle (génétique, bio-psycho-sociale)."
    },
    {
        "titre": "Annales : Cannabis et Grossesse",
        "type": "vraies",
        "items": {
            "A": "Traverse la barrière placentaire.",
            "B": "Retard de croissance intra-utérin.",
            "C": "Risque accru de prématurité.",
            "D": "Troubles neurocomportementaux chez l'enfant.",
            "E": "Aucun risque si consommé sous forme d'huile."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Le THC reste toxique pour le fœtus quelle que soit la forme."
    },
    {
        "titre": "Annales : Méthadone et Buprénorphine",
        "type": "fausses",
        "items": {
            "A": "Ce sont des médicaments de substitution.",
            "B": "La Méthadone est un agoniste pur.",
            "C": "La Buprénorphine est un agoniste partiel.",
            "D": "La Méthadone ne donne jamais de dépression respiratoire.",
            "E": "Leur prescription est encadrée."
        },
        "correctes": ["D"],
        "explication": "D est Faux : La Méthadone PEUT donner une dépression respiratoire en cas de surdosage ou mélange (alcool/BZD)."
    },
    {
        "titre": "Annales : Amphétamines (Effets)",
        "type": "vraies",
        "items": {
            "A": "Effet anorexigène (coupe-faim).",
            "B": "Augmentation de la vigilance.",
            "C": "Hyperthermie maligne à l'effort.",
            "D": "Dépendance psychique forte.",
            "E": "Sédation importante."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Ce sont des psychostimulants puissants, l'inverse de sédatifs."
    },
    {
        "titre": "Annales : Kétamine",
        "type": "vraies",
        "items": {
            "A": "C'est un anesthésique dissociatif.",
            "B": "Usage détourné pour ses effets hallucinogènes.",
            "C": "Toxicité urinaire grave (cystite, hydronéphrose).",
            "D": "Troubles cognitifs chez le jeune.",
            "E": "C'est un opioïde."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La Kétamine n'est pas un opioïde, elle agit sur les récepteurs NMDA."
    },
    {
        "titre": "Annales : GBL et GHB",
        "type": "vraies",
        "items": {
            "A": "Le GBL est un précurseur transformé en GHB dans le corps.",
            "B": "Le GBL est un solvant industriel (nettoyant jantes).",
            "C": "Risque de coma profond et dépression respiratoire.",
            "D": "Risque d'addiction sévère (dépendance physique 24h/24).",
            "E": "Le GHB est un stimulant pur."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Le GHB est un dépresseur (sédatif/anesthésiant) à forte dose."
    }
]
# --- BANQUE DE QUESTIONS UE2 : SANTE ENVIRONNEMENT ---
questions_ue2 = [
    # --- THEME 1 : PERTURBATEURS ENDOCRINIENS (PE) ---
    {
        "titre": "Parmi les propositions suivantes concernant la définition et les généralités des Perturbateurs Endocriniens (PE), lesquelles sont vraies ?",
        "type": "vraies",
        "items": {
            "A": "Selon l'OMS (2002), un PE est une substance exogène altérant le système endocrinien.",
            "B": "Les effets nocifs ne concernent que l'organisme exposé directement, pas sa descendance.",
            "C": "Ces substances agissent souvent à de très faibles doses.",
            "D": "La relation dose-effet est toujours linéaire (plus la dose est forte, plus l'effet est grand).",
            "E": "Ils peuvent être d'origine naturelle (phytoestrogènes) ou synthétique (xénobiotiques)."
        },
        "correctes": ["A", "C", "E"],
        "explication": "B est Faux : Les effets peuvent être transgénérationnels via l'épigénétique. D est Faux : Une caractéristique des PE est d'avoir des courbes dose-réponse non monotones (en U ou U inversé), où de faibles doses peuvent être plus actives que de fortes doses."
    },
    {
        "titre": "Concernant les mécanismes d'action moléculaires des Perturbateurs Endocriniens, cochez les réponses exactes :",
        "type": "vraies",
        "items": {
            "A": "Ils peuvent imiter une hormone naturelle (effet agoniste, ex: DDT sur ERa).",
            "B": "Ils peuvent bloquer un récepteur hormonal (effet antagoniste, ex: DDE sur AR).",
            "C": "Ils peuvent modifier la synthèse, le transport ou la dégradation des hormones.",
            "D": "Ils agissent uniquement sur les récepteurs nucléaires classiques.",
            "E": "Ils peuvent induire des modifications épigénétiques (méthylation de l'ADN, histones)."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Ils agissent aussi sur des récepteurs membranaires (voies non canoniques comme GPER) et via des mécanismes épigénétiques complexes."
    },
    {
        "titre": "Parmi les propositions suivantes sur le concept DOHaD et les fenêtres d'exposition, lesquelles sont vraies ?",
        "type": "vraies",
        "items": {
            "A": "L'adage classique de la toxicologie 'C'est la dose qui fait le poison' s'applique parfaitement aux PE.",
            "B": "Pour les PE, on dit plutôt : 'C'est la période (le moment) qui fait le poison'.",
            "C": "Les 1000 premiers jours de vie (conception à 2 ans) constituent une période critique.",
            "D": "Une exposition in utero peut entraîner des pathologies apparaissant seulement à l'âge adulte.",
            "E": "La puberté est également une fenêtre de sensibilité accrue (développement glande mammaire)."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : Pour les PE, le timing de l'exposition (fenêtre de vulnérabilité) est souvent plus critique que la dose elle-même (effets retardés)."
    },
    {
        "titre": "Concernant les substances historiques comme le Distilbène (DES) et le Bisphénol A (BPA), cochez les vérités :",
        "type": "vraies",
        "items": {
            "A": "Le Distilbène a provoqué des cancers vaginaux chez les filles exposées in utero (filles DES).",
            "B": "Le Bisphénol A (BPA) est un mimétique des œstrogènes utilisé dans les plastiques.",
            "C": "Le DDT est un insecticide organochloré possédant des effets perturbateurs endocriniens.",
            "D": "Les Phtalates sont utilisés pour durcir les plastiques.",
            "E": "Le Distilbène a été interdit en France dès 1950."
        },
        "correctes": ["A", "B", "C"],
        "explication": "D est Faux : Les phtalates sont des ASSOUPLISSANTS (plastifiants). E est Faux : Le DES a été interdit en 1977 en France, bien après les USA (scandale sanitaire)."
    },
    {
        "titre": "Quelles sont les pathologies humaines suspectées d'être favorisées par les Perturbateurs Endocriniens ?",
        "type": "vraies",
        "items": {
            "A": "Le Syndrome de dysgénésie testiculaire (baisse sperme, hypospadias, cryptorchidie).",
            "B": "L'avance de l'âge de la puberté chez la jeune fille.",
            "C": "L'augmentation de l'obésité et du diabète de type 2.",
            "D": "Les troubles du neuro-développement (Autisme, TDAH, baisse de QI).",
            "E": "Une diminution du risque de cancer du sein."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'exposition aux PE (oestrogéno-mimétiques) augmente le risque de cancers hormono-dépendants comme le cancer du sein et de la prostate."
    },
    {
        "titre": "Concernant l'effet cocktail des Perturbateurs Endocriniens, quelles affirmations sont justes ?",
        "type": "vraies",
        "items": {
            "A": "Il désigne l'exposition simultanée à plusieurs substances chimiques.",
            "B": "Les effets des mélanges sont toujours la somme exacte des effets individuels (1+1=2).",
            "C": "Les effets peuvent être synergiques, c'est-à-dire amplifiés (1+1=10).",
            "D": "Cela rend l'évaluation du risque toxicologique classique très difficile.",
            "E": "L'exposome ne prend pas en compte ces mélanges."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : Les effets peuvent être antagonistes, additifs ou synergiques (amplifiés). E est Faux : L'exposome inclut justement la totalité des expositions."
    },
    {
        "titre": "Parmi les propositions suivantes sur les mécanismes épigénétiques, lesquelles sont correctes ?",
        "type": "vraies",
        "items": {
            "A": "L'épigénétique modifie la séquence de l'ADN (changement des lettres).",
            "B": "La méthylation de l'ADN est un mécanisme épigénétique majeur.",
            "C": "La modification des histones (acétylation) change la compaction de l'ADN.",
            "D": "Ces modifications sont irréversibles et figées.",
            "E": "Ces modifications peuvent être transmises à la descendance."
        },
        "correctes": ["B", "C", "E"],
        "explication": "A est Faux : L'épigénétique ne change pas la séquence (lettres), mais l'expression des gènes (la 'partition'). D est Faux : C'est réversible et adaptatif."
    },
    {
        "titre": "Quels sont les tests recommandés par l'OCDE pour détecter les Perturbateurs Endocriniens ?",
        "type": "vraies",
        "items": {
            "A": "Le niveau 1 correspond à l'analyse des données existantes.",
            "B": "Le niveau 2 utilise des tests in vitro (mécanistiques).",
            "C": "Le test d'Hershberger (in vivo) sert à évaluer l'effet androgénique.",
            "D": "Le test utérotrophique (in vivo) sert à évaluer l'effet œstrogénique.",
            "E": "Les tests sur poissons (in vivo) ne sont jamais utilisés."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les tests sur poissons et amphibiens sont des tests de niveau 3 (court terme) très utilisés."
    },
    {
        "titre": "Quelles sont les principales sources d'exposition aux Perturbateurs Endocriniens ?",
        "type": "vraies",
        "items": {
            "A": "L'alimentation est une voie d'exposition majeure.",
            "B": "Les cosmétiques peuvent contenir des parabènes et du triclosan.",
            "C": "L'air intérieur est exempt de tout PE.",
            "D": "Les amalgames dentaires peuvent libérer du mercure.",
            "E": "Les tickets de caisse contenaient du Bisphénol A (absorbable par la peau)."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : L'air intérieur concentre de nombreux PE (poussières, retardateurs de flamme)."
    },
    {
        "titre": "Concernant les substances spécifiques (Triclosan, Parabènes, Phtalates), repérez l'ERREUR :",
        "type": "fausses",
        "items": {
            "A": "Le Triclosan est un antibactérien présent dans certains dentifrices.",
            "B": "Les Phtalates sont principalement des plastifiants.",
            "C": "Les Parabènes sont utilisés comme conservateurs.",
            "D": "Le DDT est un insecticide organochloré encore autorisé en France.",
            "E": "La génistéine est un phytoestrogène naturel du soja."
        },
        "correctes": ["D"],
        "explication": "D est Faux : Le DDT est interdit depuis longtemps (c'est un POP), mais il persiste dans l'environnement."
    },

    # --- THEME 2 : PFAS (Polluants Éternels) ---
    {
        "titre": "Parmi les propositions suivantes sur la structure et les propriétés des PFAS, lesquelles sont vraies ?",
        "type": "vraies",
        "items": {
            "A": "Ce sont des substances per- et polyfluoroalkylées.",
            "B": "Ils possèdent une liaison Carbone-Fluor très stable, d'où leur surnom de 'Polluants Éternels'.",
            "C": "Ce sont des composés amphiphiles (une tête hydrophile et une queue hydrophobe).",
            "D": "Ils sont très volatils et se dégradent rapidement à la chaleur.",
            "E": "Ils sont utilisés pour leurs propriétés antiadhésives, imperméabilisantes et ignifuges."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Ils sont très peu volatils, résistants aux fortes chaleurs et ne se dégradent quasiment pas (persistance extrême)."
    },
    {
        "titre": "Concernant la toxicocinétique des PFAS (absorption, distribution, élimination), que peut-on dire ?",
        "type": "vraies",
        "items": {
            "A": "Ils sont bien absorbés par voie orale (alimentation, eau).",
            "B": "Une fois dans le sang, ils se lient aux protéines plasmatiques (albumine).",
            "C": "Contrairement aux dioxines, ils ne s'accumulent pas dans les graisses mais dans le foie et les reins.",
            "D": "Leur demi-vie chez l'homme est très courte (quelques jours).",
            "E": "Ils traversent la barrière placentaire et exposent le fœtus."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Leur demi-vie est très longue, de l'ordre de plusieurs ANNÉES (ex: 4-5 ans pour le PFOS) en raison d'une réabsorption rénale."
    },
    {
        "titre": "Quels sont les effets avérés ou suspectés des PFAS sur la santé humaine ?",
        "type": "vraies",
        "items": {
            "A": "Une augmentation du taux de cholestérol (dyslipidémie).",
            "B": "Une diminution de la réponse aux vaccins chez les enfants.",
            "C": "Une augmentation du poids de naissance des nouveau-nés.",
            "D": "Un risque accru de cancer du rein et du testicule.",
            "E": "Une perturbation de la fonction thyroïdienne (hypothyroïdie)."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Les PFAS entraînent une DIMINUTION du poids de naissance (retard de croissance intra-utérin)."
    },
    {
        "titre": "À propos de la réglementation et de l'imprégnation par les PFAS, quelles sont les affirmations exactes ?",
        "type": "vraies",
        "items": {
            "A": "Le PFOA et le PFOS sont inscrits à la Convention de Stockholm (POPs).",
            "B": "La nouvelle directive 'Eau potable' fixe une limite à 0,1 µg/L pour la somme de 20 PFAS.",
            "C": "L'étude Esteban montre que les enfants sont moins imprégnés que les adultes pour le PFOA/PFOS.",
            "D": "En France, il existe environ 17 000 sites contaminés ou suspectés.",
            "E": "L'interdiction totale de tous les PFAS est effective depuis 2023."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Des plans d'action sont en cours (2023-2027) avec des interdictions progressives (textiles, emballages) mais pas d'interdiction totale immédiate."
    },
    {
        "titre": "Parmi ces sources, lesquelles contribuent à l'exposition de la population aux PFAS ?",
        "type": "vraies",
        "items": {
            "A": "Les poêles antiadhésives (type Teflon) endommagées.",
            "B": "Les mousses anti-incendie utilisées sur les plateformes industrielles.",
            "C": "Les vêtements techniques imperméables (type Gore-Tex).",
            "D": "Les emballages de fast-food (papiers ingraissables).",
            "E": "La consommation de poissons et fruits de mer (bioaccumulation)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Toutes ces sources sont réelles. L'alimentation (produits de la mer, œufs) et l'eau de boisson sont les vecteurs majeurs pour la population générale."
    },
    {
        "titre": "Concernant les mécanismes d'action moléculaires des PFAS, cochez les réponses vraies :",
        "type": "vraies",
        "items": {
            "A": "Activation des récepteurs nucléaires PPAR-alpha.",
            "B": "Perturbation du transport des hormones thyroïdiennes.",
            "C": "Induction d'un stress oxydatif.",
            "D": "Ils sont métabolisés très rapidement par le foie (biotransformation).",
            "E": "Interférence avec le métabolisme des acides gras."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Ils sont très peu ou pas métabolisés (très stables chimiquement), d'où leur longue persistance dans l'organisme."
    },
    {
        "titre": "Quelles sont les atteintes hépatiques possibles liées aux PFAS ?",
        "type": "vraies",
        "items": {
            "A": "Le foie est une cible majeure d'accumulation.",
            "B": "Induction d'une stéatose hépatique (foie gras).",
            "C": "Augmentation des enzymes hépatiques (ALAT).",
            "D": "Risque d'adénomes hépatiques.",
            "E": "Ils protègent contre la stéatose hépatique non alcoolique (NAFLD)."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Au contraire, ils favorisent le développement de la NAFLD."
    },
    {
        "titre": "Concernant les effets des PFAS sur la reproduction, que sait-on ?",
        "type": "vraies",
        "items": {
            "A": "Diminution de la fertilité féminine (délai de conception).",
            "B": "Altération de la qualité du sperme (nombre et mobilité).",
            "C": "Augmentation du risque d'hypertension gravidique (pré-éclampsie).",
            "D": "Augmentation du risque de fausse couche.",
            "E": "Ils n'ont aucun effet sur le développement de la glande mammaire."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Ils peuvent retarder ou altérer le développement de la glande mammaire."
    },
    {
        "titre": "Comparaison PFAS chaîne courte vs chaîne longue :",
        "type": "vraies",
        "items": {
            "A": "Les chaînes longues (C8 et +) s'accumulent davantage dans les organismes.",
            "B": "Les chaînes courtes sont plus solubles dans l'eau.",
            "C": "Les chaînes courtes sont plus mobiles dans l'environnement.",
            "D": "Les chaînes courtes sont faciles à filtrer sur charbon actif.",
            "E": "L'industrie a substitué les longs par les courts."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Les chaînes courtes sont très difficiles à filtrer car elles sont peu adsorbables sur charbon."
    },
    {
        "titre": "Quels sont les effets immunitaires observés avec les PFAS ?",
        "type": "vraies",
        "items": {
            "A": "Effet immunosuppresseur global.",
            "B": "Augmentation de la fréquence des infections respiratoires.",
            "C": "Augmentation du risque d'allergies et d'asthme.",
            "D": "La réponse vaccinale est augmentée.",
            "E": "Augmentation du risque de colite ulcéreuse (MICI)."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : La réponse vaccinale est DIMINUÉE chez les enfants exposés."
    },

    # --- THEME 3 : PESTICIDES ---
    {
        "titre": "Parmi les propositions suivantes sur la classification des pesticides, cochez celles qui sont vraies :",
        "type": "vraies",
        "items": {
            "A": "Les produits phytosanitaires sont destinés à la protection des végétaux (usage agricole).",
            "B": "Les biocides sont destinés aux usages non agricoles (hygiène, domestique).",
            "C": "Les herbicides luttent contre les insectes.",
            "D": "Les fongicides luttent contre les champignons et moisissures.",
            "E": "Les rodenticides luttent contre les mauvaises herbes."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux (Herbicides = Végétaux/Mauvaises herbes). E est Faux (Rodenticides = Rongeurs/Rats)."
    },
    {
        "titre": "Concernant la toxicité des Insecticides Organophosphorés (IOP), quelles sont les affirmations exactes ?",
        "type": "vraies",
        "items": {
            "A": "Ils agissent en inhibant de façon irréversible l'enzyme Acétylcholinestérase.",
            "B": "Cela entraîne une accumulation d'acétylcholine dans les synapses.",
            "C": "L'intoxication aiguë provoque un syndrome Muscarinique (myosis, hypersécrétions).",
            "D": "L'intoxication aiguë provoque un syndrome Nicotinique (fasciculations, paralysie).",
            "E": "Ils sont très persistants dans l'environnement (POPs)."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les organophosphorés sont peu persistants et se dégradent assez vite, contrairement aux organochlorés (DDT) qui sont des POPs."
    },
    {
        "titre": "Quelle est la conduite à tenir face à une intoxication aiguë aux Organophosphorés ?",
        "type": "vraies",
        "items": {
            "A": "Décontamination cutanée et oculaire immédiate.",
            "B": "Administration d'Atropine pour contrer les effets muscariniques.",
            "C": "Administration de Pralidoxime (Contrathion) pour réactiver l'enzyme.",
            "D": "Administration de Benzodiazépines (Valium) en cas de convulsions.",
            "E": "Le dosage de l'activité des cholinestérases est inutile."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'effondrement de l'activité des cholinestérases (globulaires et plasmatiques) est le critère biologique de diagnostic."
    },
    {
        "titre": "Concernant les effets chroniques des pesticides sur la santé, quelles pathologies sont reconnues ?",
        "type": "vraies",
        "items": {
            "A": "La maladie de Parkinson est reconnue comme maladie professionnelle chez l'agriculteur.",
            "B": "Le cancer de la prostate est lié à l'exposition au Chlordécone (Antilles).",
            "C": "Les lymphomes non hodgkiniens sont plus fréquents chez les exposés.",
            "D": "Il existe un lien avec des troubles de la fertilité masculine.",
            "E": "Les pesticides protègent contre les maladies neurodégénératives."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Ils favorisent au contraire les maladies neurodégénératives (Parkinson, Alzheimer, SLA)."
    },
    {
        "titre": "Parmi les propositions sur les familles spécifiques de pesticides, lesquelles sont vraies ?",
        "type": "vraies",
        "items": {
            "A": "Le Glyphosate est un herbicide qui inhibe la synthèse des acides aminés aromatiques.",
            "B": "Les Néonicotinoïdes agissent sur le système nerveux des insectes et sont toxiques pour les abeilles.",
            "C": "Les SDHI sont des fongicides inhibant la respiration mitochondriale (Succinate Déshydrogénase).",
            "D": "Le DDT est un organochloré interdit car très persistant et bioaccumulable.",
            "E": "Les Carbamates sont des inhibiteurs irréversibles de l'acétylcholinestérase."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les Carbamates sont des inhibiteurs RÉVERSIBLES (inhibition labile), donc moins dangereux à long terme que les OP."
    },
    {
        "titre": "Concernant les Insecticides Organochlorés (DDT, Lindane), cochez les réponses vraies :",
        "type": "vraies",
        "items": {
            "A": "Ce sont des Polluants Organiques Persistants (POPs).",
            "B": "Ils sont très lipophiles et s'accumulent (biomagnification).",
            "C": "Ils sont très volatils et instables.",
            "D": "Leur mode d'action est l'inhibition de l'acétylcholinestérase.",
            "E": "Ils perturbent les canaux ioniques (Na+, Ca2+) des neurones."
        },
        "correctes": ["A", "B", "E"],
        "explication": "C est Faux : Ils sont très stables. D est Faux : Ce sont les Organophosphorés qui inhibent l'AChE. Les Organochlorés sont excito-toxiques."
    },
    {
        "titre": "À propos du Glyphosate, quelles sont les informations correctes ?",
        "type": "vraies",
        "items": {
            "A": "C'est l'herbicide le plus utilisé au monde.",
            "B": "Il a été classé 'cancérogène probable' (2A) par le CIRC.",
            "C": "Il inhibe la voie du shikimate chez les plantes.",
            "D": "Il est suspecté d'être un perturbateur endocrinien.",
            "E": "Il n'est jamais détecté dans les urines de la population."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Il est retrouvé de façon ubiquitaire dans les urines de la population générale."
    },
    {
        "titre": "Concernant les fongicides SDHI, que peut-on dire ?",
        "type": "vraies",
        "items": {
            "A": "Ils inhibent la Succinate Déshydrogénase (Complexe II mitochondrial).",
            "B": "Ils bloquent la respiration cellulaire des champignons.",
            "C": "Ils sont parfaitement spécifiques aux champignons et sans effet sur l'homme.",
            "D": "Ils pourraient causer des anomalies mitochondriales chez l'homme.",
            "E": "Le Boscalid est un exemple de SDHI."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : L'enzyme SDH est conservée chez toutes les espèces, il y a un risque de toxicité croisée (non-spécificité)."
    },
    {
        "titre": "À propos des Pyréthrinoïdes de synthèse :",
        "type": "vraies",
        "items": {
            "A": "Ce sont des dérivés du pyrèthre naturel (Chrysanthème).",
            "B": "Ils agissent sur les canaux sodium voltage-dépendants.",
            "C": "Ils sont moins toxiques pour l'homme que les Organophosphorés.",
            "D": "Ils sont utilisés dans les prises anti-moustiques domestiques.",
            "E": "Ils peuvent provoquer des paresthésies cutanées."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tout est vrai. Ils maintiennent les canaux sodium ouverts (effet excitateur)."
    },
    {
        "titre": "Concernant le Chlordécone aux Antilles :",
        "type": "vraies",
        "items": {
            "A": "C'est un insecticide organochloré.",
            "B": "Il a été utilisé massivement dans les bananeraies.",
            "C": "Il est très persistant dans les sols (pollution séculaire).",
            "D": "Il contamine l'eau et les aliments locaux.",
            "E": "Il augmente le risque de cancer de la prostate."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "C'est un scandale sanitaire majeur aux Antilles."
    },

    # --- THEME 4 : DIOXINES ---
    {
        "titre": "Concernant l'origine et les propriétés des Dioxines, cochez les réponses vraies :",
        "type": "vraies",
        "items": {
            "A": "Elles sont produites volontairement par l'industrie pour fabriquer des plastiques.",
            "B": "Ce sont des sous-produits involontaires de combustion (incinérateurs, incendies).",
            "C": "Ce sont des Polluants Organiques Persistants (POPs) très lipophiles.",
            "D": "Elles s'accumulent le long de la chaîne alimentaire (biomagnification).",
            "E": "On calcule leur toxicité globale via le TEQ (Toxic Equivalent Quantity)."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : Les dioxines ne sont jamais produites intentionnellement, ce sont des déchets de combustion ou d'impuretés de synthèse."
    },
    {
        "titre": "Quel est le mécanisme d'action moléculaire principal des Dioxines ?",
        "type": "vraies",
        "items": {
            "A": "La dioxine se lie au récepteur cytosolique AhR (Aryl hydrocarbon Receptor).",
            "B": "Le complexe Dioxine-AhR transloque dans le noyau de la cellule.",
            "C": "Il se dimérise avec la protéine ARNT.",
            "D": "Il se fixe sur des séquences d'ADN (XRE) et active la transcription de gènes.",
            "E": "Il induit fortement l'enzyme CYP1A1 (Cytochrome P450)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tout est vrai. C'est la voie canonique d'activation qui conduit à la toxicité et à la perturbation endocrinienne."
    },
    {
        "titre": "Quels sont les effets toxiques (aigus et chroniques) des Dioxines chez l'homme ?",
        "type": "vraies",
        "items": {
            "A": "Le Chloracné est la lésion cutanée typique d'une forte exposition.",
            "B": "La TCDD (dioxine de Seveso) est classée cancérogène certain (Groupe 1).",
            "C": "Elles agissent comme des perturbateurs endocriniens (reproduction, thyroïde).",
            "D": "Elles augmentent le risque de diabète de type 2.",
            "E": "Elles provoquent une mort immédiate par arrêt cardiaque."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La toxicité aiguë est retardée (syndrome de dépérissement), la mort n'est pas immédiate. Les effets sont surtout chroniques."
    },
    {
        "titre": "Concernant l'exposition de la population générale aux Dioxines :",
        "type": "vraies",
        "items": {
            "A": "L'inhalation de l'air est la voie d'exposition majeure (90%).",
            "B": "L'alimentation (produits animaux gras) représente 95% de l'exposition.",
            "C": "Les nourrissons allaités sont une population particulièrement exposée.",
            "D": "Les végétariens sont généralement moins exposés.",
            "E": "Les émissions industrielles ont drastiquement baissé depuis les années 90."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : L'air est une voie mineure. Les dioxines se déposent sur l'herbe -> vaches -> lait/viande -> homme. C'est la chaîne alimentaire qui concentre le toxique."
    },
    {
        "titre": "À propos de l'accident de Seveso (1976) et de l'Agent Orange :",
        "type": "vraies",
        "items": {
            "A": "L'accident de Seveso a libéré un nuage de TCDD en Italie.",
            "B": "Il a entraîné une modification du sex-ratio (plus de naissances féminines).",
            "C": "L'Agent Orange était un défoliant utilisé au Vietnam contaminé par la dioxine.",
            "D": "L'Agent Orange a causé des malformations congénitales et des cancers.",
            "E": "Ces événements n'ont eu aucun impact sanitaire à long terme."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les impacts sanitaires (cancers, diabètes, effets tératogènes) sont observés des décennies après."
    },
    {
        "titre": "Concernant le TEQ (Toxic Equivalent Quantity) des Dioxines :",
        "type": "vraies",
        "items": {
            "A": "Il permet d'évaluer la toxicité globale d'un mélange de dioxines.",
            "B": "La molécule de référence est la TCDD (Seveso).",
            "C": "Le facteur d'équivalence toxique (TEF) de la TCDD est fixé à 1.",
            "D": "Toutes les dioxines ont le même TEF de 1.",
            "E": "C'est la somme des concentrations pondérées par leur TEF."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Les TEF varient de 0.0001 à 1 selon la toxicité de chaque congénère."
    },
    {
        "titre": "Quelles sont les propriétés physico-chimiques des Dioxines ?",
        "type": "vraies",
        "items": {
            "A": "Elles sont très lipophiles (aiment le gras).",
            "B": "Elles sont très persistantes dans l'environnement.",
            "C": "Elles sont bioaccumulables.",
            "D": "Elles sont très solubles dans l'eau.",
            "E": "Elles sont détruites facilement par la lumière."
        },
        "correctes": ["A", "B", "C"],
        "explication": "D est Faux (hydrophobes). E est Faux (très stables chimiquement)."
    },
    {
        "titre": "À propos du récepteur AhR (Aryl hydrocarbon Receptor) :",
        "type": "vraies",
        "items": {
            "A": "C'est un facteur de transcription activé par un ligand.",
            "B": "Il possède des fonctions physiologiques naturelles (développement, immunité).",
            "C": "Il régule le métabolisme des xénobiotiques (enzymes CYP1).",
            "D": "Il n'est activé que par des toxiques industriels.",
            "E": "Il possède des ligands endogènes (dérivés du tryptophane)."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Il a un rôle naturel important, détourné par les dioxines."
    },
    {
        "titre": "Concernant les PCB (Polychlorobiphényles) :",
        "type": "vraies",
        "items": {
            "A": "Ils étaient utilisés comme isolants électriques (Pyralène).",
            "B": "Certains PCB sont dits 'Dioxin-like' (structure plane).",
            "C": "Ils sont aujourd'hui interdits de production.",
            "D": "Ils contaminent encore les sédiments des fleuves (Rhône, Seine).",
            "E": "Ils n'ont aucune toxicité pour l'homme."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Ils ont une toxicité similaire aux dioxines (et neurologique pour les non-dioxin-like)."
    },
    {
        "titre": "Quels sont les mécanismes de toxicité chronique des Dioxines ?",
        "type": "vraies",
        "items": {
            "A": "Induction d'un stress oxydatif.",
            "B": "Promotion tumorale (cancer).",
            "C": "Effet immunosuppresseur (atrophie du thymus).",
            "D": "Perturbation de l'homéostasie thyroïdienne.",
            "E": "Altération du développement dentaire."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tout est vrai. La toxicité est systémique et touche de multiples organes."
    }
]
# --- BANQUE DE QUESTIONS UE3 : HYDROLOGIE ---
questions_hydro = [
    # --- PARTIE 1 : GÉNÉRALITÉS & PHYSICO-CHIMIE (20 QCMs) ---
    # Basé sur "COURS M1S1 HYDRO 2024.pdf"
    {
        "titre": "Répartition de l'eau sur Terre :",
        "type": "vraies",
        "items": {
            "A": "L'eau salée représente 97% de l'eau totale.",
            "B": "L'eau douce représente environ 50% de l'eau totale.",
            "C": "L'eau douce liquide accessible (lacs, rivières) ne représente que 0,007%.",
            "D": "La majorité de l'eau douce est stockée dans les glaciers et calottes glaciaires.",
            "E": "Les eaux souterraines sont plus abondantes que les eaux de surface (lacs/rivières)."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "L'eau douce est une ressource rare (3% du total), dont la majeure partie est gelée ou souterraine."
    },
    {
        "titre": "Concernant les périmètres de protection des captages :",
        "type": "vraies",
        "items": {
            "A": "Ils sont obligatoires pour tous les captages d'eau potable.",
            "B": "Le périmètre de protection immédiate (PPI) doit être clôturé.",
            "C": "Dans le périmètre rapproché (PPR), toutes les activités sont autorisées.",
            "D": "Ils visent à lutter contre les pollutions ponctuelles et accidentelles.",
            "E": "Le périmètre éloigné (PPE) correspond à l'ensemble du bassin d'alimentation."
        },
        "correctes": ["A", "B", "D"],
        "explication": "Le PPR impose des restrictions. Le PPE est facultatif et sert à gérer les risques de pollution persistante mais ne couvre pas forcément tout le bassin."
    },
    {
        "titre": "Les étapes de la potabilisation (Traitement) :",
        "type": "vraies",
        "items": {
            "A": "Le dégrillage élimine les gros déchets.",
            "B": "La coagulation/floculation sert à éliminer les nitrates.",
            "C": "La décantation permet d'éliminer les flocs formés.",
            "D": "La filtration sur sable est une étape de clarification finale.",
            "E": "L'ozonation est utilisée uniquement pour le goût."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : La coagulation élimine les colloïdes (trouble), pas les nitrates dissous. E est Faux : L'ozone est un désinfectant puissant."
    },
    {
        "titre": "Propriétés des désinfectants :",
        "type": "vraies",
        "items": {
            "A": "Le chlore a une bonne rémanence (effet durable).",
            "B": "L'ozone est très rémanent dans le réseau.",
            "C": "Les UV n'ont aucune rémanence.",
            "D": "Le chlore peut former des sous-produits (THM) nocifs.",
            "E": "L'ozone améliore les qualités organoleptiques (goût/odeur)."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : L'ozone est instable et disparaît vite, il faut souvent rechlorer derrière pour protéger le réseau."
    },
    {
        "titre": "Paramètres physico-chimiques : Le pH",
        "type": "vraies",
        "items": {
            "A": "Le pH de l'eau potable doit être compris entre 6,5 et 9.",
            "B": "Une eau acide (pH < 6,5) est dite entartrante.",
            "C": "Une eau acide favorise la corrosion des métaux (plomb, cuivre).",
            "D": "Une eau basique (pH élevé) favorise les dépôts de tartre.",
            "E": "Le pH n'a aucune influence sur l'efficacité du chlore."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : Acide = Agressive/Corrosive. E est Faux : Le chlore est plus efficace à pH acide."
    },
    {
        "titre": "Dureté de l'eau (Titre Hydrotimétrique - TH) :",
        "type": "vraies",
        "items": {
            "A": "Le TH mesure la concentration en Calcium et Magnésium.",
            "B": "Une eau dure (TH élevé) mousse beaucoup avec le savon.",
            "C": "Une eau dure entartre les canalisations (eau chaude).",
            "D": "Une eau trop douce peut être agressive pour les tuyaux.",
            "E": "La limite de qualité impose un TH = 0°f."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : Le calcaire empêche le savon de mousser. E est Faux : Une certaine dureté est recommandée pour la santé et pour protéger les tuyaux (couche carbonatée)."
    },
    {
        "titre": "Les Nitrates (NO3-) :",
        "type": "vraies",
        "items": {
            "A": "La limite de qualité est de 50 mg/L.",
            "B": "Ils proviennent essentiellement de l'agriculture (engrais, élevage).",
            "C": "Ils sont directement toxiques pour l'adulte à faible dose.",
            "D": "Ils peuvent entraîner une méthémoglobinémie chez le nourrisson (après réduction en nitrites).",
            "E": "L'ébullition de l'eau élimine les nitrates."
        },
        "correctes": ["A", "B", "D"],
        "explication": "E est Faux : Faire bouillir concentre les nitrates (l'eau s'évapore, pas les sels)."
    },
    {
        "titre": "L'assainissement des eaux usées (STEP) :",
        "type": "vraies",
        "items": {
            "A": "Le traitement primaire est purement physique (décantation).",
            "B": "Le traitement biologique (boues activées) dégrade la matière organique dissoute.",
            "C": "La DBO5 mesure la pollution biodégradable.",
            "D": "La DCO est toujours inférieure à la DBO5.",
            "E": "L'azote et le phosphore doivent être éliminés en zone sensible (eutrophisation)."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : DCO (tout ce qui est oxydable chimiquement) > DBO5 (ce que les bactéries peuvent manger)."
    },
    {
        "titre": "Métaux lourds et risques sanitaires :",
        "type": "vraies",
        "items": {
            "A": "Le Plomb (Pb) peut provenir des vieilles canalisations (Saturnisme).",
            "B": "Le Cadmium (Cd) est toxique pour le rein (Maladie Itaï-Itaï).",
            "C": "Le Mercure (Hg) est neurotoxique (Maladie de Minamata).",
            "D": "Les métaux ne s'accumulent pas dans l'organisme.",
            "E": "La limite pour le plomb est de 10 µg/L."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le propre des métaux lourds est la bioaccumulation."
    },
    {
        "titre": "Résidus de pesticides :",
        "type": "vraies",
        "items": {
            "A": "La limite pour un pesticide individuel est de 0,1 µg/L.",
            "B": "La limite pour la somme des pesticides est de 0,5 µg/L.",
            "C": "L'atrazine est un herbicide interdit mais encore retrouvé (rémanence).",
            "D": "Le glyphosate est un fongicide.",
            "E": "Les pesticides peuvent être des perturbateurs endocriniens."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le glyphosate est un herbicide."
    },
    {
        "titre": "Le cycle de l'eau :",
        "type": "vraies",
        "items": {
            "A": "L'évapotranspiration concerne les plantes.",
            "B": "L'infiltration alimente les nappes phréatiques.",
            "C": "Le ruissellement alimente les cours d'eau.",
            "D": "L'eau des nappes captives est généralement plus polluée que celle des rivières.",
            "E": "Le temps de résidence dans une nappe peut être très long."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Les nappes captives sont protégées par des couches imperméables et sont souvent très pures."
    },
    {
        "titre": "Conduite à tenir en cas de pollution bactérienne :",
        "type": "vraies",
        "items": {
            "A": "Chloration choc du réseau.",
            "B": "Avis de non-consommation (restriction d'usage).",
            "C": "Distribution d'eau en bouteille.",
            "D": "Laisser couler l'eau suffit toujours.",
            "E": "Informer la population (Mairie/ARS)."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Si la source est contaminée, laisser couler ne change rien."
    },
    {
        "titre": "Concernant le Fluor :",
        "type": "vraies",
        "items": {
            "A": "Il est bénéfique pour l'émail dentaire à faible dose.",
            "B": "À forte dose, il provoque la fluorose (taches dentaires, os).",
            "C": "La limite de qualité est de 1,5 mg/L.",
            "D": "Il est ajouté systématiquement dans l'eau en France.",
            "E": "Certaines eaux minérales sont riches en fluor."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : La fluoration artificielle de l'eau du robinet ne se fait pas en France."
    },
    {
        "titre": "Les eaux conditionnées :",
        "type": "vraies",
        "items": {
            "A": "L'eau de source doit être naturellement potable (sans traitement chimique).",
            "B": "L'eau minérale naturelle a une composition stable et des propriétés favorables à la santé.",
            "C": "L'eau rendue potable par traitement (eau de table) est autorisée.",
            "D": "Une eau minérale peut être très riche en sels (non potable au sens du réseau public).",
            "E": "Toutes les eaux en bouteille conviennent aux nourrissons."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Seules celles avec le logo spécifique conviennent (faible minéralisation, nitrates bas)."
    },
    {
        "titre": "Indicateurs de pollution fécale :",
        "type": "vraies",
        "items": {
            "A": "Escherichia coli est le meilleur indicateur de contamination fécale récente.",
            "B": "Les Entérocoques sont plus résistants qu'E. coli.",
            "C": "La présence de ces germes indique un risque potentiel de pathogènes (Salmonelles, virus...).",
            "D": "La norme pour l'eau potable est : 0 UFC / 100 mL.",
            "E": "On recherche systématiquement le virus de la Polio dans l'eau potable."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : On cherche les indicateurs bactériens, pas les virus directement (trop compliqué/cher)."
    },
    {
        "titre": "Turbidité de l'eau :",
        "type": "vraies",
        "items": {
            "A": "Elle mesure le trouble de l'eau (matières en suspension).",
            "B": "Une forte turbidité peut protéger les bactéries de la désinfection (effet parapluie).",
            "C": "La référence de qualité est < 0,5 ou 2 NFU selon les cas.",
            "D": "Elle est sans importance sanitaire.",
            "E": "Elle s'élimine par filtration."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : C'est un paramètre critique pour l'efficacité de la désinfection."
    },
    {
        "titre": "Chloration et demande en chlore :",
        "type": "vraies",
        "items": {
            "A": "Le chlore réagit d'abord avec les matières organiques (demande en chlore).",
            "B": "Le chlore libre est la partie qui reste active pour désinfecter.",
            "C": "Le point de rupture (Break point) est atteint quand la demande est satisfaite.",
            "D": "Il faut maintenir du chlore libre dans tout le réseau de distribution.",
            "E": "L'odeur de chlore est signe d'une eau toxique."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'odeur est souvent due aux chloramines (chlore combiné) ou à un dosage normal de sécurité."
    },
    {
        "titre": "Eutrophisation :",
        "type": "vraies",
        "items": {
            "A": "C'est un enrichissement excessif de l'eau en nutriments (N et P).",
            "B": "Elle entraîne une prolifération d'algues.",
            "C": "Elle provoque une anoxie (manque d'oxygène) en profondeur.",
            "D": "Elle favorise la biodiversité des poissons.",
            "E": "Les cyanobactéries peuvent libérer des toxines lors de ce phénomène."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : L'eutrophisation asphyxie le milieu et tue les poissons."
    },
    {
        "titre": "Rôle de l'Agence Régionale de Santé (ARS) :",
        "type": "vraies",
        "items": {
            "A": "Elle définit le programme de prélèvements du contrôle sanitaire.",
            "B": "Elle réalise elle-même les analyses en laboratoire.",
            "C": "Elle inspecte les installations.",
            "D": "Elle prend les mesures de gestion en cas de non-conformité (avec le Préfet).",
            "E": "Elle facture l'eau aux usagers."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux (laboratoires agréés indépendants). E est Faux (c'est l'exploitant/mairie)."
    },
    {
        "titre": "Radioactivité dans l'eau :",
        "type": "vraies",
        "items": {
            "A": "On mesure l'activité Alpha globale et Bêta globale résiduelle.",
            "B": "Le tritium (H3) est un indicateur d'activité anthropique (centrales nucléaires).",
            "C": "La dose indicative (DI) doit être inférieure à 0,1 mSv/an.",
            "D": "Le Radon est un gaz radioactif naturel présent dans certaines eaux souterraines.",
            "E": "L'eau radioactive est verte fluo."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux (c'est dans les Simpson ça)."
    },

    # --- PARTIE 2 : RISQUES MICROBIOLOGIQUES (20 QCMs) ---
    # Basé sur "Hydrologie.pdf"
    {
        "titre": "Vibrio cholerae (Le Choléra) :",
        "type": "vraies",
        "items": {
            "A": "C'est un bacille Gram négatif incurvé.",
            "B": "La contamination est féco-orale (eau souillée).",
            "C": "Il provoque une diarrhée hydrique massive ('eau de riz').",
            "D": "La déshydratation est la cause principale de décès.",
            "E": "Il existe un vaccin oral efficace."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Le choléra tue par déshydratation rapide. Le traitement principal est la réhydratation."
    },
    {
        "titre": "Legionella pneumophila (La Légionellose) :",
        "type": "vraies",
        "items": {
            "A": "La transmission se fait par ingestion d'eau contaminée.",
            "B": "La transmission se fait par inhalation d'aérosols (douches, tours aéro-réfrigérantes).",
            "C": "Elle se développe bien dans les eaux chaudes (25-45°C).",
            "D": "Elle colonise les biofilms des canalisations.",
            "E": "Elle provoque une pneumopathie grave."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : On peut boire de l'eau contaminée sans tomber malade. Le danger est pulmonaire (inhalation)."
    },
    {
        "titre": "Facteurs favorisant les Légionelles :",
        "type": "vraies",
        "items": {
            "A": "Eau stagnante (bras morts).",
            "B": "Température de l'eau < 20°C.",
            "C": "Présence de tartre et de corrosion (Fer, Zinc).",
            "D": "Présence d'amibes libres (hôtes de multiplication).",
            "E": "Température de l'eau > 55°C."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B et E sont Faux : Le froid (<20) les endort, le chaud (>50-55) les tue. La zone de danger est l'eau tiède."
    },
    {
        "titre": "La Leptospirose :",
        "type": "vraies",
        "items": {
            "A": "C'est une maladie bactérienne (spirochète).",
            "B": "Le réservoir est animal (rongeurs, rats).",
            "C": "La transmission se fait par contact de la peau lésée avec de l'eau souillée par l'urine de rat.",
            "D": "C'est une maladie professionnelle (égoutiers) et de loisirs (baignade, pêche).",
            "E": "Elle ne donne jamais de forme grave."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Forme grave ictéro-hémorragique (Maladie de Weil) avec insuffisance rénale."
    },
    {
        "titre": "Virus de l'Hépatite A (VHA) :",
        "type": "vraies",
        "items": {
            "A": "C'est un virus à ADN.",
            "B": "La transmission est féco-orale (eau, aliments, coquillages).",
            "C": "Il est très résistant dans le milieu extérieur.",
            "D": "Il provoque une infection chronique du foie.",
            "E": "Il existe un vaccin efficace."
        },
        "correctes": ["B", "C", "E"],
        "explication": "A est Faux (ARN). D est Faux : L'hépatite A est aiguë et ne passe jamais à la chronicité (contrairement au B et C)."
    },
    {
        "titre": "Norovirus et Rotavirus :",
        "type": "vraies",
        "items": {
            "A": "Principaux agents des gastro-entérites aiguës.",
            "B": "Très contagieux et résistants dans l'environnement.",
            "C": "Se traitent par antibiotiques.",
            "D": "Le Rotavirus touche particulièrement les jeunes enfants.",
            "E": "La transmission peut être hydrique ou interhumaine."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Ce sont des virus, les antibios ne servent à rien."
    },
    {
        "titre": "Poliovirus (Poliomyélite) :",
        "type": "vraies",
        "items": {
            "A": "C'est un Entérovirus à transmission féco-orale.",
            "B": "Il atteint le système nerveux central (paralysie flasque).",
            "C": "Il a été éradiqué en France grâce à la vaccination.",
            "D": "Le vaccin oral (VPO) est un virus vivant atténué.",
            "E": "Le virus ne survit pas dans l'eau."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Comme tous les entérovirus, il survit bien dans l'eau."
    },
    {
        "titre": "Pseudomonas aeruginosa (Bacille Pyocyanique) :",
        "type": "vraies",
        "items": {
            "A": "C'est une bactérie opportuniste fréquente dans les hôpitaux.",
            "B": "Elle aime les environnements humides (siphons, robinetterie).",
            "C": "Elle est naturellement résistante à de nombreux antibiotiques.",
            "D": "Elle forme facilement des biofilms.",
            "E": "Sa recherche est obligatoire dans l'eau embouteillée."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Redoutable en milieu hospitalier (nosocomial) et très surveillée dans les eaux conditionnées."
    },
    {
        "titre": "Campylobacter jejuni :",
        "type": "vraies",
        "items": {
            "A": "Principale cause bactérienne de gastro-entérite dans les pays industrialisés.",
            "B": "Réservoir : tube digestif des volailles.",
            "C": "Peut compliquer en syndrome de Guillain-Barré.",
            "D": "Transmission par eau ou aliments mal cuits (poulet).",
            "E": "C'est un virus."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : C'est une bactérie."
    },
    {
        "titre": "Salmonelles (Fièvre Typhoïde) :",
        "type": "vraies",
        "items": {
            "A": "Salmonella Typhi a un réservoir strictement humain.",
            "B": "La typhoïde est une maladie systémique grave (septicémie).",
            "C": "Le signe du 'Tuphos' (prostration) est caractéristique.",
            "D": "Les Salmonelles mineures (non typhiques) causent des gastro-entérites.",
            "E": "La contamination est respiratoire."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Féco-orale (ingestion)."
    },
    {
        "titre": "Le Biofilm dans les réseaux d'eau :",
        "type": "vraies",
        "items": {
            "A": "C'est une couche de micro-organismes fixés sur les parois.",
            "B": "Il protège les bactéries des désinfectants (chlore).",
            "C": "Il se forme surtout si l'eau stagne.",
            "D": "Il peut héberger des Légionelles et des Amibes.",
            "E": "Il est facile à éliminer complètement."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Le biofilm est très tenace et difficile à éradiquer."
    },
    {
        "titre": "Indicateurs de qualité microbiologique (Normes) :",
        "type": "vraies",
        "items": {
            "A": "Flore aérobie revivifiable à 22°C et 37°C (témoin de la charge globale).",
            "B": "Coliformes totaux (témoin de l'efficacité du traitement).",
            "C": "Spores de bactéries sulfito-réductrices (Clostridium) : témoin de contamination ancienne/résistante.",
            "D": "E. coli : témoin de contamination fécale.",
            "E": "La présence d'un seul E. coli rend l'eau non potable."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tous ces paramètres sont surveillés. E. coli doit être ABSENT."
    },
    {
        "titre": "Prévention de la Légionellose (Réseau ECS) :",
        "type": "vraies",
        "items": {
            "A": "Maintenir l'eau chaude à au moins 50°C aux points de puisage.",
            "B": "Maintenir l'eau chaude à au moins 55°C en sortie de production.",
            "C": "Faire couler l'eau régulièrement pour éviter la stagnation.",
            "D": "Détartrer les pommeaux de douche.",
            "E": "Baisser la température du ballon à 40°C pour économiser l'énergie."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : C'est DANGEREUX ! 40°C est la température idéale de multiplication des légionelles."
    },
    {
        "titre": "Shigella (Dysenterie bacillaire) :",
        "type": "vraies",
        "items": {
            "A": "Très contagieuse (faible dose infectieuse).",
            "B": "Provoque des selles glaireuses et sanglantes.",
            "C": "Strictement humaine.",
            "D": "Produit la toxine de Shiga.",
            "E": "Se transmet par piqûre de moustique."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Transmission féco-orale."
    },
    {
        "titre": "Diagnostic de la Légionellose :",
        "type": "vraies",
        "items": {
            "A": "Antigénurie (recherche d'antigènes dans les urines) pour le sérogroupe 1.",
            "B": "PCR sur prélèvement pulmonaire.",
            "C": "Culture sur milieu spécifique (BCYE).",
            "D": "Sérologie (augmentation des anticorps).",
            "E": "Coproculture (selles)."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Ce n'est pas une maladie digestive classique, le germe est dans le poumon."
    },
    {
        "titre": "Traitement de l'eau en cas de contamination :",
        "type": "vraies",
        "items": {
            "A": "Ébullition (efficace sur bactéries, virus, parasites).",
            "B": "Pastilles de chlore (efficace sur bactéries/virus, moins sur parasites).",
            "C": "Filtration (efficace sur parasites si pores assez fins).",
            "D": "Rayons UV (efficace si l'eau est claire).",
            "E": "Ajout de sirop de menthe."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "L'ébullition est la méthode la plus sûre en urgence."
    },
    {
        "titre": "E. coli entérohémorragique (ECEH) :",
        "type": "vraies",
        "items": {
            "A": "Produit des Shiga-toxines.",
            "B": "Peut causer le Syndrome Hémolytique et Urémique (SHU) chez l'enfant.",
            "C": "Contamination par viande mal cuite ou eau souillée.",
            "D": "Traitement antibiotique systématique recommandé.",
            "E": "Provoque des diarrhées sanglantes."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Les antibiotiques peuvent aggraver le SHU en libérant massivement les toxines (lyse bactérienne)."
    },
    {
        "titre": "Adenovirus :",
        "type": "vraies",
        "items": {
            "A": "Peut causer des gastro-entérites.",
            "B": "Peut causer des conjonctivites (piscines).",
            "C": "Virus très résistant dans l'environnement.",
            "D": "Sensible au chlore.",
            "E": "Transmission uniquement respiratoire."
        },
        "correctes": ["A", "B", "C"],
        "explication": "D : Il est relativement résistant au chlore comparé à d'autres. E : Transmission fécale-orale, oculaire, respiratoire."
    },
    {
        "titre": "Eaux de baignade (Piscines) :",
        "type": "vraies",
        "items": {
            "A": "Le chlore doit être présent en permanence.",
            "B": "Le pédiluve et la douche sont obligatoires pour réduire l'apport de germes.",
            "C": "Les chloramines (odeur) sont irritantes pour les yeux et les voies respiratoires.",
            "D": "Le Staphylococcus aureus est un indicateur de pollution humaine (peau).",
            "E": "On ne risque rien si l'eau est transparente."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Une eau claire peut être contaminée chimiquement ou microbiologiquement."
    },
    {
        "titre": "Contamination des eaux souterraines :",
        "type": "vraies",
        "items": {
            "A": "Elles sont naturellement mieux protégées que les eaux de surface.",
            "B": "Elles peuvent être polluées par les fosses septiques défectueuses.",
            "C": "En terrain karstique (calcaire fissuré), la pollution circule très vite.",
            "D": "La filtration par le sol élimine tous les virus.",
            "E": "Elles nécessitent souvent moins de traitement que l'eau de rivière."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Les virus sont très petits et peuvent migrer loin, surtout en terrain fissuré."
    },

    # --- PARTIE 3 : RISQUES PARASITAIRES (20 QCMs) ---
    # Basé sur "Cours hydro 2025-2026.pdf"
    {
        "titre": "Cryptosporidium spp. :",
        "type": "vraies",
        "items": {
            "A": "C'est un protozoaire intracellulaire.",
            "B": "Il forme des oocystes très résistants dans l'environnement.",
            "C": "Il résiste aux concentrations habituelles de chlore.",
            "D": "Il provoque des diarrhées graves chez l'immunodéprimé (SIDA).",
            "E": "La dose infectante est élevée (> 100 000 oocystes)."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La dose infectante est très faible (quelques oocystes suffisent)."
    },
    {
        "titre": "Giardia intestinalis (Giardiase) :",
        "type": "vraies",
        "items": {
            "A": "C'est le parasite intestinal le plus fréquent.",
            "B": "Il forme des kystes résistants dans l'eau froide.",
            "C": "Il provoque malabsorption et diarrhées graisseuses (stéatorrhée).",
            "D": "Il est sensible aux traitements classiques de chloration.",
            "E": "Le réservoir est animal et humain (castor, chien, homme)."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Les kystes de Giardia sont plus résistants au chlore que les bactéries (mais moins que Crypto)."
    },
    {
        "titre": "Traitement de l'eau contre Giardia et Crypto :",
        "type": "vraies",
        "items": {
            "A": "La filtration (Ultrafiltration) est très efficace.",
            "B": "Les rayons UV sont efficaces (inactivation ADN).",
            "C": "L'ébullition est efficace.",
            "D": "Le chlore seul est souvent insuffisant.",
            "E": "L'ozone est inefficace."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'ozone est l'un des rares oxydants chimiques efficaces sur ces kystes."
    },
    {
        "titre": "Naegleria fowleri :",
        "type": "vraies",
        "items": {
            "A": "C'est une amibe libre.",
            "B": "Elle vit dans les eaux douces et chaudes (> 25°C).",
            "C": "Elle pénètre par le nez lors de baignades.",
            "D": "Elle provoque une Méningo-Encéphalite Amibienne Primitive (MEAP).",
            "E": "La mortalité est faible."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La mortalité est > 95%, c'est foudroyant."
    },
    {
        "titre": "Acanthamoeba spp. :",
        "type": "vraies",
        "items": {
            "A": "C'est une amibe libre ubiquiste (présente partout).",
            "B": "Elle provoque des kératites graves chez les porteurs de lentilles.",
            "C": "Elle peut provoquer des encéphalites chez l'immunodéprimé.",
            "D": "Le rinçage des lentilles à l'eau du robinet est un facteur de risque.",
            "E": "Elle ne forme pas de kystes."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Elle forme des kystes très résistants, difficiles à traiter dans l'œil."
    },
    {
        "titre": "Épidémies hydriques à Protozoaires (Milwaukee 1993) :",
        "type": "vraies",
        "items": {
            "A": "Causée par Cryptosporidium.",
            "B": "400 000 personnes malades.",
            "C": "Due à une défaillance de la filtration de l'usine d'eau potable.",
            "D": "Le chlore avait disparu du réseau.",
            "E": "A révélé la résistance du parasite au chlore."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le chlore était présent et conforme aux normes bactériennes, mais inefficace sur le parasite."
    },
    {
        "titre": "Prévention individuelle des parasitoses hydriques :",
        "type": "vraies",
        "items": {
            "A": "Ne pas boire l'eau des rivières en randonnée sans traitement.",
            "B": "Utiliser des filtres portables (céramique) ou UV.",
            "C": "Lavage des mains après contact avec animaux/selles.",
            "D": "Lavage des fruits et légumes à l'eau potable.",
            "E": "La congélation tue immédiatement tous les kystes."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les kystes résistent bien au froid."
    },
    {
        "titre": "Cycle de vie de Cryptosporidium :",
        "type": "vraies",
        "items": {
            "A": "L'oocyste est la forme infectante.",
            "B": "La multiplication est sexuée et asexuée dans l'intestin.",
            "C": "Les oocystes sont excrétés dans les selles.",
            "D": "Il faut un hôte intermédiaire (escargot).",
            "E": "L'auto-infestation est possible."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Cycle monoxène (un seul hôte)."
    },
    {
        "titre": "Cycle de vie de Giardia :",
        "type": "vraies",
        "items": {
            "A": "Le trophozoïte est la forme mobile qui se multiplie dans l'intestin.",
            "B": "Le kyste est la forme de résistance et de dissémination.",
            "C": "Les trophozoïtes survivent longtemps dans l'environnement.",
            "D": "Le parasite se fixe à la paroi intestinale (disque adhésif).",
            "E": "La contamination est directe ou indirecte."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Les trophozoïtes sont fragiles et meurent vite dehors ; ce sont les kystes qui survivent."
    },
    {
        "titre": "Particularités des Amibes libres :",
        "type": "vraies",
        "items": {
            "A": "Elles vivent naturellement dans l'environnement (eau, sol).",
            "B": "Elles ne sont pas des parasites obligatoires.",
            "C": "Elles peuvent servir de 'Cheval de Troie' pour des bactéries (Légionelles).",
            "D": "Elles résistent à la chaleur mieux que la plupart des bactéries.",
            "E": "Elles sont toutes pathogènes pour l'homme."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La majorité sont inoffensives, seules certaines (Naegleria, Acanthamoeba) sont redoutables."
    },
    {
        "titre": "Facteurs de risque de kératite à Acanthamoeba :",
        "type": "vraies",
        "items": {
            "A": "Port de lentilles de contact.",
            "B": "Baignade avec lentilles.",
            "C": "Douche avec lentilles.",
            "D": "Utilisation d'eau du robinet pour rincer l'étui.",
            "E": "Traumatisme cornéen avec végétal souillé."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tout contact de la lentille avec de l'eau non stérile est un risque majeur."
    },
    {
        "titre": "Détection des parasites dans l'eau :",
        "type": "vraies",
        "items": {
            "A": "Nécessite une filtration de grand volume (10 à 100 L).",
            "B": "Utilise l'immunofluorescence (anticorps marqués).",
            "C": "C'est une analyse de routine quotidienne en station d'épuration.",
            "D": "La PCR permet de déterminer l'espèce.",
            "E": "C'est techniquement difficile et coûteux."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Ce n'est pas fait en routine, seulement en cas de crise ou d'étude spécifique."
    },
    {
        "titre": "Symptômes de la Cryptosporidiose :",
        "type": "vraies",
        "items": {
            "A": "Diarrhée aqueuse profuse.",
            "B": "Douleurs abdominales.",
            "C": "Fièvre modérée.",
            "D": "Méningite.",
            "E": "Peut être mortelle chez l'immunodéprimé."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : C'est une pathologie intestinale (sauf rares disséminations chez SIDA, mais pas méningite classique)."
    },
    {
        "titre": "Symptômes de la MEAP (Naegleria) :",
        "type": "vraies",
        "items": {
            "A": "Début brutal après baignade en eau chaude.",
            "B": "Céphalées violentes, fièvre, vomissements.",
            "C": "Raideur de nuque.",
            "D": "Troubles de l'odorat (parfois).",
            "E": "Évolution fatale rapide (coma)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tableau de méningite purulente gravissime."
    },
    {
        "titre": "Traitement de la Giardiase :",
        "type": "vraies",
        "items": {
            "A": "Métronidazole (Flagyl).",
            "B": "Albendazole.",
            "C": "Pénicilline.",
            "D": "Réhydratation.",
            "E": "Corticoides."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C et E sont Faux : Antibio inefficace, Corticoides contre-indiqués (baisse immunité)."
    },
    {
        "titre": "Résistance des Oocystes de Crypto :",
        "type": "vraies",
        "items": {
            "A": "Résistent à l'eau de Javel pure plusieurs minutes.",
            "B": "Résistent dans l'environnement humide plusieurs mois.",
            "C": "Sensibles à la dessiccation (séchage).",
            "D": "Sensibles aux UV industriels.",
            "E": "Sensibles à la congélation rapide."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E : Ils résistent assez bien au froid, moins bien au gel extrême mais ce n'est pas une méthode de stérilisation fiable."
    },
    {
        "titre": "Zones à risque pour l'eau du robinet (Parasites) :",
        "type": "vraies",
        "items": {
            "A": "Zones d'élevage intensif (bovins, ovins).",
            "B": "Zones avec station d'épuration défaillante en amont.",
            "C": "Réseaux vétustes avec fuites.",
            "D": "Après de fortes pluies (lessivage des sols).",
            "E": "Zones de haute montagne (glaciers)."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E : L'eau de montagne est généralement pure, bien que les animaux sauvages puissent la contaminer, le risque est plus faible qu'en zone agricole intensive."
    },
    {
        "titre": "Rôle du pharmacien (Hydrologie) :",
        "type": "vraies",
        "items": {
            "A": "Conseil sur la potabilisation de l'eau en voyage (filtre, comprimés).",
            "B": "Prévention des risques liés aux lentilles de contact.",
            "C": "Contrôle de l'eau de dialyse (Hôpital).",
            "D": "Vente d'eau minérale.",
            "E": "Réparation des fuites d'eau."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : C'est le plombier."
    },
    {
        "titre": "Microsporidies (En bref) :",
        "type": "vraies",
        "items": {
            "A": "Ce sont des champignons parasites intracellulaires.",
            "B": "Transmission hydrique possible.",
            "C": "Diarrhées chroniques chez le patient SIDA.",
            "D": "Spores résistantes dans l'environnement.",
            "E": "Sensibles au chlore."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les spores sont résistantes aux désinfectants classiques."
    },
    {
        "titre": "Toxoplasmose et Eau :",
        "type": "vraies",
        "items": {
            "A": "Toxoplasma gondii peut être transmis par l'eau (oocystes).",
            "B": "Epidémies hydriques décrites (rares mais graves).",
            "C": "Le chat est l'hôte définitif qui contamine l'environnement.",
            "D": "Les oocystes résistent longtemps dans l'eau.",
            "E": "Le chlore est très efficace sur Toxoplasma."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les oocystes de Toxo sont très résistants aux traitements chimiques."
    }
]# --- BANQUE DE QUESTIONS UE2 : TOXIQUES & ENVIRONNEMENT (Méthanol, Éthylène Glycol, Plomb) ---
questions_toxiques = [
    # --- MÉTHANOL (12 QCMs) ---
    {
        "titre": "Généralités sur le Méthanol :",
        "type": "vraies",
        "items": {
            "A": "Il est également appelé alcool de bois.",
            "B": "C'est un liquide volatil à odeur d'amande amère.",
            "C": "Il est très toxique par lui-même avant métabolisation.",
            "D": "Il est utilisé comme solvant et carburant.",
            "E": "La dose létale est d'environ 30 à 50 mL."
        },
        "correctes": ["A", "D", "E"],
        "explication": "B est Faux : Odeur légèrement sucrée. C est Faux : Il n'est pas toxique en soi, ce sont ses métabolites (formaldéhyde/acide formique) qui le sont."
    },
    {
        "titre": "Métabolisme du Méthanol :",
        "type": "vraies",
        "items": {
            "A": "Il est métabolisé par l'Alcool Déshydrogénase (ADH).",
            "B": "Son premier métabolite est l'acide formique.",
            "C": "Le formaldéhyde est transformé en acide formique par l'ALDH.",
            "D": "L'acide formique est responsable de l'acidose métabolique.",
            "E": "L'élimination est majoritairement pulmonaire."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : Méthanol -> Formaldéhyde -> Acide Formique. E est Faux : Élimination métabolique hépatique majeure (>90%)."
    },
    {
        "titre": "Toxicité du Méthanol (Mécanisme) :",
        "type": "vraies",
        "items": {
            "A": "L'acide formique bloque la respiration mitochondriale.",
            "B": "Il provoque une alcalose respiratoire.",
            "C": "Il a une affinité spécifique pour le nerf optique.",
            "D": "Il entraîne un découplage de la phosphorylation oxydative.",
            "E": "Il provoque une cécité irréversible sans traitement."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Il provoque une ACIDOSE métabolique à trou anionique élevé."
    },
    {
        "titre": "Symptomatologie de l'intoxication au Méthanol :",
        "type": "vraies",
        "items": {
            "A": "La phase de latence dure généralement 12 à 24 heures.",
            "B": "La phase d'état associe troubles visuels et dyspnée de Kussmaul.",
            "C": "On observe souvent une mydriase aréactive.",
            "D": "Le patient présente une hypoglycémie sévère.",
            "E": "Le décès survient par défaillance cardio-respiratoire."
        },
        "correctes": ["A", "B", "E"],
        "explication": "C et D ne sont pas les signes majeurs spécifiques décrits (bien que le coma puisse donner des signes oculaires, le signe clé est la baisse d'acuité/flou)."
    },
    {
        "titre": "Diagnostic biologique du Méthanol :",
        "type": "vraies",
        "items": {
            "A": "Méthanolémie toxique > 0,2 g/L.",
            "B": "Acidose métabolique à trou anionique normal.",
            "C": "Augmentation modérée des lactates.",
            "D": "Trou anionique élevé.",
            "E": "Présence de cristaux d'oxalate de calcium."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : Trou anionique AUGMENTÉ. E est Faux : C'est spécifique à l'Éthylène Glycol."
    },
    {
        "titre": "Traitement de l'intoxication au Méthanol :",
        "type": "vraies",
        "items": {
            "A": "Le Fomépizole est l'antidote de première intention.",
            "B": "L'éthanol peut être utilisé comme antidote (compétition ADH).",
            "C": "L'acide folique favorise l'élimination des formiates.",
            "D": "L'hémodialyse est contre-indiquée.",
            "E": "Il faut alcaliniser avec des bicarbonates en cas d'acidose."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : L'hémodialyse est indiquée dans les formes graves (troubles visuels, pH < 7.25)."
    },
    {
        "titre": "Toxicocinétique du Méthanol :",
        "type": "vraies",
        "items": {
            "A": "L'absorption digestive est rapide (pic en 30-60 min).",
            "B": "Le volume de distribution est faible (0.6 L/kg), proche de l'eau totale.",
            "C": "La demi-vie est raccourcie par la prise d'éthanol.",
            "D": "La voie pulmonaire (inhalation) est négligeable.",
            "E": "Il passe la barrière hémato-encéphalique."
        },
        "correctes": ["A", "B", "E"],
        "explication": "C est Faux : L'éthanol sature l'ADH, donc le méthanol n'est plus dégradé, sa demi-vie est ALLONGÉE (ce qui est le but de l'antidote)."
    },
    {
        "titre": "Origines des intoxications au Méthanol :",
        "type": "vraies",
        "items": {
            "A": "Consommation d'alcools frelatés (contexte festif).",
            "B": "Ingestion d'antigel ou liquide lave-glace.",
            "C": "Accidents professionnels (vernis, solvants).",
            "D": "Morsure d'animaux.",
            "E": "Contamination alimentaire par les pesticides."
        },
        "correctes": ["A", "B", "C"],
        "explication": "Les épidémies d'intoxications collectives sont souvent dues à de l'alcool de contrebande."
    },
    {
        "titre": "Pronostic du Méthanol :",
        "type": "vraies",
        "items": {
            "A": "Un pH < 7 est de très mauvais pronostic.",
            "B": "Les séquelles visuelles sont rares.",
            "C": "La cécité peut être définitive.",
            "D": "Le trou anionique est corrélé à la gravité.",
            "E": "La guérison est impossible."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : Les séquelles visuelles (cécité) sont la complication majeure classique."
    },
    {
        "titre": "Action du Fomépizole :",
        "type": "vraies",
        "items": {
            "A": "Il inhibe l'Aldéhyde Déshydrogénase.",
            "B": "Il inhibe l'Alcool Déshydrogénase (ADH).",
            "C": "Il empêche la formation de formaldéhyde.",
            "D": "Il se donne uniquement par voie orale.",
            "E": "Il accélère la dégradation du méthanol."
        },
        "correctes": ["B", "C"],
        "explication": "E est Faux : Il BLOQUE la dégradation (métabolisme toxique), donc le méthanol reste sous forme inchangée (moins toxique) et est éliminé par les reins/poumons lentement."
    },
    {
        "titre": "Comparaison Éthanol / Méthanol :",
        "type": "vraies",
        "items": {
            "A": "L'ADH a plus d'affinité pour l'éthanol que pour le méthanol.",
            "B": "L'éthanol est utilisé pour saturer l'enzyme ADH.",
            "C": "L'objectif est une éthanolémie de 1 g/L.",
            "D": "Le méthanol enivre moins que l'éthanol.",
            "E": "Les deux provoquent une acidose formique."
        },
        "correctes": ["A", "B", "C"],
        "explication": "E est Faux : Seul le méthanol produit de l'acide formique."
    },
    {
        "titre": "Circonstances d'intoxication (Méthanol) :",
        "type": "vraies",
        "items": {
            "A": "Ingestion volontaire (suicide).",
            "B": "Ingestion accidentelle (confusion de bouteille).",
            "C": "Inhalation de vapeurs en milieu industriel.",
            "D": "Passage transcutané significatif en cas de contact prolongé.",
            "E": "Piqûre d'insecte."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "Toutes les voies d'exposition chimique sont possibles."
    },

    # --- ÉTHYLÈNE GLYCOL (11 QCMs) ---
    {
        "titre": "Propriétés de l'Éthylène Glycol :",
        "type": "vraies",
        "items": {
            "A": "Liquide incolore et inodore.",
            "B": "Goût sucré.",
            "C": "Très volatil.",
            "D": "Utilisé comme antigel.",
            "E": "Responsable d'intoxications pédiatriques fréquentes."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Il est peu volatil (contrairement au méthanol). Son goût sucré attire les enfants."
    },
    {
        "titre": "Métabolisme de l'Éthylène Glycol :",
        "type": "vraies",
        "items": {
            "A": "Transformé en acide glycolique puis oxalique.",
            "B": "L'acide oxalique est le métabolite final toxique.",
            "C": "Il ne consomme pas de NAD+.",
            "D": "L'enzyme clé est l'ADH.",
            "E": "Il produit de l'acide formique en quantité majoritaire."
        },
        "correctes": ["A", "B", "D"],
        "explication": "E est Faux : C'est le méthanol qui produit l'acide formique. L'EG produit de l'acide oxalique."
    },
    {
        "titre": "Physiopathologie de l'Éthylène Glycol :",
        "type": "vraies",
        "items": {
            "A": "Acidose métabolique sévère.",
            "B": "Formation de cristaux d'oxalate de calcium.",
            "C": "Hypercalcémie majeure.",
            "D": "Hypocalcémie par précipitation.",
            "E": "Obstruction des tubules rénaux."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Le calcium précipite avec l'oxalate, donc le calcium sanguin BAISSE (Hypocalcémie)."
    },
    {
        "titre": "Phases cliniques de l'intoxication à l'Éthylène Glycol :",
        "type": "vraies",
        "items": {
            "A": "Phase 1 : Signes digestifs et ébriété (SNC).",
            "B": "Phase 2 : Atteinte cardiovasculaire (Tachycardie, OAP).",
            "C": "Phase 3 : Insuffisance rénale aiguë.",
            "D": "L'atteinte rénale est immédiate (dans l'heure).",
            "E": "Le décès peut survenir par défaillance cardiaque."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : L'atteinte rénale est retardée (24-72h)."
    },
    {
        "titre": "Signes biologiques spécifiques (Éthylène Glycol) :",
        "type": "vraies",
        "items": {
            "A": "Trou anionique élevé.",
            "B": "Trou osmolaire élevé.",
            "C": "Cristaux d'oxalate de calcium dans les urines.",
            "D": "Hypocalcémie.",
            "E": "Alcalose métabolique."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "La présence de cristaux urinaires et d'une hypocalcémie avec acidose est très évocatrice."
    },
    {
        "titre": "Traitement de l'Éthylène Glycol :",
        "type": "vraies",
        "items": {
            "A": "Le Fomépizole est l'antidote de choix.",
            "B": "L'éthanol est une alternative.",
            "C": "L'hémodialyse épure le toxique et corrige l'acidose.",
            "D": "Il faut corriger l'hypocalcémie.",
            "E": "L'administration de vitamine B6 (Pyridoxine) est inutile."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "La vitamine B6 (et B1) est parfois donnée comme cofacteur pour dévier le métabolisme, donc 'inutile' est faux (bien que ce soit un traitement adjuvant)."
    },
    {
        "titre": "Complications rénales de l'Éthylène Glycol :",
        "type": "vraies",
        "items": {
            "A": "Nécrose tubulaire aiguë.",
            "B": "Oligo-anurie.",
            "C": "Lombalgies.",
            "D": "Hématurie et protéinurie.",
            "E": "Toujours irréversibles."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La fonction rénale peut récupérer après traitement/dialyse."
    },
    {
        "titre": "Trou osmolaire (Éthylène Glycol) :",
        "type": "vraies",
        "items": {
            "A": "C'est la différence entre osmolarité mesurée et calculée.",
            "B": "Il est augmenté en présence d'un alcool de bas poids moléculaire.",
            "C": "Une valeur > 15 mOsm/kg est significative.",
            "D": "Il est normal dans cette intoxication.",
            "E": "Il aide au diagnostic précoce."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "L'EG est une petite molécule osmotiquement active, elle creuse le trou osmolaire."
    },
    {
        "titre": "Cristallurie (Éthylène Glycol) :",
        "type": "vraies",
        "items": {
            "A": "Les cristaux sont faits d'acide formique.",
            "B": "Ce sont des cristaux d'oxalate de calcium.",
            "C": "Ils ont une forme d'enveloppe de lettre (dihydratés) ou d'aiguille (monohydratés).",
            "D": "Ils sont visibles au microscope dans le culot urinaire.",
            "E": "Ils témoignent de la gravité rénale."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux."
    },
    {
        "titre": "Indication de l'hémodialyse (EG et Méthanol) :",
        "type": "vraies",
        "items": {
            "A": "Acidose sévère (pH < 7,25).",
            "B": "Insuffisance rénale installée.",
            "C": "Signes visuels (pour le méthanol).",
            "D": "Trou anionique élevé persistant.",
            "E": "Dès l'ingestion d'une petite quantité asymptomatique."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Si pris très tôt, l'antidote seul peut suffire."
    },
    {
        "titre": "Sources d'Éthylène Glycol :",
        "type": "vraies",
        "items": {
            "A": "Liquides de refroidissement.",
            "B": "Liquides de frein.",
            "C": "Dégivrants pour avions.",
            "D": "Certains détergents.",
            "E": "Piles boutons."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux."
    },

    # --- PLOMB / SATURNISME (12 QCMs) ---
    {
        "titre": "Propriétés et Sources du Plomb :",
        "type": "vraies",
        "items": {
            "A": "C'est un métal lourd ubiquitaire.",
            "B": "Il a une forte affinité pour les groupements thiols (-SH).",
            "C": "Le saturnisme désigne l'intoxication chronique.",
            "D": "Il est présent dans les vieilles peintures (Céruse).",
            "E": "Il n'est jamais présent dans l'alimentation."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'alimentation (eau, végétaux) est une source d'exposition (bruit de fond)."
    },
    {
        "titre": "Toxicocinétique du Plomb :",
        "type": "vraies",
        "items": {
            "A": "L'absorption digestive est plus forte chez l'enfant (40-50%) que chez l'adulte (10%).",
            "B": "Il se fixe majoritairement sur les globules rouges (intra-érythrocytaire).",
            "C": "Il s'accumule dans l'os (demi-vie > 10 ans).",
            "D": "Il ne passe pas la barrière placentaire.",
            "E": "Il est éliminé par les urines."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Il passe le placenta, toxique pour le fœtus."
    },
    {
        "titre": "Mécanisme de toxicité du Plomb (Hème) :",
        "type": "vraies",
        "items": {
            "A": "Il inhibe l'ALA-Déshydratase (ALA-D).",
            "B": "Il inhibe la Ferrochélatase.",
            "C": "Il entraîne une accumulation d'ALA dans les urines.",
            "D": "Il entraîne une accumulation de Zinc-Protoporphyrine (PPZ).",
            "E": "Il provoque une anémie macrocytaire."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Anémie MICROcytaire ou normocytaire (défaut de synthèse de l'hème)."
    },
    {
        "titre": "Signes cliniques du Saturnisme :",
        "type": "vraies",
        "items": {
            "A": "Coliques de plomb (douleurs abdominales).",
            "B": "Liseré de Burton (gencives).",
            "C": "Encéphalopathie (convulsions) dans les formes graves.",
            "D": "Baisse du QI et troubles de l'attention chez l'enfant.",
            "E": "Hypertension artérielle chez l'adulte."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tableau complet. L'atteinte intellectuelle chez l'enfant est la plus redoutée à faible dose."
    },
    {
        "titre": "Marqueurs biologiques du Plomb :",
        "type": "vraies",
        "items": {
            "A": "Plombémie (sang total) : reflet de l'exposition récente.",
            "B": "ALA urinaire augmenté.",
            "C": "PPZ érythrocytaire augmentée.",
            "D": "Granulations basophiles des hématies.",
            "E": "Le plomb plasmatique est le meilleur marqueur."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Le plomb est à 99% dans les globules rouges, on dose le PLOMB SANGUIN TOTAL, pas le plasmatique."
    },
    {
        "titre": "Traitement du Saturnisme :",
        "type": "vraies",
        "items": {
            "A": "Éviction de la source (déplombage) est prioritaire.",
            "B": "Chélation par EDTA calcique (IV).",
            "C": "Chélation par DMSA (Succimer) per os.",
            "D": "La chélation est systématique dès que le plomb est détectable.",
            "E": "Déclaration obligatoire du saturnisme infantile."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : La chélation a des seuils d'intervention (ex: > 450 µg/L chez l'enfant ou symptômes). À faible dose, on surveille et on supprime la source."
    },
    {
        "titre": "Populations à risque (Plomb) :",
        "type": "vraies",
        "items": {
            "A": "Enfants (Pica = ingestion d'écailles de peinture).",
            "B": "Femmes enceintes.",
            "C": "Travailleurs du bâtiment (rénovation ancienne).",
            "D": "Travailleurs des fonderies et batteries.",
            "E": "Personnes âgées uniquement."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "Les enfants sont les plus vulnérables (absorption digestive élevée + cerveau en développement)."
    },
    {
        "titre": "Atteinte rénale du Plomb :",
        "type": "vraies",
        "items": {
            "A": "Néphropathie tubulaire aiguë (Syndrome de Fanconi) si intoxication massive.",
            "B": "Néphropathie interstitielle chronique.",
            "C": "Sclérose glomérulaire.",
            "D": "Hypertension artérielle secondaire.",
            "E": "L'atteinte rénale est toujours réversible."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : L'atteinte chronique mène à l'insuffisance rénale définitive."
    },
    {
        "titre": "Réglementation et Seuils (Plomb) :",
        "type": "vraies",
        "items": {
            "A": "Le seuil de déclaration du saturnisme est de 50 µg/L.",
            "B": "Le plomb est classé cancérogène probable (2A) pour ses composés inorganiques.",
            "C": "Les peintures au plomb sont interdites depuis 1948 en France (pour les pros).",
            "D": "Le diagnostic plomb (CREP) est obligatoire pour les ventes de logements anciens.",
            "E": "L'eau du robinet ne doit pas dépasser 10 µg/L."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Toutes ces mesures visent à réduire l'exposition."
    },
    {
        "titre": "Effets hématologiques du Plomb :",
        "type": "vraies",
        "items": {
            "A": "Inhibition de la synthèse de l'hème.",
            "B": "Anémie régénérative (réticulocytes élevés).",
            "C": "Hémolyse possible en aigu.",
            "D": "Ponctuations basophiles (ARN résiduel) dans les hématies.",
            "E": "Augmentation de l'hémoglobine."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : C'est une ANÉMIE (baisse de l'Hb)."
    },
    {
        "titre": "Sources professionnelles de Plomb :",
        "type": "vraies",
        "items": {
            "A": "Fabrication de batteries et accumulateurs.",
            "B": "Récupération de vieux métaux.",
            "C": "Démolition de bâtiments anciens.",
            "D": "Céramique et poterie artisanale (émaux).",
            "E": "Industrie du plastique (stabilisants)."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "De nombreux secteurs industriels utilisent encore le plomb ou y sont exposés lors du recyclage."
    },
    {
        "titre": "Chélateurs (Plomb) :",
        "type": "vraies",
        "items": {
            "A": "EDTA calcique (se donne en perfusion).",
            "B": "DMSA (Succimer) (se donne par voie orale).",
            "C": "BAL (Dimercaprol) (ancien chélateur).",
            "D": "Ils augmentent l'élimination urinaire du plomb.",
            "E": "Ils n'ont aucun effet secondaire."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Risque de redistribution vers le cerveau si mal géré, risque rénal pour l'EDTA, allergies, etc."
    }
]# --- BANQUE DE QUESTIONS : ÉTHERS DE GLYCOL ---
questions_ethers = [
    {
        "titre": "Propriétés physico-chimiques des éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "Ce sont des liquides incolores à odeur agréable.",
            "B": "Ils sont amphiphiles (solubles dans l'eau et les graisses).",
            "C": "Ils ne franchissent pas la barrière cutanée.",
            "D": "Ce sont des solvants aprotiques.",
            "E": "Ils sont ininflammables."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Ils passent très bien la barrière cutanée. E est Faux : Ils sont inflammables."
    },
    {
        "titre": "Classification des éthers de glycol (Séries E et P) :",
        "type": "vraies",
        "items": {
            "A": "La série E dérive de l'éthylène glycol.",
            "B": "La série P dérive du propylène glycol.",
            "C": "Le Méthyl Glycol et l'Ethyl Glycol appartiennent à la série E.",
            "D": "La série P comprend deux isomères (alpha et beta).",
            "E": "La toxicité est identique pour les deux séries."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Les séries n'ont pas le même profil métabolique ni la même toxicité (l'isomère bêta de la série P est généralement moins toxique)."
    },
    {
        "titre": "Toxicocinétique : Absorption des éthers de glycol",
        "type": "vraies",
        "items": {
            "A": "L'absorption cutanée est très importante.",
            "B": "L'absorption pulmonaire est proportionnelle à la concentration atmosphérique.",
            "C": "L'absorption cutanée est proportionnelle à la masse molaire.",
            "D": "Ils passent la barrière foeto-placentaire.",
            "E": "Ils ne sont pas absorbés par voie digestive."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Elle est inversement proportionnelle à la masse molaire (plus c'est petit, mieux ça passe). E est Faux : Ils sont bien absorbés par voie digestive."
    },
    {
        "titre": "Métabolisme des éthers de glycol de la série E :",
        "type": "vraies",
        "items": {
            "A": "La voie principale est l'oxydation par l'Alcool Déshydrogénase (ADH).",
            "B": "Ils sont transformés en alcoxyaldéhydes puis en alcoxyacides.",
            "C": "Les métabolites acides (alcoxyacides) sont responsables de la toxicité.",
            "D": "Le métabolisme est rapide, mais l'élimination des métabolites est lente.",
            "E": "Ils sont éliminés tels quels sans transformation."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "C'est l'accumulation des métabolites acides (causée par une demi-vie longue d'élimination) qui crée la toxicité."
    },
    {
        "titre": "Symptômes de l'intoxication aiguë aux éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "Dépression du système nerveux central (SNC).",
            "B": "Acidose métabolique.",
            "C": "Insuffisance rénale aiguë (toxicité tubulaire).",
            "D": "Hyperactivité et convulsions immédiates.",
            "E": "Troubles de la conscience pouvant aller jusqu'au coma."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "Le tableau clinique associe atteinte neuro, métabolique (acidose) et rénale."
    },
    {
        "titre": "Toxicité chronique hématologique des éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "Ils peuvent provoquer une anémie.",
            "B": "Ils peuvent provoquer une leucopénie.",
            "C": "Les cytopénies sont généralement irréversibles.",
            "D": "La toxicité médullaire est un risque connu.",
            "E": "Ils provoquent une augmentation des plaquettes."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C est Faux : Les cytopénies sont réversibles à l'arrêt de l'exposition."
    },
    {
        "titre": "Toxicité chronique sur la reproduction (Éthers de glycol) :",
        "type": "vraies",
        "items": {
            "A": "Certains sont classés reprotoxiques de catégorie 2.",
            "B": "Chez l'homme : risque d'oligospermie.",
            "C": "Chez la femme : troubles du cycle menstruel.",
            "D": "Risque de malformations congénitales (tératogénicité).",
            "E": "Aucun risque d'avortement spontané n'a été décrit."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Le risque d'avortement spontané (fausse couche) est avéré."
    },
    {
        "titre": "Traitement spécifique d'une intoxication aux éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "Il n'existe aucun antidote.",
            "B": "L'administration de Fomépizole est indiquée.",
            "C": "L'administration d'éthanol est une alternative.",
            "D": "Le but est de bloquer l'enzyme ADH.",
            "E": "L'épuration extra-rénale (dialyse) peut être nécessaire."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "Comme pour le méthanol ou l'éthylène glycol, on bloque l'ADH pour empêcher la formation des métabolites acides toxiques."
    },
    {
        "titre": "Prévention et biométrologie des éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "La substitution des produits les plus dangereux est prioritaire.",
            "B": "Les gants en latex offrent la meilleure protection.",
            "C": "On peut doser les métabolites (ex: acide méthoxyacétique) dans les urines.",
            "D": "La mesure des concentrations atmosphériques est utile.",
            "E": "Il faut stocker les produits dans des récipients ouverts pour aérer."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : Il faut des gants en CAOUTCHOUC. E est Faux : Récipients métalliques FERMÉS."
    },
    {
        "titre": "Concernant l'élimination des éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "Elle est majoritairement urinaire.",
            "B": "L'élimination se fait sous forme de CO2 expiré principalement.",
            "C": "Les métabolites acides sont éliminés dans les urines.",
            "D": "Plus la chaîne est longue, plus l'élimination est difficile.",
            "E": "La demi-vie d'élimination des métabolites est courte (moins d'1h)."
        },
        "correctes": ["A", "C"],
        "explication": "D est Faux : Plus la chaîne est longue, plus le métabolite est facilement éliminé. E est Faux : Demi-vie longue (7 à 40h)."
    },
    {
        "titre": "Sources d'exposition aux éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "Peintures et vernis.",
            "B": "Produits cosmétiques (laques, colorations).",
            "C": "Carburants aéronautiques.",
            "D": "Produits phytosanitaires.",
            "E": "Uniquement dans l'industrie lourde."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "On les trouve aussi dans des produits domestiques et cosmétiques."
    },
    {
        "titre": "Toxicité neurologique chronique des éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "Troubles de la concentration.",
            "B": "Somnolence et apathie.",
            "C": "Tremblements.",
            "D": "Troubles de la marche.",
            "E": "Hyperacousie."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : On décrit plutôt des troubles de l'audition, mais pas spécifiquement une hyperacousie."
    },
    {
        "titre": "Interactions métaboliques :",
        "type": "vraies",
        "items": {
            "A": "Les enzymes du métabolisme sont saturables.",
            "B": "L'alcool éthylique (boisson) n'a aucune influence sur leur métabolisme.",
            "C": "La consommation d'alcool peut ralentir le métabolisme des éthers de glycol.",
            "D": "L'inhibition de l'ADH augmente la toxicité.",
            "E": "Les métabolites sont des sulfoconjugués (phase 2)."
        },
        "correctes": ["A", "C", "E"],
        "explication": "D est Faux : L'inhibition de l'ADH DIMINUE la toxicité car elle empêche la formation des acides toxiques."
    },
    {
        "titre": "Voies d'exposition en milieu professionnel :",
        "type": "vraies",
        "items": {
            "A": "L'inhalation de vapeurs est une voie majeure.",
            "B": "Le contact cutané (liquide) est une voie majeure.",
            "C": "L'ingestion accidentelle est la cause la plus fréquente.",
            "D": "Le port de masque à cartouches est une protection collective.",
            "E": "L'encoffrement des machines est une protection collective."
        },
        "correctes": ["A", "B", "E"],
        "explication": "C est Faux : L'ingestion est rare. D est Faux : Le masque est une protection INDIVIDUELLE."
    },
    {
        "titre": "Propriétés métaboliques spécifiques (Série P) :",
        "type": "vraies",
        "items": {
            "A": "L'isomère alpha donne un alcool secondaire.",
            "B": "L'isomère béta donne un alcool primaire.",
            "C": "L'alcool secondaire est transformé en cétone moins toxique.",
            "D": "L'alcool primaire est transformé en acide toxique.",
            "E": "La série P est globalement plus toxique que la série E."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : La série P (surtout isomère alpha majoritaire) est souvent considérée comme moins toxique car elle forme moins d'acides."
    },
    {
        "titre": "Concernant l'utilisation des éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "Environ 30 éthers de glycol sont exploités industriellement.",
            "B": "Leur consommation est en baisse constante.",
            "C": "Ils sont utilisés dans les produits d'entretien (lave-vitre).",
            "D": "Les 4 éthers les plus toxiques sont interdits dans les cosmétiques et médicaments.",
            "E": "Ils sont utilisés comme antigel alimentaire."
        },
        "correctes": ["A", "C", "D"],
        "explication": "D est Vrai : Une mesure de prévention importante pour le grand public."
    },
    {
        "titre": "Signes métaboliques de l'intoxication aiguë :",
        "type": "vraies",
        "items": {
            "A": "Alcalose respiratoire.",
            "B": "Acidose métabolique.",
            "C": "Trou anionique élevé.",
            "D": "Hyperventilation compensatrice.",
            "E": "Hypoglycémie sévère."
        },
        "correctes": ["B", "C", "D"],
        "explication": "L'acidose métabolique est due à l'accumulation des alcoxyacides."
    },
    {
        "titre": "Indicateurs biologiques d'exposition (IBE) :",
        "type": "vraies",
        "items": {
            "A": "On dose l'éther de glycol inchangé dans le sang.",
            "B": "On dose les métabolites acides dans les urines.",
            "C": "Pour l'EGME, on dose l'acide 2-méthoxyacétique.",
            "D": "Le dosage se fait en début de poste.",
            "E": "Ces dosages permettent d'évaluer l'exposition interne."
        },
        "correctes": ["B", "C", "E"],
        "explication": "Le dosage urinaire des métabolites est la méthode de référence."
    },
    {
        "titre": "Toxicité rénale des éthers de glycol :",
        "type": "vraies",
        "items": {
            "A": "Elle est liée à une obstruction des voies urinaires.",
            "B": "C'est une toxicité tubulaire.",
            "C": "Elle peut entraîner une polyurie par hyperosmolarité.",
            "D": "Elle conduit à une insuffisance rénale.",
            "E": "Elle est irréversible."
        },
        "correctes": ["B", "C", "D"],
        "explication": "L'atteinte est tubulaire et métabolique."
    },
    {
        "titre": "Comparaison Éthers de glycol / Solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "Les deux sont des dépresseurs du SNC.",
            "B": "Les deux peuvent être hépatotoxiques.",
            "C": "Les éthers de glycol sont plus volatils que les solvants chlorés.",
            "D": "Les éthers de glycol sont solubles dans l'eau, contrairement à la plupart des solvants chlorés.",
            "E": "Les deux nécessitent une protection cutanée."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Les solvants chlorés sont généralement plus volatils. La solubilité dans l'eau est une caractéristique clé des éthers de glycol (amphiphiles)."
    }
]

# --- BANQUE DE QUESTIONS : SOLVANTS CHLORÉS ---
questions_chlores = [
    {
        "titre": "Propriétés physico-chimiques des solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "Ce sont des dérivés halogénés.",
            "B": "Ils sont très inflammables.",
            "C": "Ils sont très volatils.",
            "D": "S'ils sont chauffés (>400°C), ils peuvent dégager du Phosgène (gaz toxique).",
            "E": "Leur emploi est en augmentation constante."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux : Ils sont PEU inflammables. E est Faux : Emploi limité à cause de leur toxicité."
    },
    {
        "titre": "Métabolisme du Dichlorométhane :",
        "type": "vraies",
        "items": {
            "A": "Il est métabolisé en Monoxyde de Carbone (CO).",
            "B": "Il provoque une formation de carboxyhémoglobine (HbCO).",
            "C": "Il est métabolisé en époxyde.",
            "D": "Son élimination est principalement rénale.",
            "E": "90% est éliminé par voie respiratoire sous forme inchangée."
        },
        "correctes": ["A", "B", "E"],
        "explication": "C est Faux : C'est le trichloréthylène qui fait des époxydes. D est Faux : Élimination respiratoire majoritaire."
    },
    {
        "titre": "Toxicité aiguë du Trichloréthylène :",
        "type": "vraies",
        "items": {
            "A": "Dépression du SNC (narcose, ébriété).",
            "B": "Hyperexcitabilité cardiaque (troubles du rythme).",
            "C": "Effet bathmotrope positif.",
            "D": "Risque d'hépatite cytolytique massive immédiate.",
            "E": "Dermite irritative."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "Les troubles de l'excitabilité cardiaque sont un risque spécifique et grave."
    },
    {
        "titre": "Toxicité du Tétrachlorure de Carbone (CCl4) :",
        "type": "vraies",
        "items": {
            "A": "C'est un puissant hépatotoxique (stéatose, cytolyse).",
            "B": "Il est très néphrotoxique (tubulopathie aiguë).",
            "C": "Il est utilisé couramment en pressing de nos jours.",
            "D": "Il est moins toxique que le dichlorométhane.",
            "E": "Il provoque des nécroses hépatiques."
        },
        "correctes": ["A", "B", "E"],
        "explication": "C est Faux : Son usage est très restreint/interdit à cause de sa toxicité majeure. C'est l'un des plus toxiques."
    },
    {
        "titre": "Toxicité du Chlorure de Vinyle (monomère) :",
        "type": "vraies",
        "items": {
            "A": "Il est classé cancérogène certain (Groupe 1 par le CIRC).",
            "B": "Il provoque des angiosarcomes hépatiques.",
            "C": "Il peut causer le syndrome de Raynaud (trouble vasculaire des doigts).",
            "D": "Il provoque une acro-ostéolyse (atteinte osseuse des extrémités).",
            "E": "Il est inoffensif pour le foie."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "C'est un toxique industriel majeur avec des effets spécifiques (syndrome de Raynaud, ostéolyse, cancer du foie)."
    },
    {
        "titre": "Traitement de l'intoxication aiguë aux solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "Administration d'adrénaline en cas de malaise cardiaque.",
            "B": "Oxygénothérapie et ventilation assistée.",
            "C": "Lavage gastrique en cas d'ingestion.",
            "D": "Administration de N-acétylcystéine (protecteur hépatique).",
            "E": "Administration de bêta-bloquants pour le trichloréthylène."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : L'adrénaline est CONTRE-INDIQUÉE car le cœur est hyper-excitable, cela provoquerait une fibrillation ventriculaire."
    },
    {
        "titre": "Voies d'absorption des solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "La voie respiratoire est la plus importante.",
            "B": "L'absorption digestive est lente et faible.",
            "C": "L'absorption cutanée est possible.",
            "D": "Ils traversent la barrière hémato-encéphalique (liposolubles).",
            "E": "Ils traversent la barrière foeto-placentaire."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : L'absorption digestive est élevée et rapide, bien que ce soit une voie rare (accidentelle)."
    },
    {
        "titre": "Métabolisme hépatique des solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "Ils sont métabolisés par le cytochrome P450 (CYP2E1).",
            "B": "Ce sont des inducteurs enzymatiques.",
            "C": "Le métabolisme réduit toujours leur toxicité.",
            "D": "La formation d'époxydes est une voie d'activation toxique.",
            "E": "Le métabolisme peut saturer."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Le métabolisme crée souvent des composés plus réactifs et toxiques (époxydes, radicaux libres)."
    },
    {
        "titre": "Symptômes neurologiques de l'intoxication aiguë :",
        "type": "vraies",
        "items": {
            "A": "Syndrome ébrieux (comme l'alcool).",
            "B": "Narcose (endormissement).",
            "C": "Convulsions.",
            "D": "Neuropathies trigéminales ou optiques.",
            "E": "Hypervigilance."
        },
        "correctes": ["A", "B", "D"],
        "explication": "Ce sont des dépresseurs du système nerveux central, ils causent somnolence et coma, pas d'hypervigilance."
    },
    {
        "titre": "Toxicité chronique des solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "Dermatoses d'irritation (peau sèche).",
            "B": "Troubles de la mémoire et du comportement (SNC).",
            "C": "Cytolyse hépatique.",
            "D": "Cancer (leucémies, lymphomes, foie).",
            "E": "Amélioration des réflexes."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "L'exposition à long terme affecte le cerveau, le foie, la peau et est cancérigène."
    },
    {
        "titre": "Prévention technique et médicale (Solvants chlorés) :",
        "type": "vraies",
        "items": {
            "A": "Travail sous hotte aspirante (protection collective).",
            "B": "Surveillance des VLEP (Valeurs Limites d'Exposition Professionnelle).",
            "C": "Réaction de Fujiwara-Ross pour la détection colorimétrique.",
            "D": "Surveillance médicale tous les 5 ans.",
            "E": "Étiquetage et stockage sécurisé."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Surveillance médicale à l'embauche puis tous les 6 mois."
    },
    {
        "titre": "Le Chloroforme (CHCl3) :",
        "type": "vraies",
        "items": {
            "A": "Ancien anesthésique.",
            "B": "Peu toxique pour le foie.",
            "C": "Hépatotoxique et néphrotoxique.",
            "D": "Pouvoir ébrionarcotique très fort (+++).",
            "E": "Utilisé comme solvant industriel."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Il est connu pour provoquer des hépatites cytolytiques et des nécroses rénales."
    },
    {
        "titre": "Intoxication au Dichlorométhane (Décapant peinture) :",
        "type": "vraies",
        "items": {
            "A": "C'est le moins volatil des solvants chlorés.",
            "B": "Il provoque une intoxication au monoxyde de carbone (CO) endogène.",
            "C": "On peut observer des taux de carboxyhémoglobine (HbCO) jusqu'à 30%.",
            "D": "Il est classé cancérogène possible (2B) par le CIRC.",
            "E": "Le traitement inclut l'oxygénothérapie."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : C'est un liquide très volatil. La production de CO est sa signature toxique unique."
    },
    {
        "titre": "Cancer et solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "Le trichloréthylène est classé Groupe 1 (Cancérogène certain).",
            "B": "Le chlorure de vinyle est classé Groupe 1.",
            "C": "Le tétrachloroéthylène est classé Groupe 2A (Probable).",
            "D": "Ils provoquent uniquement des cancers du poumon.",
            "E": "Les organes cibles sont le foie, le rein et le système hématopoïétique."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Ils causent des cancers du foie (angiosarcome), du rein, des lymphomes/leucémies."
    },
    {
        "titre": "Analyses toxicologiques (Solvants chlorés) :",
        "type": "vraies",
        "items": {
            "A": "Le dosage sanguin se fait par GC-FID ou GC-MS (Chromatographie gazeuse).",
            "B": "On dose les métabolites dans le sang uniquement.",
            "C": "On dose les solvants inchangés dans le sang.",
            "D": "On dose les métabolites dans les urines.",
            "E": "La réaction de Fujiwara-Ross est une méthode de dosage précise."
        },
        "correctes": ["A", "C", "D"],
        "explication": "E est Faux : C'est une méthode colorimétrique de dépistage/détection (rose/rouge), pas un dosage précis."
    },
    {
        "titre": "Facteurs aggravant la toxicité des solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "La consommation d'alcool (induction enzymatique).",
            "B": "L'obésité (stockage dans les graisses).",
            "C": "L'hypoxie.",
            "D": "L'effort physique (augmentation du débit respiratoire et cardiaque).",
            "E": "La prise de médicaments inhibiteurs du CYP2E1."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Ce sont les INDUCTEURS (comme l'alcool) qui augmentent la production de métabolites toxiques via le CYP2E1."
    },
    {
        "titre": "Élimination des solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "La majorité est éliminée par les reins.",
            "B": "La majorité est éliminée par les poumons (air expiré) sous forme inchangée.",
            "C": "Le chlorure de méthylène est éliminé à 90% par voie respiratoire.",
            "D": "Le trichloréthylène est peu éliminé par voie respiratoire (10%).",
            "E": "L'élimination dépend de la volatilité et de la liposolubilité."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "A est Faux : C'est la voie respiratoire qui prime pour la forme inchangée, la voie rénale est pour les métabolites."
    },
    {
        "titre": "Symptômes cardiaques du Trichloréthylène :",
        "type": "vraies",
        "items": {
            "A": "Bradycardie.",
            "B": "Hyperexcitabilité ventriculaire.",
            "C": "Fibrillation ventriculaire possible.",
            "D": "Sensibilisation du myocarde aux catécholamines endogènes.",
            "E": "Hypertension sévère."
        },
        "correctes": ["B", "C", "D"],
        "explication": "C'est un risque de mort subite par trouble du rythme ('bathmotrope positif')."
    },
    {
        "titre": "Utilisations industrielles des solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "Dégraissage des métaux.",
            "B": "Nettoyage à sec (pressings).",
            "C": "Décapage de peintures.",
            "D": "Industrie du froid (fluides frigorigènes).",
            "E": "Additifs alimentaires."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Ce sont des produits toxiques, jamais alimentaires."
    },
    {
        "titre": "Protection individuelle contre les solvants chlorés :",
        "type": "vraies",
        "items": {
            "A": "Masque à poussière simple.",
            "B": "Masque à cartouche filtrante adaptée (gaz organiques).",
            "C": "Gants en matériaux résistants (PVA, Viton).",
            "D": "Les gants en latex sont recommandés.",
            "E": "Combinaison de protection."
        },
        "correctes": ["B", "C", "E"],
        "explication": "A est Faux (ce sont des gaz/vapeurs). D est Faux : Le latex est souvent perméable aux solvants chlorés, il faut des matériaux spécifiques."
    }
]# --- BANQUE DE QUESTIONS : LE PLOMB (SATURNISME) ---
questions_plomb = [
    {
        "titre": "Propriétés physico-chimiques et sources du Plomb :",
        "type": "vraies",
        "items": {
            "A": "C'est un métal lourd fondant à basse température (327°C).",
            "B": "Il a une forte affinité pour les fonctions thiols (cystéine).",
            "C": "Il est utilisé dans les batteries (accumulateurs) et les peintures (minium, céruse).",
            "D": "Il ne traverse pas le placenta.",
            "E": "La limite de qualité dans l'eau de boisson est de 10 µg/L."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Il passe facilement la barrière placentaire."
    },
    {
        "titre": "Concernant l'absorption et le transport du Plomb :",
        "type": "vraies",
        "items": {
            "A": "L'absorption digestive est de 10% chez l'adulte et 40-50% chez l'enfant.",
            "B": "L'absorption pulmonaire est d'environ 35%.",
            "C": "Dans le sang, il se fixe majoritairement sur les protéines plasmatiques.",
            "D": "La concentration intra-érythrocytaire est 16 fois supérieure à celle du plasma.",
            "E": "Il emprunte les transporteurs du Calcium et du Fer."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "C est Faux : Il se fixe aux HÉMATIES (globules rouges)."
    },
    {
        "titre": "Distribution et Stockage du Plomb :",
        "type": "vraies",
        "items": {
            "A": "95% de la charge corporelle se trouve dans le squelette.",
            "B": "La demi-vie dans l'os cortical est d'environ 1 mois.",
            "C": "La demi-vie dans l'os cortical est d'environ 9,5 ans.",
            "D": "Il s'accumule aussi dans le foie, les reins et le SNC.",
            "E": "La concentration osseuse diminue avec l'âge."
        },
        "correctes": ["A", "C", "D"],
        "explication": "B est Faux. E est Faux : La concentration augmente jusqu'à 50-60 ans."
    },
    {
        "titre": "Mécanisme toxique sur l'Hème (Toxicodynamie) :",
        "type": "vraies",
        "items": {
            "A": "Il inhibe l'ALA déshydratase.",
            "B": "Il inhibe la Ferrochélatase.",
            "C": "Cela entraîne une augmentation de l'ALA dans les urines.",
            "D": "Cela entraîne une augmentation de la Zinc-Protoporphyrine (PPZ).",
            "E": "Il stimule la synthèse de la globine."
        },
        "correctes": ["A", "B", "C", "D"],
        "explication": "E est Faux : Il DIMINUE la synthèse de la globine."
    },
    {
        "titre": "Conséquences hématologiques du Saturnisme :",
        "type": "vraies",
        "items": {
            "A": "Anémie normochrome normocytaire.",
            "B": "Caractère régénératif (augmentation des réticulocytes).",
            "C": "Diminution de la durée de vie des hématies.",
            "D": "Présence de granulations basophiles dans les hématies.",
            "E": "Inhibition de la pyrimidine 5' nucléotidase."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tableau hématologique complet du saturnisme."
    },
    {
        "titre": "Symptômes neurologiques de l'intoxication chronique :",
        "type": "vraies",
        "items": {
            "A": "Chez l'enfant : baisse de QI dès 100 µg/L.",
            "B": "Chez l'enfant : encéphalopathie (coma, convulsions) si > 1000 µg/L.",
            "C": "Chez l'adulte : neuropathie périphérique motrice.",
            "D": "Chez l'adulte : paralysie des muscles fléchisseurs.",
            "E": "Chez l'adulte : paralysie des muscles extenseurs."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : C'est une paralysie des EXTENSEURS (chute du poignet)."
    },
    {
        "titre": "Atteinte rénale du Plomb :",
        "type": "vraies",
        "items": {
            "A": "L'atteinte précoce est une tubulopathie proximale.",
            "B": "L'atteinte précoce est irréversible.",
            "C": "Signes précoces : glycosurie, hypercalciurie, protéinurie.",
            "D": "L'atteinte tardive est une néphropathie tubulo-interstitielle chronique.",
            "E": "L'atteinte tardive comprend atrophie glomérulaire et fibrose."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : L'atteinte précoce est réversible à l'arrêt de l'exposition."
    },
    {
        "titre": "Autres effets toxiques (Cardio, Digestif, Cancer) :",
        "type": "vraies",
        "items": {
            "A": "Hypertension artérielle paroxystique.",
            "B": "Coliques de plomb (douleurs abdominales).",
            "C": "Diminution du périmètre thoracique chez l'enfant.",
            "D": "Classé groupe 1 (cancérogène certain) par le CIRC.",
            "E": "Classé groupe 2A (probablement cancérogène) par le CIRC."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Les dérivés inorganiques sont classés 2A."
    },
    {
        "titre": "Intoxication aiguë (Rare) :",
        "type": "vraies",
        "items": {
            "A": "Douleurs abdominales intenses (coliques) et vomissements.",
            "B": "Hémolyse.",
            "C": "Cytolyse hépatique.",
            "D": "Insuffisance rénale aiguë (tubulaire).",
            "E": "Décès par collapsus cardio-vasculaire."
        },
        "correctes": ["A", "B", "C", "D", "E"],
        "explication": "Tableau clinique de l'intoxication aiguë massive."
    },
    {
        "titre": "Réglementation et Déclaration :",
        "type": "vraies",
        "items": {
            "A": "Le saturnisme infantile est une maladie à déclaration obligatoire.",
            "B": "Le seuil de déclaration est de 100 µg/L.",
            "C": "Le seuil de déclaration a été abaissé à 50 µg/L en 2014.",
            "D": "Il existe un seuil de vigilance à 25 µg/L.",
            "E": "La VLEP est de 0,1 mg/m3."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : L'ancien seuil était 100, le nouveau est 50 µg/L."
    },
    {
        "titre": "Indicateurs biologiques d'exposition :",
        "type": "vraies",
        "items": {
            "A": "Le dosage de référence est la plombémie (sang total).",
            "B": "La plomburie provoquée est un excellent indicateur.",
            "C": "Dosage de l'ALA urinaire (N < 4 mg/g créatinine).",
            "D": "Dosage de la PPZ érythrocytaire (N < 3 µg/g Hb).",
            "E": "Analyses par SAA-F ou ICP-MS."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : C'est un indicateur MÉDIOCRE."
    },
    {
        "titre": "Traitement chélateur si plombémie > 1000 µg/L :",
        "type": "vraies",
        "items": {
            "A": "Traitement à domicile.",
            "B": "Traitement d'urgence à l'hôpital.",
            "C": "Utilisation de DMSA seul.",
            "D": "Association BAL (IM) + EDTA (IV).",
            "E": "Nécessite une hyperhydratation."
        },
        "correctes": ["B", "D", "E"],
        "explication": "C'est le schéma pour les intoxications massives ou encéphalopathies."
    },
    {
        "titre": "Traitement chélateur si plombémie entre 700 et 1000 µg/L :",
        "type": "vraies",
        "items": {
            "A": "Association EDTA + DMSA.",
            "B": "Traitement à l'hôpital.",
            "C": "Traitement ambulatoire simple.",
            "D": "5 cures sont nécessaires.",
            "E": "Hyperhydratation nécessaire."
        },
        "correctes": ["A", "B", "D", "E"],
        "explication": "Protocole lourd nécessitant une hospitalisation."
    },
    {
        "titre": "Traitement chélateur si plombémie entre 450 et 700 µg/L :",
        "type": "vraies",
        "items": {
            "A": "Traitement par DMSA seul.",
            "B": "Traitement par EDTA IV.",
            "C": "Administration orale.",
            "D": "Peut se faire à domicile (HAD).",
            "E": "3 cures sont nécessaires."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "Dans cette tranche, on passe au DMSA oral, possible à domicile."
    },
    {
        "titre": "Traitement si plombémie entre 250 et 450 µg/L :",
        "type": "vraies",
        "items": {
            "A": "Chélation systématique.",
            "B": "Ce n'est pas une indication habituelle de chélation.",
            "C": "Chélation si la plombémie stagne malgré l'éviction de la source.",
            "D": "Chélation si anémie microcytaire persistante.",
            "E": "Surveillance simple si baisse spontanée."
        },
        "correctes": ["B", "C", "D", "E"],
        "explication": "La priorité est l'enquête environnementale. On ne traite chimiquement que si ça ne suffit pas."
    },
    {
        "titre": "Propriétés du BAL (Dimercaprol) :",
        "type": "vraies",
        "items": {
            "A": "Plus ancien chélateur (anti-lewisite).",
            "B": "S'administre par voie orale.",
            "C": "S'administre par injection intramusculaire (IM).",
            "D": "Peut causer HTA et tachycardie.",
            "E": "Peut causer des brûlures des muqueuses."
        },
        "correctes": ["A", "C", "D", "E"],
        "explication": "B est Faux : Uniquement en IM douloureuse."
    },
    {
        "titre": "Prévention et mesures hygiéno-diététiques :",
        "type": "vraies",
        "items": {
            "A": "Détection des peintures au plomb (> 1 mg/cm²).",
            "B": "Couper les ongles des enfants.",
            "C": "Lavage fréquent des mains.",
            "D": "Nettoyage des sols à sec (balai).",
            "E": "Nettoyage des surfaces avec un linge humide."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Le balayage à sec remet les poussières de plomb en suspension, il faut un nettoyage humide."
    },
    {
        "titre": "Doses limites hebdomadaires (OMS) :",
        "type": "vraies",
        "items": {
            "A": "25 µg/kg de poids corporel.",
            "B": "Soit environ 1750 µg/semaine pour un adulte de 70 kg.",
            "C": "En France, l'apport alimentaire moyen est de 4000 µg/semaine.",
            "D": "En France, l'apport alimentaire moyen est d'environ 400 µg/semaine.",
            "E": "L'exposition alimentaire est négligeable."
        },
        "correctes": ["A", "B", "D"],
        "explication": "C et E sont Faux : L'apport alimentaire existe (57 µg/jour) et n'est pas négligeable."
    },
    {
        "titre": "Méthodes d'analyse du Plomb :",
        "type": "vraies",
        "items": {
            "A": "SAA-F (Absorption Atomique Flamme).",
            "B": "ICP-MS (Torche à plasma couplée masse).",
            "C": "Le prélèvement atmosphérique se fait sur filtre quartz.",
            "D": "Le dosage sanguin se fait sur plasma.",
            "E": "Le dosage sanguin se fait sur sang total."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : Sang total car le plomb est dans les hématies."
    },
    {
        "titre": "Élimination du Plomb :",
        "type": "vraies",
        "items": {
            "A": "La phase rapide concerne le plomb non fixé.",
            "B": "La phase très lente concerne le plomb osseux (années).",
            "C": "L'élimination urinaire est majoritaire (75%).",
            "D": "L'élimination digestive est majoritaire.",
            "E": "La filtration glomérulaire est le mécanisme rénal."
        },
        "correctes": ["A", "B", "C", "E"],
        "explication": "D est Faux : La voie digestive ne représente que la fraction non absorbée (0,5%)."
    }
]


# --- INITIALISATION DES ETATS (Session State) ---
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'questions_du_jour' not in st.session_state:
    st.session_state.questions_du_jour = []
if 'etape' not in st.session_state:
    st.session_state.etape = 0
if 'score' not in st.session_state:
    st.session_state.score = 0.0
if 'reponse_validee' not in st.session_state:
    st.session_state.reponse_validee = False

# --- FONCTION POUR LANCER UNE PARTIE ---
def demarrer_partie(liste_questions, titre_mode):
    if not liste_questions:
        st.error("Erreur de chargement des questions.")
        return
    nb_q = min(20, len(liste_questions))
    st.session_state.questions_du_jour = random.sample(liste_questions, nb_q)
    st.session_state.titre_mode = titre_mode
    st.session_state.quiz_started = True
    st.session_state.etape = 0
    st.session_state.score = 0.0
    st.session_state.reponse_validee = False
    st.rerun()

# ==========================================
# GESTION DE LA NAVIGATION (SIDEBAR)
# ==========================================
st.sidebar.title("📌 Navigation")
choix_page = st.sidebar.radio(
    "Matière :",
    ["UE1 : Pathologies Sociales", "UE2 : Santé Environnement", "UE3 : Hydrologie"],
    index=0 # Par défaut sur la première
)

# Petit fix pour garder la page active en mémoire si on recharge
if 'page_active' not in st.session_state:
    st.session_state.page_active = "UE1 : Pathologies Sociales"

if choix_page != st.session_state.page_active:
    st.session_state.page_active = choix_page
    st.session_state.quiz_started = False
    st.rerun()

if 'page_active' not in st.session_state or choix_page != st.session_state.page_active:
    st.session_state.page_active = choix_page
    st.session_state.quiz_started = False
    st.rerun()

# ==========================================
# ECRAN 1 : LE MENU PRINCIPAL (ACCUEIL)
# ==========================================
if not st.session_state.quiz_started:
    st.title(f"📚 {st.session_state.page_active}")
    st.write("Choisissez votre mode d'entraînement :")
    st.info("ℹ️ **Barème PASS :** 1 point par question. -0.2 par erreur. Min 0.")
    st.write("---")

    # --- PAGE 1 : PATHOLOGIES SOCIALES ---
    if st.session_state.page_active == "UE1 : Pathologies Sociales":
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("🔄 **Mixte UE1**")
            if st.button("Tout l'UE1", key="btn_ue1_mixte", use_container_width=True):
                # UE1 = Alcool, Dopage, Gaz, Addicto, Drogues
                pool = questions[:150] 
                demarrer_partie(pool, "Mixte Pathologies Sociales")
        with col2:
            st.warning("🍷 **Alcool**")
            if st.button("Lancer Alcool", key="btn_alcool", use_container_width=True):
                demarrer_partie(questions[:30], "Spécial Alcool")
        with col3:
            st.error("💉 **Dopage**")
            if st.button("Lancer Dopage", key="btn_dopage", use_container_width=True):
                demarrer_partie(questions[30:60], "Spécial Dopage")

        st.write("")
        col4, col5, col6 = st.columns(3)
        with col4:
            st.success("🎈 **Gaz**")
            if st.button("Lancer Gaz", key="btn_gaz", use_container_width=True):
                demarrer_partie(questions[60:90], "Spécial Gaz")
        with col5:
            st.info("🧠 **Addicto**")
            if st.button("Lancer Addicto", key="btn_addicto", use_container_width=True):
                demarrer_partie(questions[90:120], "Spécial Addicto")
        with col6:
            st.error("💊 **Drogues**")
            if st.button("Lancer Drogues", key="btn_drogues", use_container_width=True):
                demarrer_partie(questions[120:150], "Spécial Drogues")

        st.write("---")
        st.warning("🏆 **ANNALES UE1**")
        if st.button("Questions Examens UE1", key="btn_annales_ue1", use_container_width=True, type="primary"):
            # Annales UE1 sont à la fin de la liste principale
            demarrer_partie(questions[150:], "Annales Pathologies Sociales")

# --- PAGE 2 : SANTE ENVIRONNEMENT ---
    elif st.session_state.page_active == "UE2 : Santé Environnement":
        
        col_mixte, col_vide = st.columns([1, 1])
        with col_mixte:
            st.info("🌍 **Mixte UE2 Global**")
            if st.button("Tout l'UE2", key="btn_ue2_mixte", use_container_width=True):
                # On ajoute les nouvelles listes au pool global
                pool_global = questions_ue2 + questions_toxiques + questions_ethers + questions_chlores + questions_plomb
                demarrer_partie(pool_global, "Mixte Santé Environnement (Tout)")

        st.write("---")
        # Ligne 1 : Les 4 thèmes initiaux
        colA, colB, colC, colD = st.columns(4)

        with colA:
            st.warning("🧬 **PE (Endoc)**")
            if st.button("Perturbateurs", key="btn_pe", use_container_width=True):
                demarrer_partie(questions_ue2[:10], "Spécial PE")

        with colB:
            st.error("🔥 **PFAS**")
            if st.button("PFAS", key="btn_pfas", use_container_width=True):
                demarrer_partie(questions_ue2[10:20], "Spécial PFAS")

        with colC:
            st.success("🌾 **Pesticides**")
            if st.button("Pesticides", key="btn_pest", use_container_width=True):
                demarrer_partie(questions_ue2[20:30], "Spécial Pesticides")

        with colD:
            st.info("🏭 **Dioxines**")
            if st.button("Dioxines", key="btn_diox", use_container_width=True):
                demarrer_partie(questions_ue2[30:], "Spécial Dioxines")
        
        st.write("")
        st.subheader("☣️ Toxicologie Environnementale")
        # Ligne 2 : Les Toxiques
        col_new1, col_new2, col_new3, col_new4 = st.columns(4) # On passe à 4 colonnes
        
        with col_new1:
            st.error("☢️ **Solvants & Métaux**")
            st.caption("Méthanol, EG") 
            if st.button("Lancer Alcools Tox", key="btn_tox_env", use_container_width=True):
                demarrer_partie(questions_toxiques, "Spécial Solvants (Méthanol/EG)")
        
        with col_new2:
            st.warning("🧪 **Éthers de Glycol**")
            st.caption("Séries E/P, Toxicité")
            if st.button("Lancer Éthers", key="btn_ethers", use_container_width=True):
                demarrer_partie(questions_ethers, "Spécial Éthers de Glycol")

        with col_new3:
            st.success("🧽 **Solvants Chlorés**")
            st.caption("Trichlo, CCl4, Vinyle")
            if st.button("Lancer Chlorés", key="btn_chlores", use_container_width=True):
                demarrer_partie(questions_chlores, "Spécial Solvants Chlorés")

        with col_new4:
            st.error("🏗️ **Le Plomb**") # Nouveau bouton spécifique
            st.caption("Saturnisme, Chélation")
            if st.button("Lancer Plomb", key="btn_plomb", use_container_width=True):
                demarrer_partie(questions_plomb, "Spécial Plomb & Saturnisme")
    # --- PAGE 3 : HYDROLOGIE ---
    elif st.session_state.page_active == "UE3 : Hydrologie":
        
        st.info("💧 **Cours d'Hydrologie**")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.success("🌊 **Généralités & Physico-Chimie**")
            st.caption("Ressources, Potabilisation, Normes")
            # Questions 0 à 20
            if st.button("Lancer Généralités", key="btn_hydro_gen", use_container_width=True):
                demarrer_partie(questions_hydro[:20], "Hydrologie : Généralités")

        with col2:
            st.warning("🦠 **Risques Microbiologiques**")
            st.caption("Bactéries (Choléra, Légio) & Virus")
            # Questions 20 à 40
            if st.button("Lancer Microbio", key="btn_hydro_micro", use_container_width=True):
                demarrer_partie(questions_hydro[20:40], "Hydrologie : Microbiologie")

        with col3:
            st.error("parasite **Risques Parasitaires**")
            st.caption("Giardia, Crypto, Amibes")
            # Questions 40 à 60
            if st.button("Lancer Parasito", key="btn_hydro_para", use_container_width=True):
                demarrer_partie(questions_hydro[40:], "Hydrologie : Parasitologie")
        
        st.write("---")
        if st.button("🔄 Tout l'UE3 (Mixte)", key="btn_hydro_mixte", use_container_width=True):
            demarrer_partie(questions_hydro, "Mixte Hydrologie")

# ==========================================
# ECRAN 2 : LE JEU
# ==========================================
else:
    # --- BARRE LATERALE ---
    with st.sidebar:
        st.write("---")
        st.write(f"Mode : **{st.session_state.titre_mode}**")
        score_display = round(st.session_state.score, 2)
        st.metric(label="Score actuel", value=f"{score_display}")
        
        total_questions = len(st.session_state.questions_du_jour)
        progress_val = st.session_state.etape / total_questions if total_questions > 0 else 0
        st.progress(progress_val)
        
        st.write("---")
        if st.button("🚪 Quitter le QCM", key="btn_exit_sidebar", type="primary"):
            st.session_state.quiz_started = False
            st.session_state.reponse_validee = False
            st.session_state.etape = 0
            st.session_state.score = 0.0
            st.rerun()

    # --- CONTENU PRINCIPAL ---
    ma_serie = st.session_state.questions_du_jour
    
    st.title(f"🎓 {st.session_state.titre_mode}")

    if st.session_state.etape < len(ma_serie):
        q_actuelle = ma_serie[st.session_state.etape]
        
        st.subheader(f"Question {st.session_state.etape + 1} / {len(ma_serie)}")
        st.markdown(f"**{q_actuelle['titre']}**")
        
        type_q = q_actuelle.get("type", "vraies")
        if type_q == "fausses":
            st.error("⚠️ ATTENTION : Cochez les propositions FAUSSES (ce qui est INEXACT) :")
        else:
            st.info("Cochez les propositions VRAIES (ce qui est EXACT) :")
        
        with st.form(key=f'qcm_form_{st.session_state.etape}'): 
            c_a = st.checkbox(f"A. {q_actuelle['items']['A']}")
            c_b = st.checkbox(f"B. {q_actuelle['items']['B']}")
            c_c = st.checkbox(f"C. {q_actuelle['items']['C']}")
            c_d = st.checkbox(f"D. {q_actuelle['items']['D']}")
            c_e = st.checkbox(f"E. {q_actuelle['items']['E']}")
            
            submit_button = st.form_submit_button(label='Valider ma réponse')

        if submit_button:
            st.session_state.reponse_validee = True
        
        if st.session_state.reponse_validee:
            user_list = []
            if c_a: user_list.append("A")
            if c_b: user_list.append("B")
            if c_c: user_list.append("C")
            if c_d: user_list.append("D")
            if c_e: user_list.append("E")
            
            user_set = set(user_list)
            correct_set = set(q_actuelle["correctes"])
            
            oublis = correct_set - user_set
            intrus = user_set - correct_set
            nb_erreurs = len(oublis) + len(intrus)
            
            note_question = max(0.0, 1.0 - (0.2 * nb_erreurs))
            note_question = round(note_question, 2)
            
            if submit_button: 
                st.session_state.score += note_question

            if nb_erreurs == 0:
                st.success(f"PARFAIT ! (+1 pt)")
            else:
                # C'EST ICI QU'ON MODIFIE POUR LA LISIBILITÉ
                col_res1, col_res2 = st.columns([1, 3])
                with col_res1:
                    if note_question >= 0.5:
                        st.warning(f"Note : {note_question}/1")
                    else:
                        st.error(f"Note : {note_question}/1")
                
                with col_res2:
                    # On construit le message d'erreur
                    msg_err = ""
                    if oublis:
                        msg_err += f"❌ Oublis : {', '.join(oublis)}\n\n"
                    if intrus:
                        msg_err += f"⛔ En trop : {', '.join(intrus)}\n\n"
                    
                    # On ajoute la bonne réponse à la fin
                    msg_err += f"✅ Réponse attendue : {', '.join(q_actuelle['correctes'])}"
                    
                    # ON UTILISE st.info POUR METTRE LE TEXTE DANS UNE BOITE BLEUE OPAQUE
                    st.info(msg_err)

            # --- MODIFICATION POUR L'EXPLICATION ---
            with st.expander("Voir l'explication détaillée", expanded=True):
                # On utilise du HTML pour forcer un fond blanc opaque autour du texte
                st.markdown(
                    f"""
                    <div style="
                        background-color: rgba(255, 255, 255, 0.95); 
                        padding: 20px; 
                        border-radius: 10px; 
                        border: 1px solid #ccc; 
                        color: black;
                        font-size: 16px;
                    ">
                        {q_actuelle['explication']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            if st.button("Question Suivante ➡️", key=f"btn_next_{st.session_state.etape}"):
                st.session_state.etape += 1
                st.session_state.reponse_validee = False
                st.rerun()

    else:
        st.balloons()
        note_finale = round(st.session_state.score, 2)
        total = len(ma_serie)
        
        st.success(f"🎉 Série terminée !")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Note brute", value=f"{note_finale} / {total}")
        with col2:
            if total > 0:
                note_20 = round((note_finale / total) * 20, 2)
            else:
                note_20 = 0
            st.metric(label="Note sur 20", value=f"{note_20} / 20")
        
        st.write("---")
        
        col_A, col_B = st.columns(2)
        with col_A:
            if st.button("🏠 Retour au Menu Principal", key="btn_home_end", use_container_width=True):
                st.session_state.quiz_started = False
                st.session_state.reponse_validee = False
                st.session_state.etape = 0
                st.session_state.score = 0
                st.rerun()
        with col_B:
            if st.button("🔄 Relancer une série", key="btn_restart_end", use_container_width=True):
                # Relance intelligente
                if st.session_state.page_active == "UE1 : Pathologies Sociales":
                    if "Alcool" in st.session_state.titre_mode: pool = questions[:30]
                    elif "Dopage" in st.session_state.titre_mode: pool = questions[30:60]
                    elif "Gaz" in st.session_state.titre_mode: pool = questions[60:90]
                    elif "Addicto" in st.session_state.titre_mode: pool = questions[90:120]
                    elif "Drogues" in st.session_state.titre_mode: pool = questions[120:150]
                    elif "ANNALES" in st.session_state.titre_mode: pool = questions[150:]
                    else: pool = questions[:150]
                
                elif st.session_state.page_active == "UE2 : Santé Environnement":
                    if "PE" in st.session_state.titre_mode: pool = questions_ue2[:10]
                    elif "PFAS" in st.session_state.titre_mode: pool = questions_ue2[10:20]
                    elif "Pesticides" in st.session_state.titre_mode: pool = questions_ue2[20:30]
                    elif "Dioxines" in st.session_state.titre_mode: pool = questions_ue2[30:]
                    elif "Solvants & Plomb" in st.session_state.titre_mode: pool = questions_toxiques
                    elif "Éthers" in st.session_state.titre_mode: pool = questions_ethers
                    elif "Chlorés" in st.session_state.titre_mode: pool = questions_chlores
                    else: pool = questions_ue2 + questions_toxiques + questions_ethers + questions_chlores

                elif st.session_state.page_active == "UE3 : Hydrologie":
                    if "Généralités" in st.session_state.titre_mode: pool = questions_hydro[:20]
                    elif "Microbiologie" in st.session_state.titre_mode: pool = questions_hydro[20:40]
                    elif "Parasitologie" in st.session_state.titre_mode: pool = questions_hydro[40:]
                    else: pool = questions_hydro
                
                demarrer_partie(pool, st.session_state.titre_mode)
