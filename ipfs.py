import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"

	account_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJjNzk3YzFlNC0yMjQ1LTQwZDgtYWRhYi03MzkyYWRkZDJiODciLCJlbWFpbCI6ImJkdWhhaW1lQGVuZ2luZWVyaW5nLnVwZW5uLmVkdSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiJiNmY1NDFjOTM2YWUyMTQ5OTQ3YyIsInNjb3BlZEtleVNlY3JldCI6IjRiYjEzZTY3OTM4N2I0MDZlZjdmNTBjOWFiZjI1YWNhYTQ5MWEzNGMzMDg0N2NjYzRhY2E5ZWNjZGQ5NmI1YzkiLCJleHAiOjE4MjMzNzE0MzZ9.9w-a8WlpW795uZCjLRdMrJLxHk8AQM8gxMX-zv1H5ig"
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

	upload_payload = {
		"pinataContent": data
	}

	header = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {account_jwt}"
	}

	response = requests.post(url, json=payload, headers=header)
	cid = response.json().get("IpfsHash")
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#response = requests.get(f"harlequin-quickest-rhinoceros-835.mypinata.cloud/ipfs/{cid}")
	response = requests.get(f"https://pinata.cloud{cid}")
	data = response.json()
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
