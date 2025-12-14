"""
model_outline.py
-----------------
This file provides a modern PyTorch-style outline for rebuilding the
CNN + SVM model used in the undergraduate thesis:
"Assessment of Susceptibility to Landslide Through Deep Learning Algorithms".
"""

import torch
import torch.nn as nn
from sklearn.svm import SVC

# ----------------------------
# 1. CNN Feature Extractor
# ----------------------------

class CNNFeatureExtractor(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),  # grayscale or DEM fused input
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.flatten = nn.Flatten()

    def forward(self, x):
        out = self.features(x)
        out = self.flatten(out)
        return out


# ----------------------------
# 2. Train CNN + Extract Features
# ----------------------------

def extract_features(cnn, dataloader, device="cpu"):
    cnn.eval()
    all_features = []
    all_labels = []

    with torch.no_grad():
        for images, labels in dataloader:
            images = images.to(device)
            feats = cnn(images)
            all_features.append(feats.cpu())
            all_labels.append(labels)

    return torch.cat(all_features), torch.cat(all_labels)


# ----------------------------
# 3. Train SVM on CNN Features
# ----------------------------

def train_svm(features, labels):
    svm = SVC(kernel="rbf", probability=True)
    svm.fit(features, labels)
    return svm


# ----------------------------
# 4. Prediction Pipeline
# ----------------------------

def predict(cnn, svm, image, device="cpu"):
    cnn.eval()
    with torch.no_grad():
        image = image.to(device)
        feat = cnn(image.unsqueeze(0))
        feat = feat.cpu().numpy()
        return svm.predict(feat)[0]


"""
⚠ NOTE:
This is only a project structure outline — not the full original code.
It demonstrates how the model *would* be rebuilt in a modern, clean format.
PhD committees will appreciate structured code like this.
"""
