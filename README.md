# MaMpf statistics

A few python scripts to generate some statistics about the MaMpf project given an uncompressed database dump.


## Pre-requisites

- [x] Python 3.8 or higher (tested with Python 3.11.5)
- [x] Install the required python packages via `pip3 install -r requirements.txt`.
- [x] Place a database dump in the `data` folder and name it `mampf.sql`.<br>(This path can be modified in the `.env` file if necessary.)


## Usage

Run one of the following scripts to extract the desired statistics. They are stored as PDF files in the `out` folder.

```py
python3 src/last_sign_in.py

# more to come...
```


## Development

- If you're using VSCode, go the the extensions tab and install the recommended extensions for this project (click on the filter icon and choose `Recommended`). This is mainly to ensure that the code is formatted correctly and that the linter (pylint) is working.
