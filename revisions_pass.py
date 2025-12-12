import random
import streamlit as st

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Entrainement PASS", page_icon="💊")

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
    nb_q = min(20, len(liste_questions))
    st.session_state.questions_du_jour = random.sample(liste_questions, nb_q)
    st.session_state.titre_mode = titre_mode
    st.session_state.quiz_started = True
    st.session_state.etape = 0
    st.session_state.score = 0.0
    st.session_state.reponse_validee = False
    st.rerun()

# ==========================================
# ECRAN 1 : LE MENU PRINCIPAL
# ==========================================
if not st.session_state.quiz_started:
    st.title("📚 Menu de Révision PASS")
    st.write("Choisissez votre mode d'entraînement :")
    st.info("ℹ️ **Barème PASS :** 1 point par question. -0.2 par erreur (oubli ou faute). Minimum 0.")
    st.write("---")

    # 6 colonnes pour les 6 boutons
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.info("🔄 **Mixte**")
        st.caption("Tout le programme")
        if st.button("Lancer Mixte", key="btn_mixte", use_container_width=True):
            demarrer_partie(questions, "Mode Mixte Général")

    with col2:
        st.warning("🍷 **Alcool**")
        st.caption("Q. 1 à 30")
        if st.button("Lancer Alcool", key="btn_alcool", use_container_width=True):
            pool = questions[:30]
            demarrer_partie(pool, "Spécial Alcool")

    with col3:
        st.error("💉 **Dopage**")
        st.caption("Q. 31 à 60")
        if st.button("Lancer Dopage", key="btn_dopage", use_container_width=True):
            pool = questions[30:60] 
            demarrer_partie(pool, "Spécial Dopage")
    
    with col4:
        st.success("🎈 **Gaz**")
        st.caption("Q. 61 à 90")
        if st.button("Lancer Gaz", key="btn_gaz", use_container_width=True):
            pool = questions[60:90]
            demarrer_partie(pool, "Spécial Gaz & Inhalants")

    with col5:
        st.info("🧠 **Addicto**")
        st.caption("Q. 91 à 120")
        if st.button("Lancer Addicto", key="btn_addicto", use_container_width=True):
            pool = questions[90:120]
            demarrer_partie(pool, "Spécial Généralités Addicto")

    with col6:
        st.error("💊 **Drogues/PEC**")
        st.caption("Q. 121 à 150")
        if st.button("Lancer Drogues", key="btn_drogues", use_container_width=True):
            # On prend les nouvelles questions (120 à la fin)
            pool = questions[120:]
            demarrer_partie(pool, "Spécial Drogues & Prise en Charge")

# ==========================================
# ECRAN 2 : LE QCM (Une fois lancé)
# ==========================================
else:
    # --- BARRE LATERALE ---
    with st.sidebar:
        st.header("Navigation")
        st.write(f"Mode : **{st.session_state.titre_mode}**")
        
        # Affichage du score arrondi
        score_display = round(st.session_state.score, 2)
        st.metric(label="Score actuel", value=f"{score_display}")
        
        progress_val = st.session_state.etape / len(st.session_state.questions_du_jour)
        st.progress(progress_val)
        
        st.write("---")
        if st.button("🚪 Quitter / Menu", key="btn_exit_sidebar", type="primary"):
            st.session_state.quiz_started = False
            st.session_state.reponse_validee = False
            st.session_state.etape = 0
            st.session_state.score = 0
            st.rerun()

    # --- CONTENU PRINCIPAL ---
    ma_serie = st.session_state.questions_du_jour
    
    st.title(f"🎓 {st.session_state.titre_mode}")

    # TANT QU'IL RESTE DES QUESTIONS
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
        
        # --- LOGIQUE NOTATION PASS ---
        if st.session_state.reponse_validee:
            user_list = []
            if c_a: user_list.append("A")
            if c_b: user_list.append("B")
            if c_c: user_list.append("C")
            if c_d: user_list.append("D")
            if c_e: user_list.append("E")
            
            user_set = set(user_list)
            correct_set = set(q_actuelle["correctes"])
            
            # Calcul erreurs
            oublis = correct_set - user_set
            intrus = user_set - correct_set
            nb_erreurs = len(oublis) + len(intrus)
            
            # Note PASS : 1 - (0.2 * faute), min 0
            note_question = max(0.0, 1.0 - (0.2 * nb_erreurs))
            note_question = round(note_question, 2)
            
            if submit_button: 
                st.session_state.score += note_question

            # Affichage résultats
            if nb_erreurs == 0:
                st.success(f"PARFAIT ! (+1 pt)")
            else:
                col_res1, col_res2 = st.columns([1, 3])
                with col_res1:
                    if note_question >= 0.5:
                        st.warning(f"Note : {note_question}/1")
                    else:
                        st.error(f"Note : {note_question}/1")
                
                with col_res2:
                    msg_err = ""
                    if oublis:
                        msg_err += f"❌ Oublis : {', '.join(oublis)} "
                    if intrus:
                        msg_err += f"⛔ En trop : {', '.join(intrus)}"
                    st.markdown(f"**{msg_err}**")
                    st.write(f"Réponse attendue : {', '.join(q_actuelle['correctes'])}")

            with st.expander("Voir l'explication détaillée", expanded=True):
                st.write(q_actuelle['explication'])
            
            if st.button("Question Suivante ➡️", key=f"btn_next_{st.session_state.etape}"):
                st.session_state.etape += 1
                st.session_state.reponse_validee = False
                st.rerun()

    # ECRAN DE FIN DE SÉRIE
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
            if st.button("🔄 Relancer une série (Même mode)", key="btn_restart_end", use_container_width=True):
                # Relance le même mode
                pool = questions
                if "Alcool" in st.session_state.titre_mode:
                    pool = questions[:30]
                elif "Dopage" in st.session_state.titre_mode:
                    pool = questions[30:60]
                elif "Gaz" in st.session_state.titre_mode:
                    pool = questions[60:90]
                elif "Addicto" in st.session_state.titre_mode:
                    pool = questions[90:120]
                elif "Drogues" in st.session_state.titre_mode:
                    pool = questions[120:]
                
                demarrer_partie(pool, st.session_state.titre_mode)
