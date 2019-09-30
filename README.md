# Image Compare Project
This app will automate the manual task of comparing image pairs. 
This will also introduce the user to basics of machine learning.
# Objective
Create an app that will compare image pairs, find if they are similar, rate the difference and populate the elapsed time.
A .csv file should be created which will have 2 fields with absolute raw path to the images mentioned in the fields.
The app will read the .csv file and perform the above mentioned tasks for N number of pairs mentioned in the .csv file.
# What you'll need
- Python (2.X or 3.X)
- Favorite IDE (Pycharm, Anaconda or intelliJ). Not a must. Still can get the work done using cmd.
- Access to Git repo https://github.com/harshavijay85/Image-Compare/ (In this case the repo is open to public)
- Git or Bitbucket account for yourself and clone the above mentioned repo to yourself.

1. Install Python using the link https://www.python.org/downloads/
2. Once installed open your cmd or Terminal (windows/mac) to check if it is installed properly. Type "python" and see what output you get.
You should see something like the below. If you see something else then Please revisit the installation again.

Sample Terminal Output: 
(base) HarshavdhansMBP:Loblaw harshavardhanvijayasekar$ python
Python 3.7.2 (default, Dec 29 2018, 00:00:04) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 

3. Install necessary python modules needed for this particular app such as "pandas", "timeit", "time", "imagehash", "Image", "numpy", "PIL" and "urllib".
The above can be installed through command line tool.

Command to install: 

pip install timeit

pip install pandas

Proceed to install the other modules with the same pip command.

# What the app does
The app basically does 4 main things. (Read, compare, loop (N) and save)
1. It uses urllib to get the .csv file from the public git repo.
2. The image comparision is done using the numpy module where threshold of "15" is set. So if the percentage difference between 2 images is > 15 then they are considered not alike. The elapsed time is calculated by the timeit module. 
3. In order to compare N number of images pandas profiling dataframe is used.
4. The results are found in the results.csv file that gets created in the home directory where you save and execute your icompare.py
5. Initially imagehash module was used but later used numpy since the later provided much better comparision in terms of percentage whereas imagehash can only give basic differences.

# Run the App locally with the image and source csv files in github (Approach 1)
Once you have all the files within the git repo cloned to your repo and with python installed along with your modules continue to test the code by following steps. 
1. Download a local copy of the icompare.py file on your pc. Execute the python file using the below command. All you need is the icompare.py file in case you want to run a test without making any changes to the image files and source csv file.

Eg: python icompare.py

This should create the results.csv file with percentage difference and time elapsed for the images along with the pass or fail classification.

2. Steps to consider in case you want to use your git repo instead of harshavijay85. 
Replace the https://raw.githubusercontent.com/harshavijay85/Image-Compare/master/Image-Compare.csv with your git repo link and correct source csv filename. Make sure you have the source csv file and images in your git repo. You can download new images.

3. Steps to consider in case you want to use your images. Remove the file extensions of the image files such as .jpg and .png and then upload them to your git repo. Once the files are uploaded add the raw image file path link to the source file.
Eg: https://github.com/harshavijay85/Image-Compare/blob/master/watch1?raw=true,https://github.com/harshavijay85/Image-Compare/blob/master/watch2?raw=true
If you add more images, make sure to add the pairs in the csv as well. Image files in column A are compared with image files in column B.
IMPORTANT: Do not use the absolute path of the link in the source csv.
This is limitation within GIT and has nothing to do with the app. This can changed once the app is onboarded to an app engine.

# Run the App using google app engine and google drive (Approach 2)

While there are multiple ways how you want to store your image files. My initial approach was to store the image file and the source csv
in google drive and integrate that in the icompare.py file.
But integrating the gdrive api and leveraging its potential was getting a bit complicated since it needed API approvals from google.

