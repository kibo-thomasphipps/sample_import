print ('please work')
try:
    import shared1
except ImportError:
    print ('shared1 not found')
try:
    import shared2
except ImportError:
    print ('shared2 not found')
