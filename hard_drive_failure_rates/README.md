# BACKBLAZE Hard Drive Data and Stats

#### Analysis of Backblaze hard drive data
Intro on [Backblaze data page](https://www.backblaze.com/b2/hard-drive-test-data.html)

> _Since 2013, Backblaze has published statistics and insights based on the hard drives in our data center. You'll find links to those reports below. We also publish data underlying these reports, so that anyone can reproduce them. You'll find an overview of this data and the download links further down this page._

#### Overview of the Hard Drive Data
A snapshot of each operational hard drive is taken each day at Backblaze's data center. This snapshot includes basic drive information along with the S.M.A.R.T. statistics reported by that drive. The daily snapshot of one drive is one record or row of data. All of the drive snapshots for a given day are collected into a file consisting of a row for each active hard drive. The format of this file is a `csv` (Comma Seperated Values) file. Each day this file is names in the format `YYYY-MM-DD.csv`, for example, `2013-04-10.csv`.

The first raw of each file contains the column names, the remaining rows are the actual data. The columns are as follows:

>- **Date** - the date of the file in `yyyy-mm-dd` format.
>- **Serial Number** - the manufacturer-assigned serial number of the drive.
>- **Model** - the manufacturer-assigned model number of the drive.
>- **Capacity** - the drive capacity in bytes.
>- **Failure** - contains a "0" if the drive is OK. Contains a "1" if this is the day the drive was operational before failling.
>- **2013-2014 SMART Stats** - 80 columns of data, that are the Raw and Normalized values of 40 different SMART stats as reported by the given drive. Each value is the number reported by the drive.
- **2015 SMART Stats** - 90 columns of data, that are the Raw and Normalized values of 45 different SMART stats as reported by the given drive. Each value is the number reported on the drive.
