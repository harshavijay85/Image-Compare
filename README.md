# Image Compare Project
This app will automate the manual task of comparing image pairs. 
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

3. Install necessary python modules needed for this particular app such as "pandas", "timeit", "time" and "numpy"
The above can be installed through command line tool.

Command to install: 

$ pip install timeit

$ pip install pandas

Proceed to install the other modules with the same pip command.

# What the app does
The app basically does 4 main things. (Read, compare, loop (N) and save)
1. The script open the local csv file using the path provided in the script.
2. The image comparision is done using the numpy module where threshold of "15" is set. So if the percentage difference between 2 images is > 15 then they are considered not alike. The elapsed time is calculated by the timeit module. 
3. In order to compare N number of images pandas profiling dataframe is used.
4. The results are found in the results.csv file that gets created in the home directory where you save and execute your icompare.py
5. Initially imagehash module was used but later used numpy since the later provided much better comparision in terms of percentage whereas imagehash can only give basic differences.
6. Once you have all the files within the git repo cloned to your repo and with python installed along with your modules continue to test the code by following the below steps. 

# Run the App locally with the image and source csv files in local directory (Approach 1)

1. Steps to consider incase you want use local image files. 

Download a local copy of the icompare.py file on your pc from the Git repo (https://github.com/harshavijay85/Image-Compare/)
Make sure you create the following directory path. C:\Documents\Documents\Loblaw\Image-Compare-master or in case you want to use your path, please update the python file accordingly.
Create and place the csv file in the local path mentioned above - "C:\Documents\Documents\Loblaw\Image-Compare-master\Image-Compare.csv"
You can use the sample csv file (Image-Compare.csv) in the git repo as a reference. 
Place the absolute paths of your images in column1 and column2 within the csv and save the csv.
You should get the results generated in the same path.
A sample results.csv can be found in the git repo. But your result should get generated in your absolute path.

Limitations:

Make sure the 1st column and 2nd column are renamped Image1 and Image2 respectively. 

Command to execute: 

Code: $ python icompare.py

This should create the results.csv file with percentage difference and time elapsed for the images.

# Unit-Testing Criteria

1. Change the image files to multiple png, jpg and execute the comparision
2. Use the same image with different color format

# Unit-Testing Success Criteria
1. The comparision rank will be > 0 even for the slightest change regardless of color and image size.
