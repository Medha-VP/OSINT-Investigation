# **Google Hacking Database (GHDB) Analysis** 

## **<u>Aim</u>** 

To understand the Google Hacking Database (GHDB), explore different categories of Google Dorks, and learn how these search queries help discover publicly available information during an OSINT investigation. 

## **<u>What is GHDB?</u>** 

The **Google Hacking Database (GHDB)** is a collection of Google search queries (called Google Dorks) that help locate publicly accessible information on the internet. 

These dorks are useful for: 

- Finding documents 

- Identifying login pages 

- Discovering directory listings 

- Detecting exposed configuration files 

- Finding publicly available sensitive information 

GHDB is mainly used by security researchers and OSINT investigators to identify information that organizations may have unintentionally exposed online. 

## **<u>Dork Analysis</u>** 

|**No.**|**Category**|**Google Dork**|**What It Finds**|**Security Risk**|
|---|---|---|---|---|
|**1**|Files|site:ibm.com|PDF documents|Internal documents may|
|||filetype:pdf|on IBM website|become publicly accessible if<br>not intended for public<br>release.|
|**2**|Files|site:ibm.com|Excel files|May expose business data or|



|||filetype:xlsx||reports.|
|---|---|---|---|---|
|**3**|Login Portals|site:ibm.com<br>inurl:login|Login pages|Helps identify authentication<br>portals that should be properly<br>secured.|
|**4**|Login Portals|site:ibm.com<br>intitle:"Login"|Pages with<br>"Login" in the<br>title|Reveals publicly accessible<br>login interfaces.|
|**5**|Sensitive<br>Information|site:ibm.com<br>filetype:txt|Text files|Could contain notes,<br>configuration details, or other<br>information if exposed.|
|**6**|Sensitive<br>Information|site:ibm.com<br>ext:xml|XML files|May reveal website<br>configuration or publicly<br>available data feeds.|
|**7**|Vulnerable<br>Servers|intitle:"index of"<br>site:ibm.com|Open directory<br>listings|Exposed folders may allow<br>browsing of files that were<br>not meant to be indexed.|
|**8**|Vulnerable<br>Servers|site:ibm.com<br>ext:log|Log files|If exposed, logs may reveal<br>technical details useful to<br>attackers.|
|**9**|Configuration<br>Files|site:ibm.com<br>filetype:conf|Configuration<br>files|Public configuration files may<br>expose system settings.|
|**10**|Configuration<br>Files|site:ibm.com<br>filetype:ini|INI configuration<br>files|Could reveal application<br>configuration if<br>unintentionally published.|



## **Observations** 

- Most organizations publish many public documents for customers and employees. 

- Login pages are usually easy to locate using Google Dorks. 

- Open directory listings should be disabled because they may expose unnecessary files. 

- Publicly accessible configuration or log files can reveal technical information and increase security risks. 

## **Conclusion** 

The Google Hacking Database provides a collection of useful search queries that help locate publicly available information on the internet. During this exercise, different categories of Google Dorks were explored to understand how documents, login portals, configuration files, and directory listings can be identified through search engines. This activity demonstrated the importance of proper website configuration and secure information management to reduce accidental exposure of sensitive data. 

