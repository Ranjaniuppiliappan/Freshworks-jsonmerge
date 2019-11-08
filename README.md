# Freshworks-jsonmerge
view this notebook file in nbviewer [link](https://nbviewer.jupyter.org/github/Ranjaniuppiliappan/Freshworks-jsonmerge/blob/master/notebookfile/Merge-JSON.ipynb)
# merge() function
* It merges two json object into one
* Takes two json files as input(input is in dictionary format converted using json.loads()) 
* If both the file have same key then we want to merge them under common key name 
* This is done by calling merge() function again
* Else if keys are different add both the keys to the merge file
* This function merges two dictionary files and puts the output in one of the file
* merge(b,a) - merges b into a
# input() function
* It takes four parameter path, input file basename, output file basename, maxfile size
* Uses glob to fetch all the input file in the specified path having basename as prefix and number as suffix
* Stores all the json input file name in a list
* Implements as static counter for adding suffix to output file
* Creates output json file using output file basename as prefix and counter as suffix
* Calls merge() function iteratively for each input file passing input file and output file as parameter
* Each iteration merges the input file and output file and writes the merge output back to output json file
* Open the file using open() function and convert it to dictionary using json.loads()
* Iterate until all input file have been merged to the output file
