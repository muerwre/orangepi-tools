
import requests

FOLDERS_URL="/rest/stats/folder"
FOLDER_STATUS_URL="/rest/db/status"

def get_uplink_item_count(host, key, id):
  needed_files = 0;

  try:
    response = requests.get(
          f'{host}{FOLDERS_URL}',
          headers={
              'Accept': 'application/json',
              'X-API-Key': key,
          }
      )
    data = response.json();
    for folder in data.keys():
      try:
        response = requests.get(
            f'{host}{FOLDER_STATUS_URL}?folder={folder}',
            headers={
                'Accept': 'application/json',
                'X-API-Key': key,
            }
        )
        status = response.json();
        needed_files += status.get("needTotalItems", 0);
      except:
        continue;
    return needed_files
  except:
    return -1