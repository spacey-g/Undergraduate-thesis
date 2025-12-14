🔧 Rebuild Plan for the Landslide Susceptibility Model
Modernizing the CNN + SVM Undergraduate Project

This document outlines how the original undergraduate thesis model can be rebuilt, improved, and extended using modern machine learning and geospatial techniques.

✅ 1. Rewrite the Entire Pipeline Using PyTorch

Implement a full PyTorch deep-learning pipeline

Replace manual preprocessing with torchvision.transforms

Use modular dataloaders (Dataset, DataLoader)

Improve code structure (already started in model_outline.py)

✅ 2. Replace Basic CNN With Transfer Learning

Use pre-trained models on satellite imagery or natural images:

ResNet18

EfficientNet

VGG16

MobileNet

Then fine-tune final layers on your landslide dataset.

Benefits:

Better feature extraction

Faster convergence

Higher accuracy

✅ 3. Replace SVM With a Fully Trainable End-to-End Network

Instead of CNN → SVM, build a full classifier:

CNN → Flatten → Dense Layers → Softmax


This allows:

Joint optimization

Better gradient flow

More stable predictions

✅ 4. Add More Input Features

Integrate multi-source geospatial data:

Rainfall intensity

Soil type

Land use/land cover

Vegetation index (NDVI)

Slope, aspect, curvature from DEM

Combine them using:

Multi-channel input tensors

Or late fusion models

✅ 5. Upgrade the Dataset

Build a larger, balanced dataset

Augment imagery (rotation, flip, contrast, brightness)

Use public landslide datasets like NASA/GloH2O or OpenLandMap

✅ 6. Add Evaluation Improvements

Use additional metrics:

ROC–AUC

Confusion matrix

IoU for spatial segmentation

Precision–Recall curves

✅ 7. Deploy the Model

Optional deployment ideas:

Web app (Streamlit / FastAPI)

GIS plugin (QGIS or ArcGIS)

Mobile early warning system

🚀 Long-Term Vision

Turn this thesis into a fully modern geospatial ML system capable of:

Real-time landslide detection

Risk visualization on maps

Integration with government or research data

Adaptation to other natural hazards (floods, erosion, drought)

📌 Note

This rebuild plan is intentionally designed to show:

Research maturity

Software engineering skills

Ability to extend previous work

Readiness for graduate-level ML/astro-ML research
