import dns.resolver
resolver = dns.resolver.Resolver()
answers = resolver.query("fam.finc.com", "A")
for rdata in answers:
    print rdata
