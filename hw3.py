import county_demographics
from data import CountyDemographics

import build_data
build_data.get_data() #a function within bulid_data

def population_total(counties: list[CountyDemographics]) -> int:
    # return the sum of the "2014 Population" values for every county in the supplied list
    sum = 0
    for county in counties:
        sum += county.population["2014 Population"]
    return sum

def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    # return a list of county objects from the input list whose state attribute matches the supplied two-letter state abbreviation
    filtered_counties = []
    for county in counties:
        if county.state == state:
            filtered_counties.append(county)
    return filtered_counties

def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    # return the total estimated 2014 sub-population for the specified education dictionary key. If the key does not exist, return 0.
    subpop = 0
    for county in counties:
        if key in county.education:
            subpop += county.education[key]/100*county.population["2014 Population"]
    return subpop//1

def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    # return the total estimated 2014 sub-population for the specified ethnicities dictionary key. If the key does not exist, return 0.
    subpop = 0
    for county in counties:
        if key in county.ethnicities:
            subpop += county.ethnicities[key]/100*county.population["2014 Population"]
    return subpop//1 #this will actually return an integer, but it rounds so that you have a whole number of people


def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    #return the total estimated 2014 sub-population represented by the income dictionary key "Persons Below Poverty Level" across the supplied counties
    subpop = 0
    for county in counties:
        subpop += county.income["Persons Below Poverty Level"]/100*county.population["2014 Population"]
    return subpop//1

def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    # return the percentage of the 2014 total population corresponding to the specified education key. If the key does not exist, return 0.
    if population_total(counties)>0:
        return 100*population_by_education(counties, key)/population_total(counties)

def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    # return the percentage of the 2014 total population corresponding to the specified ethnicities key. If the key does not exist, return 0.
    if population_total(counties)>0:
        return 100*population_by_ethnicity(counties, key)/population_total(counties)

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    #return the percentage of the 2014 total populatin that lies below the povery level
    if population_total(counties)>0:
        return 100*population_below_poverty_level(counties)/population_total(counties)

def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    # return counties whose education[key] value is greater than the given percentage threshold
    edu_above = []
    for county in counties:
        if county.education[key] > threshold:
            edu_above.append(county)
    return edu_above

def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    #return counties whose education[key] value is less than the given percentage threshold
    edu_below = []
    for county in counties:
        if county.education[key] < threshold:
                edu_below.append(county)
    return edu_below

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    # return counties whose ethnicity[key] value is greater than the given percentage threshold
    eth_above = []
    for county in counties:
        if county.ethnicities[key] > threshold:
            eth_above.append(county)
    return eth_above

def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    #return counties whose ethnicity[key] value is less than the given percentage threshold
    eth_below = []
    for county in counties:
        if county.ethnicities[key] < threshold:
                eth_below.append(county)
    return eth_below

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    # return counties whose ethnicity[key] value is greater than the given percentage threshold
    poverty_above = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] > threshold:
            poverty_above.append(county)
    return poverty_above

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    #return counties whose ethnicity[key] value is less than the given percentage threshold
    poverty_below = []
    for county in counties:
        if county.income["Persons Below Poverty Level"] < threshold:
            poverty_below.append(county)
    return poverty_below