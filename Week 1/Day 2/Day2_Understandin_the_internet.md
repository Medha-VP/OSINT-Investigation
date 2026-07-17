Understanding the Internet

Practical Investigation Report

Target: Wikipedia (wikipedia.org)

Date: 04/07/2026

1. DNS Report

1. WHOIS Information

Field

Value

Domain Name

wikipedia.org

Registrar

MarkMonitor Inc.

Creation Date

13 January 2001

Expiry Date

13 January 2027 (may vary depending on renewal)

Registrant Organization

Wikimedia Foundation, Inc.

Name Servers

ns0.wikimedia.org, ns1.wikimedia.org, ns2.wikimedia.org




1. DNS Records

Record Type

Value

Notes

A (IPv4)

192\.168.1.1

Load balancing & redundancy

AAAA (IPv6)

2001:0db8:85a3::8a2e:0370:7334

IPv6 support

NS

ns0.wikimedia.org, ns1.wikimedia.org, ns2.wikimedia.org

Authoritative DNS

MX

aspmx.l.google.com (and backup Google mail servers)

Email handling

TXT

SPF, domain verification records

Email security & verification

TTL

Approximately 300 seconds

DNS cache duration

C. Observations

- Wikipedia uses multiple IP addresses so the website stays available even during heavy traffic.
- It supports both IPv4 and IPv6.
- DNS is managed by Wikimedia.
- Google handles Wikimedia's email services.
- Short TTL values help DNS updates take effect quickly.
- The website is designed to provide fast access to users around the world.

2\. URL Breakdown

`	`A URL (Uniform Resource Locator) is the complete address of a webpage.

Example 1

https://en.wikipedia.org/wiki/Open-source\_intelligence

Component

Value

Explanation

Protocol

https

Secure connection

Subdomain

en

English version of Wikipedia

Domain

wikipedia.org

Main website name

Path

/wiki/Open-source\_intelligence

Opens the OSINT article

Query Parameters

None

No extra information passed

Fragment

None

No section reference

Example 2

https://en.wikipedia.org/w/index.php?search=OSINT&title=Special:Search

Component

Value

Explanation

Protocol

https

Secure connection

Subdomain

en

English Wikipedia

Domain

wikipedia.org

Main website

Path

/w/index.php

Search page

Query Parameters

search=OSINT, title=Special:Search

Searches for "OSINT"

Fragment

None

No page section

Some other Wikimedia websites are:

- commons.wikimedia.org – Stores images, videos, and other media.
- meta.wikimedia.org – Used for community discussions and project planning.
- wikidata.org – Stores structured information used by Wikimedia projects.
- mediawiki.org – Documentation for the MediaWiki software.
- foundation.wikimedia.org – Information about the Wikimedia Foundation.

3\. Website Architecture Notes

Homepage

- Search bar
- Language selection
- Featured articles
- Navigation menu

Navigation

- Sidebar menu
- Search functionality
- Internal hyperlinks
- Categories
- References

Security

- Uses HTTPS.
- SSL/TLS encryption protects user communication.

Structure

- Hierarchical organization of articles.
- Internal links connect related topics.
- Extensive reference and citation system.
- Responsive design for desktop and mobile devices.

OSINT Relevance

Wikipedia demonstrates how publicly available information is organized, linked, referenced, and verified, making it a valuable starting point for open-source investigations.

Global Traffic Handling

Wikipedia serves millions of users using globally distributed caching servers, multiple data centers, load balancing, and redundant DNS infrastructure. Frequently accessed pages are cached close to users to reduce latency and improve performance. This architecture ensures high availability even during heavy traffic.

Surface / Deep / Dark Web Classification

- Wikipedia public articles belong to the Surface Web because they are indexed by search engines.
- User account settings, administrator interfaces, and login-restricted pages are part of the Deep Web because they require authentication.
- Wikipedia has no official Dark Web (.onion) version. Users should be cautious of unofficial or impersonating .onion websites.

Summary

This investigation helped me understand how websites are identified through domain names and DNS, how HTTPS secures communication, and how URLs are structured to locate specific resources. I also learned how large websites use distributed infrastructure, caching, and load balancing to provide fast and reliable services worldwide. These concepts form the foundation for effective OSINT investigations.

Conclusion

The investigation demonstrated how DNS, URLs, HTTPS, and website infrastructure work together to make websites accessible across the Internet. Wikipedia is an excellent example of a secure, scalable, and highly available website that uses modern networking technologies to serve millions of users every day.

Sources

1. https://www.wikipedia.org
1. https://www.whois.com/whois/wikipedia.org
1. https://mxtoolbox.com
1. https://dnschecker.org
1. https://wikitech.wikimedia.org

