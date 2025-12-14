Load satellite_images
Load DEM_data
Load labels (landslide / non-landslide)
For each image:
    resize to (128 × 128)
    normalize pixel values
    apply noise reduction
    combine satellite + DEM into input tensor
Split data into train / test sets (70/30)
Define CNN:
    Conv2D(filters=32, kernel=3) + ReLU
    MaxPool2D
    Conv2D(filters=64, kernel=3) + ReLU
    MaxPool2D
    Flatten()
Return feature_vector
Train SVM on CNN feature_vectors
Predict labels on test data
Evaluate using:
    accuracy
    precision
    recall
    F1-score
Return classification_map
Highlight landslide-prone areas
Print evaluation metrics
