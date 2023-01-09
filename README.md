# SSH's Randomart

## Description
SSH's randomart is used for humans to visually distinguish between two SSH keys more easily, as opposed to comparing long strings.
The method used for these visualistations is called The Drunken Bishop algorithm, which functioning is replicated in this script.

More information on the topic: [The drunken bishop: An analysis of the OpenSSH fingerprint visualization algorithm](http://www.dirk-loss.de/sshvis/drunken_bishop.pdf).

## Run

To run the script, simply use the command `python3 drunken_bishop.py`. If no fingerprint is provided, one will be randomly generated.
The script accepts 2 optional arguments:

| Argument name | flag | type   | Description                                                                                                 |
|---------------|-----|---------|-------------------------------------------------------------------------------------------------------------|
| `fingerprint` | -f  | string  | Fingerprint Input, e.g. "fc:94:b0:c1:e5:b0:98:7c:58:43:99:76:97:ee:9f:b7".                                  |
| `iterations`  | -i  | integer | No. of iterations (max. 10) to show the evolution of drawing the board, should be used without the -f flag. |

## Run Tests

A number of different tests are provided to verify the correct implementation of the algorithm. The test script can be called with the command `python3 drunken_bishop_test.py`.
