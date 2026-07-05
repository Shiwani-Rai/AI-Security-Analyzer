import requests


def get_ip_info(ip):

    try:

        url = f"http://ip-api.com/json/{ip}"

        response = requests.get(url, timeout=10)

        data = response.json()

        if data["status"] != "success":

            return {
                "ip": ip,
                "country": "Unknown",
                "city": "Unknown",
                "isp": "Unknown"
            }

        return {

            "ip": ip,

            "country": data["country"],

            "city": data["city"],

            "isp": data["isp"]

        }

    except:

        return {

            "ip": ip,

            "country": "Unknown",

            "city": "Unknown",

            "isp": "Unknown"

        }