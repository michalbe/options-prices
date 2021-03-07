Options prices helper for Google Sheets
---

This script builds an almost realtime list of option prices that can be easily imported into Google Sheets.

### Run
  - create a `symbols.txt` file with list of your options symbols
```
T220121C00030000
IPOF210716C00017500
...
```
  - upload the script to the server, and add `python index.py > index.html` to your crontable (15 min interval is enough)
  - make sure `index.html` is publicly accessible thru an open URL
  - add a following formula to Google Sheets:
```
  =index(query(importhtml(concatenate("YOUR URL HERE"),"table",0), "SELECT * WHERE Col1 = '" & CELL WITH THE OPTION SYMBOL & "'"), 1, 2)
```
  - enjoy option prices updated every 15 minutes
