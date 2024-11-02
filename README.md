# GitHub Berlin Users and Repositories

### Overview
- This project analyzes GitHub users in Berlin with over 200 followers to uncover trends in programming language popularity and community engagement.
- It utilizes the GitHub API to scrape user profiles and their repositories, providing insights that can help developers enhance their visibility and engagement.
- Key findings include patterns in language preferences, user engagement dynamics, and recommendations for optimizing GitHub profiles.

### How the Data Was Scraped
I employed the GitHub REST API to gather user data from Berlin, filtering for those with over 200 followers. I collected their profiles and public repositories, cleaning the data for consistency. For company names, I ensured they were trimmed, stripped of leading @ symbols, and converted to uppercase. I captured a range of fields to provide a comprehensive view of the developers in Berlin.

### Most Interesting Findings
One surprising finding was the increasing popularity of languages like JavaScript and Python, indicating a shift towards more systems-oriented programming. This reflects the city's vibrant tech community's willingness to embrace emerging technologies.
Surprisingly, some high-followed users are working with emerging technologies and contribute to innovative projects


### Dataset Summary
The following CSV files are included in this repository:

- **users.csv**: Contains user data for GitHub users in Berlin with over 200 followers.
- **repositories.csv**: Lists public repositories for each user, detailing key metrics.
  
### Findings
1. **Top 5 Users by Followers**
2. **Earliest Registered Users**
3. **Most Popular Licenses**
4. **Majority Company** 
5. **Most Popular Language** 
6. **Second Most Popular Language (after 2020)**
7. **Language with Highest Average Stars**
8. **Top 5 by Leader Strength**
9. **Correlation Between Followers and Repos**
10. **Regression Slope (Followers on Repos)**
11. **Correlation Between Projects and Wiki Enabled**
12. **Average Following Difference (Hireable)**
13. **Regression Slope (Followers on Bio Word Count)**
14. **Top 5 Weekend Repository Creators**
15. **Email Share Difference for Hireable Users**
16. **Most Common Surname**

### A Heartfelt Thanks
Thank you for taking the time to explore these findings! Your curiosity and commitment to learning are what drive innovation in our tech community. Happy coding, and may your GitHub journey be as enriching as the Berlin tech scene itself!
