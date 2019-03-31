elasticcache

## Description
ElasticCacheに対して設定するためのツール


## Create Env And modules install
```
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

## set values
```
vi config/config.yml
xxxにffffを追加する例

key_vales:
  test: "value1"
  xxx: "ffff"

```

## RUN
```
python set-values.py config/config.yml 
```

