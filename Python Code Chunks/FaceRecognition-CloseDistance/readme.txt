This readme.txt is for Facial Recognition For Close Distance(upto 2.5m)
It can be used for various purposes for eg. Biometric attendance.

Cascades Folder contain all .xml files to be used.

testData Contain your saved data for training.

STEP-1:

To ADD a new face:
record.py
>>>python3 record.py option-1 "name of person"
for option-1, you can give 2 values
    1. live - for recording the live feed.
    >>> python3 record.py live ayush

    2. "Video file Location" - to record the person's face from the video.
    >>>python3 record.py FolderXYZ/fileABC ayush

Now, images has been save in data/Videodata folder with folder's name as name of the person.

STEP-2

To find encodings of all people in your database.

>>>python3 encodings.py folderLocation

STEP-3

To train these encodings

>>>python3 train.py

STEP-4

To run the program.

>>>python3 run.py option-1
    for option-1, you can give 2 values
    1. live - for check the live feed.
    >>> python3 record.py live

    2. "Video file Location" - to check the person's face from the video.
    >>>python3 record.py FolderXYZ/fileABC