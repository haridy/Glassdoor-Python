# Glassdoor-Python
Contains function to fetch public company profile from Glassdoor API (http://www.glassdoor.com/api/companiesApiActions.htm)

To install just download the .py file and use it directly. Feel free to change and redistribute it, it's simple and anyone with any level of Python skills should be able to read and change it.

The module is a simple one file with 2 function calls and a class.

Class CompanyProfile - represents an object with the properties fetched from Glassdoor

getCompanyPublicProfileAsObject(companyName) - returns an object of type CompanyProfile filled with the data from Glassdoor

getCompanyPublicProfile(companyName) - returns the JSON object fetched from the Glasdoor API call

Both do the same thing just use whichever is more comfortable for your application. Also, if you run into errors with non-unicode characters then the JSON object is probably more suitable for you.

Hope this saved you a few minutes of your time.
