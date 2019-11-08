import json
import glob
def merge(a, b):#merges json array in a and b into a
    for key in b:
        if key in a:# if key is in both a and b
            if isinstance(a[key], dict) and isinstance(b[key], dict):# if the key is dict Object
                merge(a[key], b[key])# combine the values of common key by calling function again
            else:#if key is not a dict object
              a[key] =a[key]+ b[key]
        else: # if the key is not in both a and b add b value inside a
            a.update({key:b[key]})
    return a
def samp(path,infile,outfile,maxsize):
    # static counter that increments count each time function is called
    # this counter is used in naming output file(basename+counter)eg(output1.json)
    if 'cnt' not in samp.__dict__:
        samp.cnt = 0
    samp.cnt += 1
    # list that holds the input file
    file=[]
    # regular expression for selecting all file in the specified path with basename and increasing order of number added as suffix
    regex=path+infile+str("[0-9]*.json")
    # print(regex)
    # using glob to fetch all files with common base name and suffix as number in the path specified
    for name in glob.glob(regex):
        # append file to the list
        file.append(name)
        #print(name)
    data={}
    # creating output file with base name and counter(basename+counter)
    outfile=outfile+str(samp.cnt)+str(".json")
    with open(outfile, 'w') as f:
        json.dump(data, f)
        print("Writing the merged output of json files to the file...\n"+outfile)
    # iterate for each file in the path
    for i in range(0,len(file)):
        size=os.stat(outfile).st_size
        # checks if the file size exceeds the maximum size
        if size >maxsize:
            print('Data File Exceeds the Limit... Please choose New file..')
            return None
        # open the json file in list
        with open(file[i]) as fp1:
            # open the output file
            with open(outfile) as fp2:
                # read the file
                jsondata1=json.load(fp1)
                jsondata2=json.load(fp2)
                # write the merge output back to the output file
                with open(outfile, 'w') as f:
                  json.dump(merge(jsondata1,jsondata2),f,sort_keys=True)
                # iterate for the next file