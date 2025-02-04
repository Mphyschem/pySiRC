
<body style='text-align: justify; color: black;'>
<h1 style='text-align: justify; color: black;'>pySiRC</h1>
<p> This application consists of the automatic prediction of reaction rate constant of the radical-based oxidation process
of aqueous and atmospheric organic contaminants based on Machine Learning models using molecular fingerprints.
It is only necessary to inform the SMILES or CAS Number format of a specific molecule.
The models present in this work were built using <a href="https://scikit-learn.org/stable/"target="_blank">scikit-learn</a> and <a href="https://xgboost.readthedocs.ien/latest/python/python_api.html"target="_blank">XGBoost</a> packages.
The predict values can be confronted with experimental values available in our work or <a href="https://kinetics.nist.gov/solution/"target="_blank">kinetics.nist.gosolution</a>.
To access this application remotely use the link <a href="http://pysirc.com.br/"target="_blank">pysirc.com.br</a>. pySiRC was developed using the python language and has some dependencies.
</p>
</body>

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

<h2 style='text-align: justify; color: black;'>Citation</h2>
Please cite the following reference when publishing results obtained with pySiRC:<br>
(i) Sanches-Neto, F. O., Dias-Silva, J. R., Keng Queiroz Junior, L. H., & Carvalho-Silva, V. H. (2021). “pySiRC”: Machine Learning Combined with Molecular Fingerprintto Predict the Reaction Rate Constant of the Radical-Based Oxidation Processes of Aqueous Organic Contaminants. Environmental Science & Technology, 55(18), 12437-12448<a href="https://doi.org/10.1021/acs.est.1c04326"target="_blank">https://doi.org/10.1021/acs.est.1c04326</a><br>
(ii) Sanches-Neto, F. O., Dias-Silva, J. R., de Oliveira, V.M,  Aquilanti, V., & Carvalho-Silva, V. H. (2022). Evaluating and elucidating the reactivity of OH radicalwith atmospheric organic pollutants: Reaction kinetics and mechanisms by machine learning. Atmospheric Environment, 119019, <a href="https://doi.org/10.1016/j.atmosen2022.119019"target="_blank">https://doi.org/10.1016/j.atmosenv.2022.119019</a>
</p>
</body>

