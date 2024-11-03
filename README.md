## TL;DR
Goto [https://sailowtech.github.io/google-groups-difference/](https://sailowtech.github.io/google-groups-difference/)

## Project description

A simple script to easily create google groups.

Main feature for now is to create groups by making the difference between two csv files (aka two groups).


### Inputs and outputs

#### Inputs

You need to export users from both groups in a csv file each. They need to have the following columns (should be default ones in google groups)(**order matters!**):
- _Member Name_ (first + last name)
- _Member Email_
- _Member Relation_ Type (DIRECT or INDIRECT)
- _Member Type_ (USER or GROUP)

#### Outputs

Output will be a csv file with the following columns:
- _Group Email [required]_
- _Member Email_


### Usage

1. Download your inputs from google groups and upload them in the inputs fields.
2. Fill the output email field with the email of the new group (important!).
3. Click on "Compute Difference".
4. Check the output is the one intended.
5. Click on "Download Output" to get your new group.
