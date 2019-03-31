import redis
import yaml
import sys


def get_yaml_data (config_file):
  with open(config_file, "r") as f:
    data = yaml.load(f)
    return data
  return ""

args = sys.argv
config_file = args[1]
yml_data = get_yaml_data(config_file)

con_info  = yml_data['connection']
data_hash = yml_data['key_vales']

r = redis.StrictRedis(host=con_info['host'], port=con_info['port'], db=0)
for k, v in data_hash.items():
    print(k, v)
    r.set(k, v)

######################3
# for debug
print("==== print current values =====")
for k in data_hash.keys():
    print(k)
    print(r.get(k))
