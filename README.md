# Assumptions

1) Assumes only version 2 inputs are received, ignores rest (MVP++ : add support for other version expansion).
2) Assumes all valid log lines have 14 columns (in flowLogData), ignores other lines that are more or less than 14.
3) Assumes lookup csv file always has 3 elements in each line. No more, no less.
4) All values (in both the lookup table and flowLogData) will work if all characters are turned to lower case in protocol name
    ## Note: tags will still be case sensitive.
5) 


# Design decisions

1) Using tuple for tagCount and protocolCount: converting pair of dstport and protocol values to string using separators would be possible but conversion back is unnecessarily 

# Imports

1) os
2) socket
3) collections
4) shutil
5) filecmp
6) unittest