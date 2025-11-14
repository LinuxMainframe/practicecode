"""
Challenge 1:

log_data = [
    "192.168.1.1 - - [10/Nov/2025:13:55:36] GET /admin 401",
    "192.168.1.5 - - [10/Nov/2025:13:56:12] POST /login 200",
    "192.168.1.1 - - [10/Nov/2025:13:57:01] GET /admin 401",
]

# Create a dict counting failed login attempts per IP
# Failed = status code 401


	Preliminary Notes:

	So these are REST commands and their return codes, which are http status codes

	Common codes are as follows,
	- Informational responses (100 – 199)
	- Successful responses (200 – 299)
    - Redirection messages (300 – 399)
    - Client error responses (400 – 499)
    - Server error responses (500 – 599)

	200 - SUCCESS, depends on context of REST caller -
		- GET: The resource has been fetched and transmitted in the message body
		- POST: Representation headers are included in the response without any message body
		- PUT/POST: The resource describing the result of the action is transmitted in the message body
		- TRACE: The message body contains the request as received by the server

	400 - Bad Request: The server cannot or will not process the request due to something that is perceived to be a client error
	401 - Unauthorized: Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.
	403 - Forbidden: The client does not have access rights to the content. User may be authenticated w/ server knowing identity, but privelleges too low or non-existent
	404 - NOT FOUND: The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist

	Assuming we cannot use REGEX, then we must do the following:
	break into sections and store as tokens.
	The structure is the following:

		"<ip addr> <spacer> <date/time> <rest method> <endpoint> <return code>"

	they are all broken up by spaces, so we really can avoid dealing with anything too crazy.
	So we will create a 2D matrix (nested lists), where we take each and then break into tokens.
	then we iterate over tokens and interpret them


"""


log_data = [
    "192.168.1.1 - - [10/Nov/2025:13:55:36] GET /admin 401",
    "192.168.1.5 - - [10/Nov/2025:13:56:12] POST /login 200",
    "192.168.1.1 - - [10/Nov/2025:13:57:01] GET /admin 401",
]

def count_fails(log_data:list[str]) -> int:
	"""
		Counts the total fails for RESTful endpoint commands

		Args:
			log_data - a list of strings, each taking the form:
				"<ip addr> <spacer> <date/time> <rest method> <endpoint> <return code>"

		Returns:
			integer representing total failures
	"""
	token_list = []

	for data in log_data:
		token_list.append(data.split())

	fails = 0
	for entry in token_list:
		if (int(entry[6]) < 200) and (int(entry[6]) > 99): # 100-199
			pass
		elif (int(entry[6]) < 300) and (int(entry[6]) > 199): # 200-299
			pass
		elif (int(entry[6]) < 400) and (int(entry[6]) > 299): # 300-399
			pass
		elif (int(entry[6]) < 500) and (int(entry[6]) > 399): # 400-499
			fails += 1
		elif (int(entry[6]) < 200) and (int(entry[6]) > 99): # 500-599
			fails += 1

	return fails

print(count_fails(log_data))

def fails_per_ip(log_data: list[str]) -> dict[str, int]:
	"""
		Provides a failure count per IP address

		Args:
			log_data - a list of strings, each taking the form:
				"<ip addr> <spacer> <date/time> <rest method> <endpoint> <return code>"

		Returns:
			dictionary of str:int pairs representing the unique IP address and fail count
	"""
	token_list = []

	for data in log_data:
		token_list.append(data.split())

	unique_ips = []
	ip_fail_count = []

	for entry in token_list:
		if entry[0] not in unique_ips:
			unique_ips.append(entry[0])
			ip_fail_count.append(0)

		if (int(entry[6]) < 200) and (int(entry[6]) > 99): # 100-199
			pass
		elif (int(entry[6]) < 300) and (int(entry[6]) > 199): # 200-299
			pass
		elif (int(entry[6]) < 400) and (int(entry[6]) > 299): # 300-399
			pass
		elif (int(entry[6]) < 500) and (int(entry[6]) > 399): # 400-499
			ip_fail_count[unique_ips.index(entry[0])] += 1
		elif (int(entry[6]) < 600) and (int(entry[6]) > 499): # 500-599
			ip_fail_count[unique_ips.index(entry[0])] += 1

	final_counts = {}
	for x in range(0, len(unique_ips) ):
		final_counts.update({unique_ips[x]:ip_fail_count[x]})

	return final_counts

print(fails_per_ip(log_data))