
import streamlit as st
from PIL import Image
import os

# Set page title and layout
st.set_page_config(page_title="Stroke Economic Burden Analysis", layout="wide")

# Title of the dashboard
st.title("Machine Learning Based Analysis of Economic Burden of Stroke and its Contributing Factors in the Indian Population")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Abstract", "Introduction", "Background", "Results", "Summary and Conclusions"])

# Abstract Section
if section == "Abstract":
    st.header("Abstract")
    st.write("""
    Stroke remains a significant public health challenge globally and a leading cause of death and
    disability in India. This study examines the economic burden of stroke on Indian households,
    focusing on catastrophic health expenditure (CHE) and its socio-economic determinants. Utilizing
    data from the National Sample Survey Office's (NSSO) 75th round, this study analyzed stroke-
    related healthcare costs across 1,293 hospitalization cases. Statistical and machine learning
    approaches were applied to quantify out-of-pocket (OOP) expenditures and identify key factors
    contributing to financial strain.

    Logistic regression revealed significant predictors of CHE, including OOP expenditure, household
    size, and consumption patterns, with OOP costs being the most critical determinant. Machine
    learning models, particularly XGBoost, outperformed traditional methods, achieving high
    accuracy (95.14%), precision (89.96%), and balanced F1-scores (88.30%), underscoring their
    predictive reliability. SHAP analysis further enhanced model interpretability, revealing household
    size and income quintile as the most influential features.

    The findings provide a nuanced understanding of the financial challenges associated with stroke-
    related healthcare, emphasizing the importance of integrating advanced analytics with traditional
    methods. This dual approach offers valuable insights into the socio-economic factors driving the
    economic burden of stroke in India, setting a precedent for future health economics research.
    """)

# Introduction Section
elif section == "Introduction":
    st.header("Introduction")
    st.write("""
    Globally, stroke (otherwise known as "brain attack") is a major public health concern because of
    its constantly increasing incidence and prevalence, especially in low- and middle-income (LMIC)
    nations like India. It ranks as India's fourth major cause of death and fifth leading cause of
    disability, meaning that it is one of the main causes of both mortality and morbidity. The
    estimated yearly incidence rate of stroke, ranging between 119 and 145 per million people,
    underscores this growing public health concern. This increasing burden places immense strain
    on healthcare systems and individual households, highlighting the urgent need for a comprehensive
    understanding of both the medical and economic impacts of stroke to inform effective
    interventions and policies.

    The economic burden of stroke in India is profound, driven largely by high out-of-pocket (OOP)
    expenditures incurred by households for stroke-related healthcare. Public healthcare
    infrastructure often struggles to meet demand, forcing individuals to shoulder the financial
    responsibility for treatment. This financial strain can be catastrophic, leading to long-term
    economic challenges that compromise household stability and quality of life. Additionally, stroke
    survivors often face prolonged disabilities, further exacerbating their economic hardships through
    lost productivity and the ongoing costs of rehabilitation and care.

    Despite the substantial burden of stroke, existing data on its economic impact in India is
    fragmented. Many studies rely on region-specific or small-scale samples, failing to capture
    the diversity of socio-economic contexts and the full national scope of the problem. These
    limitations hinder the development of evidence-based policies aimed at reducing the financial
    burden of stroke on households. To address this gap, this study leverages data from the National
    Sample Survey Office (NSSO) 75th round, which provides nationally representative, household-
    level data on healthcare expenditures.

    The primary objective of this study is to quantify the economic burden of stroke in India and
    analyze the socio-demographic and economic determinants of this burden using both statistical
    and machine learning approaches. This main objective is broken into three sub-objectives:

    1. Analyzing out-of-pocket expenditure and evaluating the prevalence of catastrophic health
    expenditure (CHE), defined as healthcare costs that exceed a significant proportion of household
    consumption, potentially driving families into financial hardship.

    2. Identifying key socio-demographic and economic factors contributing to the economic burden
    of stroke using logistic regression, a traditional statistical approach that provides
    interpretability and statistical rigor in understanding the relationships between variables.

    3. Applying machine learning techniques, including Support Vector Machines (SVM), Random Forest,
    and XGBoost, to predict the determinants of stroke-related healthcare expenditure. These models
    are rigorously evaluated to identify the best-performing approach, with XGBoost emerging as the
    top model.

    The study's methodology ensures a comprehensive analysis by leveraging the interpretability of
    traditional statistical methods and the predictive power of advanced machine learning techniques.
    While logistic regression excels in its ability to explain relationships between variables,
    machine learning captures complex patterns and interactions in the data that might be missed by
    conventional methods. This dual analysis provides a nuanced understanding of the economic
    determinants of stroke care in India.
    """)

# Background Section
elif section == "Background":
    st.header("Background")


    # Sub-sections for Background
    with st.expander("1. Brief Details of Stroke"):
	    st.write("""
	    Stroke ranks among the most severe health emergencies and stands as a primary source of death
	    and disability worldwide. This condition emerges when brain tissue loses its blood supply,
	    depriving neurons of the nutrients and oxygen they need to survive. Quick medical response is
	    essential, as any delay allows brain tissue to deteriorate, often beyond recovery. These precious
	    minutes can mean the difference between recovery and permanent disability, as brain cells begin
	    dying rapidly when deprived of oxygen.

	    Medical science identifies three distinct varieties of stroke: ischemic, hemorrhagic, and transient
	    ischemic attacks (TIAs). Roughly 87% of stroke incidents fall into the ischemic category. These
	    occur when debris or blood clots seal off vital brain arteries, stopping blood flow. Many ischemic
	    strokes develop due to atherosclerosis, where vessels gradually narrow as fatty substances collect
	    on their inner walls, creating ideal conditions for clots to form. The buildup process can take
	    years, often accelerated by factors like high cholesterol, smoking, and poor dietary habits.

	    Hemorrhagic strokes present differently – they strike when brain vessels tear open, allowing blood
	    to spill into surrounding tissue. These ruptures often stem from chronic hypertension, head trauma,
	    or weakened vessel walls. Uncontrolled blood pressure poses a particular risk, silently damaging
	    vessel walls until they can no longer withstand the pressure.

	    The third category, TIAs or "mini-strokes," involve brief blood flow disruptions. While their
	    effects typically resolve within hours leaving no lasting harm, TIAs signal serious danger – they
	    often precede more devastating strokes. Medical experts consider TIAs as crucial warning signs
	    that require immediate medical attention and lifestyle modifications.

	    The aftermath of stroke touches every aspect of a person's functioning. Many survivors find
	    themselves dealing with muscle weakness or complete paralysis, typically affecting one half of
	    their body. Their mental capabilities may decline, compromising everything from speech to
	    rational thinking. Memory issues can range from mild forgetfulness to severe impairment, while
	    language difficulties might include trouble speaking, reading, or understanding others.

	    The emotional toll proves equally severe, as survivors battle depression, anxiety, and deep
	    frustration while adapting to their changed circumstances. Basic functions that most take for
	    granted – speaking clearly, eating safely, managing bathroom needs – may require extensive
	    rehabilitation or permanent assistance. This sudden loss of independence often strains family
	    relationships and can lead to social isolation.
	    """)

    with st.expander("2. Economic Burden of Stroke"):
        st.write("""
        The financial shockwaves of stroke reverberate through society, crushing household savings and straining healthcare systems globally. A key concern lies in out-of-pocket expenditure – money that flows directly from family accounts to cover medical needs.(19,20) These personal payments often consume substantial portions of household income, particularly in regions lacking robust insurance coverage or government support. Understanding the complete financial picture requires examining both immediate healthcare charges and long-term economic consequences.
        """)
        
        st.markdown("#### 2.1 Direct Costs")
        st.write("""
        The upfront price tag of stroke care hits families with multiple expenses. First comes
        hospitalization, where costs spiral quickly as patients need emergency response teams,
        sophisticated brain imaging, and specialized stroke unit care.(21–23) Many cases demand complex surgical interventions to remove clots or repair damaged vessels, each procedure adding to mounting bills. Next, medication costs create ongoing strain – patients may need potent clot-busting drugs in the acute phase, followed by long-term prescriptions for blood thinners, blood pressure control, or cholesterol management. (21–23) These essential medicines drain family resources, especially where prescription coverage proves limited. Finally, rehabilitation expenses stretch over months or years. (21–23) Rebuilding strength and skills demands regular sessions with physical therapists, occupational specialists, and speech experts. (21–23) When public health systems can’t provide these services, families face steep private care costs, watching their savings dwindle with each appointment.
        
        """)

        st.markdown("#### 2.2 Indirect Costs")
        st.write("""
        Beyond obvious medical expenses lie hidden but equally devastating financial impacts. Lost
        productivity tops this list, as stroke frequently forces survivors to abandon careers temporarily or
        permanently. (21–23) This career disruption hits especially hard when the patient served as the
        primary breadwinner, leaving families scrambling to replace lost income. At a national level, these individual losses multiply into billions in reduced economic output as skilled workers step away from their roles. Equally significant is the caregiver burden, where family members often sacrifice their own earning potential to provide essential daily support. (21–23) These informal caregivers frequently reduce work hours or leave jobs entirely, creating additional household income loss. While harder to quantify, the physical and emotional toll on family caregivers carries its own economic weight.

        """)

        st.markdown("#### 2.3 Regional Economic Disparities")
        st.write("""
        The financial aftermath of stroke reveals stark contrasts between nations at different economic
        levels. Wealthy countries typically protect their citizens through comprehensive healthcare
        coverage and government assistance.(24) Nations across North America and Europe often provide substantial public funding for stroke treatment, though even these robust systems struggle with mounting costs for long-term care and lost productivity. In contrast, developing regions face far steeper challenges. Countries like India, where many lack access to public healthcare or insurance coverage, see families crushed under overwhelming medical bills. These expenses often consume dangerous portions of household income, pushing many into poverty.(25) Limited access to rehabilitation services and community support programs in these regions amplifies both the financial strain and social disruption for affected families.

        """)

    with st.expander("3. Data Gaps in the Indian Context"):
        st.write("""
        Understanding the true impact of stroke across India remains a significant challenge due to
        substantial gaps in data collection and analysis. The absence of comprehensive, national-level
        stroke data has created a fragmented picture that impedes our ability to quantify the full scope of stroke’s impact on public health and economic resources. (3,5–7) Current research efforts are
        hampered by reliance on isolated regional studies that, while valuable for local insights, fail to
        provide the broader perspective needed for nationwide analysis.

        The lack of systematic data collection mechanisms at the national level creates several critical
        challenges for researchers and analysts. Without standardized reporting protocols across healthcare facilities, the available data varies significantly in quality, completeness, and methodology. This inconsistency makes it difficult to aggregate and compare data across different regions, leading to potential biases in our understanding of stroke patterns and outcomes. Additionally, the absence of unified data collection systems means that many stroke cases, particularly in rural and underserved areas, may go undocumented or be inadequately reported.

        Regional variations in healthcare infrastructure and reporting capabilities further compound these data gaps. Urban centers typically maintain more comprehensive records due to better resources and technological capabilities, while rural areas often lack basic data collection systems. This disparity creates an uneven representation in available stroke data, potentially skewing our understanding of stroke’s impact across different geographical regions and population segments. The resulting data landscape presents an incomplete picture that may not accurately reflect the true distribution of stroke cases and outcomes across India’s diverse population.

        These data gaps particularly affect our ability to understand stroke patterns in vulnerable
        populations. Communities with limited access to healthcare facilities are often underrepresented
        in existing datasets, creating blind spots in our understanding of stroke’s impact on these groups. The lack of comprehensive data also makes it difficult to identify and address disparities in stroke care and outcomes across different socioeconomic groups, potentially perpetuating existing healthcare inequities. 

        The National Sample Survey Office ”NSSO’ emerges as a valuable resource for addressing these data gaps through its large-scale, systematic data collection efforts. NSSO surveys provide a structured approach to gathering health-related information across diverse populations and geographical regions. (26)These surveys, while not specifically focused on stroke, capture important health indicators and healthcare utilization patterns that can provide insights into stroke’s impact across different population segments.(26)

        The NSSO’s methodology offers several advantages for studying stroke patterns. Its sampling
        framework ensures representation from various socioeconomic groups and geographical regions, providing a more balanced view than hospital-based studies alone.(19) Additionally, the
        standardized data collection protocols used in NSSO surveys ensure consistency in the information gathered, making it more reliable for comparative analysis.

        Researchers can leverage NSSO datasets to examine various aspects of stroke’s impact. The
        surveys capture information about healthcare expenditure, treatment-seeking behavior, and access to medical facilities, all of which are crucial for understanding the burden of stroke across different population groups. By analyzing these datasets, researchers can identify patterns in healthcare utilization, estimate the economic impact of stroke on households, and examine regional variations in access to stroke care.

        However, while NSSO data provides valuable insights, it has significant limitations in fully
        capturing stroke’s impact across India’s diverse population. The periodic nature of NSSO surveys means they may miss short-term changes in stroke patterns and healthcare delivery. Furthermore, the surveys’ broad focus on general health indicators means they may not capture specific details about stroke cases that would be valuable for in-depth analysis.

        The limitations of NSSO data become particularly apparent when trying to understand regional
        variations in stroke care and outcomes. India’s diverse healthcare landscape, with significant
        differences in infrastructure and service delivery across regions, requires more detailed, location- specific data than NSSO surveys can provide. The surveys may not fully capture the nuances of local healthcare systems and cultural factors that influence stroke outcomes in different communities.

        Additionally, NSSO data may not adequately represent certain population segments, particularly
        those in remote or underserved areas. The surveys’ sampling methodology, while robust, may not reach the most marginalized communities, where stroke burden and healthcare access challenges might be most severe. This limitation creates gaps in our understanding of stroke’s impact on vulnerable populations. 

        The economic analysis of stroke burden using NSSO data also faces limitations. While the surveys collect information about healthcare expenditure, they may not capture indirect costs such as lost productivity, long-term care expenses, and the economic impact on caregivers. These missing elements make it difficult to estimate the true economic burden of stroke on families and communities.

        To address these limitations, researchers need to complement NSSO data with other sources of
        information. This might include hospital records, community-based surveys, and targeted studies of specific populations or regions. The integration of multiple data sources could provide a more comprehensive understanding of stroke’s impact across different segments of India’s population.

        Moving forward, there is a clear need for more systematic and comprehensive data collection
        efforts focused specifically on stroke. While NSSO data provides a valuable foundation,
        developing dedicated stroke registries and surveillance systems would help fill existing data gaps. Such systems should be designed to capture both broad patterns and local variations in stroke incidence, treatment, and outcomes.

        The path to better understanding stroke’s impact in India requires a multi-faceted approach to data collection and analysis. While leveraging existing resources like NSSO datasets is crucial, acknowledging their limitations helps identify areas where additional data collection efforts are needed. Only through a combination of national-level surveys and targeted regional studies can we develop a truly comprehensive understanding of stroke’s impact across India’s diverse population.

        """)

    with st.expander("4. Traditional Statistical Model: Logistic Regression"):
        st.write("""In predicting healthcare outcomes such as Catastrophic Health Expenditure (CHE), logistic
        regression stands as a cornerstone analytical tool. This statistical model bridges the gap between
        multiple input variables and binary outcomes by employing a sophisticated yet interpretable
	mathematical approach.(27)

	At its heart, logistic regression transforms the complex relationships between patient
	characteristics and CHE risk into a probability framework. (27,28)Rather than attempting direct
	linear prediction, the model employs the logit function – a mathematical innovation that constrains
	predictions between 0 and 1, making it perfect for yes-no outcomes. The model constructs its
	predictions using the equation:
	   
	log(p/(1-p)) = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
	   
	In this formula, 'p' represents the likelihood of experiencing CHE, while the beta coefficients (β)
	reveal how strongly each factor influences this probability. The expression p/(1-p) represents the
	odds of CHE occurrence, and taking its logarithm produces the log-odds, allowing for linear
	modeling of inherently non-linear probability relationships. (27,28)

	Healthcare researchers particularly value this model's interpretability through odds ratios. By
        exponentiating a coefficient (exp(β)), analysts can directly quantify how changes in patient
        characteristics affect CHE risk. For instance, if age shows a coefficient of 0.7, its odds ratio of
	2.01 (exp(0.7)) indicates that each unit increase in age roughly doubles the odds of experiencing
	CHE, assuming other factors remain constant.

	The model also excels in handling multiple predictor variables simultaneously, adjusting for
	confounding effects that often complicate healthcare analysis.(29) When examining stroke
	patients, for example, it can simultaneously consider age, income level, stroke severity, and
	comorbidities, providing adjusted estimates of each factor's independent impact on CHE risk.

	Despite its apparent simplicity, logistic regression offers robust tools for model validation.
	Researchers can assess goodness-of-fit through metrics like the Hosmer-Lemeshow test, while
	ROC curves help evaluate predictive performance. The model also provides standard errors for
	each coefficient, enabling statistical significance testing and confidence interval construction –
	crucial features for healthcare research where uncertainty quantification matters.

	These mathematical underpinnings make logistic regression an invaluable tool in healthcare
	analytics, offering a balanced combination of statistical rigor and practical interpretability. While
	newer machine learning methods may offer greater predictive power, logistic regression's
	transparent framework continues to serve as both a reliable analytical tool and a foundation for
	understanding more complex approaches.""")

    with st.expander("5. Relevance of Machine Learning in Healthcare"):
        st.write("""
   	The medical field has experienced a revolutionary shift through the adoption of machine learning
   	(ML) technologies. As healthcare records expand in both size and complexity, traditional analysis
   	methods fall short. (30,31)ML excels by uncovering subtle data patterns and making predictions
	without needing specific programming for each case. This proves especially valuable in managing
        healthcare costs, where spotting potential problems early can improve both medical outcomes and
        financial efficiency. The explosion of medical data, paired with increasingly powerful computing
	systems, has made ML essential for healthcare professionals seeking to optimize their resources
	and enhance patient services.

	When patients face medical bills that exceed their financial capacity, creating severe economic
	hardship, experts term this Catastrophic Health Expenditure (CHE). This scenario frequently
	affects stroke survivors, who often face both immediate treatment costs and ongoing care expenses.
	In developing healthcare environments like India's, where many lack adequate financial
	protection, identifying patients at risk of CHE becomes crucial. By predicting and preventing such
	financial crises, healthcare systems can better serve both individual patients and the broader
	community.

	ML's core strength lies in its ability to learn from experience rather than following rigid
	programmed rules. This approach perfectly suits healthcare's complex nature, where countless
	variables interact to influence patient outcomes. For stroke cases, these factors span clinical
	measurements, personal background information, and economic indicators – all affecting financial
	results. Such intricate relationships exceed traditional analysis capabilities, highlighting why
	advanced ML techniques prove necessary.

	Three fundamental components drive ML systems: the algorithmic foundation, data sources, and
	learning processes.(32) Algorithms provide the analytical framework, while diverse healthcare
	information – from medical histories to billing records – feeds the analysis. The learning aspect
	involves continuous model refinement to enhance prediction accuracy. Creating ML models
	follows a systematic approach, starting with training on existing data. For predicting CHE in stroke
	cases, this means analyzing records containing patient details, treatment information, and known
	financial outcomes.

        Healthcare data poses unique challenges for ML implementation. Information often comes
        fragmented across multiple sources, varying in quality and format. While test results provide clear
        numbers, clinical notes often contain unstructured text. Financial records may show
        inconsistencies between different healthcare providers. Successfully combining these diverse data
        types demands sophisticated processing methods and careful attention to data quality.

        ML approaches typically fall into three categories: supervised, unsupervised, and reinforcement
        learning. Healthcare finance prediction primarily uses supervised learning, which works with
        known outcomes. This method trains systems using records where CHE results are documented,
        helping models understand connections between patient characteristics and financial outcomes.
        These learned patterns then help assess CHE risk in new patients.

        The mathematical principles behind ML explain its effectiveness In healthcare applications. Linear
        algebra provides the foundation for handling complex patient information. Each patient's record
        becomes a point in multi-dimensional space, where dimensions represent various health markers,
        demographic details, and financial factors. Matrix operations allow efficient analysis across
        thousands of records simultaneously.

        Probability theory and statistics play crucial roles in healthcare ML applications. These tools help
        models manage medical data uncertainty and make reliable predictions. Statistical distributions
        characterize patient populations and risk factors, while inference methods evaluate which variables
        best predict outcomes like CHE. Bayesian approaches allow models to update predictions as new
        information arrives, proving particularly valuable in dynamic healthcare settings.
         """)        

        st.markdown("#### 5.1 Boruta Algorithm – A Novel Feature Selection Approach")
        st.write("""
        In healthcare ML applications, selecting relevant features for analysis presents a unique challenge. The Boruta algorithm offers an innovative solution, creating “shadow” copies of variables to determine which factors truly matter.(33) This method works systematically, first generating randomized copies of all variables as benchmarks. If real variables prove more significant than their randomized versions, they likely carry meaningful information. The algorithm employs Random Forest classification to measure variable importance, comparing original features against their shadows.(33)

        This approach particularly suits healthcare because it identifies all potentially relevant factors
        rather than selecting a predetermined number. Through multiple iterations, the algorithm classifies features as definitively important, potentially significant, or irrelevant. Combining Boruta with Random Forests offers additional benefits, as Random Forests effectively handle complex relationships between variables while providing built-in importance measurements. This creates a robust system for identifying truly significant predictors in complex medical scenarios, ensuring no critical medical indicators get overlooked in the analysis process.

        """)

        st.markdown("#### 5.2 Machine Learning Models for Healthcare Prediction")
        st.write("""
        """)
        
        st.markdown("##### 5.2.1 Random Forest")
        st.write("""
        Harnessing Collective Intelligence Random Forest models build upon the concept of decision
        trees, which create hierarchical rules for prediction. To understand Random Forests, we must first grasp decision trees: imagine a flowchart where each node splits patients based on specific criteria (e.g., “Age > 60?” or “Blood pressure > 140/90?”). These splits continue until reaching leaf nodes containing final predictions.

        Random Forests create multiple trees (often hundreds or thousands) using random subsets of data and features.(34) This process, called bagging (Bootstrap Aggregating), ensures each tree offers a unique perspective on the prediction problem. For example, one tree might emphasize age and income, while another focuses on clinical severity and insurance status. The forest combines these diverse viewpoints through majority voting for classification or averaging for probability estimates.

        Key advantages include:
        • Built-in handling of mixed data types common in healthcare
        • Natural capture of non-linear relationships between variables
        • Robust feature importance measures through mean decrease in impurity
        • Resistance to overfitting through ensemble averaging

        """)
        
        st.markdown("##### 5.2.2 Support Vector Machine (SVM)")
        st.write("""
        Finding Critical Boundaries SVMs approach prediction by constructing optimal hyperplanes –
        mathematical boundaries that separate different outcome groups in multi-dimensional
        space.(34,35) In its simplest form, imagine plotting patients on a graph where axes represent
        different characteristics (age, income, clinical scores). The SVM finds the best dividing line (in
        higher dimensions, a hyperplane) that maximizes the margin between CHE and non-CHE cases.The mathematical magic of SVMs lies in the kernel trick. When data isn't linearly separable in original space, kernel functions transform it into higher dimensions where separation becomes possible. Common kernels include:

        • Linear: K(x,y) = x^T y

        • Radial Basis Function (RBF): K(x,y) = exp(-γ||x-y||²)

        • Polynomial: K(x,y) = (γx^T y + r)^d

        These transformations allow SVMs to uncover complex patterns in medical data while maintaining computational efficiency. The model’s margin maximization principle helps prevent overfitting, making predictions more reliable on new patients.

        """)
        
        st.markdown("##### 5.2.3 XGBoost")
        st.write("""
        Advanced Gradient Boosting XGBoost represents a sophisticated evolution of gradient boosting,
        building strong predictive models through sequential improvement. Unlike Random Forests,
        which build trees independently, XGBoost creates each new tree to specifically correct errors made by previous trees.(34,35)

        The algorithm works by:
        1. Starting with a simple initial prediction
        2. Calculating prediction errors (residuals)
        3. Building a new tree to predict these residuals
        4. Adding this tree’s predictions (multiplied by a learning rate) to the current model
        5. Repeating steps 2-4 until reaching a specified number of trees or achieving desired accuracy

        Key innovations in XGBoost include:
        • Regularization terms to prevent overfitting
        • Efficient handling of sparse data and missing values
        • System optimization for parallel processing
        • Built-in tree pruning during construction

        These technical features enable XGBoost to achieve high prediction accuracy while maintaining
        computational efficiency. The model particularly excels with imbalanced datasets – common in
        healthcare where adverse events like CHE might affect a minority of patients.

        Each model brings unique mathematical strengths to healthcare prediction. Logistic regression
        offers clear interpretation through odds ratios, Random Forests provide robust ensemble
        predictions, SVMs excel at finding complex boundaries, and XGBoost pushes predictive accuracy through iterative improvement. Understanding these technical foundations helps healthcare researchers select and combine models effectively for optimal prediction of patient outcomes.

        """)

    with st.expander("6. Understanding SHAP Analysis: From Game Theory to Machine Learning Insights"):
        st.write("""
        Picture a poker tournament where players form different alliances throughout the game. How do we fairly determine each player’s true contribution to winning when their impact varies based on who they team up with? This was the puzzle that captivated Nobel laureate Lloyd Shapley, leading to a revolutionary concept in game theory that would later transform how we understand machine learning models.

        Like skilled casino analysts tracking player performance, SHAP (Shapley Additive exPlanations)
        breaks down complex interactions to reveal true contributions.(36) But instead of evaluating poker players, it scrutinizes how different features in a model work together to generate predictions.

        The genius of Shapley’s approach lies in its systematic evaluation of every possible combination. In poker, a player might perform brilliantly with one team but struggle with another. Similarly, in healthcare prediction, a patient’s age might strongly indicate risk when combined with certain factors but show minimal impact with others. SHAP captures these nuanced interactions by examining each feature’s contribution across all possible feature combinations.(36)

        Think of SHAP values like a detailed financial audit of each feature’s contribution. Just as auditors track both deposits and withdrawals, SHAP shows how each characteristic pushes predictions up or down from the average. When predicting catastrophic health expenditure, for instance, SHAPmight reveal that high blood pressure adds 15% to the risk score, while good insurance coverage subtracts 20%.

        The “additive” nature of SHAP mirrors double-entry bookkeeping – everything must balance
        perfectly. The sum of all SHAP values for a prediction exactly equals the difference between that
        prediction and the model’s average output. This mathematical precision ensures accountability in understanding model decisions.

        Three key principles govern SHAP analysis:
	• Fair Accounting: Just as every penny must be accounted for in an audit, SHAP values sum
	to the exact prediction difference from baseline
	•Zero Impact = Zero Credit: Features that don’t affect predictions receive zero SHAP values,
	like inactive accounts in accounting
	•Consistent Recognition: If a feature’s contribution grows stronger in the model, its SHAP
	value increases accordingly

	SHAP provides several visualization tools that transform complex calculations into clear insights:
	• Impact Summaries: Like executive dashboards showing each department’s contribution
	• Contribution Flows: Displaying how features cascade to build final predictions
	• Interaction Maps: Revealing how features influence each other, similar to analyzing
	synergies between business units
	•Step-by-Step Breakdowns: Tracing the path from baseline to final prediction 

	In healthcare settings, SHAP brings transparency to critical decisions. Medical professionals can
	see exactly how patient characteristics combine to generate risk assessments, building trust in
	model recommendations. For instance, when analyzing stroke-related financial risk, SHAP might uncover unexpected interactions between treatment choices and socioeconomic factors. 

	However, like any sophisticated analysis tool, SHAP has its challenges. The computational
	demands grow exponentially with feature count, similar to how auditing complexity increases with transaction volume. Modern implementations often use clever approximations to balance accuracy with efficiency. Additionally, interpreting SHAP values requires both technical understanding and domain expertise to avoid misreading the results.

	Despite these considerations, SHAP analysis stands as a masterpiece of analytical thinking,
	bridging theoretical elegance with practical necessity. By adapting game theory’s insights to
	machine learning interpretation, it provides healthcare researchers and practitioners with a
	powerful tool for understanding and validating model behavior, ultimately supporting better
	patient care decisions.

        """)

# Results Section
elif section == "Results":
    st.header("Results")
    result_section = st.selectbox(
        "Select Section", 
        [
            "1. Overview of the Study Design",
            "2. Exploratory Data Analysis (EDA)",
            "3. Objective 1 - OOP Expenditure & CHE",
            "4. Objective 2 - Socio-demographic Factors",
            "5. Objective 3 - Machine Learning Models"
        ]
    )

    if result_section == "1. Overview of the Study Design":
        st.subheader("Overview of the Study Design")
        st.write("""
        This study analyzed the economic burden of stroke using secondary data from the National Sample Survey Office (NSSO) 75 th round
        survey conducted between July 2017 and June 2018. The survey employed a stratified multistage sampling design and covered 113,822 households
        and 555,351 individuals across India. It focused on:

	• The nature of ailments requiring hospitalization across various demographics.

	• Detailed out-of-pocket expenditure (OOPE), including direct (e.g., medical fees, diagnostic
	tests) and indirect costs (e.g., food, lodging, transportation).
	
	For this study, Usual Monthly Consumption Expenditure (UMCE) was converted to Usual
	Monthly Per-Capita Consumption Expenditure (UMPCE) to classify households into income
	quintiles. Annual household consumption expenditure was used as a proxy for ability to pay.
	Households with OOPE exceeding 10% of their annual expenditure were classified as
	experiencing catastrophic health expenditure (CHE). The dataset used for analysis included 1,293 individuals
        hospitalized due to strokes, extracted from a total of 91,449 hospitalization episodes. 

	Data was initially stored in 13 SPSS datasets, converted to CSV format, and analyzed using Python. Weighted averages
        were used to calculate hospitalization rates, and statistical techniques such as Kruskal-Wallis and Chi-square tests
        were applied to compare medians and proportions. Logistic regression assessed socio-economic factors influencing CHE, with sensitivity analyses
	conducted at varying thresholds for defining catastrophic spending (5%, 10%, and 20%).

        """)

    elif result_section == "2. Exploratory Data Analysis (EDA)":
        st.subheader("Exploratory Data Analysis (EDA)")
        st.markdown("####Socio-Demographic and Economic Characteristics")
        st.write("""
        The dataset revealed diverse characteristics of hospitalized stroke patients, segmented by sex, age,
        education, place of residence, and income quintiles (Table 01). Notably:
        
        •Older age groups showed a higher prevalence of stroke, emphasizing age as a key
        demographic factor.
        
        •Rural populations exhibited higher stroke rates, possibly reflecting disparities in healthcare
         access and preventive care.

        •Income quintiles highlighted socioeconomic inequalities, with lower-income groups facing
         higher relative economic burdens despite lower hospitalization rates.
        """)

        st.image("Socio-demographic and economic characteristics of patients who were hospitalized due to Stroke, India, 2017– 18.png",
                 caption="Table 01: Socio-demographic and economic characteristics of patients who were hospitalized due to Stroke, India, 2017– 18")
    elif result_section == "3. Objective 1 - OOP Expenditure & CHE":
        st.subheader("Objective 1 - Analyze the total out-of-pocket (OOP) expenditure and evaluate the prevalence of catastrophic health expenditure (CHE)")
        st.write("""
        [Insert content for Objective 1]
        """)
        
        # Display images for Objective 1
        st.image("Distribution of Out-of-Pocket (OOP) Expenditure (Including Free Cases).png", 
                 caption="Figure 01: Distribution of Out-of-Pocket (OOP) Expenditure (Including Free Cases)")
        st.image("Overlayed Distribution of Out-of-Pocket (OOP) Expenditure (Filtered: OOP > 0).png", 
                 caption="Figure 02: Overlayed Distribution of Out-of-Pocket (OOP) Expenditure (Filtered: OOP > 0)")
        st.image("Log-transformed Distribution of Out-of-Pocket (OOP) Expenditure (After Capping).png", 
                 caption="Figure 03: Log-transformed Distribution of Out-of-Pocket (OOP) Expenditure (After Capping)")
        st.image("Adjusted Distribution of Out-of-Pocket (OOP) Expenditure (After Capping).png", 
                 caption="Figure 04: Adjusted Distribution of Out-of-Pocket (OOP) Expenditure (After Capping)")
        st.image("Box Plot of OOP Expenditure by Income Quintile (After Capping).png", 
                 caption="Figure 05: Box Plot of OOP Expenditure by Income Quintile (After Capping)")
        st.image("Sensitivity Analysis.png", 
                 caption="Figure 06: Sensitivity Analysis")

    elif result_section == "4. Objective 2 - Socio-demographic Factors":
        st.subheader("Objective 2 - Identify key socio-demographic and economic factors contributing to the economic burden of stroke")
        st.write("""
        [Insert content for Objective 2]
        """)
        
        # Display images for Objective 2
        st.image("Logistic Regression results.png", 
                 caption="Figure 07: Logistic Regression results")
        st.image("Confusion Matrix for Logistic Regression.png", 
                 caption="Figure 08: Confusion Matrix for Logistic Regression")

    elif result_section == "5. Objective 3 - Machine Learning Models":
        st.subheader("Objective 3 - Fit machine learning models and compare their accuracy with statistical models")
        st.write("""
        [Insert content for Objective 3]
        """)
        
        # Display images for Objective 3
        st.image("(a): ROC Curve comparison of models; (b) Precision-Recall Curve Comparison of Models.png", 
                 caption="Figure 09: (a): ROC Curve comparison of models; (b) Precision-Recall Curve Comparison of Models")
        st.image("Confusion matrices of all 4 models used.png", 
                 caption="Figure 10: Confusion matrices of all 4 models used")
        st.image("Beeswarm plot (SHAP Analysis) reveals not just the relative importance of features, but their actual relationships with the predicted outcome.png", 
                 caption="Figure 11: Beeswarm plot (SHAP Analysis)")
        st.image("Bar Plot showing feature importance (SHAP Analysis).png", 
                 caption="Figure 12: Bar Plot showing feature importance (SHAP Analysis)")
        st.image("TABLE2.png", 
                 caption="Table 02: Comprehensive comparison of XGBoost and logistic regression")

# Summary and Conclusions Section
elif section == "Summary and Conclusions":
    st.header("Summary and Conclusions")
    st.write("""
    This study provided a comprehensive analysis of the economic burden of stroke in India, with a
    particular focus on catastrophic health expenditure (CHE) and its contributing factors. The findings revealed that 35.96% of households faced CHE at a 5% threshold, 21.50% at a 10% threshold, and 11.45% at a 20% threshold, underscoring the substantial financial strain imposed on families.

    Income disparities were a significant driver of out-of-pocket (OOP) expenditure, with lower-
    income groups bearing disproportionately higher financial burdens.
    The statistical logistic regression model identified key predictors of CHE, including OOP
    expenditure, household size, monthly consumer expenditure, and annual household consumption expenditure. These factors provided critical insights into the socio-economic determinants of financial vulnerability. In contrast, machine learning approaches, particularly XGBoost, demonstrated superior predictive performance, achieving 95.14% accuracy, 89.96% precision, and AUC metrics of 0.99 (ROC) and 0.95 (PR). The XGBoost model’s robust performance across various metrics, combined with its ability to handle non-linear relationships and interactions, underscored its utility in identifying high-risk households.

    Machine learning models, with their enhanced predictive accuracy and ability to uncover complex patterns, complemented the traditional statistical approaches by offering actionable insights.

    Together, these methods provide a robust framework for understanding and addressing the
    economic burden of stroke. The study’s findings emphasize the need for targeted policy
    interventions to alleviate financial hardship and promote equitable access to healthcare. By
    integrating advanced analytics with traditional methods, this research contributes to the
    development of effective strategies for reducing the economic impact of stroke and fostering a
    more inclusive healthcare system.

    """)
 
