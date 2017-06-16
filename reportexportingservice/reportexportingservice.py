#!../venv/bin/python
from dicttoxml import dicttoxml
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response
from jinja2 import Environment, PackageLoader, select_autoescape
import json
import pdfkit

from database import db_session
from models import Report


env = Environment(
    loader=PackageLoader('reportexportingservice', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)


def fetch_report_type(report_id):
    """ Returns a dictionary of the report information with passed report id
    """
    report = Report.query.filter_by(id=report_id).first()
    return json.loads(report.type)


@app.route('/report/api/v1.0/pdf/<int:report_id>', methods=['GET'])
def get_pdf(report_id):
    template = env.get_template('pdftemplate.html')
    rendered = template.render(
        data = fetch_report_type(report_id)
        )
    pdf = pdfkit.from_string(rendered, False)
    return Response(pdf, mimetype='application/pdf')


@app.route('/report/api/v1.0/xml/<int:report_id>', methods=['GET'])
def get_xml(report_id):
    report_dict = fetch_report_type(report_id)
    xml = dicttoxml(report_dict, attr_type=False)
    return Response(xml, mimetype='text/xml')


if __name__ == '__main__':
    app.run(debug=True)
