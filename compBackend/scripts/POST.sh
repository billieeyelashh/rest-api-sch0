#!/bin/bash

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"dept_no":"d999","dept_name":"stucker"}' \
  http://0.0.0.0:8080/api/departments
