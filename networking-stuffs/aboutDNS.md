# About DNS

## DNS
DNS stands for Domain Name Server. DNS keeps the DNS records, and translates domain name to IP address. 

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
* NS: name server, which keeps the records of the DNS entries.

## Domain name resolution
Say siliconion.github.io, your computer will:
1. go to the name server for .io, to find the name server for github.io
1. go to the name server for github.io, and find the a record for siliconion, which is an IP address
1. To to the IP address
1. profit!

