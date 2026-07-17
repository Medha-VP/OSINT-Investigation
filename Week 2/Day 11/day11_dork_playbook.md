# **<u>Google Dork Playbook</u>** 

## <u>Aim</u> 

To create a reusable Google Dork Playbook by organizing the search techniques and Google Dorks learned during previous practical sessions into categories based on their use cases for efficient OSINT investigations. 

## <u>Objective</u> 

The objective of this practical is to consolidate the Google Dorks, advanced search techniques, Google Hacking Database (GHDB) queries, search automation concepts, and multi-search engine findings from Days 3 to 10 into a single reference document. This playbook can be reused during future investigations to quickly identify the appropriate search query for different information requirements. 

## <u>Introduction</u> 

Google Dorking is an advanced search technique that uses Google's search operators to locate specific publicly available information on the internet. During the previous practical sessions, different search operators, GHDB queries, automation techniques, and search engines were explored. 

Instead of keeping these techniques in separate reports, they have been organized into this playbook based on their purpose. This makes the information easier to understand and reuse during future OSINT investigations. 

## <u>Google Dork Playbook</u> 

## 1. Reconnaissance 

## Purpose 

Reconnaissance Dorks are used to gather general information about a target organization before beginning a detailed investigation. 

|Google Dork|Purpose|
|---|---|
|site:ibm.com|Search only IBM website|
|cache:ibm.com|View Google's cached version of IBM|
|related:ibm.com|Find websites similar to IBM|
|site:ibm.com security|Locate IBM security pages|
|site:ibm.com careers|Find IBM career pages|



Use Case 

Used during the initial stage of an OSINT investigation to understand the target's online presence. 

## 2. Document Discovery 

Purpose 

These Dorks help locate publicly available documents. 

|Google Dork|Purpose|
|---|---|
|filetype:pdf|PDF documents|
|filetype:docx|Word documents|
|filetype:ppt OR<br>filetype:pptx|PowerPoint presentations|
|filetype:xlsx|Excel spreadsheets|
|filetype:xls|Excel files|
|site:ibm.com filetype:pdf|IBM PDF documents|
|site:ibm.com filetype:ppt|IBM presentations|



Use Case 

Useful for locating reports, technical manuals, research publications, presentations, and publicly available documentation. 

## 3. Research and Academic Resources 

Purpose 

Locate research papers published by educational institutions. 

|Google Dork|Purpose|
|---|---|
|site:edu filetype:pdf artificial intelligence|AI research papers|
|site:edu filetype:pdf machine learning|Machine learning research|
|site:edu deep learning pdf|Deep learning papers|
|site:edu blockchain pdf|Blockchain research|
|site:edu IoT pdf|Internet of Things research|



Use Case 

Helpful for collecting academic references and technical knowledge during OSINT investigations. 

## 4. Government Information 

Purpose 

Locate official government documents and reports. 

|Google Dork|Purpose|
|---|---|
|site:gov.in filetype:pdf cyber security|Cybersecurity guidelines|
|site:gov.in filetype:pdf disaster management|Disaster management reports|
|site:gov.in filetype:pdf education policy|Education policies|
|site:gov.in filetype:pdf health policy|Health policy documents|
|site:gov filetype:pdf climate change|Climate reports|



Use Case 

Useful for obtaining official publications, policies, and regulatory documents. 

5. Credentials / Login Portals 

Purpose 

Locate publicly indexed login interfaces. 

|Google Dork|Purpose|
|---|---|
|inurl:login|Login pages|
|intitle:"Login"|Login interfaces|
|inurl:admin|Administration pages|
|site:ibm.com<br>inurl:login|IBM login portals|



Use Case 

Helps identify authentication portals during passive reconnaissance. 

Note: Login pages were only observed. No login attempts or unauthorized access was performed. 

## 6. Infrastructure and Technical Resources 

Purpose 

Locate technical files that may reveal infrastructure information. 

|Google Dork|Purpose|
|---|---|
|ext:xml|XML files|
|ext:log|Log files|
|filetype:conf|Configuration files|
|filetype:ini|INI configuration files|
|filetype:txt|Text files|



Use Case 

Useful for identifying publicly available technical resources and understanding website configurations. 

7. Directory Listings 

Purpose 

Locate publicly indexed directories. 

|Google Dork|Purpose|
|---|---|
|intitle:"index of"|Open directory listings|
|intitle:"index of" backup|Backup folders|
|intitle:"index of" uploads|Upload directories|
|Use Case||



Directory listings may expose unnecessary files if directory browsing is enabled. 

## 8. Advanced Google Dorks 

During Day 7, multiple search operators were combined to perform more targeted searches on IBM. 

Examples include: 

|Google Dork|Purpose|
|---|---|
|site:ibm.com filetype:pdf intitle:"Annual Report"|Find IBM annual reports|
|site:ibm.com filetype:pdf intext:"Artificial Intelligence"|AI publications|
|site:ibm.com filetype:pdf -jobs|Exclude job-related documents|
|site:ibm.com inurl:careers AROUND(3) AI|AI career opportunities|
|site:ibm.com filetype:xlsx|Public spreadsheets|
|Use Case||



Combining multiple search operators improves search accuracy and reduces irrelevant search results. 

## 9. Google Hacking Database (GHDB) 

During Day 8, Google Dorks from the Google Hacking Database were studied to understand how publicly available information can be discovered through search engines. 

The categories explored included: 

- Files 

- Login Portals 

- Vulnerable Servers 

- Sensitive Information 

- Configuration Files 

Key Learning 

GHDB demonstrates how improperly exposed resources can be indexed by search engines, emphasizing the importance of secure website configuration. 

## 10. Search Automation 

Day 9 introduced automation to reduce repetitive manual searching. 

The developed Python script: 

- Reads Google Dorks from a text file. 

- Opens each search automatically in the web browser. 

- Records search URLs. 

- Saves timestamps. 

- Generates a search log. 

## Benefits 

- Saves time. 

- Reduces manual effort. 

- Maintains search history. 

- Improves consistency. 

## 11. Multi-Search Engine Investigation 

The IBM investigation was performed using multiple search engines. 

Search Engine Main Finding 

Google Best source for official documents and reports 

Bing Revealed additional indexed pages 

DuckDuckGo Displayed similar information with different rankings 

Key Learning 

Using multiple search engines provides broader coverage because each search engine indexes web pages differently. 

## 12. Best Practices 

While using Google Dorks during OSINT investigations: 

- Search only publicly available information. 

- Respect ethical and legal boundaries. 

- Never attempt unauthorized access. 

- Avoid interacting with authentication pages. 

- Verify findings using multiple search engines. 

- Maintain proper documentation of all observations. 

## <u>Conclusion</u> 

This Google Dork Playbook consolidates the techniques learned from Days 3 to 10 into a single, organized reference. By grouping Google Dorks according to their use cases—such as reconnaissance, document discovery, login portals, infrastructure, and research—the playbook makes it easier to select the appropriate search technique during an OSINT investigation. It also reinforces ethical practices, search automation, and the importance of using multiple search engines to obtain comprehensive and reliable publicly available information. 

