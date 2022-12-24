import yaml

with open("example.yaml", 'r') as stream:
    try:
        config = yaml.load(stream)
        services = config['services']
        for s in services:
            print(s)
            print(s.get('long_run_jobs', []))
    except yaml.YAMLError as exc:
        print(exc)
