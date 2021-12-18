import requests, json, decode, os

host = "https://production-dlc.lina.gu3.jp/AssetBundle/deploy_211119_res_ggM8FOakyt/Android/" #Latest version, no longer possible to get these URLs

r = requests.get(host + "!LinaExr.txt")
contents = json.loads(decode.DecryptJSONString(r.text))["contents"]

for filename in contents:
	req = requests.get(host + filename + "_" + contents[filename]["md5"])
	try:
		req.raise_for_status()
	except requests.exceptions.HTTPError as err:
		pass 
	else:
		os.makedirs(os.path.dirname("Bundles/" + filename), exist_ok = True)
		with open("Bundles/" + filename, "wb") as f:
			f.write(req.content)
		print("Downloaded " + filename)