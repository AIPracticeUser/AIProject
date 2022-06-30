# Singapore-Food-Image-Classification

For more in-depth information, please refer to the pdf https://github.com/AIPracticeUser/Singapore-Food-Image-Classification/raw/main/singapore_food_image_classification.pdf
For testing out the web application, please visit https://aipracticeuser-application-sg-food-gxvvoy.streamlitapp.com/
Note that you can use the above link on your phone and testing out with your phone's camera

### Problem Statement
![image](https://user-images.githubusercontent.com/100339175/156583940-72a20737-aafb-484e-8fb4-bf8e7078585a.png)

As we know for a fact that obesity is a major contributor to diseases such as diabetes, congestive heart failures, restrictive mobility. In recent local studies of Singapore and obesity, it shows
1. Singaporean’s average weight is increasing as compared to a decade ago
2. Obesity in Singapore is projected to hit 15% by 2024 if nothing is done (Currently, it is 11%)
3. An adult Singaporean average calories per day is increasing

### Problem Statement (contiuned)
Currently the available weight managements mobile apps in the market needs to input the food manually in order for the inbuilt calories calculator to work. These leads to several problems such as
1. Not entering the right food
2. Pick the lowest calorie option every time to “cheat”
3. Wait too long to log and ends up forgotten about it

### Proposed Solution
![image](https://user-images.githubusercontent.com/100339175/156584426-57139369-9cbe-41f1-a8d7-19295832efe8.png)
Decided to use Convolution Neural Network (CNN) as our solution to the problem 

Automatic recognition of dishes would not only help users effortlessly organize their extensive photo collections but would also help online photo repositories make their content more accessible

Additionally, mobile food photography can be used to help patients estimate and track their daily calorie intake on Singapore local foods efficiently.

### Implementation
Splitting the implementation into 3 parts
1. Image Scraping
2. CNN Modeling and Validation
3. Web Deployment

![Implementation](https://user-images.githubusercontent.com/100339175/156587769-3ec3a757-2325-40eb-b154-43a9db44e020.jpg)
### TECHNICAL ARCHITECHTURE
1. Image Scraping, 
- will be using Google Image Scraper to collect at least 750 training images and 250 testing images for one particular food
- zip and store the images (after cleansing) to Google Cloud
- Dataspell/Google Colab will download the zip file and preprocess the images for path directories and normalization

2. CNN OPERATION
- Using Tensforflow to build the model based on different classification problems
- Will be working on Binary Classification, Multi-Classification and Transfer Learning method
- Passing and saved the models to the Github Repository for Web Deployment

3. Web Deployment
- Setup environment using Anaconda for a workable requirement.txt file
- Writing Python codes to test the web app locally on your computer through port 8501
- Passing Github Repositiory directory with the web app python file to streamlit to start building according to the specifications and allows to be used remotely on streamlit server
![technical](https://user-images.githubusercontent.com/100339175/156588212-bd05a0ef-10ed-4be7-9583-06d9016d65f9.jpg)

### Image Scraping
By inputting the desired food and how many pictures needed, google image scraper will automatically capture each of the food into the folder. (Problems discussed in pdf file)
![image](https://user-images.githubusercontent.com/100339175/156588673-b93b7fb2-01c2-4a53-b84d-39757bbf3b67.png)

### Steps in modelling with Tensorflow
1. Download the image zip file from google cloud
2. Turn all the image data into numbers as Neural Network cannot handle images
3. Normalize the tensors to fit between [0...1] for better performance
4. Build Neural Networks Model with layers
5. Fit the model to the data and make prediction
6. Evaluate the model to see the performance through training-data loss and accuracy, and test-data loss and accuracy
7. Improve through experiments to see the results
8. Save and reload the model for hyperparameter turning and improve the model
![image](https://user-images.githubusercontent.com/100339175/156592177-cd06225a-4dc6-4152-828d-50ccb7c67293.png)

### Binary Classification
Reason why start with Binary Classification because of following "Fail Fast Fail Cheap" motto and testing if the amount of images were sufficient to do image classification
Steps taken to improve Binary Classification (Problem discussion in pdf)

![image](https://user-images.githubusercontent.com/100339175/156593880-d610789d-eba7-4b6c-86d1-a63e58ff79ee.png)

### Multi-Class Classification
Since binary classification, upscale the test from 2 food classes to 10 food classes
![image](https://user-images.githubusercontent.com/100339175/156594525-e40337ad-cd22-43ff-88b2-0ba5ae65d5cd.png)

Steps taken to improve multi-class classification (Problem discussion in pdf)

![image](https://user-images.githubusercontent.com/100339175/156595084-b54c1aa0-c1a4-441d-90b6-8b4c6a812ade.png)

### Transfer Learning
Even though multi-class classification has proven a success, but foreseen a lot of problems if contiuned to train with multi-class classification. Therefore decided to use Transfer Learning.

Transfer Learning is a popular machine learning method where a model developed for a task is reused as the starting point for a model on second task

![image](https://user-images.githubusercontent.com/100339175/156595479-851a08e1-ccb4-4dd9-947b-e9f6edd18cf0.png)

With transfer learning, we are able to reduce the number of images needed to a mere 10% of the total images needed in binary/multi-class classifications.
And by testing two of the most popular Transfer learning models (ResNet and EfficientNet), able to determine which is better for food classification with only 5 epochs
![image](https://user-images.githubusercontent.com/100339175/156596906-dd7b15dd-0abb-49d1-b14c-6ae36e6a329f.png)


### Web app functions
1. Able to select classification model to test it out
2. Display of the Loss and Accuracy of both training and testing data
3. Able to select images to place into the image holder
4. After pressing predict, it will have a prediction outcome and the confidence percentage
5. A graph of the top 5 possible food of highest Confidence Scoring of the current predicted food
6. A general list of the Nutrition facts with calories included, breakdown of calories and the list of the possible ingredients for the current predicted food
7. If the predicted food is a fruit, it will capture the calories directly from google website with BeautifulSoup web scraping and display on the web app
8. Camera function has been added that allows to work on any laptops and smartphones with camera attached
9. *Work in Progress* A feedback function is included to gather feedback from the users with results stored in database through SQL. This is to determine how accurate our application will be in real world scenario and able to amend the mistakes pointed out by the users.
![image](https://user-images.githubusercontent.com/100339175/156597202-75402bc7-2a1f-48e0-8472-acd0ace927f5.png)
![image](https://user-images.githubusercontent.com/100339175/156597443-27061254-74cc-4a15-9566-8f2e17561d47.png)

