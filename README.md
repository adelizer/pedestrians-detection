# Pedestrians Detection using FCNs

This project explores the usage of FCNs to detect pedestrians for autonomous driving applications.

A number of successful approaches include YOLO with different versions and Mask R-CNNs. However, this project considers 
the simple approach of extending a classification model (VGG16) and train retrain the last layers 
using pedestrians datasets.


![Alt text](images/segmentation_sample.png?raw=true "Example of semantic segmentation performed on an image in the Carla environment")

Semantic segmentation is regarded as one of the main challenges in the computer vision and machine learning communities. It can be simply described as the task of labeling each pixel in an image according to the class of objects that it represents, thus the whole image can be recognized. There are many application that require such dense prediction such as, medical diagnosis, autonomous driving, surveillance systems, and many more. Semantic segmentation is one of the topics that witnessed transformative breakthroughs by the recent advances in deep learning that is shown to yield superior performance in multiple computer vision tasks. Therefore, this extended abstract focuses on three key contributions towards semantic segmentation using convolutional neural networks, and discusses some of their commonalities and differences.

Integrating the segmentation and tracking into a simulator offers a convenient way to test multiple scenarios
since the actors can be controlled to produce any arbitrary motion model at different location in the scene.
E.g. simulate humans that rush into crossing the street or stop abruptly.


## Motion Prediction:
Given a sequence of observations of multiple pedestrians, how can we predict their motion in the future?
* Consider motion dynamics and physical constraints
* Context cues, such as head pose, their acknowledgement of the vehicle, etc.
* Higher level semantics, such as their relation towards


### References

* [FCN paper](https://people.eecs.berkeley.edu/~jonlong/long_shelhamer_fcn.pdf)
* [Datasets](http://www.gavrila.net/)
* [MIT Self-driving car lecture (Waymo)](https://www.youtube.com/watch?v=Q0nGo2-y0xY&index=2&list=PLrAXtmErZgOeY0lkVCIVafdGFOTi45amq)
* [Medium post](https://medium.com/nanonets/how-to-do-image-segmentation-using-deep-learning-c673cc5862ef)


### TODO:

* Investigate ConvLSTMs on the Kitti dataset
* Use region proposals
* Extract the 3D location of the detected pedestrians.
* Compare RNNs prediction to motion models.
* Use Carla's perfect information about the pedestrians for validation
* How to include uncertainty of each prediction given the sensors inherent properties ? (Bayesian networks ?)