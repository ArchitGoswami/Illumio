
# Prerequisites

1) python
2) git (optional)

# Instructions to run

1) Clone this repository
2) Navigate to the repository (directory should be called 'Illumio') in your local machine
3) To run using default files use the command: 'python3 run.py'

    #### Note: By default, the project runs the files 'flowLogData' and 'lookupTable' under "inputFiles" directory (does not include unit tests).
    #### Note: The keyword for "python3" might differ.

4) To run files different from the default use the command: 'python3 run.py --lookupTableSource=<path_to_your_lookupTableSource> --flowLogSource=<path_to_your_flowLogSource> --writeSource=<path_to_your_writeSource>'
4) To run unit tests use the command: 'python3 run.py -u'


# Assumptions

1) Assumes only version 2 inputs are received, ignores rest.
2) Assumes all valid log lines have 14 columns (in flowLogData), and ignores other lines that are more or less than 14.
3) Assumes only default log format is provided (no strings where integers are expected etc).
3) Assumes lookup csv file always has 3 elements in each line. No more, no less.
4) All values (in both the lookup table and flowLogData files) will work if all characters are turned to lowercase in the protocol name.

    #### Note: tags will still be case-sensitive.


# Design decisions

1) Using tuple for tagCount and protocolCount: converting pa air of dstport and protocol values to string using separators would be possible but conversion back is unnecessarily 
2) using filecmp to compare files instead of checking with hard-coded string values. Slower but more accurate for stress testing of the defined system.

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
