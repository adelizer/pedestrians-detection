# Pedestrians Detection using FCNs

This project explores the usage of FCNs to detect pedestrians for autonomous driving applications.

A number of successful approaches include YOLO with different versions and Mask R-CNNs. However, this project considers 
the simple approach of extending a classification model (VGG16) and train retrain the last layers 
using pedestrians datasets.  

![Alt text](images/segmentation_sample.png?raw=true "Sample segmentation")


### TODO:

* Use region proposals
* Extract the 3D location of the detected pedestrians.
* Compare RNNs prediction to motion models.
* Use Carla's perfect information about the pedestrians for validation