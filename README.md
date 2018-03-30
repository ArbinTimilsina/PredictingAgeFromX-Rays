# Predicting Age FromX-Rays

# Goal
Develop an algorithm to determine the age of a child by utilizing pediatric hand radiographs (x-rays of hands). 

# Dataset
The dataset was originally published on [CloudApp](http://rsnachallenges.cloudapp.net/competitions/4) as an RSNA challenge. However, for this project, it was downloaded from [Kaggle](https://www.kaggle.com/kmader/rsna-bone-age/data).
### Original Dataset Acknowledgements
The Radiological Society of North America (RSNA) Radiology Informatics Committee (RIC) Pediatric Bone Age Machine Learning Challenge Organizing Committee: 
* Kathy Andriole, Massachusetts General Hospital
* Brad Erickson, Mayo Clinic
* Adam Flanders, Thomas Jefferson University
* Safwan Halabi, Stanford University
* Jayashree Kalpathy-Cramer, Massachusetts General Hospital
* Marc Kohli, University of California - San Francisco
* Luciano Prevedello, The Ohio State University

Data sets used in the Pediatric Bone Age Challenge have been contributed by Stanford University, the University of Colorado and the University of California - Los Angeles. 

The MedICI platform (built CodaLab) used for the challenge is provided by Jayashree Kalpathy-Cramer, supported through NIH grants (U24CA180927) and a contract from Leidos.

# Instructions to run this project on the AWS 
## Instance settings
* AWS Marketplace: Deep Learning AMI with Source Code (CUDA 8, Ubuntu)
* Instance type: p2.xlarge (Filter by: GPU compute)

### SSH into the AWS instance
```
ssh -i path/To/myKey.pem ubuntu@Public-DNS(IPv4)
```

#### Clone the repo
```
 git clone https://github.com/ArbinTimilsina/PredictingAgeFromX-Rays.git
 ```
 ```
 cd PredictingAgeFromX-Rays
```

#### Install the requirements
```
sudo python3 -m pip install -r Requirements/GPU-Requirements.txt
```

#### Switch Keras backend to TensorFlow
```
KERAS_BACKEND=tensorflow python -c "from keras import backend"
```

#### Download the dataset from kaggle; API credentials needs to be in the location ~/.kaggle/kaggle.json
```
scp -i path/to/key ~/.kaggle/kaggle.json ubuntu@Public-DNS(IPv4):~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```
```
pip install kaggle
kaggle datasets download -d kmader/rsna-bone-age -p .
tar -xvzf rsna-bone-age.tgz
mv
rm rsna-bone-age.tgz
```

####  Run the Jupyter notebook: First generate config file and then change the IP address config setting
```
jupyter notebook --generate-config
sed -ie "s/#c.NotebookApp.ip = 'localhost'/#c.NotebookApp.ip = '*'/g" ~/.jupyter/jupyter_notebook_config.py
jupyter notebook --ip=0.0.0.0 --no-browser
```
