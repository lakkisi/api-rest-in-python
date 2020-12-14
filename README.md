# Request all keys values : 
curl -i "http://localhost:5000/keyvalues/"

# Create a key / values pair
curl -i -H "Content-type: application/json" -X POST -d '{"key":"key1", "value": "value1"}'  http://localhost:5000/keyvalues/

# retrieve key / value pair list
curl -i "http://localhost:5000/keyvalues/"

# add new key / value pair
curl -i -H "Content-type: application/json" -X POST -d '{"key":"key2", "value": "value2"}'  http://localhost:5000/keyvalues/

# retrieve again key / value list
curl -i "http://localhost:5000/keyvalues/"

# update value key2
curl -i -H "Content-type: application/json" -X PUT -d '{"value":"new_value2"}'  http://localhost:5000/keyvalues/2/

# retrieve again key / value list
curl -i "http://localhost:5000/keyvalues/"

# delete value key2
curl -i -X DELETE "http://localhost:5000/keyvalues/2/"

# retrieve again key / value list
curl -i "http://localhost:5000/keyvalues/"
