from base64 import b64decode
string='VmtkMFUyTnJNVlpPVlZaV1YwZG9VRlpyVlhka01WSnpWV3hLYkdGNlVqVlZNVkpQVkRGS1JrMVVUbFZYU0VKRFZGWmFkMk5XWkhSa1JUVnNZa1ZXTlZZeWVGTldhelZXVGxab1dGZElRazlhVjNoM1l6RlNkR05GTlU1aVNFSjRWakZTUTFSdFZuSldXR3hZWWtaS1lWUlVRWGhPYkZwWllrVTFWMUl4U25rPQ=='

i=0
while (i<5):
	i=i+1
	string=b64decode(string)

decoded_string = bytes.fromhex(string.decode('utf-8'))
print(decoded_string.decode('utf-8'))

