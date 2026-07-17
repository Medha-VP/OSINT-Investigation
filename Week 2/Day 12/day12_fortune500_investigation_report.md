# **<u>Fortune 500 OSINT Investigation Report</u>** 

## **<u>Company</u>** 

## **IBM (International Business Machines Corporation)** 

## **<u>Objective</u>** 

To perform an Open-Source Intelligence (OSINT) investigation on IBM using publicly available information and search intelligence techniques learned during Week 2. The investigation focused on discovering publicly accessible documents, login portals, technical resources, and other indexed information without interacting with restricted systems. 

## **<u>Methodology</u>** 

- Selected IBM as the target organization. 

- Used Google, Bing, and DuckDuckGo for information gathering. 

- Applied advanced Google Dorks and GHDB dorks. 

- Searched for publicly available documents, login pages, support resources, and directory listings. 

- Compared results from multiple search engines. 

- Recorded only publicly accessible information. 

## **<u>Search Engines Used</u>** 

- Google 

- Bing 

##  DuckDuckGo 

## **<u>Google Dorks Used</u>** 

|**Google Dork**|**Purpose**|
|---|---|
|**site:ibm.com filetype:pdf**|Find PDF documents|
|**site:ibm.com filetype:xlsx**|Search for Excel files|
|**site:ibm.com inurl:login**|Locate login pages|
|**site:ibm.com intitle:"index of"**|Check for public directory listings|
|**site:ibm.com inurl:support**|Find support pages|



## **<u>Advanced Dorks Used</u>** 

|**Dork**|**Purpose**|
|---|---|
|**site:ibm.com filetype:pdf intitle:"AI"**|Find AI-related PDF documents|
|**site:ibm.com filetype:pdf intext:"cloud"**|Search cloud-related documents|
|**site:research.ibm.com filetype:pdf**|Locate IBM research papers|
|**site:ibm.com inurl:docs filetype:pdf**|Find technical documentation|
|**site:ibm.com filetype:ppt OR filetype:pptx**|Find presentations|



## **<u>GHDB Dorks Used</u>** 

The following GHDB categories were tested safely: 

- Files Containing Sensitive Information 

- Login Portals 

- Sensitive Directories 

- Vulnerable Files (publicly indexed only) 

- Configuration Files 

No unauthorized access or interaction was performed. 

## **<u>Public Documents Found</u>** 

- IBM Annual Reports 

- AI Research Papers 

- Technical Whitepapers 

- Product Documentation 

- User Manuals 

- Developer Guides 

## **<u>Login Portals</u>** 

Publicly indexed login pages identified include: 

- IBM Account Login 

- IBM Cloud Login 

- IBM Support Login 

These pages were only observed and not accessed. 

## **<u>Directory Listings</u>** 

No publicly accessible directory listings (intitle:"index of") were identified during the investigation. 

## **<u>Cached Pages</u>** 

Cached versions of several IBM pages were available through search engines and were useful for viewing previously indexed content. 

## **<u>Interesting Findings</u>** 

- IBM publishes a large number of research papers and technical documents. 

- Extensive developer documentation is publicly available. 

- Multiple official support and authentication portals are indexed. 

- Search engines returned different results, providing broader visibility when used together. 

## **<u>Security Observations</u>** 

- No exposed confidential information was identified. 

- Public documents appear to be intentionally published. 

- IBM maintains well-organized public resources and documentation. 

- Public login pages are properly separated from internal resources. 

## **<u>Conclusion</u>** 

The OSINT investigation demonstrated how search engines, Google Dorks, and GHDB techniques can be used to gather valuable intelligence from publicly available sources. IBM provides extensive public documentation, research papers, and technical resources while maintaining good security practices by limiting exposure of sensitive information. This investigation highlights the importance of responsible and ethical OSINT practices using only publicly accessible data. 

