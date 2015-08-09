# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 11:01:42 2015

@author:Omar Haridy
"""

import urllib2,json
#put your ID and Key here
PartnerID=''
Key=''

class CompanyProfile:
    """A class represeting company profile information"""
    name="" 
    website=""
    overallRating=0.
    isEEP=False
    cultureAndValuesRating = 0. 
    industry=""
    compensationAndBenefitsRating=0.
    numberOfRatings=0
    exactMatch=True;
    ratingDescription=''
    workLifeBalanceRating=0.
    careerOpportunitiesRating=0.
    recommendToFriendRating=0.
    squareLogo=""
    seniorLeadershipRating=0.
    id=-1


def getCompanyPublicProfileAsObject(companyName):
    name=str(companyName);
    name=name.replace(' ','+');
    call_url = "http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p="+PartnerID+"&t.k="+Key+"&action=employers&q="+name;
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    call_headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url=call_url,headers=call_headers);
    response=urllib2.urlopen(req)
    html=response.read()
    response=json.loads(html);
    #checking response
    if(response['success']==True): 
        #print "Request made successfully"
        True
    else:
        print "Request failed, the following is the response"
        print response
        return

    recordCount=response['response']['totalRecordCount']
    if(recordCount==0):
        print "Search returned no results"
        return    

    if(recordCount>1):
        #print "Search returned "+str(recordCount) +" results, looking for exact match"
        True
    #checking returned results by name
    selectedCompany=None
    for company in response['response']['employers']:
         name = str(companyName)
         name = name.lower();
        # fetchedName= str(company['name'])
         #fetchedName=fetchedName.lower()
         if (company['exactMatch']):
             selectedCompany = company;
             break;
    
    if(selectedCompany==None):
        print "could not find exact match"
        return
    
    profile=CompanyProfile()
    profile.website=selectedCompany['website']    
    profile.careerOpportunitiesRating=selectedCompany['careerOpportunitiesRating']
    profile.compensationAndBenefitsRating=selectedCompany['compensationAndBenefitsRating']
    profile.cultureAndValuesRating=selectedCompany['cultureAndValuesRating']

    profile.id=selectedCompany['id']
    profile.industry=selectedCompany['industry']
    profile.isEEP=selectedCompany['isEEP']
    profile.name=str(companyName)
    profile.numberOfRatings=selectedCompany['numberOfRatings']
    profile.overallRating=selectedCompany['overallRating']
    profile.ratingDescription=selectedCompany['ratingDescription']
    profile.recommendToFriendRating=selectedCompany['recommendToFriendRating']
    profile.seniorLeadershipRating=selectedCompany['seniorLeadershipRating']
    profile.squareLogo=selectedCompany['squareLogo']
    profile.workLifeBalanceRating=selectedCompany['workLifeBalanceRating']    
    #print "Company profile returned successfully"
    
    return profile;
    
    
def getCompanyPublicProfile(companyName):
    name=str(companyName);
    name=name.replace(' ','+');
    call_url = "http://api.glassdoor.com/api/api.htm?v=1&format=json&t.p="+PartnerID+"&t.k="+Key+"&action=employers&q="+name;
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    call_headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url=call_url,headers=call_headers);
    response=urllib2.urlopen(req)
    html=response.read()
    response=json.loads(html);
    #checking response
    if(response['success']==True): 
        #print "Request made successfully"
        True
    else:
        print "Request failed, the following is the response"
        print response
        return

    recordCount=response['response']['totalRecordCount']
    if(recordCount==0):
        print "Search returned no results"
        return    

    if(recordCount>1):
        #print "Search returned "+str(recordCount) +" results, looking for exact match"
        True
    #checking returned results by name
    selectedCompany=None
    for company in response['response']['employers']:
         name = str(companyName)
         name = name.lower();
        # fetchedName= str(company['name'])
         #fetchedName=fetchedName.lower()
         if (company['exactMatch']):
             selectedCompany = company;
             break;
    
    if(selectedCompany==None):
        print "could not find exact match"
        return
    return selectedCompany;
