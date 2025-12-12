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
questions = questions = questions = [
    {
        "titre": "Epidémiologie et Mortalité",
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
        "titre": "Définitions et Dosages (Recherchez les ERREURS)",
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
        "titre": "Pharmacocinétique : Absorption",
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
        "titre": "Métabolisme de l'éthanol (Recherchez les ERREURS)",
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
        "titre": "Variabilité génétique et enzymatique",
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
        "titre": "Conséquences métaboliques",
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
        "titre": "Toxicité hépatique (Recherchez les ERREURS)",
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
        "titre": "Alcool et Cancer",
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
        "titre": "Syndrome d'Alcoolisation Fœtale (SAF)",
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
        "titre": "Système nerveux et Sevrage (Recherchez les ERREURS)",
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
        "titre": "Marqueurs biologiques",
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
        "titre": "Législation routière (France)",
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
        "titre": "Pathologies digestives hors foie",
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
        "titre": "Questionnaires de repérage (Recherchez les ERREURS)",
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
        "titre": "Binge Drinking",
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
        "titre": "Interactions médicamenteuses",
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
        "titre": "Physiopathologie de la fibrose hépatique",
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
        "titre": "Sevrage et Delirium Tremens",
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
        "titre": "Cardiomyopathie et Cœur (Recherchez les ERREURS)",
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
        "titre": "Excrétion de l'alcool",
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
        "titre": "Prise en charge hépatite alcoolique",
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
        "titre": "Signes cliniques d'imprégnation chronique",
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
        "titre": "Définition de la dépendance (Critères)",
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
        "titre": "Alcool et Accidents",
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
        "titre": "Effets sur le sang (Hématologie)",
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
        "titre": "Encéphalopathie de Gayet-Wernicke",
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
        "titre": "Coût social de l'alcool",
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
        "titre": "Méthode de Cordebard (Chimie)",
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
        "titre": "Marqueurs et Sevrage (Délais)",
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
        "titre": "Facteurs influençant l'alcoolémie",
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

    # --- PARTIE 2 : DOPAGE (30 Questions) ---
    {
        "titre": "Définition et Structures (Recherchez les ERREURS)",
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
        "titre": "Classification S1 : Anabolisants",
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
        "titre": "Effets secondaires des Stéroïdes (S1)",
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
        "titre": "Classification S2 : Hormones peptidiques",
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
        "titre": "Bêta-2 Agonistes (S3) (Recherchez les ERREURS)",
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
        "titre": "Modulateurs hormonaux (S4)",
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
        "titre": "Diurétiques et Masquants (S5)",
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
        "titre": "Stimulants (S6)",
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
        "titre": "Narcotiques et Cannabinoïdes (S7/S8)",
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
        "titre": "Glucocorticoïdes (S9)",
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
        "titre": "Méthodes interdites (M1, M2, M3)",
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
        "titre": "Contrôle Antidopage (Recherchez les ERREURS)",
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
        "titre": "AUT et Responsabilité",
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
        "titre": "Profil Biologique (Passeport)",
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
        "titre": "Bêta-bloquants (P1)",
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
        "titre": "Risques de l'hormone de croissance (hGH)",
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
        "titre": "Substances spécifiques (Quiz)",
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
        "titre": "Dopage génétique",
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
        "titre": "Statistiques et Compléments (Recherchez les ERREURS)",
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
        "titre": "Localisation et Acteurs",
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
        "titre": "Cibles des anabolisants",
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
        "titre": "EPO et physiologie",
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
        "titre": "Historique du Dopage",
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
        "titre": "Cannabis et Dopage",
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
        "titre": "Glucocorticoïdes : Effets recherchés",
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
        "titre": "Masquage physique (M2)",
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
        "titre": "Stimulants SNC (Recherchez les ERREURS)",
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
        "titre": "Conduite à tenir (AMPD)",
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
        "titre": "Alcool et dopage (S1 à P1)",
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
        "titre": "Synthèse Dopage",
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
    },# --- PARTIE 3 : GAZ ET INHALANTS ---
    {
        "titre": "Généralités sur les Inhalants",
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
        "titre": "Modes de consommation (Définitions)",
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
        "titre": "Classification des Hydrocarbures volatils",
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
        "titre": "Mécanisme d'action des solvants",
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
        "titre": "Effets initiaux (Ivresse)",
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
        "titre": "Nitrites d'alkyles (Poppers) : Généralités",
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
        "titre": "Mécanisme d'action des Poppers",
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
        "titre": "Effets recherchés des Poppers",
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
        "titre": "Toxicité Aiguë des Solvants (Recherchez les ERREURS)",
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
        "titre": "Mort subite du renifleur",
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
        "titre": "Toxicité Chronique des Solvants",
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
        "titre": "Toxicité Aiguë des Poppers (Nitrites)",
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
        "titre": "Lésions spécifiques des Poppers (Chronique)",
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
        "titre": "Prise en charge et Traitement",
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
        "titre": "Analyses toxicologiques",
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
        "titre": "Produits spécifiques et risques",
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
        "titre": "Facteurs de toxicité",
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
        "titre": "Interactions Poppers (Danger)",
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
        "titre": "Symptômes cutanés (Dermatologie)",
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
        "titre": "Epidémiologie Inhalants",
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
        "titre": "Méthanol et Dichlorométhane",
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
        "titre": "Effets sur le sang (Hématologie)",
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
        "titre": "Chemsex et Poppers",
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
        "titre": "Analyse Headspace (Espace de tête)",
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
        "titre": "Risques cardiaques (Détails)",
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
        "titre": "Comparaison Alcool / Solvants",
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
        "titre": "Addiction aux inhalants",
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
        "titre": "Propriétés physico-chimiques",
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
        "titre": "Législation et Prévention",
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
        "titre": "Synthèse Gaz et Inhalants",
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
    },# --- PARTIE 4 : ADDICTOLOGIE GÉNÉRALITÉS ---
    {
        "titre": "Histoire et Étymologie",
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
        "titre": "Physiopathologie (Circuit de la récompense)",
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
        "titre": "Définition de l'Addiction (Concepts actuels)",
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
        "titre": "Le Craving (Définition)",
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
        "titre": "Tolérance (Pharmacologie)",
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
        "titre": "Le Sevrage",
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
        "titre": "Dépendance Physique vs Psychique",
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
        "titre": "Classification des substances (Effets)",
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
        "titre": "Classification CIM-10 (Usage)",
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
        "titre": "Trivarié de l'Addiction (Facteurs de risque)",
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
        "titre": "Facteurs de vulnérabilité individuels",
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
        "titre": "Comorbidités psychiatriques",
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
        "titre": "Facteurs environnementaux",
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
        "titre": "Potentiel addictif des substances",
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
        "titre": "Pharmacocinétique et Addiction",
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
        "titre": "Caractère envahissant (Critères)",
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
        "titre": "Classification Usage (Détails)",
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
        "titre": "Critères de Dépendance (CIM-10 / DSM)",
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
        "titre": "Neurobiologie : Structures",
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
        "titre": "Traitement et Prise en charge",
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
        "titre": "Addictions sans substance",
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
        "titre": "Facteurs de protection",
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
        "titre": "Pic de dopamine et Administration",
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
        "titre": "Risques à l'adolescence",
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
        "titre": "Concepts : Renforcement",
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
        "titre": "Comorbidités : Lien causal",
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
        "titre": "RDRD (Réduction des Risques)",
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
        "titre": "Psychothérapies",
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
        "titre": "Addiction vs Habitude",
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
        "titre": "Épigénétique",
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
    st.session_state.score = 0.0 # On passe en décimal (float) pour les 0.2
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
    st.info("ℹ️ **Nouveau Barème :** 1 point par question. -0.2 par erreur (oubli ou faute). Minimum 0.")
    st.write("---")

    col1, col2, col3, col4, col5 = st.columns(5)

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
            pool = questions[90:]
            demarrer_partie(pool, "Spécial Généralités Addicto")

# ==========================================
# ECRAN 2 : LE QCM (Une fois lancé)
# ==========================================
else:
    # --- BARRE LATERALE ---
    with st.sidebar:
        st.header("Navigation")
        st.write(f"Mode : **{st.session_state.titre_mode}**")
        # Affichage du score arrondi à 2 décimales
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
        
        # --- LOGIQUE DE NOTATION PASS ---
        if st.session_state.reponse_validee:
            user_list = []
            if c_a: user_list.append("A")
            if c_b: user_list.append("B")
            if c_c: user_list.append("C")
            if c_d: user_list.append("D")
            if c_e: user_list.append("E")
            
            user_set = set(user_list)
            correct_set = set(q_actuelle["correctes"])
            
            # Calcul des erreurs
            # 1. Oublis (Ce qu'il fallait cocher mais qui manque)
            oublis = correct_set - user_set
            # 2. Intrus (Ce qu'on a coché en trop)
            intrus = user_set - correct_set
            
            nb_erreurs = len(oublis) + len(intrus)
            
            # Calcul de la note : 1 - (0.2 * nb_erreurs), minimum 0
            note_question = max(0.0, 1.0 - (0.2 * nb_erreurs))
            note_question = round(note_question, 2) # Pour éviter les 0.7999999
            
            # Ajout au score total (une seule fois au moment du clic)
            if submit_button: 
                st.session_state.score += note_question

            # --- AFFICHAGE DU RÉSULTAT ---
            if nb_erreurs == 0:
                st.success(f"PARFAIT ! (+1 pt)")
            else:
                col_res1, col_res2 = st.columns([1, 3])
                with col_res1:
                    # Couleur de la note selon le résultat
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
                if "Alcool" in st.session_state.titre_mode:
                    pool = questions[:30]
                elif "Dopage" in st.session_state.titre_mode:
                    pool = questions[30:60]
                elif "Gaz" in st.session_state.titre_mode:
                    pool = questions[60:90]
                elif "Addicto" in st.session_state.titre_mode:
                    pool = questions[90:]
                else:
                    pool = questions
                
                demarrer_partie(pool, st.session_state.titre_mode)