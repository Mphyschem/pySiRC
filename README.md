# pySiRC

pySiRC is a simple web application for predicting rate constant using machine learning models.
The models used are: XGBoost, Random Forest and MultiLayer Perceptron (Neural network). It is possible to make predictions for oxidation reactions with the radicals OH and SO4 with just a few clicks. To access this application remotely use the link [pysirc.com.br](http://pysirc.com.br/).
Another way to use this application is to install and run it locally. PySiRC was developed using the python language and has some dependencies.

### Dependencies
<ul>
<li><b>RDkit:</b> Draw molecules and convert smiles to fingerprints.</li>
<li><b>Numpy:</b> Create matrices and mathematical operations.</li>
<li><b>Cirpy:</b> Convert cas number to smiles.</li>
<li><b>Streamlit:</b> Python framework to creating dashboards.</li>
<li><b>Pandas:</b> Data manipulation.</li>
<li><b>Seaborn:</b> Plots based in matplotlib.</li>
<li><b>Scikit-learn:</b> Framework to perform ML models.</li>
<li><b>XGBoost:</b> Perform a XGBoost model.</li>
  
</ul>

## Installation to run locally

### Install dependencies via pip
The rdkit via pip (rdkit-pypi) is only available for linux (need glibc>=2.17) and macOS systems.
```
$ pip3 install streamlit numpy cirpy pandas seaborn scikit-learn XGBoost tqdm rdkit-pypi
```

### Install conda to get rdkit.
Conda version recommended [here](https://repo.anaconda.com/archive/Anaconda3-4.4.0-Linux-x86_64.sh)
```
$ chmod +x Anaconda3-4.4.0-Linux-x86_64.sh
$ ./Anaconda3-4.4.0-Linux-x86_64.sh
```
Installing rdkit from conda-forge:
```
$ conda install -c conda-forge rdkit
```
Install all dependencies packages:
```
$ pip install streamlit numpy cirpy pandas seaborn scikit-learn XGBoost tqdm
```

### Another way: install RDkit via ubuntu repository (Linux Environment)
```
$ sudo python3 apt install python3-rdkit
```
Install pip to set up all python dependencies
```
$ sudo python3 apt install python3-pip
```
Install all dependencies packages:
```
$ sudo pip3 install streamlit numpy cirpy pandas seaborn scikit-learn XGBoost tqdm
```

Download this repository, manually or via git:
```
$ git clone https://github.com/Mphyschem/pySiRC
```

## Run
Enter the pySiRC folder and run the command:
```
$ cd .../pySiRC
$ streamlit run pySiRC.py
```
That done, the application will open in the browser and the terminal will have the
local ip for access to all devices connected on the same network

## Citation
Please cite the following reference when publishing results obtained with pySiRC:

(i) Sanches-Neto, F. O., Dias-Silva, J. R., Keng Queiroz Junior, L. H., & Carvalho-Silva, V. H. (2021). “pySiRC”: Machine Learning Combined with Molecular Fingerprints to Predict the Reaction Rate Constant of the Radical-Based Oxidation Processes of Aqueous Organic Contaminants. Environmental Science & Technology, 55(18), 12437-12448, [https://doi.org/10.1021/acs.est.1c04326](https://doi.org/10.1021/acs.est.1c04326); 
(ii) Sanches-Neto, F. O., Dias-Silva, J. R., de Oliveira, V.M,  Aquilanti, V., & Carvalho-Silva, V. H. (2022). Evaluating and elucidating the reactivity of OH radicals with atmospheric organic pollutants: Reaction kinetics and mechanisms by machine learning. Atmospheric Environment, 119019,[https://doi.org/10.1016/j.atmosenv.2022.119019](https://doi.org/10.1016/j.atmosenv.2022.119019). 

