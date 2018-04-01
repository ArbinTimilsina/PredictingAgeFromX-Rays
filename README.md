# Predicting Age From X-Rays

## Goal
Develop an algorithm to determine the age of a child by utilizing x-rays of hands (pediatric hand radiographs).

## Dataset
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

## Instructions to run this project on the AWS 
### AWS instance settings
* AWS Marketplace: Deep Learning AMI with Source Code (CUDA 8, Ubuntu)
* Instance type: p2.xlarge (Filter by: GPU compute)
* Dataset is 9.3 GB- default size for p2.xlarge is 50 GB (which includes instant snapshot); so change the volume size to something larger

### SSH into the AWS instance
```
ssh -i path/To/myKey.pem ubuntu@Public-DNS(IPv4)
```

### Clone the repo
```
git clone https://github.com/ArbinTimilsina/PredictingAgeFromX-Rays.git
cd PredictingAgeFromX-Rays
```

### Install the requirements
```
sudo pip install --upgrade pip
not needed for the current AWS instance: sudo python3 -m pip install -r Requirements/GPU-Requirements.txt
```

### Switch Keras backend to TensorFlow
```
KERAS_BACKEND=tensorflow python -c "from keras import backend"
```

### Download the dataset from kaggle
```
sudo pip install kaggle
```

API credentials needs to be in the location ~/.kaggle/kaggle.json; so, **from a different terminal**
```
scp -i path/To/myKey.pem ~/.kaggle/kaggle.json ubuntu@Public-DNS(IPv4):~/.kaggle/kaggle.json
```

```
chmod 600 ~/.kaggle/kaggle.json
cd Input
kaggle datasets download -d kmader/rsna-bone-age -p .
unzip boneage-training-dataset.zip
mv boneage-training-dataset boneage-dataset
mv boneage-training-dataset.csv boneage-dataset.csv
rm *.zip boneage-test-dataset.csv
cd ..
```

### Install emacs
```
sudo apt install emacs
```

###  Run the Jupyter notebook: First generate config file and then change the IP address config setting
```
jupyter notebook --generate-config
sed -ie "s/#c.NotebookApp.ip = 'localhost'/#c.NotebookApp.ip = '*'/g" ~/.jupyter/jupyter_notebook_config.py
jupyter notebook --ip=0.0.0.0 --no-browser
```
