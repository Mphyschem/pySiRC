from PIL import Image

class Texts:
    def __init__(self):
        pass

    def text1(self):        
        TEXT1 = """
        <body style='text-align: justify; color: black;'>
        <p> This application consists of the automatic prediction of reaction rate constant of the radical-based oxidation process
        of aqueous and atmospheric organic contaminants based on Machine Learning models using molecular fingerprints.
        It is only necessary to inform the SMILES or CAS Number format of a specific molecule.
        The models present in this work were built using <a href="https://scikit-learn.org/stable/"target="_blank">scikit-learn</a> and <a href="https://xgboost.readthedocs.io/en/latest/python/python_api.html"target="_blank">XGBoost</a> packages.
        The predict values can be confronted with experimental values available in our work or <a href="https://kinetics.nist.gov/solution/"target="_blank">kinetics.nist.gov/solution</a>. 
        </p>
        </body>         
        """

        return TEXT1
    
    def text1_2(self):
        TEX1_2 = """
        ###  WorkFlow
        <body style='text-align: justify; color: black;'>
        <p>
        The routine follows guidelines of the Organization for Economic Cooperation and Development (OECD). 
        Data from the literature, structured and with molecular names converted by SMILES provide molecular fingerprints (MF) – these are the independent variables, 
        while rate constants are the dependent variables of our model developed implemented in three machine learning algorithms – XGboost (XBG), Random Forest (RF), 
        and Neural Network (NN). Validation of the model's performance involved: applicability domain (AD), mechanistic interpretation with the SHAP method, internal and 
        external validation (IEV), and randomization of the dependent variable (Y RAND). Final step is a user-friendly web application.
        </p>
        </body>
        """

        return TEX1_2
    
    
    def text1_3(self):
        TEX1_3 = """
        <body style='text-align: justify; color: black;'>
        <h2 style='text-align: justify; color: black;'>Pictorial View - How to use pySiRC platform</h2>
        <p>In the flowchart below, we show step by step how to use our platform to predict the required kinetic parameters.</p>
        </body>
        <br>
        """
        
        return TEX1_3
    
    def text1_4(self):
        TEXT1_4 = """
        <body style='text-align: justify; color: black;'>
        <h1 style='text-align: justify; color: black;'>pySiRC website</h1>
        <p> pySiRC - a program that permits compilation of kinetic parameters in aqueous and atmospheric environment.
        <h2 style='text-align: justify; color: black;'>Citation</h2>
        Please cite the following reference when publishing results obtained with pySiRC:<br>
        (i) Sanches-Neto, F. O., Dias-Silva, J. R., Keng Queiroz Junior, L. H., & Carvalho-Silva, V. H. (2021). “pySiRC”: Machine Learning Combined with Molecular Fingerprints to Predict the Reaction Rate Constant of the Radical-Based Oxidation Processes of Aqueous Organic Contaminants. Environmental Science & Technology, 55(18), 12437-12448, <a href="https://doi.org/10.1021/acs.est.1c04326"target="_blank">https://doi.org/10.1021/acs.est.1c04326</a><br>
        (ii) Sanches-Neto, F. O., Dias-Silva, J. R., de Oliveira, V.M,  Aquilanti, V., & Carvalho-Silva, V. H. (2022). Evaluating and elucidating the reactivity of OH radicals with atmospheric organic pollutants: Reaction kinetics and mechanisms by machine learning. Atmospheric Environment, 119019, <a href="https://doi.org/10.1016/j.atmosenv.2022.119019"target="_blank">https://doi.org/10.1016/j.atmosenv.2022.119019</a>
        </p>
        </body>
        """
        return TEXT1_4

    
    def text2(self):
        TEXT2 = """
        This web platform is free and open source and you are very welcome to contribute.
        This Application has GNU GPL license. All source code can be accessed [here](https://github.com/Mphyschem/pySiRC).
        """

        return TEXT2
    
    def text3(self):
        TEXT3 = """
        <body style='text-align: justify; color: black;'>
        <h2 style='text-align: justify; color: black;'>About</h2>
        <p>
        pySiRC was designed to facilitate the automatic researchers to prediction and analyze of reaction rate constants
        using Machine Learning models, since the theoretical calculation and experimental measures of these kinetic
        parameters can be extremely challenging. The tools are designed to be quick and simple users with few clicks
        can make the prediction. The tools are rigorous enough to have applications in academic research.
        All the source code for this application and the steps for local installation are at <a href="https://github.com/Mphyschem/pySiRC"target="_blank">GitHub</a>.
        You are free to use, change and distribute this application under the GNU GPL license. The maintainers of this
        package so far are: Flávio Olimpio Sanches Neto (flavio_olimpio@outlook.com), Jefferson Richard Dias (jrichardquimica@gmail.com),
        and Vitor Mendes (vitor.mendes.ag@gmail.com).

        <h2 style='text-align: justify; color: black;'>Supporters</h2>
        </p>
        </body>
        """

        return TEXT3
