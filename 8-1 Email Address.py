def normalize_email(email):
    local, domain = email.lower().split('@')
    # 로컬에 + 이후에 모든 것을 무시
    local = local.split('+')[0]
    # 로컬에 모든 점을 제거
    local = local.replace('.', '')
    return f"{local}@{domain}"

def unique_emails_count(emails):
    unique_emails = set()
    for email in emails:
        normalized_email = normalize_email(email)
        unique_emails.add(normalized_email)
    return len(unique_emails)

# Reading input
for _ in range(10):  # 10개의 데이터 세트가 있다.
    N = int(input().strip())
    emails = [input().strip() for _ in range(N)]
    # 각 데이터 세트의 결과를 출력
    print(unique_emails_count(emails))
