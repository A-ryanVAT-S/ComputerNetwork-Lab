import dns.resolver

domain = "www.youtube.com"
log_file = "dns_log.txt"

with open(log_file, "w") as f:
    f.write(f"DNS Query Results for: {domain}\n")
    for record_type in ['A', 'MX', 'CNAME']:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            f.write(f"\n{record_type} Records:\n")
            for record in answers:
                f.write(f"- {record.to_text()}\n")
        except Exception as e:
            f.write(f"\nNo {record_type} records found or error: {e}\n")

print(f"DNS query results logged to '{log_file}'.")

