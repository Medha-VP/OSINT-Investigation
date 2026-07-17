# **<u>Domains, WHOIS, Registrar, TLD Analysis</u>** 

## **<u>Objective</u>** 

The objective of this practical is to perform WHOIS lookups on five different domains and identify their registrar, registration date, expiry date, privacy protection status, and publicly available registration information. 

## **<u>Domains Selected</u>** 

1. **ibm.com** (.com) 

2. **usa.gov** (.gov) 

3. **wikipedia.org** (.org) 

4. **nic.in** (.in – Country Code TLD) 

5. **github.com** (.com) 

## **-** **<u>Types of Top Level Domains (TLDs)</u>** 

## **1) Generic Top-Level Domain (gTLD)** 

Generic domains that are not associated with a specific country. 

**Examples:** .com, .org, .net 

## **2) Country Code Top-Level Domain (ccTLD)** 

Domains assigned to individual countries. 

**Examples:** .in (India), .uk (United Kingdom), .jp (Japan) 

## **3) New Generic Top-Level Domain (New gTLD)** 

Recently introduced domain extensions for specific industries or purposes. **Examples:** .tech, .online, .store 

## **<u>WHOIS Analysis</u>** 

|**Domain**|**TLD**<br>**Type**|**Registrar**|**Creation**<br>**Date**|**Privacy**<br>**Protection**|**Information**<br>**Exposed**|
|---|---|---|---|---|---|
|**ibm.com**|.com<br>(gTLD)|MarkMonitor<br>Inc.|1986|Yes|Registrar, creation<br>date, expiry date,<br>name servers|
|**usa.gov**|.gov|Government<br>Managed|Not<br>Public|Not<br>Applicable|Government<br>registration<br>information only|
|**wikipedia.org**|.org<br>(gTLD)|MarkMonitor<br>Inc.|2001|Yes|Registrar,<br>registration dates,<br>name servers|
|**nic.in**|.in<br>(ccTLD)|National Internet<br>Exchange of<br>India (NIXI)|Public|No|Administrative and<br>technical<br>information<br>available|
|**github.com**|.com<br>(gTLD)|MarkMonitor<br>Inc.|2007|Yes|Registrar, dates,<br>DNS information|



## **<u>Observations</u>** 

## **IBM (ibm.com)** 

- Registered through MarkMonitor Inc. 

- WHOIS privacy protection is enabled. 

- Registrar and domain dates are publicly visible. 

- Registrant's personal information is hidden. 

## **USA Government (usa.gov)** 

- Government-owned domain. 

- Registration details are limited. 

- Sensitive registrant information is not publicly disclosed. 

## **Wikipedia (wikipedia.org)** 

- Uses MarkMonitor as registrar. 

- Privacy protection is enabled. 

- Registration dates and DNS information are publicly available. 

## **NIC India (nic.in)** 

- Uses India's official domain registry (NIXI). 

- Administrative details are publicly available. 

- Represents India's country-code domain management. 

## **GitHub (github.com)** 

- Registered through MarkMonitor. 

- WHOIS privacy protection is enabled. 

- Only technical registration details are publicly visible. 

## **<u>Privacy Protection Analysis</u>** 

WHOIS privacy protection hides sensitive information such as: 

- Owner Name 

- Email Address 

- Phone Number 

- Physical Address 

Without privacy protection, these details may be publicly accessible through WHOIS records. 

## **<u>Information Commonly Exposed in WHOIS</u>** 

- Domain Name 

- Registrar 

- Registration Date 

- Expiry Date 

- Last Updated Date 

- Name Servers 

- Domain Status 

- DNSSEC Status 

## **<u>Information Commonly Redacted</u>** 

- Registrant Name 

- Organization Contact 

- Email Address 

- Phone Number 

- Postal Address 

## **<u>Conclusion</u>** 

This practical demonstrated how WHOIS records provide valuable public information about domain registrations. Different TLDs such as **.com** , **.org** , **.gov** , and **.in** follow different registration policies. Most commercial organizations use WHOIS privacy protection to hide personal registrant information, while still exposing technical details like registrar, registration dates, and name servers. Understanding WHOIS information helps analysts identify domain ownership patterns, registration history, and basic infrastructure details during an OSINT investigation. 

