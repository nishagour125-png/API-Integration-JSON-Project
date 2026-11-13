
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_data():
    try:
        response = requests.get(API_URL, timeout=10)

        response.raise_for_status()

        data = response.json()

        print("\nAPI DATA FETCHED SUCCESSFULLY!")
        print("Total Records:", len(data))

        return data

    except requests.exceptions.RequestException as error:
        print("API Error:", error)
        return []

def filter_data(data):
    print("\n--- FILTERED DATA ---")

    filtered = [
        post for post in data
        if post["userId"] == 1
    ]

    for post in filtered[:5]:
        print("\nTitle:", post["title"])
        print("Body:", post["body"])

def search_data(data):
    keyword = input("\nEnter title keyword: ").lower()

    results = [
        post for post in data
        if keyword in post["title"].lower()
    ]

    print("\n--- SEARCH RESULTS ---")

    if results:
        for post in results:
            print(post["title"])
    else:
        print("No matching records found.")

def main():
    data = fetch_data()

    if data:
        filter_data(data)
        search_data(data)

if __name__ == "__main__":
    main()
