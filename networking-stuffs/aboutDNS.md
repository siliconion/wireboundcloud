# About DNS

## DNS
DNS stands for domain name server. DNS keeps the DNS records, and translates domain name to IP address. 

You can find the DNS you're using in `System Preference -> Network -> DNS`(on mac).

## Domain name
An identification string, that represents an internet protocal(IP) resource.

Domain names are organized in subdomains of root domain, which is nameless. 

First level of subdomains are top-level domains(TLD), which includes generic TLD, like .com, .io, and country code TLD, like .tw, .ca.

Second and third level subdomains are open for reservation.

Business-wise, domain names are registered at domain registars. Domain registry though, is a company that owns the TLD.

## DNS records
A DNS records has the following fields:
* type: type of the record. See below.
* name: the domain to be mapped. 
* rdata: the return value of the k-v pair. Can be IP, domain or numbers.
* TTL, Class, RDLength

Some of the common types are:
* A: address record. Returns an IPv4 address.
* CNAME: canonical name. Maps another domain name (can't be IP).
* NS - name server, which keeps the records of the DNS entries. Each domain name must have 2+ name servers. This record returns multiple NS domain names.
* SOA

---
Say I registered my domain at GoDaddy, but host my website on AWS. When I create a hosted zone in Route 53, it automatically gives me a NS record which points to 5 aws name servers, and a SOA record. I have to go to GoDaddy and change the name server record to the 5 aws name servers. 
 
So say if you enter the DNS records in route 53. Are these records just go to the NS records?