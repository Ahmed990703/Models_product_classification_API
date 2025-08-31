from transformers import pipeline
classifier= pipeline("image-classification",model="my_model")
print(classifier('Desktop/product_classification_api/notebook/data/molokhia.jpg'))
if __name__=='__main__' :
    preds=classifier('Desktop/product_classification_api/notebook/data/molokhia.jpg')