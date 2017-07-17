from suds.client import Client
from suds.plugin import MessagePlugin


class LogPlugin(MessagePlugin):
    def sending(self, context):
        print(str(context.envelope))

    def received(self, context):
        print(str(context.reply))


url = "http://api.rlcarriers.com/1.0.2/RateQuoteService.asmx?WSDL"
key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
client = Client(url, plugins=[LogPlugin()])

request = client.factory.create('RateQuoteRequest')

request.CustomerData = 'Ryan Tester'
request.QuoteType = 'Domestic'
request.CODAmount = 0.00

service_point_origin = client.factory.create('ServicePoint')
service_point_origin.City = 'Burns'
service_point_origin.StateOrProvince = 'TN'
service_point_origin.ZipOrPostalCode = '37029'
service_point_origin.CountryCode = 'USA'

service_point_dest = client.factory.create('ServicePoint')
service_point_dest.City = 'Tampa'
service_point_dest.StateOrProvince = 'FL'
service_point_dest.ZipOrPostalCode = '33635'
service_point_dest.CountryCode = 'USA'

request.Origin = service_point_origin
request.Destination = service_point_dest

item = {
    'Class': 55.0,
    'Weight': 200.0
}

items = client.factory.create('ArrayOfItem')
items.Item = [item]
request.Items = items

request.DeclaredValue = 1.0
request.OverDimensionPcs = 0

accessorials = client.factory.create('ArrayOfAccessorial')
accessorial = None #ResidentialDelivery
accessorials.Accessorial = [accessorial]
request.Accessorials = accessorials


result = client.service.GetRateQuote(key, request)
print result