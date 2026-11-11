---
title: "What to do when I get an error while creating an ODBC connection to the SuperOffice CRM database?"
url: https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-while-creating-an-odbc-connection-to-the-superoffice-crm-database/
lang: en
updated: "30 Nov 2021"
---

# What to do when I get an error while creating an ODBC connection to the SuperOffice CRM database?

Updated on 30 Nov 2021

While creating an ODBC connection to the SuperOffice CRM database I get an error:

*Connection failed:
SQLState ‘08001’
[Microsoft][SQL Server Native Client 10.0] SQL Server Netwrok
Interfaces: Error Locating Server/Instance Specified [xFFFFFFFF].
Connection failed:
SQLState: ‘HYT00’
SQL Server Error: 0
Microsoft][SQL Server Native Client 10.0] Login timeout expired*

Why does it happen and how do I fix it?

There are several known situations when this error occurs:

- [SQL Server Browser service is disabled](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-while-creating-an-odbc-connection-to-the-superoffice-crm-database/#1)
- [Client Protocols “TCP/IP” and “Named Pages” is disabled](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-while-creating-an-odbc-connection-to-the-superoffice-crm-database/#2)
- [SuperOffice server does not allow remote connections](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-while-creating-an-odbc-connection-to-the-superoffice-crm-database/#3)
- [IPv4 enabled on the server](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-while-creating-an-odbc-connection-to-the-superoffice-crm-database/#4)
- [Firewall configuration](https://community.superoffice.com/en/support-faqs/faq/what-to-do-when-i-get-an-error-while-creating-an-odbc-connection-to-the-superoffice-crm-database/#5)

​

**SQL Server Browser service is disabled**

To check if the SQL Server Browser is running you need to:

1. Go to **Services** on the server and check if the **SQL Server Browser** service is started (as in the screenshot below).

   ![](https://cs.superoffice.com/scripts/customer.fcgi/getAttachment/2887085-2ip6WZ2WKw9GCSKyX0jsgkOhD48c5p1s2X4CRyManFWeBCLGAuhCeuyP0cEtn99I-0/image.png)
2. Go to **SQL Server Configuration Manager** and check if the **SQL Server Browser** is running.

   ![](https://cs.superoffice.com/scripts/customer.fcgi/getAttachment/2887143-Ip9FA0u9tdet2sywezq0lEQhuNJqlXuikPzQc1nU4AfLYa9eSzbK8ipH9mYAIM90-0/image.png)

**Client Protocols “TCP/IP” and “Named Pages” is disabled**

To check if the Client Protocols "TCP/IP" and "Named Pages" are enabled you need to go to **SQL Server Configuration Manager** click on **Client Protocols.**

![](https://cs.superoffice.com/scripts/customer.fcgi/getAttachment/2887096-Xaj3wKC1agN1LKzaJoCiXkBxicJ1WMeJdxbEjH9Fx0DxGN6AACD4fpyaJgL3qYgJ-0/image.png)

**SuperOffice server does not allow remote connections**

To check if this is the case open **SQL Server Manager** click on **Connections** and make sure that “Allow remote connections to this server” is enabled.

![](https://cs.superoffice.com/scripts/customer.fcgi/getAttachment/2887097-ewdGsG2bcCh38mh4TPu8HZsMd5T5Bd1dLtwaQRlCnpFwH3fN5JEw1z5RQyc0s67F-0/image.png)

​

**IPv4 enabled on the server**

If you are able to create the ODBC connection on the server, but not on client computers it can be that the server is using IPv4 but IPv6 is enabled too. To make sure this is the case, try to ["Ping"](http://www.wikihow.com/Ping-an-IP-Address) the server it should fail. To fix it go to **Local Area Connection Properties** and disable **IPv6**.

![](https://cs.superoffice.com/scripts/customer.fcgi/getAttachment/2887138-DecmobAQHeu32qBCQPP2seRunC4iRiNBfgRxIpxm1NrR5YdXPuPm00nW9W4e92I0-0/image.png)

​

**Firewall configuration**

If it still not working you can try to disable Firewall to test if then you can create a connection. If you can connect then, discuss with your network administrator how to configure it.

**Note!** It is not a recommended procedure, but some times can be necessary to identify the cause.
