

def getWeightsAndNames(model):
    # For finding the order of weights
    names = [weight.name for layer in model.layers for weight in layer.weights]
    weights = model.get_weights()

    for name, weight in zip(names, weights):
        keras_print(name,"\n",weight.shape)