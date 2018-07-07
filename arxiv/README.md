# arXiv Submissions & Downloads

_Simulating time series for [arXiv](https://arxiv.org) submissions and downloads.

Some caveats on the data:
    1. the data is from the main arXiv site and the arXiv mirrors, though some mirror data is incomplete;
    2. only web downloads are included (and not FTP or email "downloads" that were formerly supported);
    3. we have counted downloads according to the COUNTER algorithm which excludes rapid repeat downloads;
    4. we have attempted to identify and remove robot or automated downloads from the count (false
       positives lead to undercounting, failing to identify robots leads to overcounting);
    5. data prior to 2009 has not been cleaned with as much care as later data, it shows trends nonetheless.