""" This module provides a reusable byline for the author's services."""

import math
import statistics

#Variables
company_name: str= "Trucking Analysis Inc."
count_active_projects: int = 5
has_international_presence: bool = False
average_client_satisfaction: float = 7.4
services_offered: list = ["Data Analysis", "Fuel Efficiency Consulting", "Business Intelligence Solutions"]
satisfaction_scores: list = [10.0,6.0,7.0,5.2,8.8]

# F-Strings
client_satisfaction_string: str = f" Average Client Satisfaction: {average_client_satisfaction}"  
count_active_projects_string:str = f"Active Projects: { count_active_projects}"
has_international_presence_string:str = f" has international presence: { has_international_presence}"

#Statistics Section
smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total=sum(satisfaction_scores)
count=len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation= statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for our Satisfaction Scores:
Smallest: {smallest}
Largest: {largest}
Total: {total}
Count: {count}
Mean: {mean}
Mode: {mode}
Median: {median}
Standard Deviation: {standard_deviation} 
"""
#Define Main Function
def main():
    """Display all output"""
print(company_name)
print(count_active_projects_string)
print(has_international_presence_string)
print(client_satisfaction_string)
print(stats_string)
print(byline)
    
byline:str =f'''
  {company_name}
  {active_projects_string}
  {has_international_presence_string}
  {client_satisfaction_string}
  {services_offered_string}
  {stats_string}'''



