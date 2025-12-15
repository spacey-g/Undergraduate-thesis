# Assessment of Landslide Susceptibility Using CNN and SVM
### *Undergraduate Thesis Project*

This repository contains the complete documentation, methodology, and analysis from my undergraduate engineering thesis titled:  
**“Assessment of Susceptibility to Landslide Through Deep Learning Algorithms.”**

The project proposes a hybrid deep-learning system using:  
- **Convolutional Neural Networks (CNN)** for feature extraction  
- **Support Vector Machines (SVM)** for classification  

The model aims to predict landslide-prone areas using satellite imagery and topographical data.

---


##  Abstract

Landslide susceptibility mapping identifies regions likely to experience landslides based on environmental, geological, and topographic conditions.  
This project introduces a deep-learning-based hybrid approach that combines **CNN** for automated feature extraction and **SVM** for accurate classification of landslide vs non-landslide regions.

The proposed method shows **high accuracy** in prediction and offers a promising tool for early warning systems and disaster mitigation.

---

##  Methodology

### **1. Data Collection**
- Satellite imagery  
- DEM (Digital Elevation Model)  
- Environmental and topographical attributes  

### **2. Preprocessing**
- Noise reduction  
- Image normalization  
- Feature extraction  
- Splitting dataset: **70% training / 30% testing**

### **3. CNN Architecture**
CNN layers extract spatial and terrain-based features from the input imagery:
- Convolution layers  
- ReLU activation  
- Pooling layers  
- Fully connected layers  

### **4. SVM Classifier**
- Uses CNN-extracted features  
- Performs binary classification  
- Kernel-based high-dimensional separation  

### **5. Evaluation Metrics**
- Accuracy  
- Precision  
- Recall  
- F1-score  

The hybrid CNN–SVM model combines powerful feature learning with robust classification ability.

---

##  Results

The proposed CNN–SVM hybrid approach achieved:

- **91.22% accuracy**  
- Improved feature extraction vs traditional ML models  
- Higher precision and recall  
- Better generalization performance  

This demonstrates its suitability for practical landslide risk assessment.

---

##  Future Improvements

This project can be extended by:

- Implementing **transfer learning** with modern deep networks  
- Including **multi-source GIS data** (rainfall, soil type, land use)  
- Creating a **real-time risk monitoring system**  
- Training on larger and more diverse datasets  
- Rebuilding the model using **PyTorch or TensorFlow**  

A detailed rebuild plan will be added in the `future-work/` directory.

---

##  Full Thesis Document

Click below to view the full project report:

 **[`docs/UPDATED LANDSLIDE REPORT.pdf`](docs/UPDATED%20LANDSLIDE%20REPORT.pdf)**

---

##  About This Project

This thesis was completed as part of my  
**Bachelor of Engineering (ECE)** at  
**Hindusthan College of Engineering and Technology, Coimbatore.**

The work demonstrates the integration of machine learning, image processing, and disaster prediction techniques for environmental risk assessment.

---

