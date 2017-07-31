debin = ['ubuntu','mintos']

redhat = ['centos','fedodra']


def generate_package(typeos):
	val = typeos.lower()

	if val in debin:
		if val == 'ubuntu':
			print("your package manager is apt",val)
		else:
			print("Your package manager is minpack",val)
	elif val in redhat:
		if val == 'centos':
			print("Your package manager is yum",val)

		else:
			print("Your package manager is dnf",val)
	else:
		print("I dont find anything for",val)




