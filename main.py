import asyncio
import httpx

# Replace this with your API key
API_KEY = ""


async def main():
    rate_quote = await post_rate_quote(
        {
            "RateQuote": {
                "CODAmount": 0,
                "Origin": {
                    "City": "Tampa",
                    "StateOrProvince": "FL",
                    "ZipOrPostalCode": "34655",
                    "CountryCode": "USA"
                },
                "Destination": {
                    "City": "Dayton",
                    "StateOrProvince": "OH",
                    "ZipOrPostalCode": "45414",
                    "CountryCode": "USA"
                },
                "Items": [
                    {
                        "Width": 4,
                        "Height": 4,
                        "Length": 4,
                        "Class": "65",
                        "Weight": 114
                    }
                ]
            }
        }
    )
    print(rate_quote)


async def get_pallet_types():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.rlc.com/RateQuote/GetPalletTypes",
            headers={"apiKey": f"{API_KEY}"},
        )
        response.raise_for_status()
        return response.json()


async def get_pallet_types_by_points(origin_city, origin_zip, destination_city, destination_zip):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.rlc.com/RateQuote/GetPalletTypesByPoints",
            headers={"apiKey": f"{API_KEY}"},
            params={
                "originCity": origin_city,
                "originZip": origin_zip,
                "destinationCity": destination_city,
                "destinationZip": destination_zip,
            },
        )
        response.raise_for_status()
        return response.json()


async def get_rate_quote(quote_number):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.rlc.com/RateQuote",
            headers={"apiKey": f"{API_KEY}"},
            params={"quoteNumber": quote_number},
        )
        response.raise_for_status()
        return response.json()


async def post_rate_quote(rate_quote_request):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.rlc.com/RateQuote",
            headers={"apiKey": f"{API_KEY}",
                     "Content-Type": "application/json"},
            json=rate_quote_request,
        )
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    asyncio.run(main())
