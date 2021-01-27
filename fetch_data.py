import rows
from collections import OrderedDict
from io import BytesIO
import requests


url = "https://www.cic.gc.ca/english/information/where-to-give-biometrics.asp"
content = requests.get(url).content
rows_xpath="//table/tbody/tr"
fields_xpath = OrderedDict([
    ('City_ascii', './td[1]/text()'),
    ('label', './td[1]/descendant::*/text()'),
    ('Country', './td[2]/text()'),
    ('Website', './td[3]/a/@href'),
    ('Biometrics', './td[4]/descendant-or-self::*/text()'),
    ('Notes', './td[5]/descendant-or-self::*/text()'),
])

table = rows.import_from_xpath(BytesIO(content), rows_xpath, fields_xpath)
rows.export_to_csv(table, "biometrics.csv")
