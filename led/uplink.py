
import requests

CONNECTIONS_URL="/rest/system/connections"

def get_uplink_status(host, key, id):
  try:
    response = requests.get(
          f'{host}{CONNECTIONS_URL}',
          headers={
              'Accept': 'application/json',
              'X-API-Key': key,
          }
      )
    data = response.json();
    return data.get('connections', {}).get(id, {}).get('connected', False)
  except:
    return False