Builded a [Django app](https://bms-370-215.science.uu.nl/database/) to detect, view, and compare phosphorylation sites in proteins.<br>

I have builded an data importer for protein-, phosphorylation-, and kinase data of multiple organisms. The importer uses python to download FTP files, converts the data to the desired database format using Python, and imports the data to a SQL database using Django.<br>

I also connected the data to a GUI for an user friendly experience. I have build a 'Google style' search page in which the user can search for a protein, protein features or phosphorylation sites. I have also added the option to add filters; to for example filter on organism. When a protein is selected, the GUI shows information about the protein, its phosphorylation sites and the kinases that caused the phosphorylation sites. Finally, the protein sequence can be compared with all other protein sequences in the database using the integrated bioinformatics tools 'HMMER'
