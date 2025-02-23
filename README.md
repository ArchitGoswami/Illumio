
# Instructions to run

1) Clone this repository
2) Navigate to the repository in your local
3) 'python3 run.py'

    #### Note: By default the project runs the unit test and then the files 'flowLogData' and 'lookupTable' under "inputFiles" directory.


# Assumptions

1) Assumes only version 2 inputs are received, ignores rest (MVP++ : add support for other version expansion).
2) Assumes all valid log lines have 14 columns (in flowLogData), ignores other lines that are more or less than 14.
3) Assumes only default log format is provided (no strings where integers are expected etc).
3) Assumes lookup csv file always has 3 elements in each line. No more, no less.
4) All values (in both the lookup table and flowLogData) will work if all characters are turned to lower case in protocol name.

    #### Note: tags will still be case sensitive.


# Design decisions

1) Using tuple for tagCount and protocolCount: converting pair of dstport and protocol values to string using separators would be possible but conversion back is unnecessarily 
2) using filecmp to compare files instead of checking with hard coded string value. Slower but more accurate for stress testing of the defined system.

# Testing

1) Test for empty flow logs with default/sample lookup table
2) Test for default/sample flow logs with default/sample lookup table
3) Test for single entry flow logs with default/sample lookup table
4) Test for single entry flow logs with empty lookup table
5) Test for default/sample flow logs with empty lookup table
6) Test for max flow logs with max lookup table (this also serves as duplicate tester)

# Imports

1) os
2) socket
3) collections
4) shutil
5) filecmp
6) unittest