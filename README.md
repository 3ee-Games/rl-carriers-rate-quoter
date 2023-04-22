# 🚚 Rate Quote API client

This async client will help you understand how to use R+L Carriers rate quote API for shipping calculations.

Docs: https://api.rlc.com/swagger/ui/index#/RateQuote

## Requirements
- **Developer API Key**: MyRLC Account to retrieve your API key.  If you do not have an account, sign up here: https://www.rlcarriers.com/company/myrlc-signup

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [API Key Setup](#api-key-setup)
3. [Functions](#functions)
    - [main](#main)
    - [get_pallet_types](#get_pallet_types)
    - [get_pallet_types_by_points](#get_pallet_types_by_points)
    - [get_rate_quote](#get_rate_quote)
    - [post_rate_quote](#post_rate_quote)
4. [Usage Example](#usage-example)

## Prerequisites
Make sure you have the following dependencies installed:

- `httpx`
- `asyncio`

To install these dependencies, run:

```bash
pip install httpx asyncio
```

## API Key Setup

Replace the `API_KEY` variable with your actual API key:

```python
API_KEY = "your_api_key_here"
```

## Functions

### main

`main()` is the main function that demonstrates the usage of the other functions. You can modify the input data in this function to test different scenarios.

### get_pallet_types

```python
async def get_pallet_types()
```

Fetches all available pallet types from the API. No parameters are required for this function.

### get_pallet_types_by_points

```python
async def get_pallet_types_by_points(origin_city, origin_zip, destination_city, destination_zip)
```

Fetches pallet types based on the origin and destination points. Parameters:

- `origin_city`: Origin city as a string.
- `origin_zip`: Origin zip code as a string.
- `destination_city`: Destination city as a string.
- `destination_zip`: Destination zip code as a string.

### get_rate_quote

```python
async def get_rate_quote(quote_number)
```

Fetches the rate quote based on the provided quote number. Parameters:

- `quote_number`: The quote number as a string.

### post_rate_quote

```python
async def post_rate_quote(rate_quote_request)
```

Submits a rate quote request and receives a response with the calculated rate. Parameters:

- `rate_quote_request`: A dictionary containing the rate quote request data.

## Usage Example

To use this script, simply run it:

```bash
python rate_quote_api.py
```

By default, the `main` function demonstrates the usage of the `post_rate_quote` function. You can modify the input data in the `main` function and call other functions to test different scenarios.
