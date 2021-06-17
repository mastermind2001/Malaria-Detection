# Malaria-Classification

## Overview

Malaria is a mosquito-borne infectious disease that affects humans and other animals. Malaria causes symptoms that typically include fever, tiredness, vomiting, and headaches. In severe cases it can cause yellow skin, seizures, coma, or death.Malaria 
is typically diagnosed by the microscopic examination of blood using blood films, or with antigen-based rapid diagnostic tests.
So, I've used segmented cells from the thin blood smear slide images to classify whether a person has malaria or not.
<br><br>

## Project Details

I have used Keras (an open source neural network library) to build this classifier. The model (Model.ipynb) contains a self-
made ConvNet (Convolutional Neural Network) that has around 4 convlutional layers, 4 Max Pool layers and 2 dense layers having 
'relu' activation unit. The last layer has the 'sigmoid' activation unit to classify  cell images having Malaria or not. It has around 336017 trainable parameters.

I have got around <strong>96% accuracy</strong> in the Test set.
<br><br>

## Dataset

The dataset contains two folders
<ul>
<li>Infected</li>
<li>Uninfected</li>
</ul>

And a total of 27,558 images.
<br><br>
Datatset Source : <strong>Kaggle</strong>

In order to use this model for this dataset, you have to organize the data in a particular format.

<img src="directory_structure.png" width="400" height="500" />
<br><br>

## Inspiration

Save humans by detecting Image Cells that contain Malaria or not
<br>

<h5>Copyright &copy; 2020 Akshit Sharma</h5>
