
import asyncio
# import httpx # A popular library for async API calls
import time
# 1st Example
async def loginform(name: str, age: int, location: list[str]):
    return {
        "name": name,
        "age": age,
        "location": location
    }

async def main():
    result = await loginform('Ali', 18, ["Lahore", "Karachi", "Islamabad"])
    print(result)
asyncio.run(main())



# 2nd Example:
async def fetch_user_data(user_id: int):
    print(f"Searching database for User ID: {user_id}..")
    await asyncio.sleep(2) 
    return {"id": user_id, "username": "CodingWizard", "status": "Online"}

async def main():
    print("Request started.")
    user_profile = await fetch_user_data(101)
    print(f"Request finished! Welcome back, {user_profile['username']}.")

asyncio.run(main())

# 3rd Example

async def make_coffee():
    print("☕ Starting coffee...")
    await asyncio.sleep(2) 
    print("☕ Coffee is ready!")
    return "Hot Coffee"

async def toast_bread():
    print("🍞 Putting bread in toaster...")
    await asyncio.sleep(3) 
    print("🍞 Toast is ready!")
    return "Crispy Toast"

async def main():
    start_time = time.perf_counter()
    print("--- Breakfast Started ---")


    results = await asyncio.gather(make_coffee(), toast_bread())

    end_time = time.perf_counter()
    
    print(f"--- Breakfast Finished! Menu: {results} ---")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

asyncio.run(main())


# 4th Exmample

'''  
async def get_weather(city: str):
    print(f"☁️ Fetching weather for {city}...")
    async with httpx.AsyncClient() as client:
        # This 'await' lets the Manager do other things while the API responds
        response = await client.get(f"https://wttr.in/{city}?format=j1")
        print(f"✅ Weather for {city} received!")
        return response.json()['current_condition'][0]['temp_C']

async def get_exchange_rate():
    print("💰 Fetching exchange rate...")
    await asyncio.sleep(1) # Simulating a quick API call
    print("✅ Exchange rate received!")
    return "278.50 PKR"

async def main():
    start_time = time.perf_counter()

    # The Event Loop manages both API calls at once!
    weather_task = get_weather("London")
    rate_task = get_exchange_rate()

    # We fire them off together
    temperature, rate = await asyncio.gather(weather_task, rate_task)

    print(f"\n--- Dashboard ---")
    print(f"London Temp: {temperature}°C")
    print(f"USD to PKR: {rate}")
    
    end_time = time.perf_counter()
    print(f"Time taken: {end_time - start_time:.2f} seconds")

asyncio.run(main())
'''
