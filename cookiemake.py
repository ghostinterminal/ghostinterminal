def main():
	print 'Just Paste the raw cookie string.........'
	cookies = raw_input('PASTE RAW_STRING:\n')

	cookies = ''.join(cookies.split(';'))
	cookies = ''.join(cookies.replace('=', '\':\''))
	cookies = ''.join(cookies.replace(' ', '\',\''))
	
	print '======================= COOIKES DICT GENERATED ======================='
	print '{\''+cookies+'\'}'

main()
	
