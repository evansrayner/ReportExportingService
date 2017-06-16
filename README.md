# Installation

For Debian/Ubuntu create a virtual env and activate. Then run;

pip install -r requirements
sudo apt-get install wkhtmltopdf


# Start

In project root, run:

./reportexportingservice.py


# Example useages

## Get report 2 as a PDF

http://127.0.0.1:5000/report/api/v1.0/pdf/2

## Get report 1 as an XML

http://127.0.0.1:5000/report/api/v1.0/xml/1 