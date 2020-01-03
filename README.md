# Dog vs Cat Convolutional Neural Network classification
Our model is also deployed on [Heroku here](https://dogvscat-mobilenet.herokuapp.com)

### Data
The model is trained on Kaggle dataset [kernels edition](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data)

### Model
We use Tensorflow 2.0.0 and Keras MobileNetV2 to build our model. The last layer is Softmax with 2 classes (dog and cat). See jupyter notebook `CatvsDogCNN.ipynb` for more details.
![](https://machinethink.net/images/mobilenet-v2/ExpandProject@2x.png)
![](https://machinethink.net/images/mobilenet-v2/Compression@2x.png)

### Training
- The data from the Kaggle dataset is processed to fit into MobileNetV2 input. See jupyter notebook `CatvsDogCNN.ipynb` for more details.

- Our model achieved 98% accuracy on train set and 98% on validation set after 7 epochs (batch size 32, 782 epoch steps)

### Flask app
-  Our Flask app allows users to upload an image of cat or dog to be classified and output the class and % confidence (probability)
-   In case of misclassification, our app allows user to save test images to our Heroku PostGres database for future training.

### Database
-   We have two PostGreSQL connection configurations for our saved images: psycopg2 (for local Flask app) and SQLAlchemy (for heroku)
-   Our data table contains one id column and two columns for images (BYTEA type) and label (int type)
-   We encode images using base64 format to save into img column in our table
-   In order to run locally, users can clone the repo. First create PostGreSQL data table as describe above. Then edit the psycopg2 connections in `sql.py` to fit with your database on your local system. Then run `python app.py` to start Flask app locally.