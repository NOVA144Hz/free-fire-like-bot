import requests 
import json
import os
import time

base_url="https://bhuwan-like-api-p.vercel.app"  # Replace with your actual API domain
endpoint="/like"  # API endpoint
API_KEY = "key_inzo006nmc8gdrfw"
API_SECRET = "sec_olejbuxj0k92fttg"


timeout = 50 #seconds 

print("Welcome to the bhuwan likes bot. please enter the uid to post the likes\n")

print("\n")
print("╔═══════════════════════════════════════════════════════════════╗")
print("║                                                               ║")
print("║              ██████╗ ██╗   ██╗██╗    ██╗ █████╗ ███╗   ██╗  ║")
print("║              ██╔══██╗██║   ██║██║    ██║██╔══██╗████╗  ██║  ║")
print("║              ██████╔╝██║   ██║██║ █╗ ██║███████║██╔██╗ ██║  ║")
print("║              ██╔══██╗██║   ██║██║███╗██║██╔══██║██║╚██╗██║  ║")
print("║              ██████╔╝╚██████╔╝╚███╔███╔╝██║  ██║██║ ╚████║  ║")
print("║              ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ║")
print("║                                                               ║")
print("║                      LIKE APIS v1.0                          ║")
print("║                                                               ║")
print("╚═══════════════════════════════════════════════════════════════╝")
print("\n")


def send_request(params, headers):
    try:
        url = base_url + endpoint
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def main():
    global uid, region
    
    # Get UID and region from user
    uid = int(input("Enter your UID: "))
    region = input("Enter your region: ")
    
    # Query parameters for the API
    params = {
        "uid": uid,
        "region": region
    }
    
    # Headers for API authentication - matching Postman configuration
    headers = {
        "X-API-KEY": "key_cwuc0em02bosl20k",
        "X-API-SECRET": "sec_e4wutohjzpn7jeob",
        "X-CLIENT-ID": "cli_aimguard_01F8MECHZX3TBDSZ7XRADM79XE",
        "User-Agent": "Aimguard/1.0.0",
        "X-REQUEST-TYPE": "redifine-like"
    }
    
    # Animated loading
    print("\n📤 Sending likes request", end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
    
    response = send_request(params, headers)
    if response:
        print("=" * 60)
        print("✅ RESPONSE RECEIVED")
        print("=" * 60)
        
        # Player Info
        player = response.get("player", {})
        print(f"\n👤 Player Information:")
        print(f"   UID: {player.get('uid')}")
        print(f"   Nickname: {player.get('nickname')}")
        print(f"   Region: {player.get('region')}")
        
        # Likes Info
        likes = response.get("likes", {})
        print(f"\n❤️  Likes Status:")
        print(f"   Before: {likes.get('before')}")
        print(f"   After: {likes.get('after')}")
        print(f"   Added by API: {likes.get('added_by_api')}")
        
        # API Response
        print(f"\n📊 API Response:")
        print(f"   Status: {response.get('status')}")
        print(f"   Message: {response.get('message')}")
        print(f"   Success Count: {response.get('success_count')}")
        print(f"   Tokens Used: {response.get('token_collection_used')}")
        
        print("\n" + "=" * 60)
        print("Full Response:")
        print("=" * 60)
        print(json.dumps(response, indent=2))
    else:
        print("❌ Request failed - No response from server")

if __name__ == "__main__":
    while True:
        main()
        
        # Ask to send again
        print("\n" + "=" * 60)
        user_input = input("Press Enter to send again or type 'exit' to quit: ").strip().lower()
        print("=" * 60 + "\n")
        
        if user_input == "exit" or user_input == "q":
            print("👋 Thanks for using BHUWAN LIKE APIS!")
            break
