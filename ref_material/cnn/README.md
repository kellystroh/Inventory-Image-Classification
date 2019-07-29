# CNN lecture

## Startup

To use these notebooks, run from this directory:

`$ docker run --rm --name cnn -it -p 8881:8888 -v "$PWD":/tf/lec tensorflow/tensorflow:2.0.0a0-py3-jupyter`

You might have to replace "8881" in the above if you're already using that port.

## Objectives

By the end of the lecture you should be able to:

* Build and train a sequential model using the Keras API
* Describe data augmentation
* Use Keras to automatically find a "good filter"
* Use convolution, maxpool, and dropout layers
* Understand multichannel convolutions
* Stack a CNN with a multilayer perceptron
* Estimate that what kind of performance to expect from a CNN
 * Give input, number of layers, width of layers
 
## Sequence

1. `onefilter_logisticregression`
2. `manyfilter_logisticregression`
3. `fullpower_logisticregression`
4. `fillpower_mnist`
