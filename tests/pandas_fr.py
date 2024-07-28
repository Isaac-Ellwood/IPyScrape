# pandas for tables
import pandas as pd
url = 'https://www.chbc.school.nz/'
content = pd.read_html(url)

print(content)